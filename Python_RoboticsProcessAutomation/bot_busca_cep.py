import http.client
import json


def obter_endereco_por_cep(cep):
  conexao = http.client.HTTPSConnection("viacep.com.br")
  # conexao.request("GET", f"ws/{cep}/json/" )
  conexao.request("GET", f"/ws/{cep}/json/")

  resposta = conexao.getresponse()
  # dados = json.loads(resposta.read().decode())
  dados = resposta.read()

  endereco = json.loads(dados.decode("utf-8"))



  conexao.close()

  if "erro" not in endereco:
    return endereco

  else:
    return "Cep nao encontrado"


cep_exemplo = "09360-370"

endereco_resultado = obter_endereco_por_cep(cep_exemplo)

print(endereco_resultado)
