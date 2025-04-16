# ----------------------------------------------------------------------------------------
#  PASO3: PROGRAMA QUE CREARA UNA CITA  
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

import cfg.ZIMBRA_variables as sTv
from   cfg.ZIMBRA_library import *

# ----------------------------------------------------------------------------------------
#                                  FUNCIONES
# ----------------------------------------------------------------------------------------

def Crear_Cita_SOAP(pAuthToken, pTitulo, pEstado, pPrioridad, pLocate, pDescribe, pContent, pSu, pOrganizador, pREQ1, pREQ2, pOPT, pFIni, pFFin, pFRec):
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
    response = requests.post(sTv.var_UrlSoapZimbra, data=crear_cita_con_alarma, headers={"Content-Type": "text/xml"}, verify=False)
    print("Respuesta al crear cita:")
    print(response.text)

def Recupera_Datos_DataFrame(df, var_Fecha1):
    
    # ----------------- Importar valores para la Cita
    vIdTarea="TARE000007"
    vIdPlanif="PLAN000068"
    vClavePizzara="GASA"
    vEmisiones="Todas"
    vClase="OTROS REPORTES"
    vAsunto="Reporte de los Seguros Contratados (A SOLICITUD NUESTRA)"
    vDetalleEvento="Debe entregarnos, si así se lo solicitamos por escrito, un reporte completo respecto a los seguros contratados de forma anual, durante los 45 Días Hábiles siguientes al cierre de cada año."
    vRepositorio="https://repo.titulizaciondeactivos.com/s/YeLHrsajidFkyax?dir=/DOCUMENTACION/ARA"

    vTitulo=f"Tarea Pendiente de {vClavePizzara}: {vIdTarea} : {vIdPlanif}"
    vContent=f"Tarea Pendiente de {vClavePizzara}\n\nID_TAREA: {vIdTarea}\nID_PLANIF: {vIdPlanif} \nEmisiones: {vEmisiones} \nClase: {vClase}\n\nAsunto: {vAsunto} \n\nDetalle: {vDetalleEvento} \n\nRepositorio: {vRepositorio}"
    return vTitulo, vContent

# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------

def sTv_paso3(pAuthToken, var_Fecha1, var_Fecha2, df): 

    # Función para recuperar datos del dataframe importado
    vTitulo, vContent = Recupera_Datos_DataFrame(df, var_Fecha1)
    
    # Valores para el XML de CITAS
    vFIni = f"{var_Fecha2}T073000Z"         # (UTC+0) sumar 2horas calcular la hora de Spain
    vFFin = f"{var_Fecha2}T094500Z"         # (UTC+0) sumar 2horas calcular la hora de Spain
    vFRec = vFIni                           # (UTC+0) sumar 2horas calcular la hora de Spain
    vSu=vTitulo                             # Sujeto - Titulo de la Alerta - Pop-up
    vDescribe=vTitulo                       # Descripción de la alerta     - Pop-up
    vEstado="CONF"                          # CONF: confirmado (por defecto) | TENT: Tentativo/Provisional | CANC: Cancelado
    vPrioridad="5"                          # 1: Alta, 5: Normal (recomendado), 9: Baja
    vOrganizador="carpios@tda-sgft.com"     # Email del organizador
    vREQ1="talavanf@tda-sgft.com"           # Email de las personas requeridas 1
    vREQ2="blancod@tda-sgft.com"            # Email de las personas requeridas n
    vOPT="carpios@tda-sgft.com"             # Email de las personas opcionales
    vLocate=f""                             # Ubicación Tarea / Cita

    # Función que sirve para crear una CITA usando SOAP
    Crear_Cita_SOAP(pAuthToken, vTitulo, vEstado, vPrioridad, vLocate, vDescribe, vContent, vSu, vOrganizador, vREQ1, vREQ2, vOPT, vFIni, vFFin, vFRec)


