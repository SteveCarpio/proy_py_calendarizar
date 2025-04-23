def MODO1():
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    fernet = Fernet(key)
    # Cifrar
    cipher = fernet.encrypt(b"U9d8z?:8K,>2")
    print(f"CIFRADO    :{cipher}")
    # Descifrar
    password = fernet.decrypt(cipher).decode()
    print(f"DESCIFRADO :{password}")

def MODO2():
    import keyring
    # Guardar la contraseña (esto se hace una vez, puede hacerse manual o con un script seguro)
    #keyring.set_password("BUZON_Publicaciones_MX", "publicacionesbolsasmx@tda-sgft.com", "U9d8z?:8K,>2")
    # Obtener la contraseña
    password = keyring.get_password("BUZON_Publicaciones_MX", "publicacionesbolsasmx@tda-sgft.com")
    print(f"PASSWORD: {password}")

