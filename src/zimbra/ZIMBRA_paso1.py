# ----------------------------------------------------------------------------------------
#  PASO1: LEER CSV CON LOS AVISOS DIARIOS  
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

import cfg.ZIMBRA_variables as sTv
from   cfg.ZIMBRA_library import *

# ----------------------------------------------------------------------------------------
#                                  FUNCIONES
# ----------------------------------------------------------------------------------------
def Leer_Csv_DataFrame(var_Fecha):
    
    # Leo el CSV generado por el proceso VBA de access de Eventos
    df = pd.read_csv(f'{sTv.loc_RutaAccess}{sTv.var_NombreCsvDiario}', delimiter=';', quotechar='"', encoding='latin1')
  
    # Convertir la columna 1 a fecha
    df['FECHA_AVISO'] = pd.to_datetime(df['FECHA_AVISO'], errors='coerce', dayfirst=True)

    # Filtramos los registros a informar 
    df_filtrado = df[df['FECHA_AVISO'].dt.date == pd.to_datetime(var_Fecha).date()]
    df_filtrado = df_filtrado.copy()
    df_filtrado['REPOSITORIO2'] = df_filtrado['REPOSITORIO'].str.extract(r'href="([^"]+)"')
    df_filtrado = df_filtrado.reset_index(drop=True)
    df_filtrado.index = df_filtrado.index + 1

    return df_filtrado

# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------

def sTv_paso1(var_Fecha):

    # Leer CSV en un DataFrame
    df = Leer_Csv_DataFrame(var_Fecha)
    if len(df) > 1:
        print(df)
        return df
    else:
        print(f"No hay datos para este dia: {var_Fecha}")
        exit(0)

