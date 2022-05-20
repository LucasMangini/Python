def checarVitoria():
	if jogador == 1:
		jog = 2
	else:
		jog = 1
		
	# Vitória em linha
	for i in range(1,4):
		if campos[i][1] == campos[i][2] == campos[i][3] and campos[i][1] != '-':
			print(f"*** JOGADOR {jog} GANHOU! ***")
			return True

	# Vitória em coluna
	for i in range(1,4):
		if campos[1][i] == campos[2][i] == campos[3][i] and campos[1][i] != '-':
			print(f"*** JOGADOR {jog} GANHOU! ***")
			return True
	
	# Vitória em diagonal
	if campos[1][1] == campos[2][2] == campos[3][3] and campos[1][1] != '-':
			print(f"*** JOGADOR {jog} GANHOU! ***")
			return True

	if campos[3][1] == campos[2][2] == campos[1][3] and campos[3][1] != '-':
			print(f"*** JOGADOR {jog} GANHOU! ***")
			return True
	return False

def checarVelha():
	if (campos[1][1] != "-" and campos[1][2] != "-" and campos[1][3] != "-"):
		if(campos[2][1] != "-" and campos[2][2] != "-" and campos[2][3] != "-"):
			if (campos[3][1] != "-" and campos[3][2] != "-" and campos[3][3] != "-"):
				if(checarVitoria() == False):
					print("*** NENHUM JOGADOR GANHOU! ***")
					return True
	return False

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

parar = 0
jogador = 1

while parar == 0:
	lin = col = 0
	print(f"--- Jogador {jogador} ---")
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

	if jogador == 1:
		simbolo = "X"
		jogador = 2
	else:
		simbolo = "O"
		jogador = 1

	campos[lin][col] = simbolo

	print("-"*30)
	for i in range(0, 4):
		for j in range(0, 4):
			print("  ", campos[i][j], "  ", end="")
		print()
	print("-"*30,"\n\n")

	# Verificar paradas
	if checarVitoria():
		parar = 1
	if checarVelha():
		parar = 1
