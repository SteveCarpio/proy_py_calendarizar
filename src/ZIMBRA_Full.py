# ----------------------------------------------------------------------------------------
#                                  ZIMBRA SOAP: Tareas / Citas
#
# Programa que agregara información dentro de Zimbra en los apartados de TAREAS y CITAS
# Autor: SteveCarpio
# Versión: V1 2025
# ----------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------
#                      LIBRERÍAS NECESARIAS
# Descripción: Abajo listo las librerías necesarias para su ejecución x pasos
# Autor: SteveCarpio-2025
# -------------------------------------------------------------------------------------

# CARGA DE LIBRERÍAS ---------------------------------------------# Ma P0 P1 P2 P3 P4 #
import requests                                                   # -- -- -- -- -- -- #
import urllib3                                                    # -- -- -- -- -- -- #
import datetime as dt                                             # -- -- -- -- -- -- #
import pandas as pd                                               # -- -- -- -- -- -- #
import os                                                         # -- -- -- -- -- -- #
import re                                                         # -- -- -- -- -- -- # 
import shutil                                                     # -- -- -- -- -- -- #
import time                                                       # -- -- -- -- -- -- #
import glob                                                       # -- -- -- -- -- -- #
import datetime                                                   # -- -- -- -- -- -- # 
import csv                                                        # -- -- -- -- -- -- #
import sys                                                        # -- -- -- -- -- -- #
from colorama import init, Fore, Back, Style                      # ma -- -- -- -- -- #
from datetime import datetime as dt                               # ma -- -- -- -- -- #
from datetime import timedelta                                    # ma -- -- -- -- -- #
from lxml import etree

# CARGA DE CONFIGURACIONES ------------------------------------------------------------
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ----------------------------------------------------------------------------------------
#                                  VARIABLES DE APOYO
# Descripción: Variables necesarias para la ejecución del proceso.
# ----------------------------------------------------------------------------------------

# **** Local ****
loc_RutaRaiz='C:\\MisCompilados\\PROY_CALENDARIZAR\\'
loc_RutaAccess=f"{loc_RutaRaiz}BBDD\\"
loc_RutaConfig=f'{loc_RutaRaiz}CONFIG\\'
loc_RutaInforme=f'{loc_RutaRaiz}INFORMES\\'
loc_RutaLog=f'{loc_RutaRaiz}LOG\\'

# **** Red ****
red_RutaRaiz=r'\\newton\comun$\Proyectos\Python\MisCompilados\PROY_CALENDARIZAR'
red_RutaAccess=f"{red_RutaRaiz}\\BBDD\\"
red_RutaConfig=f'{red_RutaRaiz}\\CONFIG\\'
red_RutaInforme=f'{red_RutaRaiz}\\INFORMES\\'

var_NombreCsvDiario="C_Export_CSV_Diario.csv"
var_NombreCsvMensual="C_Export_CSV_Mensual.csv"
var_NombreAccess="Tabla_Eventos.accdb"
var_NombreUsuarios="usuarios.txt"
var_UrlSoapZimbra = "https://zimbra.tda-sgft.com/service/soap"

var_sTv1="SteveCarpio-2025"
var_sTv2="stv.madrid@gmail.com" 


# ----------------------------------------------------------------------------------------
#                               INICIO DEL PROGRAMA PRINCIPAL
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
#                               FUNCIONES 
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
#  PASO0: VALIDAR REQUISITOS PREVIOS 
#  Autor: SteveCarpio-2025
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

def sTv_paso0(vEntorno):
 
    if vEntorno == "DEV" or vEntorno == "PRO" or vEntorno == "DEV-PACO":
        # Valida carpetas del programa
        valida_carpetas(loc_RutaRaiz)
        valida_carpetas(loc_RutaAccess)
        valida_carpetas(loc_RutaConfig)
        valida_carpetas(loc_RutaInforme)
        valida_carpetas(loc_RutaLog)
        
        valida_carpetas(red_RutaAccess)
        valida_carpetas(red_RutaConfig)
        valida_carpetas(red_RutaInforme)

        # Borra todos los files 
        borrar_archivos(loc_RutaAccess,  var_NombreCsvDiario)
        borrar_archivos(loc_RutaAccess,  var_NombreCsvMensual)
        
        print(Fore.WHITE + "\nRequisitos previos ok\n")
    else:
        pasoHelp()
        sys.exit(0)

# ----------------------------------------------------------------------------------------
#  PASO1: LEER CSV CON LOS AVISOS DIARIOS  
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

def Leer_Csv_DataFrame(var_Fecha):
    
    # Leo el CSV generado por el proceso VBA de access de Eventos
    df = pd.read_csv(f'{loc_RutaAccess}{var_NombreCsvDiario}', delimiter=';', quotechar='"', encoding='latin1')
  
    # Convertir la columna 1 a fecha
    df['FECHA_AVISO'] = pd.to_datetime(df['FECHA_AVISO'], errors='coerce', dayfirst=True)

    # Filtramos los registros a informar 
    df_filtrado = df[df['FECHA_AVISO'].dt.date == pd.to_datetime(var_Fecha).date()]
    df_filtrado = df_filtrado.copy()
    df_filtrado['REPOSITORIO2'] = df_filtrado['REPOSITORIO'].str.extract(r'href="([^"]+)"')
    df_filtrado = df_filtrado.reset_index(drop=True)
    df_filtrado.index = df_filtrado.index + 1

    return df_filtrado

