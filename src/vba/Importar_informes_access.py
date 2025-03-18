import win32com.client

# Abrir la aplicación Access
AccessApp = win32com.client.Dispatch("Access.Application")

# Abrir la base de datos
db_path = r"C:\Users\scarpio\Documents\GitHub\proy_py_calendarizar\src\vba\Tabla_Eventos.accdb"  # Cambia esto por la ruta de tu base de datos
AccessApp.OpenCurrentDatabase(db_path)

# Establecer los parámetros del informe (si es necesario)
informe_nombre = "INF_Aviso_Mensual"  # El nombre de tu informe
ANO = "2025"  # Los valores que necesitas pasar como parámetros
MES = "4"

# Puedes usar una consulta que reciba parámetros o pasar directamente los parámetros al informe
AccessApp.DoCmd.OpenReport(informe_nombre, 2, "", f"ANO = {ANO} AND MES = {MES} ")

# Exportar el informe a HTML
html_path = r"C:\Users\scarpio\Documents\GitHub\proy_py_calendarizar\src\vba\informe.html"  # La ruta donde se guardará el archivo HTML
AccessApp.DoCmd.OutputTo(6, informe_nombre, "HTML", html_path, False)

# Cerrar la base de datos y la aplicación
AccessApp.CloseCurrentDatabase()
AccessApp.Quit()
