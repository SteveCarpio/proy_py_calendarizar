# ----------------------------------------------------------------------------------------
#                                  ZIMBRA SOAP: Tareas / Citas
#
# Programa que agregara información dentro de Zimbra en los apartados de TAREAS y CITAS
# Autor: SteveCarpio
# Versión: V1 2025
# ----------------------------------------------------------------------------------------

from   cfg.ZIMBRA_library      import *
from   zimbra.ZIMBRA_paso0     import sTv_paso0
from   zimbra.ZIMBRA_paso1     import sTv_paso1
from   zimbra.ZIMBRA_paso2     import sTv_paso2
from   zimbra.ZIMBRA_paso3     import sTv_paso3
from   zimbra.ZIMBRA_paso4     import sTv_paso4

# ----------------------------------------------------------------------------------------
#                               INICIO DEL PROGRAMA
# ----------------------------------------------------------------------------------------

# Inicializar colorama
init(autoreset=True)

# Parámetro1: Producción o Desarrollo
vEntorno="DEV"
if len(sys.argv) > 1 :
    var_param1 = sys.argv[1]
    vEntorno = var_param1

# Parámetro2: Fecha (opcional)
#tiempo_inicio = dt(2025, 4, 17)    # = dt(2025, 3, 19) | dt.now()
tiempo_inicio = dt.now()    # = dt(2025, 3, 19) | dt.now()
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

# ----------------------------------------------------------------------------------------
#                               PASOS DE EJECUCIÓN 
# ----------------------------------------------------------------------------------------

# PASO-0: Validar requisitos del programa ------------------------------------------------
print(Fore.MAGENTA + "\n----------------------------------- [ Inicio del Proceso ] -----------------------------------\n")
try:
    sTv_paso0(vEntorno)
except Exception as e:
    print(f"Error Paso0: Validando requisitos previos:\n{e}")
    sys.exit(1)

# PASO-1: Leer los avisos diarios del CSV ------------------------------------------------
print(Fore.YELLOW + "\n----------------- PASO-1: LEER ARCHIVO DE EVENTOS DIARIOS CSV -----------------")
try:
    df = sTv_paso1(var_Fecha1)
except Exception as e:
    print(f"Error Paso1: Tratar el archivo csv de entrada:\n{e}")
    sys.exit(1)

# PASO-2: Crear un token de autenticación para interactuar con la API de Zimbra ----------
print(Fore.GREEN + "\n----------------- PASO-2: CREAR UN TOKEN DE ZIMBRA -----------------")
try:
    vAuthToken = sTv_paso2(vEntorno)
except Exception as e:
    print(f"Error Paso2: Obtener el Token de Autenticación:\n{e}")
    sys.exit(1)

# PASO-3: Crear una cita en el calendario de Zimbra --------------------------------------
print(Fore.CYAN + "\n----------------- PASO-3: AGREGAR CITA A LA AGENDA DE ZIMBRA -----------------")
try:
    sTv_paso3(vAuthToken, var_Fecha1, var_Fecha2, df)
except Exception as e:
    print(f"Error Paso3: Crear una cita en el calendario Zimbra:\n{e}")
    sys.exit(1)

# PASO-4: Crear una tarea dentro de Zimbra -----------------------------------------------
print(Fore.CYAN + "\n----------------- PASO-4: AGREGAR TAREAS A REALIZAR HOY EN ZIMBRA ----------------")
try:
    sTv_paso4(vAuthToken, var_Fecha1, var_Fecha2, df)
except Exception as e:
    print(f"Error Paso4: Crear una tarea dentro de Zimbra:\n{e}")
    sys.exit(1)

print(Fore.MAGENTA + "\n----------------------------------- [ Proceso Finalizado ] -----------------------------------\n")