def copiar_files(src_path, dest_path):
    try:
        # Verificar si el archivo de destino ya existe y eliminarlo si es necesario
        if os.path.exists(dest_path):
            os.remove(dest_path)
            print(f"CSV borrado de: {dest_path}")

        # Intentar copiar el archivo
        shutil.copy(src_path, dest_path)
        print(f"CSV copiado de: {src_path} a: {dest_path}")

    except PermissionError:
        print(f"Error de permiso: No se puede acceder a: {src_path} porque está siendo usado por otro proceso.")
    
    except Exception as e:
        print(f"Ha ocurrido un error: {str(e)}")

def sTv_paso1(var_Fecha):

    # Copiar CSV al servidor Python
    copiar_files(f"{red_RutaAccess}{var_NombreCsvDiario}", f"{loc_RutaAccess}{var_NombreCsvDiario}")

    # Leer CSV en un DataFrame
    df = Leer_Csv_DataFrame(var_Fecha)
    if len(df) > 1:
        print(df)
        return df
    else:
        print(f"No se encontraron datos del dia: {var_Fecha}")
        print(Fore.MAGENTA + "\n----------------------------------- [ Proceso Finalizado en el paso-1 ] -----------------------------------\n")
        sys.exit(0)
    

# ----------------------------------------------------------------------------------------
#  PASO2: PROGRAMA QUE CREARA UN TOKEN DEL USER PASSWD ZIMBRA  
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

def Crear_Token_SOAP(pUsuario, pContrasena):

    # XML de autentificación
    auth_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
    <soap:Body>
        <AuthRequest xmlns="urn:zimbraAccount">
        <account by="name">{pUsuario}</account>
        <password>{pContrasena}</password>
        </AuthRequest>
    </soap:Body>
    </soap:Envelope>"""

    # Enviar petición
    response = requests.post(var_UrlSoapZimbra, data=auth_xml, headers={"Content-Type": "text/xml"}, verify=False)

    # Mostrar respuesta
    print("Código HTTP:", response.status_code)
    print("Respuesta completa:")
    print(response.text)

    # Extraer el token (opcional, con XML parsing)
    import xml.etree.ElementTree as ET
    tree = ET.fromstring(response.content)
    ns = {'soap': 'http://www.w3.org/2003/05/soap-envelope', 'zimbra': 'urn:zimbraAccount'}

    token = tree.find('.//zimbra:authToken', ns)
    if token is not None:
        auth_token = token.text
        print("✅ Token obtenido:")
        print(f':{auth_token}:')
    else:
        print("❌ No se pudo obtener el token")

    return auth_token

def Importar_User_Passwd(pEntorno):
    xRutaArchivo=f"{loc_RutaConfig}{var_NombreUsuarios}"
    xUsuario = None
    xContrasena = None
    with open(xRutaArchivo, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo, delimiter=';')
        for fila in lector:
            if fila['ENTORNO'].strip('"') == pEntorno:
                xEmail=fila['EMAIL'].strip('"')
                xPasswd=fila['PASSWD'].strip('"')
                break # porque solo queremos la primera coincidencia
    print(xEmail)
    print(xPasswd)
    return xEmail, xPasswd

def sTv_paso2(pEntorno):
    # Importar usuario y contraseña del file .txt
    pUsuario, pContrasena = Importar_User_Passwd(pEntorno)

    # Crear un token en Zimbra
    auth_token = Crear_Token_SOAP(pUsuario, pContrasena)

    return auth_token

# ----------------------------------------------------------------------------------------
#  PASO3: PROGRAMA QUE CREARA UNA CITA  
#  Autor: SteveCarpio-2025
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
    response = requests.post(var_UrlSoapZimbra, data=crear_cita_con_alarma, headers={"Content-Type": "text/xml"}, verify=False)
    print("Respuesta al crear cita:")
    print(response.text)

def Recupera_Datos_DataFrame1(df, var_Fecha1):
    
    vContentCumulado = ""
    vLinea="-------------------------------------------------------------------------------"
    # ----------------- Importar valores para la Cita
    for _, fila in df.iterrows():
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
            f"{vLinea}\n\n"
        )
        vContentCumulado += vContent

    # ...............
    vTitulo=f"({len(df)}) Tareas Pendientes hoy {var_Fecha1}"
    vContentCumulado = f"{vTitulo}\n\n{vLinea}\n{vContentCumulado}"
    return vTitulo, vContentCumulado

def sTv_paso3(pAuthToken, var_Fecha1, var_Fecha2, df): 

    # Función para recuperar datos del dataframe importado
    vTitulo, vContent = Recupera_Datos_DataFrame1(df, var_Fecha1)
    
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

# ----------------------------------------------------------------------------------------
#  PASO4: PROGRAMA QUE CREARA UNA TAREA  
#  Autor: SteveCarpio-2025
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
    response2 = requests.post(var_UrlSoapZimbra, data=crear_tarea_con_alarma, headers={"Content-Type": "text/xml"}, verify=False)
    print("Respuesta al crear tarea:")
    print(response2.text)


def Recupera_Datos_DataFrame2(pAuthToken, var_Fecha1, var_Fecha2, df):
    
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

def sTv_paso4(pAuthToken, var_Fecha1, var_Fecha2, df):

    # Función para recuperar datos del dataframe importado
    Recupera_Datos_DataFrame2(pAuthToken, var_Fecha1, var_Fecha2, df)


# ----------------------------------------------------------------------------------------
#                               EJECUCIÓN DE PASOS
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

