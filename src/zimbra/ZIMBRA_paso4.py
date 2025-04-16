# ----------------------------------------------------------------------------------------
#  PASO4: PROGRAMA QUE CREARA UNA TAREA  
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

import cfg.ZIMBRA_variables as sTv
from   cfg.ZIMBRA_library import *

# ----------------------------------------------------------------------------------------
#                                  FUNCIONES
# ----------------------------------------------------------------------------------------

def Crear_Tarea_SOAP(pAuthToken, pTitulo, pEstado, pPrioridad, pLocate, pDescribe, pContent, pSu, pFIni, pFFin, pFRec):
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
    response2 = requests.post(sTv.var_UrlSoapZimbra, data=crear_tarea_con_alarma, headers={"Content-Type": "text/xml"}, verify=False)
    print("Respuesta al crear tarea:")
    print(response2.text)

# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------

def sTv_paso4(pAuthToken, var_Fecha1, var_Fecha2, df):

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

    # ----------------- DATOS COMUNES
    vTitulo=f"Tarea Pendiente de {vClavePizzara}: {vIdTarea} : {vIdPlanif}"
    vSu=vTitulo                                                               # Sujeto - Titulo de la Alerta - Pop-up
    vDescribe=f"Tareas Pendientes {vIdTarea} : {vIdPlanif} : {vClavePizzara}" # Descripción de la alerta     - Pop-up
    vContent=f"Tarea Pendiente de {vClavePizzara}\n\nID_TAREA: {vIdTarea}\nID_PLANIF: {vIdPlanif} \nEmisiones: {vEmisiones} \nClase: {vClase}\n\nAsunto: {vAsunto} \n\nDetalle: {vDetalleEvento} \n\nRepositorio: {vRepositorio}"
    vFIni = "20250415T163000Z"                                                # 10:30 en España (UTC+2)
    vFFin = "20250415T184500Z"                                                # 10:45 fin
    vFRec = vFIni                                                             # Fecha y Hora del recordatorio

    vEstado="NEED"                         # NEED:No se ha iniciado |INPR:En progreso |COMP:Completada |WAITING:En espera |DEFERRED:Pospuesta |CANCELLED:Cancelado 
    vPrioridad="1"                         # 1: Alta, 5: Normal, 9: Baja
    vLocate=f"Escribir aquí una nota en caso de problemas con la tarea"  # Ubicación Tarea / Cita

    Crear_Tarea_SOAP(pAuthToken, vTitulo, vEstado, vPrioridad, vLocate, vDescribe, vContent, vSu, vFIni, vFFin, vFRec)

