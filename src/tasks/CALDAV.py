









import caldav
from caldav.elements import dav
from datetime import datetime, timedelta

# URL de CalDAV para tu cuenta
url = "https://zimbra.tda-sgft.com/davs/publicacionesbolsasmx@tda-sgft.com/calendar"

# Credenciales de tu cuenta Zimbra
username = "publicacionesbolsasmx@tda-sgft.com"
password = "tu-contraseña"

# Conectar con el servidor CalDAV
client = caldav.DAVClient(url, username=username, password=password)
principal = client.principal()

# Obtener todos los calendarios disponibles (normalmente hay solo uno)
calendars = principal.calendars()

# Seleccionar el primer calendario
calendar = calendars[0]

# Crear un evento en el calendario
event = calendar.add_event("""
BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
SUMMARY:Reunión importante
DTSTART:{start_time}
DTEND:{end_time}
DESCRIPTION:Descripción de la reunión
LOCATION:Oficina central
STATUS:CONFIRMED
END:VEVENT
END:VCALENDAR
""".format(
    start_time=(datetime.now() + timedelta(days=1)).strftime('%Y%m%dT%H%M%S'),
    end_time=(datetime.now() + timedelta(days=1, hours=1)).strftime('%Y%m%dT%H%M%S')
))

print("Evento creado exitosamente.")
