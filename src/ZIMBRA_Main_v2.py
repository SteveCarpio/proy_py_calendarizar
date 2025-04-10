import requests
import xml.etree.ElementTree as ET
import urllib3

# Evitar advertencia por verify=False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# === CONFIGURA TUS DATOS ===
url = "https://zimbra.tda-sgft.com/service/soap"
usuario = "carpios@tda-sgft.com"
contrasena = "123456"  # Reemplazar con input() o variable de entorno en producción

# === AUTENTICACIÓN ===
def obtener_token():
    auth_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
      <soap:Body>
        <AuthRequest xmlns="urn:zimbraAccount">
          <account by="name">{usuario}</account>
          <password>{contrasena}</password>
        </AuthRequest>
      </soap:Body>
    </soap:Envelope>"""

    resp = requests.post(url, data=auth_xml, headers={"Content-Type": "text/xml"}, verify=False)
    tree = ET.fromstring(resp.content)
    ns = {'zimbra': 'urn:zimbraAccount'}
    token = tree.find('.//zimbra:authToken', ns)
    return token.text if token is not None else None

# === LISTAR TAREAS ===
def listar_tareas(token):
    listar_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
      <soap:Header>
        <context xmlns="urn:zimbra">
          <authToken>{token}</authToken>
        </context>
      </soap:Header>
      <soap:Body>
        <SearchRequest xmlns="urn:zimbraMail" types="task" limit="100">
          <query>*</query>
        </SearchRequest>
      </soap:Body>
    </soap:Envelope>"""

    resp = requests.post(url, data=listar_xml, headers={"Content-Type": "text/xml"}, verify=False)
    tree = ET.fromstring(resp.content)
    ns = {'zimbra': 'urn:zimbraMail'}
    tareas = tree.findall('.//zimbra:c', ns)

    if not tareas:
        print("⚠️ No hay tareas encontradas.")
        return []

    print("\n📋 Tareas encontradas:")
    resultado = []
    for tarea in tareas:
        id = tarea.attrib.get('id')
        su = tarea.attrib.get('name', 'Sin título')
        resultado.append(id)
        print(f"🆔 ID: {id} | 📝 Título: {su}")

    return resultado

# === BORRAR UNA TAREA ===
def borrar_tarea(token, id_tarea):
    borrar_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
      <soap:Header>
        <context xmlns="urn:zimbra">
          <authToken>{token}</authToken>
        </context>
      </soap:Header>
      <soap:Body>
        <ItemActionRequest xmlns="urn:zimbraMail">
          <action id="{id_tarea}" op="delete"/>
        </ItemActionRequest>
      </soap:Body>
    </soap:Envelope>"""

    resp = requests.post(url, data=borrar_xml, headers={"Content-Type": "text/xml"}, verify=False)
    print("✅ Tarea eliminada.")
    print(resp.text)

# === BORRAR TODAS LAS TAREAS ===
def borrar_todas(token, ids):
    ids_str = ",".join(ids)
    borrar_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
      <soap:Header>
        <context xmlns="urn:zimbra">
          <authToken>{token}</authToken>
        </context>
      </soap:Header>
      <soap:Body>
        <ItemActionRequest xmlns="urn:zimbraMail">
          <action id="{ids_str}" op="delete"/>
        </ItemActionRequest>
      </soap:Body>
    </soap:Envelope>"""

    resp = requests.post(url, data=borrar_xml, headers={"Content-Type": "text/xml"}, verify=False)
    print("✅ Todas las tareas fueron eliminadas.")
    print(resp.text)

# === MENÚ ===
def main():
    token = obtener_token()
    if not token:
        print("❌ Error de autenticación. Verifica usuario y contraseña.")
        return

    while True:
        print("\n=== Menú Zimbra Tareas ===")
        print("1. Listar tareas")
        print("2. Borrar tarea por ID")
        print("3. Borrar todas las tareas")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            listar_tareas(token)

        elif opcion == "2":
            id_tarea = input("ID de la tarea a borrar: ")
            borrar_tarea(token, id_tarea)

        elif opcion == "3":
            ids = listar_tareas(token)
            if ids:
                confirm = input(f"⚠️ ¿Estás seguro que deseas borrar {len(ids)} tareas? (sí/no): ")
                if confirm.lower() == "sí":
                    borrar_todas(token, ids)

        elif opcion == "4":
            print("👋 Saliendo...")
            break

        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
