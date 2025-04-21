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
    
    pContent = f"{pContent}\n--------------------------------------------------------------\nNotas:\n"

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


def Recupera_Datos_DataFrame(pAuthToken, var_Fecha1, var_Fecha2, df):
    
    n=0
    # ----------------- Importar valores para la Tarea
    for _, fila in df.iterrows():
        n = n + 1
        vIdTarea = fila['ID_TAREA']
        vIdPlanif = fila['ID_PLANIF']
        vClavePizzara = fila['CLAVE_PIZARRA']
        vEmisiones = fila['EMISIONES']
        vClase = fila['CLASE']
        vAsunto = fila['ASUNTO']
        vDetalleEvento = fila['DETALLE_DEL_EVENTO']
        vRepositorio = fila['REPOSITORIO2']

        # Crear el string con el formato deseado
        vContent = (
            f"Clave Pizarra: {vClavePizzara}\n"
            f"Id Tarea: {vIdTarea}\n"
            f"Id Planificación: {vIdPlanif}\n"
            f"Emisiones: {vEmisiones}\n"
            f"Clase: {vClase}\n\n"
            f"Asunto: {vAsunto}\n\n"
            f"Detalle del Evento:\n{vDetalleEvento}\n\n"
            f"Repositorio: {vRepositorio}\n\n"
        )

        vTitulo=f"Tarea Pendiente de {vClavePizzara}: {vIdTarea} : {vIdPlanif}"
        vSu=vTitulo                                                          # Sujeto - Titulo de la Alerta - Pop-up
        vDescribe=vTitulo                                                    # Descripción de la alerta     - Pop-up
        vFIni = f"{var_Fecha2}T073000Z"                                      # 10:30 en España (UTC+2)
        vFFin = f"{var_Fecha2}T174500Z"                                      # 10:45 fin
        vFRec = vFIni                                                        # Fecha y Hora del recordatorio
        vEstado="NEED"                                                       # NEED:No se ha iniciado |INPR:En progreso |COMP:Completada |WAITING:En espera |DEFERRED:Pospuesta |CANCELLED:Cancelado 
        vPrioridad="1"                                                       # 1: Alta, 5: Normal, 9: Baja
        vLocate=f"Escribir aquí una nota en caso de problemas con la tarea"  # Ubicación Tarea / Cita

        print(f"- Creando tarea number: {n}")
        Crear_Tarea_SOAP(pAuthToken, vTitulo, vEstado, vPrioridad, vLocate, vDescribe, vContent, vSu, vFIni, vFFin, vFRec)
    


# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------

def sTv_paso4(pAuthToken, var_Fecha1, var_Fecha2, df):

    # Función para recuperar datos del dataframe importado
    Recupera_Datos_DataFrame(pAuthToken, var_Fecha1, var_Fecha2, df)


    
  



