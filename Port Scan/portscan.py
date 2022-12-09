import socket # Biblioteca para manipular conexões de rede

alvo = "bancocn.com" # *** IMPLEMENTAR ARRAY DE ALVOS TBM ***
print(f"PORTSCAN EM: {alvo}\n")

ports = [21,22,80,443,445,3306,25] # Portas analisadas

for port in ports:
	# Criando um socket que utiliza o protocolo TCP/IP
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = socket IP | SOCK_STREAM = tipo de socket (TCP)

	client.settimeout(0.1)

	# *** EXECUTAR MAIS UMAS 3 VEZES PRA TESTE ***
	code = client.connect_ex((alvo, port)) # Tentar conexão com o array de portas (0 = Conexão estabelecida)
	
	if code == 0:
		print(port, "OPEN")
	else:
		print(port)