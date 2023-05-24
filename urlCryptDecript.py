from cryptography.fernet import Fernet

class Uri:
    def __init__(self) -> None:
        pass

    def criptografar_uri(uri, chave):
        f = Fernet(chave)
        uri_criptografada = f.encrypt(uri.encode())
        return uri_criptografada

    def descriptografar_uri(uri_criptografada, chave):
        f = Fernet(chave)
        uri = f.decrypt(uri_criptografada)
        return uri.decode()

    # Chave de criptografia (gerada aleatoriamente)
    chave = Fernet.generate_key()

    # URI a ser criptografada
    uri = input("Digite a URI a ser criptografada")

    # Criptografar a URI
    uri_criptografada = criptografar_uri(uri, chave)

    # Salvar a URI criptografada em um arquivo externo
    with open("config.txt", "wb") as file:
        file.write(uri_criptografada)

    # Ler a URI criptografada do arquivo externo
    with open("config.txt", "rb") as file:
        uri_armazenada = file.read()

    # Descriptografar a URI
    def descriptografarUri(self,uri_armazenada,chava)
    uri = descriptografar_uri(uri_armazenada, chave)

    print(uri)
