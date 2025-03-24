# ----------------------------------------------------------------------------------------
#  PASO1: COPIAR BBDD ACCESS --> RED to LOCAL  
#  Autor: SteveCarpio-2025
# ----------------------------------------------------------------------------------------

import cfg.MAILING_variables as sTv
from   cfg.MAILING_library import *

# ----------------------------------------------------------------------------------------
#                                  FUNCIONES
# ----------------------------------------------------------------------------------------

def copiar_bbdd_or_access(src_path, dest_path):
    try:
        # Verificar si el archivo de destino ya existe y eliminarlo si es necesario
        if os.path.exists(dest_path):
            os.remove(dest_path)
            print(f"Archivo de destino eliminado: {dest_path}")

        # Intentar copiar el archivo
        shutil.copy(src_path, dest_path)
        print(f"Base de datos copiada de: {src_path} a: {dest_path}")

    except PermissionError:
        print(f"Error de permiso: No se puede acceder a: {src_path} porque está siendo usado por otro proceso.")
    
    except Exception as e:
        print(f"Ha ocurrido un error: {str(e)}")


# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------

def sTv_paso1():
    # Ruta de origen y destino
    orig = f"{sTv.red_RutaAccess}{sTv.var_NombreAccess}"  
    dest = f"{sTv.loc_RutaAccess}{sTv.var_NombreAccess}"
    
    # Llamar a la función de copia
    #copiar_bbdd_or_access(orig, dest)