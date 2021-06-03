import time

# FUNÇÕES
def dijkstra(grafo, origem, fim):
    controle = { }
    distanciaAtual = { }
    noAtual = { }
    naoVisitados = []
    atual = origem
    noAtual[atual] = 0
    
    for vertice in grafo.keys():
        naoVisitados.append(vertice)
        distanciaAtual[vertice] = float('inf')

    distanciaAtual[atual] = [0,origem] 
    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo[atual].items():
             pesoCalc = peso + noAtual[atual]
             if distanciaAtual[vizinho] == float('inf') or distanciaAtual[vizinho][0] > pesoCalc:
                distanciaAtual[vizinho] = [pesoCalc,atual]
                controle[vizinho] = pesoCalc
                 
        if controle == {} : break    
        minVizinho = min(controle.items(), key=lambda x: x[1])
        atual=minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]

    print("A menor distância de %s até %s é: %s" % (origem, fim, distanciaAtual[fim][0]))
    print("O menor caminho é: %s\n" % escreveCaminho(distanciaAtual,origem, fim))          

def escreveCaminho(distancias,inicio, fim):
        if  fim != inicio:
            return "%s -> %s" % (escreveCaminho(distancias,inicio, distancias[fim][1]),fim)
        else:
            return inicio

# MÉTRICAS
metricaA = {"POA" : {"FLO":1, "BLU":1},
            "FLO" : {"BLU":1, "CUR":1, "RJO":1, "POA":1},
            "BLU" : {"CUR":1, "POA":1, "FLO":1},
            "CUR" : {"LON":1, "SPO":1, "FLO":1, "BLU":1},
            "LON" : {"SPO":1, "BAU":1, "CUR":1},
            "SPO" : {"RJO":1, "CMP":1, "SJC":1, "CUR":1, "LON":1},
            "SJC" : {"CMP":1, "SPO":1, "RJO":1, "BHO":1},
            "RJO" : {"SJC":1, "BHO":1, "SLV":1, "FLO":1, "SPO":1},
            "BHO" : {"SJC":1, "BSB":1, "RJO":1},
            "CMP" : {"BAU":1, "RBP":1, "SPO":1, "SJC":1},
            "RBP" : {"BSB":1, "CMP":1},
            "BAU" : {"CPG":1, "CMP":1, "LON":1},
            "CPG" : {"CUI":1, "BAU":1},
            "CUI" : {"MAN":1, "CPG":1},
            "MAN" : {"BEL":1, "CUI":1, "BSB":1},
            "BEL" : {"NTL":1, "MAN":1},
            "BSB" : {"MAN":1, "NTL":1, "BHO":1, "RBP":1},
            "NTL" : {"REC":1, "BEL":1, "BSB":1, "SLV":1},
            "REC" : {"SLV":1, "NTL":1},
            "SLV" : {"NTL":1, "RJO":1, "REC":1} }

metricaB = {"POA" : {"FLO":6, "BLU":7},
            "FLO" : {"BLU":1, "CUR":2, "RJO":12, "POA":6},
            "BLU" : {"CUR":2, "POA":7, "FLO":1},
            "CUR" : {"LON":6, "SPO":5, "FLO":2, "BLU":2},
            "LON" : {"SPO":7, "BAU":3, "CUR":6},
            "SPO" : {"RJO":5, "CMP":1, "SJC":2, "CUR":5, "LON":7},
            "SJC" : {"CMP":2, "SPO":2, "RJO":3, "BHO":7},
            "RJO" : {"SJC":3, "BHO":7, "SLV":20, "FLO":12, "SPO":5},
            "BHO" : {"SJC":7, "BSB":9, "RJO":7},
            "CMP" : {"BAU":3, "RBP":2, "SPO":1, "SJC":2},
            "RBP" : {"BSB":8, "CMP":2},
            "BAU" : {"CPG":10, "CMP":3, "LON":3},
            "CPG" : {"CUI":8, "BAU":10},
            "CUI" : {"MAN":20, "CPG":8},
            "MAN" : {"BEL":18, "CUI":20, "BSB":22},
            "BEL" : {"NTL":21, "MAN":18},
            "BSB" : {"MAN":22, "NTL":22, "BHO":9, "RBP":8},
            "NTL" : {"REC":4, "BEL":21, "BSB":22, "SLV":15},
            "REC" : {"SLV":8, "NTL":4},
            "SLV" : {"NTL":15, "RJO":20, "REC":8} }        

