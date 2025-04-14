# ----------------------------------------------------------------------------------------
#                                  ZIMBRA SOAP: Tareas / Citas
#
# Programa que Añadirá información en las tareas y citas del Zimbra
# Autor: SteveCarpio
# Versión: V1 2025
# ----------------------------------------------------------------------------------------

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ----------------------------------------------------------------------------------------
#                               FUNCIONES DE APOYO
# ----------------------------------------------------------------------------------------
def Crear_Token_SOAP(pUrl, pUsuario, pContrasena):

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

def Crear_Cita_SOAP (pUrl, pAuthToken, pTitulo, pEstado, pPrioridad, pLocate, pDescribe, pContent, pSu, pOrganizador, pREQ1, pREQ2, pOPT, pFIni, pFFin, pFRec):
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
    response = requests.post(pUrl, data=crear_cita_con_alarma, headers={"Content-Type": "text/xml"}, verify=False)
    print("Respuesta al crear cita:")
    print(response.text)

def Crear_Tarea_SOAP(pUrl, pAuthToken, pTitulo, pEstado, pPrioridad, pLocate, pDescribe, pContent, pSu, pFIni, pFFin, pFRec):
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
    response2 = requests.post(pUrl, data=crear_tarea_con_alarma, headers={"Content-Type": "text/xml"}, verify=False)
    print("Respuesta al crear tarea:")
    print(response2.text)



# ----------------------------------------------------------------------------------------
#                               INICIO DEL PROGRAMA
# ----------------------------------------------------------------------------------------

# ----------------- DATOS COMUNES TAREA/CITA
vTitulo="Titulo de la TAREA / CITA"
vSu=vTitulo                            # Sujeto - Titulo de la Alerta - Pop-up
vDescribe="DESCRIBE: xxxxx"            # Descripción de la alerta     - Pop-up
vLocate="Localización Clave Pizarra XXXXXXXX 3"     # Ubicación Tarea / Cita
vContent="Contenido de la tarea XXXXXXXX \n xxxxxxxxxx"
vFIni = "20250414T163000Z"             # 10:30 en España (UTC+2)
vFFin = "20250414T164500Z"             # 10:45 fin
vFRec = "20250414T161500Z"             # 10:15 Salta 15 minutos antes
vUrl = "https://zimbra.tda-sgft.com/service/soap"

print("----------------- CREAR LA TOKEN -----------------")
vUsuario = "carpios@tda-sgft.com"
#vUsuario = "talavanf@tda-sgft.com"
#vUsuario = "publicacionesbolsasmx@tda-sgft.com"
vContrasena="G3m4198005$$"
#vContrasena="Mrpotato51.."
#vContrasena="U9d8z?:8K,>2"
vAuthToken = Crear_Token_SOAP(vUrl, vUsuario, vContrasena)

print("----------------- CREAR UNA CITA -----------------")
vEstado1="CONF"                         # CONF: confirmado (por defecto) | TENT: Tentativo/Provisional | CANC: Cancelado
vPrioridad1="5"                         # 1: Alta, 5: Normal (recomendado), 9: Baja
vOrganizador="carpios@tda-sgft.com"     # Email del organizador
pREQ1="talavanf@tda-sgft.com"           # Email de las personas requeridas 1
pREQ2="blancod@tda-sgft.com"            # Email de las personas requeridas n
pOPT="carpios@tda-sgft.com"             # Email de las personas opcionales
Crear_Cita_SOAP(vUrl, vAuthToken, vTitulo, vEstado1, vPrioridad1, vLocate, vDescribe, vContent, vSu, vOrganizador, pREQ1, pREQ2, pOPT, vFIni, vFFin, vFRec)

print("----------------- CREAR UNA TAREA ----------------")
vEstado2="INPR"                         # NEED:No se ha iniciado |INPR:En progreso |COMP:Completada |WAITING:En espera |DEFERRED:Pospuesta |CANCELLED:Cancelado 
vPrioridad2="1"                         # 1: Alta, 5: Normal, 9: Baja
Crear_Tarea_SOAP(vUrl, vAuthToken, vTitulo, vEstado2, vPrioridad2, vLocate, vDescribe, vContent, vSu, vFIni, vFFin, vFRec)


                