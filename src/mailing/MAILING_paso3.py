# ----------------------------------------------------------------------------------------
#  PASO3: Enviar Email Diario   
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

def sTv_paso3(Var_Ano, Var_Mes):

    # Ruta del archivo de la base de datos Access
    db_file = f'{sTv.loc_RutaAccess}{sTv.var_NombreAccess}'
