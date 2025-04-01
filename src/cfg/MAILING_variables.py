# ----------------------------------------------------------------------------------------
#                                  VARIABLES DE APOYO
# Descripción: Variables necesarias para la ejecución del proceso.
# Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------
import os

#-----------------------------------------------------------------------------------------
#                          Funciones de APOYO
# ----------------------------------------------------------------------------------------
def valida_ruta_de_red():
    ruta1="H:\\Proyectos\\Python\\MisCompilados\\PROY_CALENDARIZAR\\"  # Mapeado en mi PC
    ruta2="H:\\MisCompilados\\PROY_CALENDARIZAR\\"                     # Mapeado en el server Python
    # Verificar si alguna de las rutas existe
    if os.path.isdir(ruta1):
        ruta = ruta1
    elif os.path.isdir(ruta2):
        ruta = ruta2
    else:
        print(f"AVISO: Ninguna de las carpetas existe. {ruta1} - {ruta2} ")
        ruta = "ERROR"
    return ruta


#-----------------------------------------------------------------------------------------
#                          RUTAS DE APOYO
# ----------------------------------------------------------------------------------------
# **** Local ****
loc_RutaRaiz='C:\\MisCompilados\\PROY_CALENDARIZAR\\'
loc_RutaAccess=f"{loc_RutaRaiz}BBDD\\"
loc_RutaConfig=f'{loc_RutaRaiz}CONFIG\\'
loc_RutaInforme=f'{loc_RutaRaiz}INFORMES\\'
loc_RutaLog=f'{loc_RutaRaiz}LOG\\'

# **** Red ****
ruta=valida_ruta_de_red()
red_RutaRaiz=ruta 
red_RutaAccess=f"{red_RutaRaiz}BBDD\\"
red_RutaConfig=f'{red_RutaRaiz}CONFIG\\'
red_RutaInforme=f'{red_RutaRaiz}INFORMES\\'

# ----------------------------------------------------------------------------------------
#                          VARIABLES DE APOYO
# ----------------------------------------------------------------------------------------
var_NombreCsvDiario="C_Export_CSV_Diario.csv"
var_NombreCsvMensual="C_Export_CSV_Mensual.csv"
var_NombreAccess="Tabla_Eventos.accdb"

# ----------------------------------------------------------------------------------------
#                          AUTOR
# ----------------------------------------------------------------------------------------
var_sTv1="SteveCarpio-2025"
var_sTv2="stv.madrid@gmail.com" 
