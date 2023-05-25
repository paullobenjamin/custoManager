from model import *
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson import BSON, json_util
from typing import Optional, List
from datetime import datetime
from cryptography.fernet import Fernet
import bcrypt
from datetime import datetime

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.client = None
        return cls._instance

    def connect(self, uri, **kwargs):
        if not self.client:
            self.client = MongoClient(uri, **kwargs)
            print("Conexão estabelecida com o MongoDB")
        else:
            print("Já existe uma conexão com o MongoDB")

    def disconnect(self):
        if self.client:
            self.client.close()
            self.client = None
            print("Conexão com o MongoDB encerrada")
        else:
            print("Não há uma conexão com o MongoDB")

class Dao:
    def __init__(self) -> None:
        pass

    def criptografar_senha(selg, pessoa: Pessoa):
        login = pessoa
        salt = bcrypt.gensalt()

    def inserirPessoa(pessoa: Pessoa):
        json = {}
        
        for doc in pessoa.get_documentos():
            if doc.get_tipo() == "cnpj":
                json["razaoSocial"] = pessoa.get_razao()
                if pessoa.get_nomeFantasia() is not None:
                    json["nomeFantasia"] = pessoa.get_nomeFantasia()
            elif doc.get_tipo() == "cpf":
                json["nome"] = pessoa.get_nome()
        
        if pessoa.get_dtRegistro is not None:
            json["dtRegistro"] = pessoa.get_dtRegistro

        for contato in pessoa.get_contatos():
            try:
                if contato is not None:
                    if "contatos" not in json:
                        json["contatos"] = []
                    c = contato.to_dict()
                    json["contatos"].append(c)
            except:
                return "É necessário pelo menos 1 (um) contato para cadastrar uma pessoa"

        for documento in pessoa.get_documentos():
            try:
                if documento is not None:
                    if "documentos" not in json:
                        json["documentos"] = []
                    json["documentos"].append(documento)
            except:
                return "É necessário pelo menos 1 (um) documento para cadastrar uma pessoa"

        for endereco in pessoa.get_enderecos():
            try:
                if endereco is not None:
                    if "enderecos" not in json:
                        json["enderecos"] = []
                    json["enderecos"].append(endereco)
            except:
                return "É necessário pelo menos 1 (um) endereco para cadastrar uma pessoa"
            
        if pessoa.get_login() is not None:
            senha = pessoa.get_login().get_senha()
            hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
            json["login"] = {
                "usuario": pessoa.get_login().get_usuario(),
                "senha": hashed_senha
            }
        """_summary_
        if pessoa.get_id() is None:
            id = ObjectId()
            pessoa.set_id(id)
            json["_id"] = pessoa.get_id()
        """
        
        uri = "mongodb://localhost:27017"
        custoManager = DatabaseConnection(uri, maxPoolSize=10)
        db = custoManager["custoManager"]
        pessoas = db["pessoas"]

        result = pessoas.insert_one(json)
        return result.inserted_id