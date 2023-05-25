from datetime import datetime
from enum import Enum
from typing import Optional
from bson import json_util
from bson.objectid import ObjectId


# Model

# Classe Login
class Login:
    def __init__(self, 
                 username: str = None, 
                 password: str = None):
        self._username = username
        self._password = password

    def get_usuario(self):
        return self._usuario
    
    def set_usuario(self, usuario):
        self._usuario = usuario
        
    def get_senha(self):
        return self._senha
    
    def set_senha(self, senha):
        self._senha = senha

    def to_dict(self):
        data = {
            "username": self._username,
            "password": self._password
        }

        data = {k: v for k, v in data.items() if v is not None}
        return data

# Classe Documento
class Documento:
    def __init__(self,
                 tipo: Optional["str"] = None,
                 numero: Optional["str"] = None,
                 emissor: Optional["str"] = None,
                 emissao: Optional["datetime"] = None,
                 validade: Optional["datetime"] = None):
        self._tipo = tipo
        self._numero = numero
        self._emissor = emissor
        self._emissao = emissao
        self._emissor = validade

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo: Optional["str"]):
        self._tipo = tipo

    def get_numero(self):
        return self._numero

    def set_numero(self, numero: Optional["str"]):
        self._numero = numero

    def get_emissor(self):
        return self._emissor

    def set_emissor(self, emissor: Optional["str"]):
        self._emissor = emissor

    def get_emissao(self):
        return self._emissao

    def set_emissao(self, emissao: Optional["datetime"]):
        self._emissao = emissao

    def get_validade(self):
        return self._validade

    def set_validade(self, validade: Optional["datetime"]):
        self._validade = validade

    def to_dict(self):
        data = {
            "tipo": self._tipo,
            "numero": self._numero,
            "emissor": self._emissor,
            "emissao": self._emissao,
            "validade": self._validade
        }

        data = {k: v for k, v in data.items() if v is not None}
        return data


# Classe Contato
class Contato:
    def __init__(self,
                 tipo: Optional["str"] = None,
                 formato: Optional["str"] = None,
                 valor: str = None,
                 ddi: Optional["str"] = None,
                 ddd: Optional["str"] = None):
        self._tipo = tipo
        self._formato = formato
        self._ddi = ddi
        self._ddd = ddd
        self._valor = valor

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo: Optional["str"]):
        self._tipo = tipo

    def get_formato(self):
        return self._formato

    def set_formato(self, formato: Optional["str"]):
        self._formato = formato

    def get_ddi(self):
        return self._ddi

    def set_ddi(self, ddi: Optional["str"]):
        self._ddi = ddi

    def get_ddd(self):
        return self._ddd

    def set_ddd(self, ddd: Optional["datetime"]):
        self._ddd = ddd

    def get_valor(self):
        return self._valor

    def set_valor(self, valor: Optional["datetime"]):
        self._valor = valor

    def to_dict(self):
        data = {
            "tipo": self._tipo,
            "formato": self._formato,
            "ddi": self._ddi,
            "ddd": self._ddd,
            "valor": self._valor
        }

        data = {k: v for k, v in data.items() if v is not None}
        return data

# Classe Endereco
class Endereco:
    def __init__(self,
                 tipo: Optional["str"] = None,
                 tipoLogradouro: Optional["str"] = None,
                 logradouro: Optional["str"] = None,
                 numero: Optional["str"] = None,
                 complemento: Optional["str"] = None,
                 bairro: Optional["str"] = None,
                 cidade: Optional["str"] = None,
                 uf: Optional["str"] = None,
                 pais: Optional["str"] = None):
        self._tipo = tipo
        self._tipoLogradouro = tipoLogradouro
        self._logradouro = logradouro
        self._numero = numero
        self._complemento = complemento
        self._bairro = bairro
        self._cidade = cidade
        self._uf = uf
        self._pais = pais

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo: Optional["str"]):
        self._tipo = tipo

    def get_tipoLogradouro(self):
        return self._tipoLogradouro

    def set_tipoLogradouro(self, tipoLogradouro: Optional["str"]):
        self._tipoLogradouro = tipoLogradouro

    def get_logradouro(self):
        return self._logradouro

    def set_logradouro(self, logradouro: Optional["str"]):
        self._logradouro = logradouro

    def get_numero(self):
        return self._numero

    def set_numero(self, numero: Optional["str"]):
        self._numero = numero

    def get_complemento(self):
        return self._complemento

    def set_complemento(self, complemento: Optional["str"]):
        self._complemento = complemento

    def get_bairro(self):
        return self._bairro

    def set_bairro(self, bairro: Optional["str"]):
        self._bairro = bairro

    def get_cidade(self):
        return self._cidade

    def set_cidade(self, cidade: Optional["str"]):
        self._cidade = cidade

    def get_uf(self):
        return self._uf

    def set_uf(self, uf: Optional["str"]):
        self._uf = uf

    def get_pais(self):
        return self._pais

    def set_pais(self, pais: Optional["str"]):
        self._pais = pais

    def to_dict(self):
        data = {
            "tipo": self._tipo,
            "tipoLogradouro": self._tipoLogradouro,
            "logradouro": self._logradouro,
            "numero": self._numero,
            "complemento": self._complemento,
            "bairro": self._bairro,
            "cidade": self._cidade,
            "uf": self._uf,
            "pais": self._pais
        }

        data = {k: v for k, v in data.items() if v is not None}
        return data


