from aicode.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aicode.search.Graph import State
import numpy as np

def convert_file_to_map(file):
    matriz = np.loadtxt(file, dtype=int, delimiter=';')
    return matriz

class VacuumWorldGeneric(State):

    def __init__(self, Map, vacuumPositionLine, vacuumPositionColumn,  op):
        self.Map = Map
        self.vacuumPositionLine = vacuumPositionLine 
        self.vacuumPositionColumn = vacuumPositionColumn 
        self.operator = op
        self.rows, self.columns =np.size(self.Map,0), np.size(self.Map,1)
    
    def sucessors(self):
        sucessors = []
    
    
    def is_goal(self):
        pass
    
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
        None


def main():
    print('Busca em profundidade iterativa')
    state = ProblemSpecification('')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()