import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def Crear_Token_SOAP():

    # Datos de acceso
    
    usuario = "carpios@tda-sgft.com"
    #usuario = "talavanf@tda-sgft.com"
    contrasena = "G3m4198005$$"  
    #contrasena = "Mrpotato51.."

    # XML de autenticación
    auth_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
    <soap:Body>
        <AuthRequest xmlns="urn:zimbraAccount">
        <account by="name">{usuario}</account>
        <password>{contrasena}</password>
        </AuthRequest>
    </soap:Body>
    </soap:Envelope>"""

    # Enviar petición
    response = requests.post(url, data=auth_xml, headers={"Content-Type": "text/xml"}, verify=False)

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
        print("✅ Token obtenido:\n", auth_token)
    else:
        print("❌ No se pudo obtener el token")

    return auth_token

def Crear_Cita_SOAP(auth_token, pTitulo, pEstado, pPrioridad, pLocate, pDescribe, pContent, pSu, pFIni, pFFin, pFRec):

    crear_tarea_con_alarma = f"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
    <soap:Header>
        <context xmlns="urn:zimbra">
        <authToken>{auth_token}</authToken>
        </context>
    </soap:Header>
    <soap:Body>
        <CreateTaskRequest xmlns="urn:zimbraMail">
        <m>
            <inv method="REQUEST" type="task">
            <comp name="{pTitulo}" percentComplete="0" status="{pEstado}" priority="{pPrioridad}">
                <s d="20250414T160000Z"/>
                <e d="20250414T170000Z"/>
                <loc>{pLocate}</loc>
                <alarm action="DISPLAY">
                <trigger>
                    <abs d="20250414T120000Z"/>
                </trigger>
                <desc>{pDescribe}</desc>
                <attach uri=""/>
                </alarm>
            </comp>
            </inv>
            <su>{pSu}</su>
            <mp ct="text/plain">
            <content>{pContent}</content>
            </mp>
        </m>
        </CreateTaskRequest>
    </soap:Body>
    </soap:Envelope>"""


    # Enviar la solicitud
    response2 = requests.post(url, data=crear_tarea_con_alarma, headers={"Content-Type": "text/xml"}, verify=False)
    
    # Mostrar respuesta
    print("Respuesta al crear tarea:")
    #print(response1.text)
    print(response2.text)

    # Enviar la solicitud
    #response2 = requests.post(url, data=crear_tarea_con_alarma, headers={"Content-Type": "text/xml"}, verify=False)
    # Mostrar respuesta
    #print("Respuesta al crear tarea:")
    #print(response2.text)



#########################################################################################
url = "https://zimbra.tda-sgft.com/service/soap"

print("----------------- CREAR LA TOKEN -----------------")
auth_token = Crear_Token_SOAP()

print("----------------- CREAR LA TAREA -----------------")
vTitulo="TITULO: xxxxxxx"
vEstado="NEED"                         # NEED: No se ha iniciado | INPR: En progreso | COMP: Completada | WAITING: En espera | DEFERRED: Pospuesta
vPrioridad="1"                         # 1   : Alta
vLocate="UBICACION: xxxxxxx"
vDescribe="DESCRIBE: xxxxx"
vContent="CONTENIDO: xxxxxxxxxxxxxx \n sdfsdfsdfsd \n sdfsdfsd"
vSu="SU: xxxxxxxxxx"
vFIni=""
vFFin=""
vFRec=""


Crear_Cita_SOAP(auth_token, vTitulo, vEstado, vPrioridad, vLocate, vDescribe, vContent, vSu, vFIni, vFFin, vFRec)
                