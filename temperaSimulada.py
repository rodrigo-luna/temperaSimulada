import random
import math
import copy

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
    temperatura_atual = TEMPERATURA_INICIAL

    # Start by initializing the current state with the initial state
    solution = estado_inicial
    same_solution = 0
    same_cost_diff = 0
    
    while same_solution < 1500 and same_cost_diff < 150000:
        sucessor = get_sucessor(solution)
        
        # Checa se o sucessor é melhor
        cost_diff = get_cost(sucessor) - get_cost(solution)
        # se a solução nova for melhor, fica com ela
        if cost_diff > 0:
            solution = sucessor
            same_solution = 0
            same_cost_diff = 0
            
        elif cost_diff == 0:
            solution = sucessor
            same_solution = 0
            same_cost_diff +=1
        # se a nova solução for pior, aceitar apenas com probabilidade e^(-custo/temperatura)
        else:
            if random.uniform(0, 1) <= math.exp(float(cost_diff) / float(temperatura_atual)):
                solution = sucessor
                same_solution = 0
                same_cost_diff = 0
            else:
                same_solution += 1
                same_cost_diff += 1
        # reduz a temperatura
        temperatura_atual = temperatura_atual*ALPHA
        print(1/get_cost(solution), same_solution)
    print(1/get_cost(solution))
    
    return solution, 1/get_cost(solution)

def get_cost(estado):
    """Retorna custo total de um trajeto"""
    distancia = 0
    for i in range(len(estado)):
        if i+1 < len(estado):
            distancia += math.dist(estado[i], estado[i+1])
        else:
            distancia += math.dist(estado[i], estado[0])
    fitness = 1/distancia
    return fitness
    
def get_sucessor(estado):
    """Retorna um novo estado."""
    
    sucessor = copy.deepcopy(estado)
    
    "Retira uma cidade aleatória da sua posição e coloca em outra posição aleatória"
    node_j = random.choice(sucessor)
    sucessor.remove(node_j)
    node_i = random.choice(sucessor)
    index = sucessor.index(node_i)
    sucessor.insert(index, node_j)
        
    return sucessor

melhor_distancia = []
melhor_rota = []
cidades = ler_cidades('cidades_20.txt')
NUM_TENTATIVAS = 10
TEMPERATURA_INICIAL = 5000
ALPHA = 0.99

for i in range(NUM_TENTATIVAS):     
    rota, distancia = tempera_simulada(cidades)
    melhor_distancia.append(distancia)
    melhor_rota.append(rota)