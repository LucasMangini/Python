import time

# Decimal - Binário
def decBin(v):
    v = int(v)
    binario = ''
    controle = True

    while controle:
        r = v % 2  # Resto da divisão entre v e 2 (1 ou 0)
        v = v // 2 # Divisão inteira de v e 2
        binario += str(r) # Concatenar r como string

        if v == 0:
            controle = False
    return(binario[::-1]) # Retornar resultado da divisão invertido

# Binário - Decimal
def binDec(v):
    decimal = i = 0
    for cont in range(len(v)-1,-1,-1):
        decimal += int(v[cont]) * (2 ** i)
        i += 1
    return decimal

# Decimal - Hexa
def decHex(v):
    v = int(v)
    hexa = ''
    controle = True

    while controle:
        r = v % 16  # Resto da divisão entre v e 16
        v = v // 16 # Divisão inteira de v e 16

        # Identificar valor em Hexadecimal e concatenar
        if r == 10:
            hexa += 'A'
        elif r == 11:
            hexa += 'B'
        elif r == 12:
            hexa += 'C'
        elif r == 13:
            hexa += 'D'
        elif r == 14:
            hexa += 'E'
        elif r == 15:
            hexa += 'F'
        else:
            hexa += str(r)

        if v == 0:
            controle = False
    return(hexa[::-1]) # Retornar resultado da divisão invertido

# Hexa - Decimal
def hexDec(v):
    decimal = i = 0
    for cont in range(len(v)-1,-1,-1):
        if 'A' in v[cont]:
            decimal += 10 * (16 ** i)
        elif 'B' in v[cont]:
           decimal += 11 * (16 ** i)
        elif 'C' in v[cont]:
            decimal += 12 * (16 ** i)
        elif 'D' in v[cont]:
            decimal += 13 * (16 ** i)
        elif 'E' in v[cont]:
            decimal += 14 * (16 ** i)
        elif 'F' in v[cont]:
            decimal += 15 * (16 ** i)
        else:
            decimal += int(v[cont]) * (16 ** i)
        i += 1
    return decimal

# Decimal - Octal
def decOct(v):
    v = int(v)
    octal = ''
    controle = True

    while controle:
        r = v % 8  # Resto da divisão entre v e 8
        v = v // 8 # Divisão inteira de v e 8
        octal += str(r) # Concatenar r como string

        if v == 0:
            controle = False
    return(octal[::-1]) # Retornar resultado da divisão invertido

# Octal - Decimal
def octDec(v):
    decimal = i = 0
    for cont in range(len(v)-1,-1,-1):
        decimal += int(v[cont]) * (8 ** i)
        i += 1
    return decimal

print('='*20)
valor = input('Valor: ').upper()
print('='*20)

print('[ 1 ] Dec - Bin \n[ 2 ] Dec - Hex \n[ 3 ] Dec - Oct \n[ 4 ] Bin - Dec \n[ 5 ] Hex - Dec \n[ 6 ] Oct - Dec \n[ 7 ] Dec - Todos')
escolha = int(input('Escolha: '))

print('-'*20)
if escolha == 1:
    print(f'decBin: {decBin(valor)}\n')
elif escolha == 2:
    print(f'decHex: {decHex(valor)}\n')
elif escolha == 3:
    print(f'decOct: {decOct(valor)}\n')
elif escolha == 4:
    print(f'binDec: {binDec(valor)}\n')
elif escolha == 5:
    print(f'hexDec: {hexDec(valor)}\n')
elif escolha == 6:
    print(f'octDec: {octDec(valor)}\n')
elif escolha == 7:
    print(f'decBin: {decBin(valor)}')
    print(f'decHex: {decHex(valor)}')
    print(f'decOct: {decOct(valor)}\n')
else:
    print('Escolha inválida\n')
    