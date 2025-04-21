# ----------------------------------------------------------------------------------------
#  PASO0: VALIDAR REQUISITOS PREVIOS 
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

import cfg.ZIMBRA_variables as sTv
from   cfg.ZIMBRA_library import *

# ----------------------------------------------------------------------------------------
#                                  FUNCIONES
# ----------------------------------------------------------------------------------------

# Función: Valida estructura de directorios
def valida_carpetas(ruta_carpeta):
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
        print(Fore.GREEN + f'Carpeta creada:    {ruta_carpeta}')
    else:
        print(Fore.CYAN  + f'Carpeta validada:  {ruta_carpeta}')

# Función: Borrar files creados
def borrar_archivos(ruta_carpeta, patron):
    # Construir la ruta completa con el patrón
    ruta_completa = os.path.join(ruta_carpeta, patron)
    
    # Encontrar todos los archivos que coincidan con el patrón
    archivos = glob.glob(ruta_completa)
    
    # Borrar cada archivo encontrado
    for archivo in archivos:
        os.remove(archivo)
        print(Fore.RED + f'Archivo borrado:   {archivo}')

def pasoHelp():
    os.system("cls")
    print(Fore.MAGENTA + "=" * 94)
    print(Fore.MAGENTA + "                               Proceso Zimbra Eventos Diarios")
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
    print(Fore.WHITE   + "    PowerShell: .\\ZIMBRA_Main_xx.exe [optional parameter]")
    print(Fore.WHITE   + "        * Desde un cmd tradicional no funcionará por el uso de librerías colorama")
    print(Fore.WHITE   + "          que no están soportadas por un cmd estándar. (Update CMD to Colorama)")
    print("")
    print(Fore.MAGENTA + "Parámetros [DEV/PRO/(?,ayuda,help)] [opcional AAAA-MM-DD]:")
    print("")
    print(Fore.WHITE   + "    (0) [vació]: Sin parámetros se ejecuta en modo DEV para el día actual")
    print(Fore.WHITE   + "    (1) DEV:  Ejecuta el proceso y manda el email a la lista desarrollo.       ")
    print(Fore.WHITE   + "    (1) PRO:  Ejecuta el proceso y manda el email a la lista usuarios finales. ")
    print(Fore.WHITE   + "    (1) HELP: Muestra la ayuda del programa, o con los valores (?, help, ayuda). ")
    print(Fore.WHITE   + "    (2) AAAA-MM-DD: Ejecuta el proceso y para el día pasado por parámetro.    ")
    print("")
    print(Fore.MAGENTA + "Planificación:")
    print("")
    print(Fore.WHITE   + "    Proceso Diario: Lun, Mar, Mié, Jue, Vie, Sab y Dom: 9:30h ")
    print("")
    print("")
    print(Fore.MAGENTA + "Dependencias importantes:")
    print("")
    print(Fore.WHITE   + "    * Existen otras dependencia técnicas que obviamos, como internet, ios, mem, ram, disco, etc..")    
    print("")
    print(Fore.CYAN   + "    - Rutas:")
    print(Fore.WHITE   + "          * Los csv de entrada estarán en estas rutas accesibles para el programa.")
    print("")
    print(Fore.WHITE   + "          C:\\MisCompilados\\PROY_CALENDARIZAR\\BBDD\\                  *** Raíz del programa en el servidor Python   ")          
    print(Fore.WHITE   + "          C:\\MisCompilados\\PROY_CALENDARIZAR\\CONFIG\\                *** Configuración del programa   ")          
    print(Fore.WHITE   + "          C:\\MisCompilados\\PROY_CALENDARIZAR\\LOG\\                   *** Log de la ejecución   ")          
    
    print(Fore.WHITE   + "          H:\\MisCompilados\\PROY_CALENDARIZAR\\BBDD (requerido)       *** Ruta Mapeada en el servidor de Python      ")  
    print(Fore.WHITE   + "          H:\\Proyectos\\Python\\MisCompilados\\PROY_CALENDARIZAR\\BBDD  *** Ruta Mapeada en los pc's de los usuarios ")

    print("")
    print(Fore.CYAN   + "    - Files CSV:")
    print(Fore.WHITE   + "          C:\\MisCompilados\\PROY_CALENDARIZAR\\BBDD\\C_Export_CSV_Diario.csv  - encoding='latin1' ")
    print(Fore.WHITE   + "          C:\\MisCompilados\\PROY_CALENDARIZAR\\CONFIG\\usuarios.txt   *** Usuario Zimbra para ejecución en modo DEV y PRO ")
    print("")
    print(Fore.CYAN   + "    - Delimitador file CSV:")
    print(Fore.WHITE   + "          \"valor1\" ; \"valor2\" ")
    print("")
    print(Fore.CYAN   + "    - Estructura del file CSV:")
    print(Fore.WHITE   + "          Se deben recibir al menos estos campos:")
    print(Fore.WHITE   + "          FECHA_AVISO, ID_TAREA, ID_PLANIF, CLAVE_PIZARRA, EMISIONES, CLASE, ASUNTO, DETALLE_DEL_EVENTO, REPOSITORIO")
    print("")

    print(Fore.CYAN   + "    - Zimbra SOAP Activo:")
    print(Fore.WHITE   + "          URL:        https://zimbra.tda-sgft.com/service/soap")
    print(Fore.WHITE   + "          Usuario:    publicacionesbolsasmx@tda-sgft.com")
    print(Fore.WHITE   + "          Contraseña: Ver en Cerberus")
    
    print("")

    print(Fore.MAGENTA + "=" * 94)
    print(Fore.WHITE   + "Para más ayuda, contactar con: SteveCarpio 'carpios@tda-sgft.com' ")
    print(Fore.WHITE   + "Versión 1 - 2025")
    print(Fore.MAGENTA + "=" * 94)

# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------

def sTv_paso0(vEntorno):
 
    if vEntorno == "DEV" or vEntorno == "PRO" or vEntorno == "DEV-PACO":
        # Valida carpetas del programa
        valida_carpetas(sTv.loc_RutaRaiz)
        valida_carpetas(sTv.loc_RutaAccess)
        valida_carpetas(sTv.loc_RutaConfig)
        valida_carpetas(sTv.loc_RutaInforme)
        valida_carpetas(sTv.loc_RutaLog)
        
        valida_carpetas(sTv.red_RutaAccess)
        valida_carpetas(sTv.red_RutaConfig)
        valida_carpetas(sTv.red_RutaInforme)

        # Borra todos los files 
        borrar_archivos(sTv.loc_RutaAccess,  sTv.var_NombreCsvDiario)
        borrar_archivos(sTv.loc_RutaAccess,  sTv.var_NombreCsvMensual)
        
        print(Fore.WHITE + "\nRequisitos previos ok\n")
    else:
        pasoHelp()
        sys.exit(0)