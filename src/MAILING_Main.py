# ----------------------------------------------------------------------------------------
#                                  WebScraping BOLSAS Comunicados
# 
# Programa que extraerá información contable de la Bolsa de BIVA Mexico
# Autor: SteveCarpio
# Versión: V2 2025
# ----------------------------------------------------------------------------------------

from   cfg.BOLSAS_librerias import *
from   bolsas.BOLSAS_paso0  import sTv_paso0
from   bolsas.BOLSAS_paso1  import sTv_paso1
from   bolsas.BOLSAS_paso2  import sTv_paso2
from   bolsas.BOLSAS_paso3  import sTv_paso3
from   bolsas.BOLSAS_paso4  import sTv_paso4

var_NombreSalida = 'BOLSAS'
var_SendEmail= 'S'

if len(sys.argv) > 1 :
    var_param1 = sys.argv[1]
    
#tiempo_inicio = dt.now()
tiempo_inicio = dt(2025, 3, 8)

# Restar 1 día a la fecha actual
fecha_reducida = tiempo_inicio - timedelta(days=1)
# Crear variables con los formatos que necesitamos
var_Fechas1 = fecha_reducida.strftime('%Y-%m-%d')  # Formato "2025-03-04"
var_Fechas2 = fecha_reducida.strftime('%d-%m-%Y')  # Formato "04-03-2025"
var_Fechas3 = fecha_reducida.strftime('%Y%m%d')    # Formato "20250304"

os.system("cls")

# Inicializar colorama
init(autoreset=True)

# Inicializar carpetas y borrado de files
sTv_paso0(var_Fechas3)

# ------------------------------- MENU -----------------------------------

# Funciones para los pasos
def paso1():
    print(Fore.GREEN + f"\nEjecutando PASO_1 - BOLSA BMV........ {dt.now()} 👌\n")
    #sTv_paso1()
    print(Fore.GREEN + "\nPaso 1 completado - BOLSA BMV! \n")

def paso2():
    print(Fore.GREEN + f"\nEjecutando PASO_2 - BOLSA BIVA........ {dt.now()} 👌\n")
    #sTv_paso2()
    print(Fore.GREEN + "\nPaso 2 completado - BOLSA BIVA! \n")

def paso3():
    print(Fore.GREEN + f"\nEjecutando PASO_3 - Copiar Resultados BMV/BIVA........ {dt.now()} 👌\n")
    sTv_paso3(var_Fechas3)
    print(Fore.GREEN + "\nPaso 3 completado - Copia de datos BOLSAS BIVA y BMV! \n")

def paso4():
    print(Fore.YELLOW + f"\nEjecutando PASO_4 - Mandar Email........ {dt.now()} 👌\n")
    sTv_paso4(var_NombreSalida, var_Fechas2, var_Fechas3, var_SendEmail)
    print(Fore.YELLOW + "\nPaso 4 completado - Envió del Email! \n")

def todos():
    print(Fore.LIGHTBLUE_EX + "\nEjecutando TODOS los pasos.......................... 💪")
    paso1()
    paso2()
    paso3()
    paso4()
    
    print(Fore.LIGHTBLUE_EX + "¡Todos los pasos completados exitosamente! 🎉 \n")
    print(Fore.CYAN + f"---------------------------------------------------------------------------------------")
    print(Fore.CYAN + f" Tiempo Transcurrido INI: {tiempo_inicio} - FIN: {dt.now()}")
    print(Fore.CYAN + f"---------------------------------------------------------------------------------------")

# Función para limpiar la pantalla (en sistemas basados en UNIX)
def limpiar_pantalla():
    os.system("cls")  

# Menú interactivo
def mostrar_menu(par_FechasSalida):
    limpiar_pantalla()
    print(Fore.MAGENTA + "=" * 37)
    print(Fore.WHITE + "   Bolsa BIVA/BMV (MX): " + par_FechasSalida)
    print(Fore.MAGENTA + "=" * 37)
    print(Fore.WHITE + "        🖥️   MENÚ PRINCIPAL 🖥️")
    print(Fore.MAGENTA + "=" * 37)
    print(Fore.LIGHTBLUE_EX + "0) 🔵 Ejecutar TODOS los pasos   ")
    print(Fore.GREEN        + "1) 🟢 Ejecutar el BOLSA BMV      ")
    print(Fore.GREEN        + "2) 🟢 Ejecutar el BOLSA BIVA     ")
    print(Fore.GREEN        + "3) 🟢 Copiar Resultados BMV/BIVA ")
    print(Fore.YELLOW       + "4) 🟡 Mandar Email               ")
    print(Fore.RED          + "x) ❌ Salir del programa   " + Fore.WHITE + "    (.v2)")
    print(Fore.MAGENTA + "=" * 37)

# Función principal para gestionar el menú
def ejecutar_menu(par_FechasSalida):
    while True:
        mostrar_menu(par_FechasSalida)
        option = input(Fore.WHITE + "Selecciona una opción: ")

        if option   == '0':
            todos()
        elif option == '1':
            paso1()
        elif option == '2':
            paso2()
        elif option == '3':
            paso3()
        elif option == '4':
            paso4()

        elif option.upper() == 'X':
            print(Fore.RED + "\n¡Saliendo del programa! 👋\n")
            break
        else:
            print(Fore.RED + "\n ❌ Opción no válida, por favor elige una opción válida ❌\n")
        
        # Pausa para que el usuario vea los resultados
        input(Fore.WHITE + "Presiona Enter para continuar...")

# Evaluamos como ejecutamos el proceso
if len(sys.argv) > 1 :
    if var_param1 == "RUN-NO-EMAIL":
        var_SendEmail = 'N'
    if "RUN" in var_param1:
        todos()
else:
    input(Fore.WHITE + "Presiona Enter para continuar...")
    ejecutar_menu(var_Fechas1)

# FIN: By Steve Carpio - 2025    
