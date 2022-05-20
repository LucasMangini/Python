# LUCAS MANGINI DE OLIVEIRA - 21296456

# -------------------------------------
def movimentoIA(board, jogador):
	possibilidades = getPosicoes(board)
	melhor_valor = None
	melhor_movimento = None
	for possibilidade in possibilidades:
		board[possibilidade[0]][possibilidade[1]] = "X" if jogador == 1 else "O"
		valor = minimax(board, jogador)
		board[possibilidade[0]][possibilidade[1]] = "-"
		print("Peso atual compilado: ", possibilidade, valor)
		if(melhor_valor is None):
			melhor_valor = valor
			melhor_movimento = possibilidade
		elif(jogador == 1):
			if(valor > melhor_valor):
				melhor_valor = valor
				melhor_movimento = possibilidade
		elif(jogador == 2):
			if(valor < melhor_valor):
				melhor_valor = valor
				melhor_movimento = possibilidade

	return melhor_movimento[0], melhor_movimento[1]

def getPosicoes(board):
	posicoes = []
	for i in range(1, 4):
		for j in range(1, 4):
			if(board[i][j] == "-"):
				posicoes.append([i, j])
	
	return posicoes

score = {
	"EMPATE": 0,
	"X": 1,
	"O": -1
}

def minimax(board, jogador):
	ganhador = checarVitoria(board)
	if(ganhador):
		return score[ganhador]

	jogador = 1 if jogador == 2 else 2
	# print(score)
	
	possibilidades = getPosicoes(board)
	melhor_valor = None
	for possibilidade in possibilidades:
		board[possibilidade[0]][possibilidade[1]] = "X" if jogador == 1 else "O"
		valor = minimax(board, jogador)
		board[possibilidade[0]][possibilidade[1]] = "-"

		if(melhor_valor is None):
			melhor_valor = valor
		elif(jogador == 1):
			if(valor > melhor_valor):
				melhor_valor = valor
		elif(jogador == 2):
			if(valor < melhor_valor):
				melhor_valor = valor

	return melhor_valor -1
# -----------------------------------

def checarVitoria(campos):
	# Vitória em linha
	for i in range(1,4):
		if campos[i][1] == campos[i][2] == campos[i][3] and campos[i][1] != '-':
			return "X" if jogador == 1 else "O"

	# Vitória em coluna
	for i in range(1,4):
		if campos[1][i] == campos[2][i] == campos[3][i] and campos[1][i] != '-':
			return "X" if jogador == 1 else "O"
	
	# Vitória em diagonal
	if campos[1][1] == campos[2][2] == campos[3][3] and campos[1][1] != '-':
			return "X" if jogador == 1 else "O"

	if campos[3][1] == campos[2][2] == campos[1][3] and campos[3][1] != '-':
			return "X" if jogador == 1 else "O"
	
	# Campos disponíveis
	for i in range(1, 4):
		for j in range(1, 4):
			if campos[i][j] == "-":
				return False

	return "EMPATE"

campos = [	[" ", 1, 2, 3],
			[1, "-", "-", "-"],
			[2, "-", "-", "-"],
			[3, "-", "-", "-"]]

print("-"*5, " JOGO DA VELHA ", "-"*5)
print("Primeiro jogador: X \nSegundo Jogador: O\n")

# i = Linha | j = Coluna
print("-"*30)
for i in range(0, 4):
	for j in range(0, 4):
		print("  ", campos[i][j], "  ", end="")
	print()
print("-"*30,"\n\n")

jogador = 1
parar = 0
while parar == 0:
	lin = col = 0
	print(f"--- Jogador {jogador} ---")

	if jogador == 1:
		linCol = movimentoIA(campos, jogador)
		lin = linCol[0]
		col = linCol[1]
	else:
		campoLivre = False
		while not campoLivre:
			while lin!=1 and lin!=2 and lin!=3:
				lin = int(input("Selecione a LINHA (1, 2 ou 3): "))

			while col!=1 and col!=2 and col!=3:
				col = int(input("Selecione a COLUNA (1, 2 ou 3): "))

			if campos[lin][col] != "-":
				print("Campo inválido, tente novamente!\n")
				lin = col = 0
				campoLivre = False
			else:
				campoLivre = True

	simbolo = "X" if jogador == 1 else "O"
	jogador = 2 if jogador == 1 else 1

	campos[lin][col] = simbolo

	print("-"*30)
	for i in range(0, 4):
		for j in range(0, 4):
			print("  ", campos[i][j], "  ", end="")
		print()
	print("-"*30,"\n\n")

	if checarVitoria(campos) == 'O':
		print(f"*** JOGADOR 1 GANHOU! ***")
		parar = 1
	elif checarVitoria(campos) == 'X':
		print(f"*** JOGADOR 2 GANHOU! ***")
		parar = 1
	elif checarVitoria(campos) == "EMP":
		print("*** NENHUM JOGADOR GANHOU! ***")
		parar = 1
