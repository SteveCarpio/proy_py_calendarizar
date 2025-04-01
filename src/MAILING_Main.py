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
from   mailing.MAILING_paso3     import sTv_paso3
from   mailing.MAILING_paso4     import sTv_paso4

tiempo_inicio2 = dt.now()


# Parámetro1: Diaria o Mensual
if len(sys.argv) > 1 :
    var_param1 = sys.argv[1]

# Parámetro2: Producción o Desarrollo
var_Entorno="DEV"
if len(sys.argv) > 2 :
    var_param2 = sys.argv[2]
    var_Entorno = var_param2

# Parámetro3: Fecha (opcional)
tiempo_inicio = dt.now()
#tiempo_inicio = dt(2025, 11, 15)
if len(sys.argv) > 3 :
    var_param3 = sys.argv[3]
    if re.match(r"^\d{4}-\d{2}-\d{2}$", var_param3):
        anio, mes, dia = map(int, var_param3.split('-'))
        tiempo_inicio = dt(anio, mes, dia)
    else:
        print("El formato de fecha debe ser, ejemplo: 2025-07-28")
        input(Fore.WHITE + f"Se ejecutará con el día {tiempo_inicio.strftime('%Y-%m-%d')}")


# Restar 1 día a la fecha actual - en este proyecto no procede por eso le resto CERO días
fecha_reducida = tiempo_inicio - timedelta(days=0)

# Crear variables con los formatos que necesitamos
var_Fecha  = fecha_reducida.strftime('%Y-%m-%d')  # Formato "2025-03-04"
var_Ano    = fecha_reducida.strftime('%Y')        # Formato "2025"
var_Mes    = fecha_reducida.strftime('%m')        # Formato "04"
var_Dia    = fecha_reducida.strftime('%d')        # Formato "01"

os.system("cls")

# Inicializar colorama
init(autoreset=True)

# Inicializar carpetas y borrado de files
sTv_paso0()

# ------------------------------- MENU -----------------------------------

# Funciones para los pasos
def paso1():
    print(Fore.YELLOW + f"\nEjecutando PASO_1........ {dt.now()} 👌\n")
    sTv_paso1()
    print(Fore.YELLOW + "\nPaso 1 completado! \n")

def paso2():
    print(Fore.GREEN + f"\nEjecutando PASO_2........ {dt.now()} 👌\n")
    #sTv_paso2()
    print("   ¡¡ Paso deshabilitado por motivos de conflictos entre las versiones de 32 y 64 bits !!\n")
    print("      Driver ODBC 32bits")
    print("      Access 32bits")
    print("      vs")
    print("      Arquitectura Windows 64bits")
    print("      Python 64bits ")
    print(Fore.GREEN + "\nPaso 2 completado! \n")

def paso3():
    print(Fore.BLUE + f"\nEjecutando PASO_3........ {dt.now()} 👌\n")
    sTv_paso3(var_Fecha, var_Entorno)
    print(Fore.BLUE + "\nPaso 3 completado! \n")

