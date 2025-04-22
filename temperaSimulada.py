import random
import math
import copy

NUM_TENTATIVAS = 10
TEMPERATURA_INICIAL = 1000
ALPHA = 0.99
MAX_MESMA_SOLUCAO = 300
MAX_MESMO_CUSTO = 300
NOME_ARQUIVO = 'cidades_20.txt'

def ler_cidades(nome_arquivo):
    cidades = []
    with open(nome_arquivo, 'r') as f:
        for linha in f:
            partes = linha.strip().split()
            if len(partes) == 3:
                # cidade_id = int(partes[0]) - 1
                x = int(partes[1])
                y = int(partes[2])
                cidades.append((x, y))
    return cidades

def tempera_simulada(estado_inicial):
    temperatura = TEMPERATURA_INICIAL
    solucao = estado_inicial    
    iteracoes = 0
    melhor_i = 0
    mesma_solucao = 0
    mesmo_custo = 0

    while mesma_solucao < MAX_MESMA_SOLUCAO and mesmo_custo < MAX_MESMO_CUSTO:
        iteracoes += 1
        sucessor = get_sucessor(solucao)
        
        # Checa se o sucessor é melhor
        diferenca = get_custo(sucessor) - get_custo(solucao)

        # se a solução nova for melhor, troca pra ela
        if diferenca > 0:
            solucao = sucessor
            mesma_solucao = 0
            mesmo_custo = 0
            melhor_i = iteracoes
        # mesma distância
        elif diferenca == 0:
            solucao = sucessor
            mesma_solucao = 0
            mesmo_custo +=1
            
        # se a nova solução for pior, aceitar apenas com probabilidade e^(-delta_custo/temperatura)
        else:
            if random.uniform(0, 1) <= math.exp(float(diferenca) / float(temperatura)):
                solucao = sucessor
                mesma_solucao = 0
                mesmo_custo = 0
        # continua com a mesma solução
            else:
                mesma_solucao += 1
                mesmo_custo += 1

        # reduz a temperatura
        temperatura = temperatura*ALPHA
        print(1/get_custo(solucao), mesma_solucao, melhor_i)
    
    return solucao, 1/get_custo(solucao), melhor_i

def get_custo(estado):
    # Retorna custo total de um estado
    distancia = 0
    for i in range(len(estado)):
        if i+1 < len(estado):
            distancia += math.dist(estado[i], estado[i+1])
        else:
            distancia += math.dist(estado[i], estado[0])
    fitness = 1/distancia
    return fitness
    
def get_sucessor(estado):
    sucessor = copy.deepcopy(estado)

    # Retira uma cidade aleatória da sua posição e coloca em outra posição aleatória
    node_j = random.choice(sucessor)
    sucessor.remove(node_j)
    node_i = random.choice(sucessor)
    index = sucessor.index(node_i)
    sucessor.insert(index, node_j)
        
    return sucessor

distancias_totais = []
rotas = []
cidades = ler_cidades(NOME_ARQUIVO)

for _ in range(NUM_TENTATIVAS):     
    # retorna a rota final, a distância total do trajeto, e o número de iterações necessárias pra chegar na solução
    rota, distancia, i = tempera_simulada(cidades)
    
    rotas.append(rota)
    distancias_totais.append([distancia, i])

    print (distancias_totais)
    with open("resultados.txt", 'a') as f:
        f.write("\n" + str([int(distancia), i]))