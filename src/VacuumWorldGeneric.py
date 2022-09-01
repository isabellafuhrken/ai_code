from functools import total_ordering
from sqlite3 import Row
from tkinter import E
from aicode.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aicode.search.Graph import State
import numpy as np

def convert_file_to_map(file):
    matriz = np.loadtxt(file, dtype=int, delimiter=';')
    return matriz

def clean_room (map, row, column):
    map[row,column]=0
    return map

class VacuumWorldGeneric(State):

    def __init__(self, Map, Row, Column,  op):
        self.Map = Map
        self.Row = Row
        self.Column = Column
        self.operator = op
        self.State=self.Map[Row,Column] #estado do quarto, 0 ou 1
        self.TotalRows, self.TotalColumns =np.size(self.Map,0)-1, np.size(self.Map,1)-1
        self.goal = np.zeros((self.TotalRows+1, self.TotalColumns+1), dtype=int)
    
    def show(self):
        print(self.Map)
        print(self.Row)
        print(self.Column)
        print(self.TotalRows)
        print(self.TotalColumns)
        print(self.goal)

    def sucessors(self):
        sucessors = []

        #Clean the room
        if self.State==1:
            map=np.copy(self.Map)
            sucessors.append(VacuumWorldGeneric(clean_room(map,self.Row,self.Column),self.Row,self.Column,'clean'))
        #Move left
        if self.Column<self.TotalColumns:
            sucessors.append(VacuumWorldGeneric(self.Map,self.Row,self.Column+1,'move right'))
        #Move right
        if self.Column>0:
            sucessors.append(VacuumWorldGeneric(self.Map,self.Row,self.Column-1,'move left'))
        #Move up
        if self.Row<self.TotalRows:
            sucessors.append(VacuumWorldGeneric(self.Map,self.Row+1,self.Column,'move up'))
        #Move down
        if self.Row>0:
            sucessors.append(VacuumWorldGeneric(self.Map,self.Row-1,self.Column+1,'move down'))
        return sucessors

    def is_goal(self):
        return np.array_equal(self.goal,self.Map)
        return False
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        #
        # Usado para imprimir a solução encontrada. 
        # O PATH do estado inicial até o final.
        return str(self.operator)
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        return str(self.operator)


def main():
    print('Busca em profundidade iterativa')
    file_map_path = 'data/vacuum_simple_0.txt'
    row=0
    column=0
    map=convert_file_to_map(file_map_path)
    state = VacuumWorldGeneric(map,row,column,'')
    print(map)
    state.show()
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()