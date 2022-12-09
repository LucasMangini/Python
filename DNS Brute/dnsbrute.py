# pip install dnspython
import dns.resolver # Biblioteca para DNS

res = dns.resolver.Resolver() # Objeto para realizar consultas DNS
arquivo = open("/home/kali/wordlist.txt", "r") # wordlist de subdomínios 
subdominios = arquivo.read().splitlines()

alvo = "alvo.com.br"

for subdominio in subdominios:
	try:
		sub_alvo = subdominio + "." + alvo 
		resultado = res.resolve(sub_alvo, "A") # Tipo de entrada ("A")
		for ip in resultado:
			print(sub_alvo, "->", ip)
	except:
		pass
