
from Basededados import* #Importa variaveis fixas da base de dados
from funcoes import *
import time
play = True


while play:
    
    #cabeçalho de inicio
    tituloinicio= "!!!!!Batalha Naval - Smoking Snake's Return!!!!!"
    tituloinicio= "="*len(tituloinicio)+'\n'+tituloinicio + "\n"+'='*len(tituloinicio)
    colorir("green",tituloinicio)

    # Cpu escolhe pais e aloca frotas - A FAZER


    # Texto de carregamento
    print('Iniciando jogo')
    time.sleep(0.3)
    print('{} está alocando seus navios para a batalha'.format('Brasil'),end='')
    time.sleep(0.6)
    for i in range(2):
        print('.',end='')
        time.sleep(0.7)
    print('.')
    time.sleep(0.5)
    colorir('green','!! A BATALHA COMEÇOU !!')

    play = False
    
