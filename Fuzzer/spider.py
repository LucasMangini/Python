# Fazer uma requisição HTTP para o site e ver o status code dele

import requests

# Lista de palavras
lista = open("common.txt", "r")

for item in lista.readlines():
	# Identando URL + item da lista, substituindo a quebra de linha de cada linha por nada
	url = "URL ALVO" + item.replace("\n","")
	resposta = requests.get(url)

	# Exibindo apenas status 200
	if resposta.status_code == 200:
		print(f"[{resposta.status_code}] - [{url}]")