def paso4():
    print(Fore.BLUE + f"\nEjecutando PASO_4........ {dt.now()} 👌\n")
    sTv_paso4(tiempo_inicio, var_Entorno)
    print(Fore.BLUE + "\nPaso 4 completado! \n")

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
    print(Fore.MAGENTA + "Servidor:")
    print("")
    print(Fore.WHITE   + "    IP: 10.10.30.55 (Python)")
    print(Fore.WHITE   + "    Usuario: Fiduciario")
    print(Fore.WHITE   + "    Contraseña: Gestionada por Cerberus")
    print("")
    print(Fore.MAGENTA + "Ruta raíz:")
    print("")
    print(Fore.WHITE   + "    C:\\MisCompilados\\PROY_CALENDARIZAR\\")
    print("")
    print(Fore.MAGENTA + "Ejecución:")
    print("")
    print(Fore.WHITE   + "    PowerShell: .\\MAILING_Main_v1.exe")
    print(Fore.WHITE   + "        * Desde un cmd tradicional no funcionará por el uso de librerías colorama")
    print(Fore.WHITE   + "          que no están soportadas por un cmd estándar. (Update CMD to Colorama)")
    print("")
    print(Fore.MAGENTA + "Parámetros [RUN-DIARIO/RUN-MENSUAL] [DEV/PRO] [opcional AAAA-MM-DD]:")
    print("")
    print(Fore.WHITE   + "    (0) [vació]: Muestra el menú actual")
    print(Fore.WHITE   + "    (1) RUN-DIARIO: Ejecuta el proceso diario y envía el email en modo DEV.   ")
    print(Fore.WHITE   + "    (1) RUN-MENSUAL: Ejecuta el proceso mensual y envía el email en modo DEV. ")
    print(Fore.WHITE   + "    (2) DEV: Ejecuta el proceso y manda el email a la lista desarrollo.       ")
    print(Fore.WHITE   + "    (2) PRO: Ejecuta el proceso y manda el email a la lista usuarios finales. ")
    print(Fore.WHITE   + "    (3) AAAA-MM-DD: Ejecuta el proceso y para el día pasado por parámetro.    ")
    print("")
    print(Fore.MAGENTA + "Planificación:")
    print("")
    print(Fore.WHITE   + "    Proceso Diario: Lun, Mar, Mié, Jue, Vie, Sab y Dom: 7:00h ")
    print(Fore.WHITE   + "    Proceso Mensual: Cada 15 días, día 1 y 15: 9:00h ")
    print("")
    print(Fore.MAGENTA + "Pasos de ejecución:")
    print("")
    print(Fore.YELLOW  + "    d) Ejecución de todo el proceso DIARIO")
    print(Fore.WHITE   + "       Se ejecutarán todos los pasos para el proceso Diario.")
    print("")
    print(Fore.GREEN   + "    m) Ejecución de todo el proceso MENSUAL")
    print(Fore.WHITE   + "       Se ejecutarán todos los pasos para el proceso Mensual.")
    print("")
    print(Fore.GREEN   + "    1) Copia los datos RED --> LOCAL")
    print(Fore.WHITE   + "       Buscará si existen nuevas entradas CSV generados por VBA.")
    print("")
    print(Fore.GREEN   + "    2) Lee los datos de la BBDD de Eventos")
    print(Fore.WHITE   + "       Por temas de conflicto ODBC(32/64) estará deshabilitado.")
    print("")
    print(Fore.BLUE    + "    3) Proceso envío de email DIARIO")
    print(Fore.WHITE   + "       Solo si existen avisos se enviará un email en formato html.")
    print(Fore.WHITE   + "       * Importante ejecutar antes el paso 1.")
    print("")
    print(Fore.BLUE    + "    4) Proceso envío de email MENSUAL")
    print(Fore.WHITE   + "       Se enviará siempre un email en formato html de la existencia de avisos.")
    print(Fore.WHITE   + "       * Importante ejecutar antes el paso 1.")
    print("")
    print(Fore.MAGENTA + "Dependencias importantes:")
    print("")
    print(Fore.WHITE   + "    * Existen otras dependencia técnicas que obviamos, como internet, ios, mem, ram, disco, etc..")    
    print("")
    print(Fore.LIGHTWHITE_EX   + "    - Rutas:")
    print(Fore.WHITE   + "          * Los csv de entrada estarán en estas rutas accesibles para el programa.")
    print("")
    print(Fore.WHITE   + "          C:\\MisCompilados\\PROY_CALENDARIZAR\\BBDD\\                  *** Raíz del programa en el servidor Python   ")          
    print(Fore.WHITE   + "          H:\\MisCompilados\\PROY_CALENDARIZAR\\BBDD (requerido)       *** Ruta Mapeada en el servidor de Python      ")  
    print(Fore.WHITE   + "          H:\\Proyectos\\Python\\MisCompilados\\PROY_CALENDARIZAR\\BBDD  *** Ruta Mapeada en los pc's de los usuarios ")
    print("")
    print(Fore.LIGHTWHITE_EX   + "    - Files CSV:")
    print(Fore.WHITE   + "          C_Export_CSV_Diario.csv  - encoding='latin1' ")
    print(Fore.WHITE   + "          C_Export_CSV_Mensual.csv - encoding='latin1' ")
    print("")
    print(Fore.LIGHTWHITE_EX   + "    - Delimitador files CSV:")
    print(Fore.WHITE   + "          \"valor1\" ; \"valor2\" ")
    print(Fore.WHITE   + "              * El programa está preparado para recibir más o menos campos según haga falta.")
    print(Fore.WHITE   + "              * teniendo en cuenta de enviar siempre los campos claves Fechas_Aviso y Fecha_Limite.")
    print("")
    print(Fore.MAGENTA + "=" * 94)
    print(Fore.WHITE   + "Para más ayuda, contactar con: SteveCarpio 'carpios@tda-sgft.com' (stv.madrid@gmail.com) ")
    print(Fore.WHITE   + "Versión 1 - 2025")
    print(Fore.MAGENTA + "=" * 94)

