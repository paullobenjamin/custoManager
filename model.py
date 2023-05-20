from datetime import datetime
from enum import Enum
from typing import Optional

from bson.objectid import ObjectId


# Model

# Classe Documento
class Documento:
    def __init__(self,
                 id: Optional["ObjectId"],
                 tipo: Optional["str"],
                 numero: Optional["str"],
                 emissor: Optional["str"],
                 emissao: Optional["datetime"],
                 validade: Optional["datetime"]):
        self._id = id
        self._numero = numero
        self._emissor = emissor
        self._emissao = emissao
        self._emissor = validade

    def get_id(self):
        return self._id

    def set_id(self, id: ObjectId):
        self._id = id

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


# Classe Contato
class Contato:
    def __init__(self,
                 id: Optional["ObjectId"],
                 tipo: Optional["str"],
                 formato: Optional["str"],
                 ddi: Optional["str"],
                 ddd: Optional["str"],
                 valor: str):
        self._id = id
        self._tipo = tipo
        self._formato = formato
        self._ddi = ddi
        self._ddd = ddd
        self._valor = valor

    def get_id(self):
        return self._id

    def set_id(self, id: ObjectId):
        self._id = id

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

    # Classe Endereco


class Endereco:
    def __init__(self,
                 id: Optional["ObjectId"],
                 tipo: Optional["str"],
                 tipoLogradouro: Optional["str"],
                 logradouro: Optional["str"],
                 numero: Optional["str"],
                 complemento: Optional["str"],
                 bairro: Optional["str"],
                 cidade: Optional["str"],
                 uf: Optional["str"],
                 pais: Optional["str"]):
        self._id = id
        self._tipo = tipo
        self._tipoLogradouro = tipoLogradouro
        self._logradouro = logradouro
        self._numero = numero
        self._complemento = complemento
        self._bairro = bairro
        self._cidade = cidade
        self._uf = uf
        self._pais = pais

    def get_id(self):
        return self._id

    def set_id(self, id: ObjectId):
        self._id = id

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


# Classe Pessoa
class Pessoa:
    def __init__(self,
                 id: Optional["ObjectId"],
                 nome: Optional["str"],
                 razao: Optional["str"],
                 nomeFantasia: Optional["str"],
                 documentos: list[Optional["Documento"]],
                 contatos: list[Optional["Contato"]],
                 enderecos: list[Optional["Endereco"]]):
        self._id = id
        self._nome = nome
        self._razao = razao
        self._nomeFantasia = nomeFantasia
        self._documentos = documentos
        self._contatos = contatos
        self._enderecos = enderecos

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


# Classe Cliente
class Cliente:
    def __init__(self,
                 id: Optional["ObjectId"],
                 pessoa: Pessoa,
                 numContrato: Optional["str"]):
        self._id = id
        self._pessoa = pessoa
        self._numContrato: numContrato

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


# Classe usuarios
class Usuario:
    def __init__(self,
                 id: Optional["ObjectId"],
                 cliente: Cliente,
                 pessoa: Pessoa,
                 username: str):
        self._id = id
        self._cliente = cliente
        self._pessoa = pessoa
        self._username = username

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

    def get_username(self):
        return self._username

    def set_username(self, username: str):
        self._username = username


# Classe vpn
class Vpn:
    def __init__(self,
                 id: Optional["ObjectId"],
                 cliente: Cliente,
                 nome: str,
                 host: Optional["str"],
                 ip: Optional["str"],
                 vpnUsers: list[Optional["Usuario"]]):
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
                 id: Optional["ObjectId"],
                 cliente: Cliente,
                 hostname: str,
                 porta: int,
                 ip: str,
                 vpn: Optional["Vpn"]):
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
                 id: Optional["ObjectId"],
                 nome: str,
                 arquitetura):
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
                 cliente: Cliente,
                 servers: list["Equipamento"],
                 tecnologia: Tecnologia,
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
