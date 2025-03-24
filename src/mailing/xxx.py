import win32com.client
import pandas as pd

try:
    # Ruta del archivo de la base de datos Access
    db_file = r'C:\\MisCompilados\\PROY_CALENDARIZAR\\BBDD\\Tabla_Eventos.accdb'  # Asegúrate de que la ruta es correcta

    # Crear un objeto de la aplicación Access
    access = win32com.client.Dispatch('Access.Application')

    # Abrir la base de datos
    db = access.DBEngine.OpenDatabase(db_file)

    # Definir la consulta SQL que quieres ejecutar (unión de tablas en este caso)
    sql_query = '''
        SELECT * FROM 3_LANZADOR;
    '''

    # Ejecutar la consulta SQL y obtener el resultado
    result_set = db.OpenRecordset(sql_query)

    # Crear una lista para almacenar los resultados
    data = []

    # Iterar a través del conjunto de resultados y agregar las filas a la lista
    while not result_set.EOF:
        row = []
        for field in result_set.Fields:
            row.append(field.Value)
        data.append(row)
        result_set.MoveNext()

    # Convertir los resultados en un DataFrame de pandas
    columns = [field.Name for field in result_set.Fields]
    df = pd.DataFrame(data, columns=columns)

    # Mostrar el DataFrame
    print(df)

except Exception as e:
    print(f"Ha ocurrido un error: {e}")

finally:
    # Cerrar la conexión a la base de datos
    if 'db' in locals():
        db.Close()
    if 'access' in locals():
        access.Quit()