metricaC = {"POA" : {"FLO":2, "BLU":2},
            "FLO" : {"BLU":3, "CUR":5, "RJO":10, "POA":2},
            "BLU" : {"CUR":5, "POA":2, "FLO":3},
            "CUR" : {"LON":2, "SPO":10, "FLO":5, "BLU":5},
            "LON" : {"SPO":2, "BAU":2, "CUR":2},
            "SPO" : {"RJO":15, "CMP":7, "SJC":16, "CUR":10, "LON":2},
            "SJC" : {"CMP":10, "SPO":16, "RJO":10, "BHO":8},
            "RJO" : {"SJC":10, "BHO":6, "SLV":6, "FLO":10, "SPO":15},
            "BHO" : {"SJC":8, "BSB":6, "RJO":6},
            "CMP" : {"BAU":6, "RBP":4, "SPO":7, "SJC":10},
            "RBP" : {"BSB":4, "CMP":4},
            "BAU" : {"CPG":3, "CMP":6, "LON":2},
            "CPG" : {"CUI":2, "BAU":3},
            "CUI" : {"MAN":3, "CPG":2},
            "MAN" : {"BEL":2, "CUI":3, "BSB":6},
            "BEL" : {"NTL":3, "MAN":2},
            "BSB" : {"MAN":6, "NTL":7, "BHO":6, "RBP":4},
            "NTL" : {"REC":3, "BEL":3, "BSB":7, "SLV":4},
            "REC" : {"SLV":5, "NTL":3},
            "SLV" : {"NTL":4, "RJO":6, "REC":5} }           

# DICIONÁRIO
cidades = ['Porto Alegre','Florianópolis','Blumenau','Curitiba','Londrina',
           'São Paulo','São José dos Campos','Rio de Janeiro','Belo Horizonte','Campinas',
           'Ribeirão Perto','Bauru','Campo Grande','Cuiabá','Manaus',
           'Belém','Brasília','Natal','Recife','Salvador']
pops = ['POA','FLO','BLU','CUR','LON','SPO','SJC','RJO','BHO','CMP','RBP','BAU','CPG','CUI','MAN','BEL','BSB','NTL','REC','SLV']

