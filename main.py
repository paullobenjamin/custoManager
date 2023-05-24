from model import *
from dao import *

e1 = Endereco(
    tipo="Residencial", 
    tipoLogradouro="Rua", 
    logradouro="Barbara Heliodora", 
    numero="1383", 
    complemento="Apto 201", 
    bairro="Jardim Sulcap",
    cidade="Rio de Janeiro",
    uf="RJ",
    pais="Brasil")
e2 = Endereco(
    tipo="Comercial", 
    tipoLogradouro="Rua", 
    logradouro="Barbara Heliodora", 
    numero="1383", 
    complemento="Apto 401", 
    bairro="Jardim Sulcap",
    cidade="Rio de Janeiro",
    uf="RJ",
    pais="Brasil")
enderecos = [e1,e2]
d1 = Documento(
    tipo="CPF", 
    numero="059.083.387-10", 
    emissor="RFB")
c1 = Contato(
    tipo="Residencial",
    formato="e-mail",
    valor="paullo.benjamin@gmail.com")
p1 = Pessoa()
p1.set_nome(nome="Paulo Cesar Benjamin Junior")
p1.set_dtRegistro(dtRegistro=datetime(1987,10,19))
p1.set_enderecos(enderecos)
p1.set_documentos(documentos=[d1])
p1.set_contatos(contatos=[c1])

try:
    inserirPessoa = Dao()
    result = Dao.inserirPessoa(pessoa=p1)
    print("O _id:ObjectId('{}') foi inserido com sucesso".format(result))
except Exception as e:
    print("Ocorreu o seguinte erro: ", e)
