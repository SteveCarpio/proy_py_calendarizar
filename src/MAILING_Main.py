# ----------------------------------------------------------------------------------------
#                                  App Python envió de Email Eventos
# 
# Programa que envía email a CiBanco con los eventos a cumplir fecha de cumplimientos
# Autor: SteveCarpio
# Versión: V1 2025
# ----------------------------------------------------------------------------------------

from   cfg.MAILING_library import *
from   mailing.MAILING_paso0     import sTv_paso0
from   mailing.MAILING_paso1     import sTv_paso1
from   mailing.MAILING_paso2     import sTv_paso2

var_NombreSalida = 'MAILING'
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
#sTv_paso0(var_NombreSalida, var_Fechas3)

# ------------------------------- MENU -----------------------------------

# Funciones para los pasos
def paso1():
    print(Fore.YELLOW + f"\nEjecutando PASO_1........ {dt.now()} 👌\n")
    sTv_paso1()
    print(Fore.YELLOW + "\nPaso 1 completado! \n")

def paso2():
    print(Fore.GREEN + f"\nEjecutando PASO_2........ {dt.now()} 👌\n")
    sTv_paso2()
    print(Fore.GREEN + "\nPaso 2 completado! \n")

def paso3():
    print(Fore.GREEN + f"\nEjecutando PASO_3........ {dt.now()} 👌\n")
    #sTv_paso3(var_NombreSalida, var_Fechas1)
    print(Fore.GREEN + "\nPaso 3 completado! \n")

def paso4():
    print(Fore.GREEN + f"\nEjecutando PASO_4........ {dt.now()} 👌\n")
    #sTv_paso4(var_NombreSalida, var_Fechas1)
    print(Fore.GREEN + "\nPaso 4 completado! \n")

def paso5():
    print(Fore.YELLOW + f"\nEjecutando PASO_5........ {dt.now()} 👌\n")
    #sTv_paso5(var_NombreSalida, var_Fechas2, var_Fechas3, var_SendEmail)
    print(Fore.YELLOW + "\nPaso 5 completado! \n")