# MAIN
while True:
    print('='*35)
    print(' '*14, 'MENU')
    print('='*35)

    print('[ 0 ]: Sair')
    print('[ 1 ]: Dicionário')
    print('[ 2 ]: Criar novo PoP')
    print('[ 3 ]: Remover um PoP')
    print('[ 4 ]: Criar novo enlace')
    print('[ 5 ]: Remover um enlace')
    print('[ 6 ]: Calcular rota')
    opcao = int(input('Selecione: '))
    
    print('')
    print('-'*35)

    if opcao == 0:
        print('- Saindo da aplicação...\n')
        exit()

    if opcao == 1:
        print(' '*12, 'OPÇÃO 1')
        print('='*35)

        for i in range(0, len(cidades)):
            print(f'{pops[i]} : {cidades[i]}')
        print(' ')

    if opcao == 2:
        print(' '*12, 'OPÇÃO 2')
        print('='*35)

        nome = str(input('Cidade: '))
        p = str(input('PoP: ')).upper()

        # Adicionar valores no dicionário
        cidades.append(nome)
        pops.append(p)

        # Iniciar PoP com enlace nele mesmo valendo 0
        metricaA[p] = {p:0}
        metricaB[p] = {p:0}
        metricaC[p] = {p:0}
        print('\n- PoP cadastrado com sucesso!\n')

    if opcao == 3:
        print(' '*12, 'OPÇÃO 3')
        print('='*35)

        p = str(input('PoP: ')).upper()

        # Validar existência do PoP
        if p not in pops:
            print('\n- PoP não cadastrado!')

        # Tentativa de excluir
        try:
            # Excluir do dicionário
            posicaoPop = pops.index(p)
            del(cidades[posicaoPop])
            del(pops[posicaoPop])

            # Excluir das Métricas
            metricaA.pop(p)
            metricaB.pop(p)
            metricaC.pop(p)

            # Excluir os Enlaces
            for i in range(0, len(pops)):
                try:
                    metricaA[pops[i]].pop(p)
                    metricaB[pops[i]].pop(p)
                    metricaC[pops[i]].pop(p)
                except:
                    continue
            print('\n- PoP excluido com sucesso!\n')
        # Se falhar na tentativa
        except:
            print('- Falha ao tentar excluir PoP!\n')

    if opcao == 4:
        print(' '*12, 'OPÇÃO 4')
        print('='*35)

        vet = [metricaA, metricaB, metricaC]
        vet2 = []

        p1 = str(input('P1: ')).upper()
        p2 = str(input('P2: ')).upper()
        vet2.append(int(input('Métrica A: ')))
        vet2.append(int(input('Métrica B: ')))
        vet2.append(int(input('Métrica C: ')))
        
        try:
            # Adicionando métricas no PoP 1
            for i in range(0, len(vet)):
                c = vet[i][p1]
                c[p2] = vet2[i]
                vet[i][p1] = c

            # Adicionando métricas no PoP 2
            for i in range(0, len(vet)):
                c = vet[i][p2]
                c[p1] = vet2[i]
                vet[i][p2] = c
            
            print('\n- Enlace criado com sucesso!\n')
        # Se a tentativa falhar
        except:
            print('\n- Erro ao criar enlace, por favor tente novamente!\n')
    
    if opcao == 5:
        print(' '*12, 'OPÇÃO 5')
        print('='*35)

        p1 = str(input('P1: ')).upper()
        p2 = str(input('P2: ')).upper()

        # Validar existência dos PoPs
        if p1 not in pops or p2 not in pops:
            print('\n- Um ou mais PoPs não estão cadastrados!', end='')
        
        # Tentativa de exclusão do Enlace
        try:
            metricaA[p1].pop(p2)
            metricaB[p1].pop(p2)
            metricaC[p1].pop(p2)

            metricaA[p2].pop(p1)
            metricaB[p2].pop(p1)
            metricaC[p2].pop(p1)
            print('\n- Enlace excluido com sucesso!\n')
        # Se a tentativa falhar
        except:
            print('\n- Erro ao tentar excluir enlace!\n')
            
    if opcao == 6:
        print(' '*12, 'OPÇÃO 6')
        print('='*35)

        origem = str(input('Digite a origem [AAA]: ')).upper()
        destino = str(input('Digite a destino [BBB]: ')).upper()
        metrica = str(input('Digite a métrica (A, B ou C): ')).upper()

        print('\n- Calculando rota, por favor aguarde.....')
        time.sleep(1)
        
        # Tentar calcular rota
        try:
            if 'A' in metrica:
                dijkstra(metricaA, origem, destino)
            elif 'B' in metrica:
                dijkstra(metricaB, origem, destino)
            elif 'C' in metrica:
                dijkstra(metricaC, origem, destino)
            else:
                print('- Métrica inválida!')
                exit()
            
            # Verificar falhas em PoPs ou Enlaces
            while True:
                mA = metricaA
                mB = metricaB
                mC = metricaC

                print('[ 0 ]: Sair')
                print('[ 1 ]: Falha em um PoP')
                print('[ 2 ]: Falha em um Enlace')
                falha = int(input('Selecione: '))
                print('')

                if falha == 0:
                    break
                
                elif falha == 1:
                    p = str(input('PoP com falha: ')).upper()

                    # Verificar existência do PoP
                    if p not in pops:
                        print('- PoP não cadastrado!\n')
                        break  

                    try:
                        # Excluir PoPs das cópias das métricas
                        mA.pop(p)
                        mB.pop(p)
                        mC.pop(p)

                        # Excluir Enlaces das cópias das métricas
                        for i in range(0, len(pops)):
                            try:
                                mA[pops[i]].pop(p)
                                mB[pops[i]].pop(p)
                                mC[pops[i]].pop(p)
                            except:
                                continue
                        
                        print('\n- Recalculando rota, por favor aguarde.....')
                        time.sleep(1)

                        # Calcular nova rota
                        if 'A' in metrica:
                            dijkstra(mA, origem, destino)
                        elif 'B' in metrica:
                            dijkstra(mB, origem, destino)
                        elif 'C' in metrica:
                            dijkstra(mC, origem, destino)
                    except:
                        print('- Erro ao tentar recalcular rota!\n')
                
                elif falha == 2:
                    p1 = str(input('PoP 1 do Enlace: ')).upper()
                    p2 = str(input('PoP 2 do Enlace: ')).upper()

                    #  Verificar existência dos PoPs
                    if p1 not in pops or p2 not in pops:
                        print('- Um ou mais PoPs não estão cadastrados!\n')
                        break  
                
                    try:
                        # Excluir Enlace das cópias das métricas
                        mA[p1].pop(p2)
                        mB[p1].pop(p2)
                        mC[p1].pop(p2)

                        mA[p2].pop(p1)
                        mB[p2].pop(p1)
                        mC[p2].pop(p1)

                        print('\n- Recalculando rota, por favor aguarde.....')
                        time.sleep(1)

                        # Calcular nova rota
                        if 'A' in metrica:
                            dijkstra(mA, origem, destino)
                        elif 'B' in metrica:
                            dijkstra(mB, origem, destino)
                        elif 'C' in metrica:
                            dijkstra(mC, origem, destino)
                    except:
                        print('\n- Erro ao tentar recalcular rota!\n')
                        break
        # Se falhar o cálculo de rota
        except:
            print('- Erro ao calcular rota, por favor tente novamente!\n')
