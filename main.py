
# distancia entre todas as estações (em linha reta)
distances = [
    [0, 10, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.6, 29.8],
    [10, 0, 8.5, 14.8, 26.6, 29.1, 26.1, 17.3, 10, 3.5, 15.5, 20.9, 19.1, 21.8],
    [18.5, 8.5, 0, 6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6],
    [24.8, 14.8, 6.3, 0, 12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4],
    [36.4, 26.6, 18.2, 12, 0, 3, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9],
    [38.8, 29.1, 20.6, 14.4, 3, 0, 3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2],
    [35.8, 26.1, 17.6, 11.5, 2.4, 3.3, 0, 20, 23, 27.3, 34.2, 25.7, 12.4, 15.6],
    [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20, 0, 8.2, 20.3, 16.1, 6.4, 22.7, 27.6],
    [17.6, 10, 9.4, 12.6, 23.3, 25.7, 23, 8.2, 0, 13.5, 11.2, 10.9, 21.2, 26.6],
    [9.1, 3.5, 10.3, 16.7, 28.2, 30.3, 27.3, 20.3, 13.5, 0, 17.6, 24.2, 18.7, 21.2],
    [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0, 14.2, 31.5, 35.5],
    [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4, 10.9, 24.2, 14.2, 0, 28.8, 33.6],
    [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0, 5.1],
    [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1, 0]
]

# distancias reais de uma estação para a próxima que é conectada a ela. A primeira
# posição indica o número da estação, e a segunda a distância em metros.
connections = [
    [[2, 10]], 
    [[1, 10], [3, 8.5], [9, 10], [10, 3.5]], 
    [[2, 8.5], [4, 6.3],[9, 9.4], [13, 18.7]],
    [[3, 6.3], [5, 13], [8, 15.3], [13, 12.8]],
    [[4, 13], [6, 3],[7, 2.4],[8, 30]],
    [[5, 3]],
    [[5, 2.4]],
    [[4, 15.3], [5, 30], [9, 9.6], [12, 6.4]],
    [[2, 10], [3, 9.4], [11, 12.2]],
    [[2, 3.5]],
    [[9, 12.2]],
    [[8, 6.4]],
    [[3, 18.7], [4, 12.8], [14, 5.1]],
    [[13, 5.1]]
]

# Cada posição do array indica a(s) linha(s) que passa(m) por esta estação
lines = [
    ["blue"],
    ["blue", "yellow"],
    ["blue", "red"],
    ["blue", "green"],
    ["blue", "yellow"],
    ["blue"], 
    ["yellow"],
    ["yellow", "green"],
    ["yellow", "red"],
    ["yellow"],
    ["red"],
    ["green"],
    ["green", "red"],
    ["green"]
]

# menor custo ja calculado, e estação vinda
bestPath = [
    {"blue": [-1, -1]},
    {"blue": [-1,-1], "yellow": [-1,-1]},
    {"blue": [-1,-1], "red": [-1,-1]},
    {"blue": [-1,-1], "green": [-1,-1]},
    {"blue": [-1,-1], "yellow": [-1,-1]},
    {"blue": [-1,-1]},
    {"yellow": [-1,-1]},
    {"yellow": [-1,-1], "green": [-1,-1]},
    {"yellow": [-1,-1], "red": [-1,-1]},
    {"yellow": [-1,-1]},
    {"red": [-1,-1]},
    {"green": [-1,-1]},
    {"green": [-1,-1], "red": [-1,-1]},
    {"green": [-1,-1]}
]

# menor custo ate o momento
lowerCost = [
    {"blue": -1},
    {"blue": -1, "yellow": -1},
    {"blue": -1, "red": -1},
    {"blue": -1, "green": -1},
    {"blue": -1, "yellow": -1},
    {"blue": -1},
    {"yellow": -1},
    {"yellow": -1, "green": -1},
    {"yellow": -1, "red": -1},
    {"yellow": -1},
    {"red": -1},
    {"green": -1},
    {"green": -1, "red": -1},
    {"green": -1}
]


# Função que coloca a distância real em função do tempo.
def connectionsToTime(speed):
    for station in range(0, len(connections)) : 
        for connection in range(0, len(connections[station])): #para cada conexão da estação
            connections[station][connection][1] =  connections[station][connection][1]/speed #ao inves de guardar a distancia, guarde o tempo gasto para percorrer se baseando na velocidade passada no parametro
    
# Função que coloca a distância em linha reta em função do tempo.
def dataToTime(speed):
    for i in range(0,len(distances)):
        for j in range(0, len(distances[i])):
            distances[i][j] =  float(distances[i][j])/speed

def readPath(end_point):
    current_state = end_point 
    path = []
    
    path.append([end_point[0], end_point[1]])
    while(bestPath[current_state[0]-1][current_state[1]][0] != -1):
        
        path.insert(0,bestPath[current_state[0]-1][current_state[1]])
        current_state = bestPath[current_state[0]-1][current_state[1]]    

    return path

#Retorna o custo real entre um estado e outro    
def calculateCost(current_state, next_station):
    # para cada conexão desta estação
    for connection in range(0, len(connections[current_state-1])):
        # se a conexão analisada for igual a proxima estação
        if(connections[current_state-1][connection][0] == next_station[0]):
            # retorne o custo real entre as estações
            return (connections[current_state-1][connection][1])  
    