# Classe Pessoa
class Pessoa:
    def __init__(self,
                 id: Optional["ObjectId"] = None,
                 nome: Optional["str"] = None,
                 razao: Optional["str"] = None,
                 nomeFantasia: Optional["str"] = None,
                 dtRegistro: Optional[datetime] = None,
                 documentos: list[Optional["Documento"]] = None,
                 contatos: list[Optional["Contato"]] = None,
                 enderecos: list[Optional["Endereco"]] = None,
                 login: Optional[Login] = None):
        self._id = id
        self._nome = nome
        self._razao = razao
        self._nomeFantasia = nomeFantasia
        self._documentos = documentos
        self._contatos = contatos
        self._enderecos = enderecos
        self._login = login

    def get_id(self):
        return self._id

    def set_id(self, id: ObjectId):
        self._id = id

    def get_nome(self):
        return self._nome

    def set_nome(self, nome: Optional["str"]):
        self._nome = nome

    def get_razao(self):
        return self._razao

    def set_razao(self, razao: Optional["str"]):
        self._razao = razao

    def get_nomeFantasia(self):
        return self._nomeFantasia

    def set_nomeFantasia(self, nomeFantasia: Optional["str"]):
        self._nomeFantasia = nomeFantasia

    def get_dtRegistro(self):
        return self._dtRegistro

    def set_dtRegistro(self, dtRegistro: Optional["str"]):
        self._dtRegistro = dtRegistro

    def get_documentos(self):
        return self._documentos

    def set_documentos(self, documentos: Optional["Documento"]):
        self._documentos = documentos

    def get_contatos(self):
        return self._contatos

    def set_contatos(self, contatos: Optional["Contato"]):
        self._contatos = contatos

    def get_enderecos(self):
        return self._enderecos

    def set_enderecos(self, enderecos: Optional["Endereco"]):
        self._enderecos = enderecos   

    def get_login(self):
        return self._login
    
    def set_login(self, login: str):
        self._login = login

    def to_dict(self):
        data = {
            "_id": self._id,
            "nome": self._nome,
            "razao": self._razao,
            "nomeFantasia": self._nomeFantasia,
            "dtRegistro": self._dtRegistro,
            "documentos": self._documentos,
            "contatos": self._contatos,
            "enderecos": self._enderecos,
            "login": self._login
        }

        data = {k: v for k, v in data.items() if v is not None}
        return data

# Classe Cliente
class Cliente:
    def __init__(self,
                 id: Optional["ObjectId"] = None,
                 pessoa: Optional[Pessoa] = None,
                 numContrato: Optional["str"] = None):
        self._id = id
        self._pessoa = pessoa
        self._numContrato = numContrato

    def get_id(self):
        return self._id

    def set_id(self, id: ObjectId):
        self._id = id

    def get_pessoa(self):
        return self._pessoa

    def set_pessoa(self, pessoa: Pessoa):
        self._pessoa = pessoa

    def get_numContrato(self):
        return self._numContrato

    def set_numContrato(self, numContrato):
        self._numContrato = numContrato

    def to_dict(self):
        data = {
            "id": self._id,
            "pessoa": self._pessoa,
            "numContrato": self._numContrato
        }

        data = {k: v for k, v in data.items() if v is not None}
        return data


