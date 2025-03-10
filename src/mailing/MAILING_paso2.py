from datetime import datetime, timedelta

# Definir la fecha inicial
fechaini = datetime.strptime('01/03/2025', '%d/%m/%Y')

# Definir la lista de fiestas de Mexico (en formato 'dd/mm/yyyy')
fiestas = [
    '12/03/2025',  # Fiesta 1
    '01/03/2025',  # Fiesta 2
    '25/03/2025',  # Fiesta 3
]

# Convertir las fechas de fiestas a objetos datetime
fiestas = [datetime.strptime(fecha, '%d/%m/%Y') for fecha in fiestas]

# 1. Sumar 10 días naturales a la fecha
fecha2 = fechaini + timedelta(days=10)

# 2. Función para restar días hábiles, excluyendo los días festivos
def restar_dias_habiles(fecha, dias_habiles, fiestas):
    dias_restados = 0
    while dias_habiles > 0:
        fecha -= timedelta(days=1)
        # Verificar si el día es un día hábil (lunes a viernes) y no es festivo
        if fecha.weekday() < 5 and fecha not in fiestas:
            dias_habiles -= 1
    return fecha

# Restar 3 días hábiles (excluyendo festivos)
fecha_final = restar_dias_habiles(fecha2, 3, fiestas)

# Mostrar los resultados
print("Fecha inicial:", fechaini.strftime('%d/%m/%Y'))
print("Fecha2 (10 días naturales después):", fecha2.strftime('%d/%m/%Y'))
print("Fecha final (3 días hábiles antes de fecha2, excluyendo fiestas):", fecha_final.strftime('%d/%m/%Y'))


##################################################

from datetime import datetime
import calendar

# Obtener la fecha actual
fecha_actual = datetime.now()

# Obtener el último día del mes actual
ultimo_dia_del_mes = calendar.monthrange(fecha_actual.year, fecha_actual.month)[1]

# Crear un objeto datetime con el último día del mes
ultimo_dia_del_mes = datetime(fecha_actual.year, fecha_actual.month, ultimo_dia_del_mes)

# Mostrar el último día del mes
print("Último día del mes actual:", ultimo_dia_del_mes.strftime('%d/%m/%Y'))

#####################################################

from datetime import datetime

# Obtener el año actual
anio_actual = datetime.now().year

# Obtener el último día del año (31 de diciembre)
ultimo_dia_del_anio = datetime(anio_actual, 12, 31)

# Mostrar el último día del año
print("Último día del año actual:", ultimo_dia_del_anio.strftime('%d/%m/%Y'))
