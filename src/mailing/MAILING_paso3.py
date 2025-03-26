# ----------------------------------------------------------------------------------------
#  PASO3: Enviar Email Diario   
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

import cfg.MAILING_variables as sTv
from   cfg.MAILING_library import *

# ----------------------------------------------------------------------------------------
#                                  FUNCIONES
# ----------------------------------------------------------------------------------------
def Leer_Csv_DataFrame(Var_Fecha):
    print("d")
    df = pd.read_csv(f'{sTv.loc_RutaAccess}{sTv.var_NombreCsvDiario}', delimiter=';', quotechar='"', encoding='latin1')

    # Convertir la columna 0 a numérica (si hay algún valor no numérico, se convertirá a NaN)
    #df.iloc[:, 0] = pd.to_numeric(df.iloc[:, 0], errors='coerce')

    # Convertir la columna 1 a cadena
    df.iloc[:, 1] = df.iloc[:, 1].astype(str)

    # Convertir la columna 1 a fecha
    df.iloc[:, 1] = pd.to_datetime(df.iloc[:, 1], errors='coerce')

    print(Var_Fecha)

    return df


# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------

def sTv_paso3(Var_Fecha):

    # Ruta del archivo
    var_csv = f'{sTv.loc_RutaAccess}{sTv.var_NombreCsvDiario}'
    print(f"File:  {var_csv}")

    # Leer CSV en un DataFrame
    df = Leer_Csv_DataFrame(Var_Fecha)
    print(df)