# Classe usuarios
class Usuario:
    def __init__(self,
                 id: Optional[ObjectId] = None,
                 cliente: Optional[Cliente] = None,
                 pessoa: Optional[Pessoa] = None,
                 login: Optional[Login] = None):
        self._id = id
        self._cliente = cliente
        self._pessoa = pessoa
        self._login = login

    def get_id(self):
        return self._id

    def set_id(self, id: ObjectId):
        self._id = id

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente: Cliente):
        self._cliente = cliente

    def get_pessoa(self):
        return self._pessoa

    def set_pessoa(self, pessoa: Pessoa):
        self._pessoa = pessoa

    def get_login(self):
        return self._login
    
    def set_login(self, login: str):
        self._login = login

    def to_dict(self):
        data = {
            "id": self._id,
            "cliente": self._cliente,
            "pessoa": self._pessoa,
            "login": self._login
        }

        data = {k: v for k, v in data.items() if v is not None}
        return data


# Classe vpn
class Vpn:
    def __init__(self,
                 id: Optional[ObjectId] = None,
                 cliente: Optional[Cliente] = None,
                 nome: Optional[str] = None,
                 host: Optional["str"] = None,
                 ip: Optional["str"] = None,
                 vpnUsers: list[Optional["Usuario"]] = None):
        self._id = id
        self._cliente = cliente
        self._nome = nome
        self._host = host
        self._ip = ip
        self._vpnUsers = vpnUsers

    def get_id(self):
        return self._id

    def set_id(self, id: ObjectId):
        self._id = id

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente: Cliente):
        self._cliente = cliente

    def get_nome(self):
        return self._nome

    def set_nome(self, nome: str):
        self._nome = nome

    def get_host(self):
        return self._host

    def set_host(self, host: Optional[str]):
        self._host = host

    def get_ip(self):
        return self._ip

    def set_ip(self, ip: Optional[str]):
        self._ip = ip

    def get_vpn_users(self):
        return self._vpnUsers

    def set_vpn_users(self, vpnUsers: list[Optional["Usuario"]]):
        self._vpnUsers = vpnUsers


# Classe Equipamento
class Equipamento:
    def __init__(self,
                 id: Optional["ObjectId"] = None,
                 cliente: Optional[Cliente] = None,
                 hostname: Optional[str] = None,
                 porta: Optional[int] = None,
                 ip: Optional[str] = None,
                 vpn: Optional["Vpn"] = None):
        self._id = id
        self._cliente = cliente
        self._hostname = hostname
        self._porta = porta
        self._ip = ip
        self._vpn = vpn

    def get_id(self):
        return self._id

    def set_id(self, id: ObjectId):
        self._id = id

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente: Cliente):
        self._cliente = cliente

    def get_hostname(self):
        return self._hostname

    def set_hostname(self, hostname: str):
        self._hostname = hostname

    def get_porta(self):
        return self._porta

    def set_porta(self, porta: int):
        self._porta = porta

    def get_ip(self):
        return self._ip

    def set_ip(self, ip: str):
        self._ip = ip

    def get_vpn(self):
        return self._vpn

    def set_vpn(self, vpn: Optional["Vpn"]):
        self._vpn = vpn


# Tipo Ambiente
class TipoAmbiente(Enum):
    PROD = "Produtivo"
    DEV = "Desenvolvimento"
    HML = "Homologacao"
    QA = "Qualidade"
    OUTRO = "Outro"


# Tecnologia
class Tecnologia:
    def __init__(self,
                 id: Optional["ObjectId"] = None,
                 nome: Optional[str] = None,
                 arquitetura = None):
        self._id = id
        self._nome = nome
        self._arquitetura = arquitetura

    def get_id(self):
        return self._id

    def set_id(self, id: ObjectId):
        self._id = id

    def get_nome(self):
        return self._nome

    def set_nome(self, nome: str):
        self._nome = nome

    def get_arquitetura(self):
        return self._arquitetura

    def set_arquitetura(self, arquitetura):
        self._arquitetura = arquitetura


# Ambiente
class Ambiente:
    def __init__(self,
                 id: Optional["ObjectId"],
                 cliente: Optional[Cliente] = None,
                 servers: list["Equipamento"] = None,
                 tecnologia: Optional[Tecnologia] = None,
                 tipo: TipoAmbiente = TipoAmbiente.OUTRO):
        self._id = id
        self._cliente = cliente
        self._servers = servers
        self._tecnologia = tecnologia
        self._tipo = tipo

    def get_id(self):
        return self._id

    def set_id(self, id: ObjectId):
        self._id = id

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente: Cliente):
        self._cliente = cliente

    def get_servers(self):
        return self._servers

    def set_servers(self, servers: list["Equipamento"]):
        self._servers = servers

    def get_tecnologia(self):
        return self._tecnologia

    def set_tecnologia(self, tecnologia: Tecnologia):
        self._tecnologia = tecnologia

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo: TipoAmbiente):
        self._tipo = tipo