def pasoHelp():
    os.system("cls")
    print(Fore.MAGENTA + "=" * 94)
    print(Fore.MAGENTA + "                         Proceso Mailing Eventos CiBanco")
    print(Fore.MAGENTA + "=" * 94)
    print("")
    print(Fore.WHITE + "Servidor:")
    print(Fore.WHITE + "    IP: 10.10.30.55 (Python)")
    print(Fore.WHITE + "    Usuario: Fiduciario")
    print(Fore.WHITE + "    Contraseña: Gestionada por Cerberus")
    print("")
    print(Fore.WHITE + "Ruta raíz:")
    print(Fore.WHITE + "    C:\\MisCompilados\\PROY_CALENDARIZAR\\")
    print("")
    print(Fore.WHITE + "Ejecución:")
    print(Fore.WHITE + "    MAILING_Main_v1.exe RUN-NO-EMAIL")
    print("")
    print(Fore.WHITE + "Parámetros:")
    print(Fore.WHITE + "    [vació]: Muestra el menú actual")
    print(Fore.WHITE + "    RUN: Ejecuta el proceso enviando el correo de la Bolsa correspondiente")
    print(Fore.WHITE + "    RUN-NO-EMAIL: Ejecuta el proceso sin enviar el correo")
    print("")
    print(Fore.WHITE + "Planificación:")
    print(Fore.WHITE + "    Lun, Mar, Mié, Jue y Vie: 08:50h")
    print(Fore.WHITE + "    Sáb, Dom: 13:00h")
    print("")
    print(Fore.WHITE + "Pasos de ejecución:")
    print("")
    print(Fore.YELLOW + "    1) Selenium-WebScraping 'biva.mx': Métodos empleados.. XPath, Html.PageSource.")
    print(Fore.WHITE + "       Tener en cuenta el explorador y el driver de google, tener acceso fluido de internet para no tener")
    print(Fore.WHITE + "       problemas de red, no es recomendable usar el explorador Google mientras este en funcionamiento.")
    print("")
    print(Fore.GREEN + "    2) Beautifulsoup y Pandas: Parsear Html y generación de excel de apoyo desde DataFrame con Pandas")
    print(Fore.WHITE + "       Se creará archivos excel con la información de apoyo para el siguiente paso.")
    print("")
    print(Fore.GREEN + "    3) Pandas: Agregar ID-Emisores")
    print(Fore.WHITE + "       Creará archivos excel con los ID de los emisores filtrador por el usuario.")
    print("")
    print(Fore.GREEN + "    4) Pandas: Preparación del informe final")
    print(Fore.WHITE + "       Creará un excel con la información final de IdEmisores, datos del WebScraping y datos de los destinatarios.")
    print("")
    print(Fore.BLUE  + "    5) Pandas y Smtplib: Envió del email")
    print(Fore.WHITE + "       Si existen datos se enviará un email en formato html desde un DataFrame.")
    print("")
    print(Fore.WHITE + "Dependencias importantes:")
    print("")
    print(Fore.WHITE + "    - Google Chrome:")
    print(Fore.WHITE + "        Es fundamental tener instalada una versión estable (no Beta).")
    print("")
    print(Fore.WHITE + "    - ChromeDriver:")
    print(Fore.WHITE + "        Debe coincidir con la versión de Google Chrome instalada.")
    print(Fore.WHITE + "        Ruta del binario: C:\\MisCompilados\\cfg\\chromedriver-win32\\chromedriver.exe")
    print(Fore.WHITE + "        Para otras versiones: C:\\MisCompilados\\cfg\\chromedriver-win32\\1??\\")
    print("")
    print(Fore.WHITE + "    - Acceso a las URL:")
    print(Fore.WHITE + "        https://www.biva.mx/")
    print("")
    print(Fore.MAGENTA + "=" * 94)
    print(Fore.WHITE + "Para más ayuda, contactar con: SteveCarpio 'carpios@tda-sgft.com' (stv.madrid@gmail.com) ")
    print(Fore.WHITE + "Versión 3 - 2025")
    print(Fore.MAGENTA + "=" * 94)

def todos():
    print(Fore.WHITE + "\nEjecutando TODOS los pasos.......................... 💪")
    paso1()
    paso2()
    paso3()
    paso4()
    paso5()
    print(Fore.WHITE + "¡Todos los pasos completados exitosamente! 🎉 \n")
    print(Fore.MAGENTA + f"---------------------------------------------------------------------------------------")
    print(Fore.WHITE + f" Tiempo Transcurrido INI: {tiempo_inicio} - FIN: {dt.now()}")
    print(Fore.MAGENTA + f"---------------------------------------------------------------------------------------")

# Función para limpiar la pantalla (en sistemas basados en UNIX)
def limpiar_pantalla():
    os.system("cls")  

# Menú interactivo
def mostrar_menu(par_FechasSalida):
    limpiar_pantalla()
    print(Fore.MAGENTA + "=" * 37)
    print(Fore.WHITE   + "     Mailing CiBanco:  " + par_FechasSalida)
    print(Fore.MAGENTA + "=" * 37)
    print(Fore.WHITE   + "        🖥️   MENÚ PRINCIPAL 🖥️")
    print(Fore.MAGENTA + "=" * 37)
    print(Fore.WHITE   + "0) ⚪ Ejecutar TODOS los pasos   ")
    print("")
    print(Fore.YELLOW  + "1) 🟡 Ejecutar el PASO_1         ")
    print(Fore.GREEN   + "2) 🟢 Ejecutar el PASO_2         ")
    print(Fore.GREEN   + "3) 🟢 Ejecutar el PASO_3         ")
    print(Fore.GREEN   + "4) 🟢 Ejecutar el PASO_4         ")
    print(Fore.BLUE    + "5) 🔵 Ejecutar el PASO_5         ")
    print("")
    print(Fore.MAGENTA + "?) 🟣 Ayuda                      ")
    print(Fore.RED     + "x) ❌ Salir del programa   " + Fore.WHITE + "    (.v3)")
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
        elif option == '5':
            paso5()
        elif option == '?':
            pasoHelp()
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
