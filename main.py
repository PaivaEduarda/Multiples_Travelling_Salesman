import random
import math 
import matplotlib.collections as mc #biblioteca para gráficos
import matplotlib.pylab as pl

n_cities = 5 #número de cidades
n_salesman = 3
def create_matrices(n_cities):
    distances = [[0 for _ in range(n_cities)] for _ in range(n_cities)] #nao esta declarando uma varivel pois nao vai utiliza-la, ele so quer executar o exercicio n_cities vezes
    
    for i in range(n_cities):
        for j in range(i + 1, n_cities):
                distances[i][j] = distances[j][i] = int(random.uniform(1, 1000))
        #else:
            #distances[i][j] = distances[j][i] = 0
    return distances

def create_coordinates(n_cities):
    coordinates = [] #tupla de valores(x, y), tupla é  imutável 
    
    for _ in range(n_cities): #até percorrer todos os caminhos 
        coordinates.append(
            (
                int(random.uniform(0, 100)),
                int(random.uniform(0, 100))
            ) # vai gerar dois numeros de valores e colocar na lista de coordenadas
        )
    distances = [[0 for _ in range(n_cities)] for _ in range (n_cities)]
    
    
    for i in range(n_cities):
        for j in range(i + 1, n_cities): 
                distances[i][j] = distances[j][i] = int(
                    math.sqrt(
                        (coordinates[j][0] - coordinates[i][0])**2 
                        + (coordinates [j][1] - coordinates[i][1])**2
                    )
                )
    return coordinates, distances

def get_biggest_distance(distances, city):
    distance = 0
    ret = 0
    for i in range(n_cities - 1):                      
        dist = distances[city][i]
        if dist > distance:
            distance = dist
            ret = i
    return ret

def get_cordinates_average(city, coordinates): #vetor de cidades
    cordinates = [[0 for _ in range(len(city))] for _ in range(len(city))]
    x = []
    y = []
    for i in city:
        x.append(coordinates[i][0])
        y.append(coordinates[i][1])
    average_x = int(sum(x) / len(city))
    average_y = int(sum(y)/ len(city)) 
    
    return average_x, average_y

def salesman_per_city():
    salesman_array = [0] * n_salesman
    n_salesman_copy = n_salesman 
    for i in range(n_cities): #5
        if n_salesman_copy > 0: #2
            salesman_array[n_salesman_copy - 1] += 1 # [1][2][2]
            n_salesman_copy = n_salesman_copy - 1 # 1
            if n_salesman_copy == 0:
                n_salesman_copy = n_salesman             
    return salesman_array

def nearest_city(coordinates, x, y):
    distances = [0] * n_cities
    dist = sys.maxint
    for i in range(len(coordinates)):
        distances = int(
                        math.sqrt(
                            (x - coordinates[i][0])**2 
                            + (y - coordinates[i][1])**2
                        )
                    )
    return
    
def heuristic_centroide():
    unvisited = list(range(n_cities))
    tour = [random.choice(unvisited)]
    unvisited.remove(tour[-1])
    for i in range(salesman_per_city()):
        dist = get_biggest_distance()
        unvisited.remove(dist)
        
    return
    


    