#Retorna se é necessário trocar de linha
def checkChangeLine(destination, line):
    for linesInStation in lines[destination-1]:
        if linesInStation == line:
            return False
    return True

#Retorna primeira linha em comum encontrada entre duas estações
def newLine(station1, station2):
    for linesInStation1 in lines[station1-1]:
        for linesInStation2 in lines[station2-1]:
            if(linesInStation1 == linesInStation2):
                return linesInStation1

def aStar (start_point, end_point):
    #Variavel para checar se chegou ao fim
    finished = False
    border = []

    #Adicionando o ponto de partida na nossa lista de prioridades
    border.append(start_point)

    #Setando o custo para chegar no estado inicial para 0
    lowerCost[start_point[0]-1][start_point[1]] = 0

    #Loop que itera enquanto a lista nao for vazia e ainda nao tivermos chegado ao fim
    while(len(border)>0 and not finished):
        print('este é o atual array de borda', border)

        #Seta o estado atual para o primeiro elemento da lista
        current_state = border.pop(0) 
        print('a estação atual é:', current_state)
        #Checa se o estado atual é o estado final
        if(current_state[0] == end_point[0]):
            finished = True 


            if(current_state[1] != end_point[1]):

                # bestPath[current_state[0]-1][end_point[1]] = bestPath[current_state[0]-1][current_state[1]]
                bestPath[current_state[0]-1][end_point[1]] = [current_state[0], current_state[1]]

                lowerCost[current_state[0]-1][current_state[1]] += 0.0666667
        
                lowerCost[current_state[0]-1][end_point[1]] = lowerCost[current_state[0]-1][current_state[1]]

                

        else:
            #Itera por todas as conexões do estado atual
            for connection in connections[current_state[0] - 1]:
                print('analisando a conexão: ', connection[0])

                #Inicializa a linha com a linha do estado atual
                thisLine = current_state[1]
                
                #Checa se será necessário uma mudança de linha 
                changeLine = checkChangeLine(connection[0], current_state[1])
                
                changeLineCost = 0
               #Se for necessario uma mudança de linha, atualiza o custo de mudança p 4 e atualiza a linha para a linha que o estado atual e essa conexão tem em comum
                if(changeLine):
                    changeLineCost = 0.0666667
                    thisLine = newLine(current_state[0], connection[0])
                    print('houve uma mudança para a linha', thisLine)

                #Calcula a heuristica referente a essa conexao
                h = distances[connection[0] - 1][end_point[0] - 1]

                #Calcula o custo real referente a essa conexao
                cost = lowerCost[current_state[0]-1][current_state[1]] +  calculateCost(current_state[0], connection) + changeLineCost
                print('o valor real para ir para estação ', connection[0] , 'é de: ', lowerCost[current_state[0]-1][current_state[1]], '+', calculateCost(current_state[0], connection), '+', changeLineCost )
                #Se o custo real calculado para chegar a esse estado for menor do que tem-se armazenado(ou se não tiver sido calculado previamente), atualiza-se ele
                print('o menor custo atual é de', lowerCost[connection[0]-1][thisLine], 'na estação' ,connection[0], thisLine)
                if(lowerCost[connection[0]-1][thisLine] == -1) or (cost <= lowerCost[connection[0]-1][thisLine]):
                    
                    #Atualiza menor custo real para esse estado
                    lowerCost[connection[0]-1][thisLine] = cost

                    if(changeLine):
                        bestPath[connection[0]-1][thisLine] = [current_state[0], thisLine]
                        bestPath[current_state[0]-1][thisLine] = [current_state[0], current_state[1]]

                    else:
                        #Atualiza o estado que leva a esse estado com esse menor custo
                        bestPath[connection[0]-1][thisLine] = [current_state[0], current_state[1]]

                    print('melhor caminho é vindo de:', bestPath[connection[0]-1][thisLine]) 
                    #Insere na nossa lista em ordem o estado (conexao, linha)
                    counter = -1
                    inserted = False

                    #Itera pelos elementos na nossa lista
                    for station in border:
                        counter = counter + 1
                        
                        print('o valor real é de:', lowerCost[connection[0]-1][thisLine], 'e a heuristica é de: ', float(h), '. O menor valor da atual lista ', lowerCost[station[0]-1][station[1]] + distances[station[0] - 1][end_point[0] - 1])
                        #Checa se a soma (valor real + heuristica) do estado que desejamos inserir é menor que essa mesma soma do elemento atual da lista
                        if(lowerCost[connection[0]-1][thisLine] + 
                        float(h) <= lowerCost[station[0]-1][station[1]] +  
                        distances[station[0] - 1][end_point[0] - 1]) :
                            border.insert(counter, [connection[0], thisLine])
                            inserted = True
                            break

                    #Se não tiver inserido, insere no fim
                    if(not inserted):
                        border.insert(counter+1,[connection[0], thisLine])

                    print('bordas atualizada para', border)
                else:
                    print('descartado')


def main():
    connectionsToTime(30)
    dataToTime(30)
    
    aStar((6, "blue"), (13, "green"))
    paths = readPath((13, "green"))
    for path in paths:
        print('E' + str(path[0]) + ' na linha ' + path[1])
    print('Tempo gasto: ' + str(lowerCost[12]["green"]))


if __name__ == "__main__":
    main()