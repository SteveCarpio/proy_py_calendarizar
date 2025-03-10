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
