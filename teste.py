from typing import Optional

class Login:
    def __init__(self, login: Optional[str], senha: Optional[str]):        
        self._login = login
        self._senha = senha

    def set_login(self, login):
        self._login = login

    def get_login(self):
        return self._login

    def set_senha(self, senha):
        self._senha = senha

    def get_senha(self):
        return self._senha

class Usuario:
    def __init__(self, nome: Optional[str], user: Optional[Login]):
        self._nome = nome
        self._user = user

    def set_nome(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_user(self, user):
        self._user = user

    def get_user(self):
        return self._user

nome = "paulo "#input("Digite seu nome: ")
usuario = "pcjunior" #input("Digite seu usuario: ")
senha = "senha" #input("Digite sua senha: ")

l = Login(login=usuario, senha=senha)
u = Usuario(nome=nome, user=l)

print('O login e senha do usuário {0} são: login({1}), senha({2})'.format(u.get_nome(), u.get_user().get_login(), u.get_user().get_senha()))