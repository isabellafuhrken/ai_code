from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from SearchAlgorithms import BuscaProfundidadeIterativa
from Graph import State

class VacuumWorld3Room(State):

    def __init__(self, vacuumPosition, isLeftRoomClean, isCenterRoomClean, isRightRoomClean, op):
        self.vacuumPosition = vacuumPosition # [right, center and left]
        self.isLeftRoomClean = isLeftRoomClean #[True, False]
        self.isCenterRoomClean = isCenterRoomClean #[True, False]
        self.isRightRoomClean = isRightRoomClean #[True, False]
        self.operator = op # string that describes the operation

    def env(self): #como deve ser
        return str(self.vacuumPosition)+";"+str(self.isLeftRoomClean)+";"+str(self.isCenterRoomClean)+";"+str(self.isRightRoomClean)
    
    
    def sucessors(self): #acoes que podem ser realizadas
        sucessors = []
        # É necessario verificar a VacuumPos antes de mover a Vacuum?
        # Nao eh necessario

        
        if (self.vacuumPosition == 'right'): #ta na direita, vai p esq e fica no centro
            sucessors.append(VacuumWorld3Room('center', self.isLeftRoomClean, self.isCenterRoomClean, self.isRightRoomClean, 'Move Left'))
        elif (self.vacuumPosition == 'center'):
            sucessors.append(VacuumWorld3Room('right', self.isLeftRoomClean, self.isCenterRoomClean, self.isRightRoomClean, 'Move Right'))
            sucessors.append(VacuumWorld3Room('left', self.isLeftRoomClean, self.isCenterRoomClean, self.isRightRoomClean, 'Move Left'))
        else:
            sucessors.append(VacuumWorld3Room('center', self.isLeftRoomClean, self.isCenterRoomClean, self.isRightRoomClean, 'Move Right'))

        
        #Implementar ações de limpeza. Importante: Verificar qual a VacuumPos e se a posição está suja
        #Como designar sucessors condicionais?
        if (self.vacuumPosition == 'right'): #isrightroomclean == true
            sucessors.append(VacuumWorld3Room(self.vacuumPosition, self.isLeftRoomClean, self.isCenterRoomClean, True, 'clean'))
        elif(self.vacuumPosition == 'center'):
            sucessors.append(VacuumWorld3Room(self.vacuumPosition, self.isLeftRoomClean, True, self.isRightRoomClean, 'clean'))
        else:
            sucessors.append(VacuumWorld3Room(self.vacuumPosition, True, self.isCenterRoomClean, self.isRightRoomClean, 'clean'))
        
        return sucessors
    
    def is_goal(self):
        return (self.isLeftRoomClean and self.isCenterRoomClean and self.isRightRoomClean and (self.vacuumPosition == 'left'))
        return False
    
    def description(self):
        return "Problema do aspirador de pó, contendo três (3) salas"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)

def main():
    
    #
    # Executando busca em largura
    #
    state = VacuumWorld3Room('left', False, False, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    
    #
    # Executando busca em profundidade
    #
    state = VacuumWorld3Room('left', False, False, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()
