# ----------------------------------------------------------------------------------------
#                                  ZIMBRA SOAP: Tareas / Citas
#
# Programa que Añadirá información en las tareas y citas del Zimbra
# Autor: SteveCarpio
# Versión: V1 2025
# ----------------------------------------------------------------------------------------

from   cfg.ZIMBRA_library import *
from   zimbra.ZIMBRA_paso0     import sTv_paso0
from   zimbra.ZIMBRA_paso1     import sTv_paso1
from   zimbra.ZIMBRA_paso2     import sTv_paso2
from   zimbra.ZIMBRA_paso3     import sTv_paso3
from   zimbra.ZIMBRA_paso4     import sTv_paso4


# ----------------------------------------------------------------------------------------
#                               INICIO DEL PROGRAMA
# ----------------------------------------------------------------------------------------

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
vFIni = "20250415T163000Z"                                                # 10:30 en España (UTC+2)
vFFin = "20250415T184500Z"                                                # 10:45 fin
vFRec = vFIni                                                             # Fecha y Hora del recordatorio

print("----------------- CREAR UN TOKEN -----------------")
vUsuario = "carpios@tda-sgft.com"
#vUsuario = "talavanf@tda-sgft.com"
#vUsuario = "publicacionesbolsasmx@tda-sgft.com"
vContrasena="G3m4198005$$"
#vContrasena="Mrpotato51.."
#vContrasena="U9d8z?:8K,>2"
vAuthToken = sTv_paso2(vUrl, vUsuario, vContrasena)

print("----------------- CREAR UNA CITA -----------------")
vEstado1="CONF"                         # CONF: confirmado (por defecto) | TENT: Tentativo/Provisional | CANC: Cancelado
vPrioridad1="5"                         # 1: Alta, 5: Normal (recomendado), 9: Baja
vOrganizador="carpios@tda-sgft.com"     # Email del organizador
pREQ1="talavanf@tda-sgft.com"           # Email de las personas requeridas 1
pREQ2="blancod@tda-sgft.com"            # Email de las personas requeridas n
pOPT="carpios@tda-sgft.com"             # Email de las personas opcionales
vLocate1=f""                            # Ubicación Tarea / Cita
sTv_paso3(vUrl, vAuthToken, vTitulo, vEstado1, vPrioridad1, vLocate1, vDescribe, vContent, vSu, vOrganizador, pREQ1, pREQ2, pOPT, vFIni, vFFin, vFRec)

print("----------------- CREAR UNA TAREA ----------------")
vEstado2="NEED"                         # NEED:No se ha iniciado |INPR:En progreso |COMP:Completada |WAITING:En espera |DEFERRED:Pospuesta |CANCELLED:Cancelado 
vPrioridad2="1"                         # 1: Alta, 5: Normal, 9: Baja
vLocate2=f"Escribir aquí nota personal si no se puede finalizar la tarea"  # Ubicación Tarea / Cita
sTv_paso4(vUrl, vAuthToken, vTitulo, vEstado2, vPrioridad2, vLocate2, vDescribe, vContent, vSu, vFIni, vFFin, vFRec)


                