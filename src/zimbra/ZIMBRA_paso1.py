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

# ----------------------------------------------------------------------------------------
#                               INICIO PROGRAMA
# ----------------------------------------------------------------------------------------

def sTv_paso1(var_Fecha):

    # Copiar CSV al servidor Python
    copiar_files(f"{sTv.red_RutaAccess}{sTv.var_NombreCsvDiario}", f"{sTv.loc_RutaAccess}{sTv.var_NombreCsvDiario}")

    # Leer CSV en un DataFrame
    df = Leer_Csv_DataFrame(var_Fecha)
    if len(df) >= 1:
        print(df)
        return df
    else:
        print(f"No se encontraron datos del dia: {var_Fecha}")
        print(Fore.MAGENTA + "\n----------------------------------- [ Proceso Finalizado en el paso-1 ] -----------------------------------\n")
        sys.exit(0)
    

