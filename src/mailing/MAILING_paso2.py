# ----------------------------------------------------------------------------------------
#  PASO2: IMPORTAR DATOS DE LA BBDD   
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

def sTv_paso2():

    # Ruta del archivo de la base de datos Access
    db_file = f'{sTv.loc_RutaAccess}{sTv.var_NombreAccess}'

    # Conexión a la base de datos Access
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        f'DBQ={db_file};'
    )
    conn = pyodbc.connect(conn_str)

    # Definir la consulta SQL
    sql_query = '''
    SELECT 
        [3_LANZADOR].FECHA_LIMITE, 
        [1_TAREAS].CLAVE_PIZARRA, 
        [1_TAREAS].EMISIONES, 
        [1_TAREAS].CLASE, 
        [1_TAREAS].ASUNTO, 
        First([1_TAREAS].DETALLE_DEL_EVENTO) AS DETALLE_DEL_EVENTO, 
        Year([3_LANZADOR].FECHA_LIMITE) AS ANO, 
        Month([3_LANZADOR].FECHA_LIMITE) AS MES
    FROM 
        ([1_TAREAS] 
        LEFT JOIN [2_PLANIFICADOR] ON [1_TAREAS].Id1 = [2_PLANIFICADOR].Id1) 
        LEFT JOIN [3_LANZADOR] ON [2_PLANIFICADOR].Id2 = [3_LANZADOR].id2
    GROUP BY 
        [3_LANZADOR].FECHA_LIMITE, 
        [1_TAREAS].CLAVE_PIZARRA, 
        [1_TAREAS].EMISIONES, 
        [1_TAREAS].CLASE, 
        [1_TAREAS].ASUNTO, 
        Year([3_LANZADOR].FECHA_LIMITE), 
        Month([3_LANZADOR].FECHA_LIMITE), 
        [1_TAREAS].ID_TAREA
    HAVING 
        Year([3_LANZADOR].FECHA_LIMITE) = 2025 
        AND Month([3_LANZADOR].FECHA_LIMITE) = 4;
    '''
  
    # Crear DataFrame directamente desde la consulta
    df = pd.read_sql(sql_query, conn)

    # Renombrar columnas si es necesario (opcional)
    df.columns = [
        "FECHA_LIMITE", "CLAVE_PIZARRA", "EMISIONES", "CLASE", "ASUNTO", 
        "DETALLE_DEL_EVENTO", "ANO", "MES"
    ]
    
    # Imprimir el DataFrame
    print(df)

    # Cerrar la conexión
    conn.close()