def todos_diario():
    print(Fore.WHITE   + "\nEjecutando TODOS los pasos DIARIOS.......................... 💪")
    paso1()
    paso2()
    paso3()
    print(Fore.WHITE   + "¡Todos los pasos DIARIOS completados exitosamente! 🎉 \n")
    print(Fore.MAGENTA + f"---------------------------------------------------------------------------------------")
    print(Fore.WHITE   + f" Tiempo Transcurrido INI: {tiempo_inicio2} - FIN: {dt.now()}")
    print(Fore.MAGENTA + f"---------------------------------------------------------------------------------------")

def todos_mensual():
    print(Fore.WHITE   + "\nEjecutando TODOS los pasos MENSUAL.......................... 💪")
    paso1()
    paso2()
    paso4()
    print(Fore.WHITE   + "¡Todos los pasos MENSUAL completados exitosamente! 🎉 \n")
    print(Fore.MAGENTA + f"---------------------------------------------------------------------------------------")
    print(Fore.WHITE   + f" Tiempo Transcurrido INI: {tiempo_inicio2} - FIN: {dt.now()}")
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
    print(Fore.WHITE   + "d) ⚪ Ejecutar TODOS los pasos DIARIO  ")
    print(Fore.WHITE   + "m) ⚪ Ejecutar TODOS los pasos MENSUAL  ")
    print("")
    print(Fore.YELLOW  + "1) 🟡 Copiar datos:  RED --> LOCAL            ")
    print(Fore.GREEN   + "2) 🟢 Leer datos BBDD Eventos (no habilitado) ") # conflicto 64vs32 bits --
    print(Fore.BLUE    + "3) 🔵 Envío Email Diario                      ") 
    print(Fore.BLUE    + "4) 🔵 Envió Email Mensual                     ")
    print("")
    print(Fore.MAGENTA + "?) 🟣 Ayuda                      ")
    print(Fore.RED     + "x) ❌ Salir del programa   " + Fore.WHITE + "    (.v1)")
    print(Fore.MAGENTA + "=" * 37)

# Función principal para gestionar el menú
def ejecutar_menu(par_FechasSalida):
    while True:
        mostrar_menu(par_FechasSalida)
        option = input(Fore.WHITE + "Selecciona una opción: ")

        if option.upper()   == 'D':
            todos_diario()
        elif option.upper()   == 'M':
            todos_mensual()
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
        elif option == '?' or option.upper() == 'H':
            pasoHelp()
        elif option.upper() == 'X':
            print(Fore.RED + "\n¡Saliendo del programa! 👋\n")
            break
        else:
            print(Fore.RED + "\n ❌ Opción no válida, por favor elige una opción válida ❌\n")
        
        # Pausa para que el usuario vea los resultados
        input(Fore.WHITE + "Presiona Enter para continuar...")

# Evaluamos como ejecutamos el proceso
if len(sys.argv) > 1:
    match(var_param1.upper()):
        case "?" | "H" | "HELP" | "AYUDA":
            pasoHelp()
        case "RUN-DIARIO":
            todos_diario()
        case "RUN-MENSUAL":
            todos_mensual()
        case _:
            print("Parámetro incorrecto: \n Modo1: RUN-DIARIO  [PRO/DEV] [opcional: AAAA-MM-DD] \n Modo2: RUN-MENSUAL [PRO/DEV] [opcional: AAAA-MM-DD]\n")
            print("Para más ayuda escriba: [ayuda, help, h, ?] \n")
            print("Cualquier duda contactar con: SteveCarpio.  \n")
else:
    input(Fore.WHITE + "Presiona Enter para continuar...")
    ejecutar_menu(var_Fecha)

# FIN: By Steve Carpio - 2025    
