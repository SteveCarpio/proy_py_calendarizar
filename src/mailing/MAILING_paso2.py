
# ----------------------------------------------------------------------------------------
#  PASO2: IMPORTAR DATOS DE LA BBDD ACCESS LOCAL  
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

    # Conectar a la base de datos
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_file)

    # Crear un cursor
    cursor = conn.cursor()


    # Escribir la consulta SQL
    sql_query = '''
        SELECT 3_LANZADOR.FECHA_LIMITE, 1_TAREAS.CLAVE_PIZARRA, 1_TAREAS.EMISIONES, 1_TAREAS.CLASE, 1_TAREAS.ASUNTO, First(1_TAREAS.DETALLE_DEL_EVENTO) AS DETALLE_DEL_EVENTO, Year(FECHA_LIMITE) AS ANO, Month(FECHA_LIMITE) AS MES
        FROM (1_TAREAS LEFT JOIN 2_PLANIFICADOR ON 1_TAREAS.Id1 = 2_PLANIFICADOR.Id1) LEFT JOIN 3_LANZADOR ON 2_PLANIFICADOR.Id2 = 3_LANZADOR.id2
        GROUP BY 3_LANZADOR.FECHA_LIMITE, 1_TAREAS.CLAVE_PIZARRA, 1_TAREAS.EMISIONES, 1_TAREAS.CLASE, 1_TAREAS.ASUNTO, Year(FECHA_LIMITE), Month(FECHA_LIMITE), 1_TAREAS.ID_TAREA
        HAVING (((Year(FECHA_LIMITE))=2025) AND ((Month(FECHA_LIMITE))=4))
        ORDER BY 3_LANZADOR.FECHA_LIMITE
    '''

    # Ejecutar la consulta
    cursor.execute(sql_query)

    # Traer el resultado a un DataFrame de pandas
    df = pd.read_sql_query(sql_query, conn)

    # Mostrar el DataFrame
    print(df)

    # Cerrar la conexión
    conn.close()