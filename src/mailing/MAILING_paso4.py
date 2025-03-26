# ----------------------------------------------------------------------------------------
#  PASO4: Enviar Email Mensual   
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

import cfg.MAILING_variables as sTv
from   cfg.MAILING_library import *

# ----------------------------------------------------------------------------------------
#                                  FUNCIONES
# ----------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------

def sTv_paso4(var_Fecha, var_Ano, var_Mes, var_Entorno):

    # Ruta del archivo
    var_csv = f'{sTv.loc_RutaAccess}{sTv.var_NombreCsvMensual}'
    print(f"File:  {var_csv}")

    # Mandar Email Diario con el DataFrame filtrado
    if var_Entorno == "PRO":
        print("Ejecución en modo: PRO")
        destinatarios_to=['carpios@tda-sgft.com']
        destinatarios_cc=['carpios@tda-sgft.com']
    else:
        print("Ejecución en modo: DEV")
        destinatarios_to=['carpios@tda-sgft.com']
        destinatarios_cc=['carpios@tda-sgft.com']