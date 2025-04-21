import math

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

cidades = ler_cidades('cidades_20.txt')

print (cidades[0])

print (cidades[1])

print (math.dist(cidades[0], cidades[1]))