from model import *
from dao import *
from bson import json_util

e1 = Endereco(
    tipo="Residencial", 
    tipoLogradouro="Avenida", 
    logradouro="Joao Silva", 
    numero="123456", 
    complemento="Sala 9955", 
    bairro="Jardim do Eden",
    cidade="Paraiso",
    uf="RJ",
    pais="Brasil")
e2 = Endereco(
    tipo="Comercial", 
    tipoLogradouro="Avenida", 
    logradouro="Joao Silva", 
    numero="123456", 
    complemento="Sala 19852", 
    bairro="Jardim do Eden",
    cidade="Paraiso",
    uf="RJ",
    pais="Brasil")
enderecos = [e1,e2]
d1 = Documento(
    tipo="CPF", 
    numero="000.000.000-00", 
    emissor="RFB")
c1 = Contato(
    tipo="Residencial",
    formato="e-mail",
    valor="paullo.benjamin@gmail.com")
p1 = Pessoa(nome="Paulo Junior")
p1.set_dtRegistro(dtRegistro=datetime(1980,1,21))
p1.set_enderecos(enderecos)
p1.set_documentos(documentos=[d1])
p1.set_contatos(contatos=[c1])

try:
    p1_bson = p1.to_dict()
    print(p1_bson)
    dao = Dao()
    result = dao.inserirPessoa(p1)
    print("O _id:ObjectId('{}') foi inserido com sucesso".format(result))
except Exception as e:
    print("Ocorreu o seguinte erro: ", e)
