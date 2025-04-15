# ----------------------------------------------------------------------------------------
#                                  ZIMBRA SOAP: Tareas / Citas
#
# Programa que Añadirá información en las tareas y citas del Zimbra
# Autor: SteveCarpio
# Versión: V1 2025
# ----------------------------------------------------------------------------------------

from   cfg.MAILING_library import *
from   zimbra.ZIMBRA_paso0     import sTv_paso0
from   zimbra.ZIMBRA_paso1     import sTv_paso1
from   zimbra.ZIMBRA_paso2     import sTv_paso2

# ----------------------------------------------------------------------------------------
#                               FUNCIONES DE APOYO
# ----------------------------------------------------------------------------------------




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

# Importación del CSV, avisos Diarios


# ----------------- DATOS ZIMBRA
vUrl = "https://zimbra.tda-sgft.com/service/soap"

# ----------------- DATOS ENTRADA
vFechaAviso="2026-03-02"
vIdTarea="TARE000007"
vIdPlanif="PLAN000068"
vClavePizzara="GASA"
vEmisiones="Todas"
vClase="OTROS REPORTES"
vAsunto="Reporte de los Seguros Contratados (A SOLICITUD NUESTRA)"
vDetalleEvento="Debe entregarnos, si así se lo solicitamos por escrito, un reporte completo respecto a los seguros contratados de forma anual, durante los 45 Días Hábiles siguientes al cierre de cada año."
vRepositorio="https://repo.titulizaciondeactivos.com/s/YeLHrsajidFkyax?dir=/DOCUMENTACION/ARA"

# ----------------- DATOS COMUNES TAREA/CITA
vTitulo=f"Tarea Pendiente de {vClavePizzara}: {vIdTarea} : {vIdPlanif}"
vSu=vTitulo                                                               # Sujeto - Titulo de la Alerta - Pop-up
vDescribe=f"Tareas Pendientes {vIdTarea} : {vIdPlanif} : {vClavePizzara}" # Descripción de la alerta     - Pop-up
vContent=f"Tarea Pendiente de {vClavePizzara}\n\nID_TAREA: {vIdTarea}\nID_PLANIF: {vIdPlanif} \nEmisiones: {vEmisiones} \nClase: {vClase}\n\nAsunto: {vAsunto} \n\nDetalle: {vDetalleEvento} \n\nRepositorio: {vRepositorio}"
vFIni = "20250414T163000Z"                                                # 10:30 en España (UTC+2)
vFFin = "20250414T184500Z"                                                # 10:45 fin
vFRec = vFIni                                                             # Fecha y Hora del recordatorio

print("----------------- CREAR LA TOKEN -----------------")
vUsuario = "carpios@tda-sgft.com"
#vUsuario = "talavanf@tda-sgft.com"
#vUsuario = "publicacionesbolsasmx@tda-sgft.com"
vContrasena="G3m4198005$$"
#vContrasena="Mrpotato51.."
#vContrasena="U9d8z?:8K,>2"
#vAuthToken = Crear_Token_SOAP(vUrl, vUsuario, vContrasena)
vAuthToken = sTv_paso2(vUrl, vUsuario, vContrasena)

print("----------------- CREAR UNA CITA -----------------")
vEstado1="CONF"                         # CONF: confirmado (por defecto) | TENT: Tentativo/Provisional | CANC: Cancelado
vPrioridad1="5"                         # 1: Alta, 5: Normal (recomendado), 9: Baja
vOrganizador="carpios@tda-sgft.com"     # Email del organizador
pREQ1="talavanf@tda-sgft.com"           # Email de las personas requeridas 1
pREQ2="blancod@tda-sgft.com"            # Email de las personas requeridas n
pOPT="carpios@tda-sgft.com"             # Email de las personas opcionales
vLocate1=f""                            # Ubicación Tarea / Cita
Crear_Cita_SOAP(vUrl, vAuthToken, vTitulo, vEstado1, vPrioridad1, vLocate1, vDescribe, vContent, vSu, vOrganizador, pREQ1, pREQ2, pOPT, vFIni, vFFin, vFRec)

print("----------------- CREAR UNA TAREA ----------------")
vEstado2="NEED"                         # NEED:No se ha iniciado |INPR:En progreso |COMP:Completada |WAITING:En espera |DEFERRED:Pospuesta |CANCELLED:Cancelado 
vPrioridad2="1"                         # 1: Alta, 5: Normal, 9: Baja
vLocate2=f"Escribir aquí nota personal si no se puede finalizar la tarea"  # Ubicación Tarea / Cita
Crear_Tarea_SOAP(vUrl, vAuthToken, vTitulo, vEstado2, vPrioridad2, vLocate2, vDescribe, vContent, vSu, vFIni, vFFin, vFRec)


                