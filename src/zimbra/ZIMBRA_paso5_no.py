# ----------------------------------------------------------------------------------------
#  PASO5: PROGRAMA NO FUNCIONA   
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

import requests
from lxml import etree
import urllib3
from datetime import datetime
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ----------------------------------------------------------------------------------------
#                                  FUNCIONES
# ----------------------------------------------------------------------------------------

def Crear_Token_SOAP(pUsuario, pContrasena):

    # XML de autentificación
    auth_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
    <soap:Body>
        <AuthRequest xmlns="urn:zimbraAccount">
        <account by="name">{pUsuario}</account>
        <password>{pContrasena}</password>
        </AuthRequest>
    </soap:Body>
    </soap:Envelope>"""

    # Enviar petición
    response = requests.post("https://zimbra.tda-sgft.com/service/soap", data=auth_xml, headers={"Content-Type": "text/xml"}, verify=False)

    # Mostrar respuesta
    print("Código HTTP:", response.status_code)
    print("Respuesta completa:")
    print(response.text)

    # Extraer el token (opcional, con XML parsing)
    import xml.etree.ElementTree as ET
    tree = ET.fromstring(response.content)
    ns = {'soap': 'http://www.w3.org/2003/05/soap-envelope', 'zimbra': 'urn:zimbraAccount'}

    token = tree.find('.//zimbra:authToken', ns)
    if token is not None:
        auth_token = token.text
        print("✅ Token obtenido:")
        print(f':{auth_token}:')
    else:
        print("❌ No se pudo obtener el token")

    return auth_token

def buscar_tareas(query):
    token = Crear_Token_SOAP("carpios@tda-sgft.com", "G3m4198005$$")
    
    soap_request = f"""
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
    <soap:Header>
        <context xmlns="urn:zimbra">
        <authToken>{token}</authToken>
        </context>
    </soap:Header>
    <soap:Body>
        <SearchRequest xmlns="urn:zimbraMail" types="task" query="{query}"></SearchRequest>
    </soap:Body>
    </soap:Envelope>
    """
    soap_request2 = f"""
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
        <soap:Header>
            <context xmlns="urn:zimbra">
                <authToken>{token}</authToken>
            </context>
        </soap:Header>
        <soap:Body>
            <SearchRequest xmlns="urn:zimbraMail" types="task" query="{query}" />
        </soap:Body>
    </soap:Envelope>
    """
     
    response = requests.post(ZIMBRA_SOAP_URL, data=soap_request2, headers={'Content-Type': 'application/xml'}, verify=False)

    print("STATUS:", response.status_code)
    print("RESPONSE TEXT:", response.text)
    xml = etree.fromstring(response.content)
    
    tareas = xml.xpath('//m', namespaces={'': 'urn:zimbraMail'})
    for t in tareas:
        asunto = t.attrib.get('su')
        print("ID:", t.attrib.get('id'), "| Asunto:", asunto)


# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------



ZIMBRA_SOAP_URL = "https://zimbra.tda-sgft.com/service/soap"  
fecha = datetime(2025, 4, 17)
timestamp = int(time.mktime(fecha.timetuple())) * 1000


buscar_tareas("in:tasks")
#buscar_tareas('in:tasks su:IDEI')
#buscar_tareas(f'in:tasks after:{timestamp}')
#buscar_tareas('in:tasks status:NEED')
#buscar_tareas(f'in:tasks su:IDEI status:NEED after:{timestamp}')

    





    
  



