# ----------------------------------------------------------------------------------------
#  PASO2: PROGRAMA QUE CREARA UN TOKEN DEL USER PASSWD ZIMBRA  
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

import cfg.ZIMBRA_variables as sTv
from   cfg.ZIMBRA_library import *

# ----------------------------------------------------------------------------------------
#                                  FUNCIONES
# ----------------------------------------------------------------------------------------

def Crear_Token_SOAP(pUrl, pUsuario, pContrasena):

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
    response = requests.post(pUrl, data=auth_xml, headers={"Content-Type": "text/xml"}, verify=False)

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

def Importar_User_Passwd(pEntorno):
    xRutaArchivo=f"{sTv.loc_RutaConfig}{sTv.var_NombreUsuarios}"
    xUsuario = None
    xContrasena = None
    with open(xRutaArchivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')
        for fila in lector:
            if fila['ENTORNO'].strip('"') == pEntorno:
                xEmail=fila['EMAIL'].strip('"')
                xPasswd=fila['PASSWD'].strip('"')
                break # porque solo queremos la primera coincidencia
    return xEmail, xPasswd

# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------

def sTv_paso2(pUrl, pEntorno):
    # Importar usuario y contraseña del file .txt
    pUsuario, pContrasena = Importar_User_Passwd(pEntorno)

    # Crear un token en Zimbra
    auth_token = Crear_Token_SOAP(pUrl, pUsuario, pContrasena)

    return auth_token

