import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def Crear_Token_SOAP(pUsuario, pContrasena):

    # XML de autenticación
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
        print("✅ Token obtenido:")
        print(f':{auth_token}:')
    else:
        print("❌ No se pudo obtener el token")

    return auth_token

def Crear_Tarea_SOAP(pAuthToken, pTitulo, pEstado, pPrioridad, pLocate, pDescribe, pContent, pSu, pOrganizador, pFIni, pFFin, pFRec):
    crear_tarea_con_alarma = f"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
    <soap:Header>
        <context xmlns="urn:zimbra">
        <authToken>{pAuthToken}</authToken>
        </context>
    </soap:Header>
    <soap:Body>
        <CreateTaskRequest xmlns="urn:zimbraMail">
        <m>
            <inv method="REQUEST" type="task">
            <comp name="{pTitulo}" percentComplete="0" status="{pEstado}" priority="{pPrioridad}">
                <s d="{pFIni}"/>
                <e d="{pFFin}"/>
                <loc>{pLocate}</loc>
                <alarm action="DISPLAY">
                <trigger>
                    <abs d="{pFRec}"/>
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
    print("Respuesta al crear tarea:")
    print(response2.text)

def Crear_Cita_SOAP (pAuthToken, pTitulo, pEstado, pPrioridad, pLocate, pDescribe, pContent, pSu, pOrganizador, pREQ1, pREQ2, pOPT, pFIni, pFFin, pFRec):
    crear_cita_con_alarma = f"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
      <soap:Header>
        <context xmlns="urn:zimbra">
          <authToken>{pAuthToken}</authToken>
        </context>
      </soap:Header>
      <soap:Body>
        <CreateAppointmentRequest xmlns="urn:zimbraMail">
          <m>
            <inv method="REQUEST" type="event">
              <comp name="{pTitulo}" status="{pEstado}" priority="{pPrioridad}">
                <s d="{pFIni}"/>
                <e d="{pFFin}"/>
                <or a="{pOrganizador}"/>
                <at role="REQ" ptst="NE" rsvp="1" a="{pREQ1}" d="{pREQ1}"/>
                <at role="REQ" ptst="NE" rsvp="1" a="{pREQ2}" d="{pREQ2}"/>
                <at role="OPT" ptst="NE" rsvp="1" a="{pOPT}" d="Steve Carpio :-) "/>
                <loc>{pLocate}</loc>
                <alarm action="DISPLAY">
                  <trigger>
                    <abs d="{pFRec}"/>
                  </trigger>
                  <desc>{pDescribe}</desc>
                </alarm>
              </comp>
            </inv>
            <su>{pSu}</su>
            <mp ct="text/plain">
              <content>{pContent}</content>
            </mp>
          </m>
        </CreateAppointmentRequest>
      </soap:Body>
    </soap:Envelope>"""

    # Enviar la solicitud
    response = requests.post(url, data=crear_cita_con_alarma, headers={"Content-Type": "text/xml"}, verify=False)
    print("Respuesta al crear cita:")
    print(response.text)


#########################################################################################
url = "https://zimbra.tda-sgft.com/service/soap"

print("----------------- CREAR LA TOKEN -----------------")
vUsuario = "carpios@tda-sgft.com"
#vUsuario = "talavanf@tda-sgft.com"
vContrasena="xxxxx"
#vAuthToken = Crear_Token_SOAP(vUsuario, vContrasena)
# Steve
x1="0_0c36221b747cab40e0c824aaa3335628595f7cc9_69643d33363a34383737623236352d313730322d343261372d386431652d3436313239396466363061313b6578703d31333a313734343739353038343830343b747970653d363a7a696d6272613b753d313a613b7469643d31303a313733333435333435343b76657273696f6e3d31343a31302e302e305f47415f343531383b"
# Paco
x2="0_21c891a3d7bda96dd766e5642b74b381c7492384_69643d33363a34383737623236352d313730322d343261372d386431652d3436313239396466363061313b6578703d31333a313734343739373234393930373b747970653d363a7a696d6272613b753d313a613b7469643d383a33333937373230353b76657273696f6e3d31343a31302e302e305f47415f343531383b"
vAuthToken=x1

print("----------------- CREAR LA TAREA -----------------")
vTitulo="Creando un tarea de prueba 16"
vEstado="INPR"                         # NEED: No se ha iniciado | INPR: En progreso | COMP: Completada | WAITING: En espera | DEFERRED: Pospuesta
vPrioridad="1"                         # 1   : Alta
vLocate="Clave Pizarra XXXXXXXX 3"
vDescribe="DESCRIBE: xxxxx"            # ¿.................?
vContent="Contenido de la tarea XXXXXXXX \n xxxxxxxxxx"
vSu="SU: xxxxxxxxxx"                   # ¿.................?
vOrganizador="carpios@tda-sgft.com"
pREQ1="talavanf@tda-sgft.com"
pREQ2="blancod@tda-sgft.com"
pOPT="carpios@tda-sgft.com"
vFIni = "20250414T163000Z"  # 10:30 en España (UTC+2)
vFFin = "20250414T164500Z"
vFRec = "20250414T161500Z"  # Salta 15 minutos antes

Crear_Tarea_SOAP(vAuthToken, vTitulo, vEstado, vPrioridad, vLocate, vDescribe, vContent, vSu, vOrganizador, vFIni, vFFin, vFRec)

#Crear_Cita_SOAP(vAuthToken, vTitulo, vEstado, vPrioridad, vLocate, vDescribe, vContent, vSu, vOrganizador, pREQ1, pREQ2, pOPT, vFIni, vFFin, vFRec)
                