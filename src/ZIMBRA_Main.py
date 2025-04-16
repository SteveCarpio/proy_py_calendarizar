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

# Parámetro1: Producción o Desarrollo
vEntorno="DEV"
if len(sys.argv) > 1 :
    var_param1 = sys.argv[1]
    vEntorno = var_param1

# Parámetro2: Fecha (opcional)
tiempo_inicio = dt.now()    # = dt(2025, 11, 15)
if len(sys.argv) > 2 :
    var_param2 = sys.argv[2]
    if re.match(r"^\d{4}-\d{2}-\d{2}$", var_param2):
        anio, mes, dia = map(int, var_param2.split('-'))
        tiempo_inicio = dt(anio, mes, dia)
    else:
        print("El formato de fecha debe ser, ejemplo: 2025-07-28")
        input(Fore.WHITE + f"Se ejecutará con el día {tiempo_inicio.strftime('%Y-%m-%d')}")


# Crear fecha con formato.... 
var_Fecha1  = tiempo_inicio.strftime('%Y-%m-%d')  # Formato "2025-03-04"
var_Fecha2  = tiempo_inicio.strftime('%Y%m%d')    # Formato "20250304"


# PASO-1: Leer los avisos diarios del CSV
print("----------------- LEER ARCHIVO CSV -----------------")
try:
    sTv_paso1(var_Fecha1)
except Exception as e:
    print(f"Error al leer el archivo csv de entrada:\n{e}")
    exit(1)

exit(0)

# PASO-2: Crear un token de autenticación para interactuar con la API de Zimbra
print("----------------- CREAR UN TOKEN -----------------")
try:
    vAuthToken = sTv_paso2(vEntorno)
except Exception as e:
    print(f"Error al ejecutar el Paso2: Obtener el Token de Autenticación:\n{e}")
    exit(1)

# PASO-3: Crear una cita en el calendario de Zimbra
print("----------------- CREAR UNA CITA -----------------")
try:
    sTv_paso3(vAuthToken, var_Fecha1, var_Fecha2)
except Exception as e:
    print(f"Error al ejecutar el Paso3: Crear una cita en el calendario Zimbra:\n{e}")
    exit(1)

# PASO-4: Crear una tarea dentro de Zimbra
print("----------------- CREAR UNA TAREA ----------------")
try:
    sTv_paso4(vAuthToken, var_Fecha1, var_Fecha2)
except Exception as e:
    print(f"Error al ejecutar el Paso4: Crear una tarea dentro de Zimbra:\n{e}")
    exit(1)


                