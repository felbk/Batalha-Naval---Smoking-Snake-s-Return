
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
    print('\nIniciando jogo\n ')
    time.sleep(0.3)
    print('{} está alocando seus navios para a batalha'.format('Brasil'),end='')
    time.sleep(0.6)
    for i in range(2):
        print('.',end='')
        time.sleep(0.7)
    print('.\n ')
    time.sleep(0.5)
    colorir('green','!! A BATALHA COMEÇOU !!\n ')

    #Jogador escolhe País - A FAZER

    colorir("yellow","\n|Analisando as Frotas disponíveis pelo mundo|\n ")
    time.sleep(0.5)
         #printa Tabela de paises
    for inf,val in PAISES.items():
        colorir('cyan',inf+':')
        time.sleep(0.2)
        for inf2 , val2 in val.items():
            colorir('black',"     "+inf2+': '+str(val2))
            time.sleep(0.3)
    print("\n ")
    paisIn = input("Escolha seu país: ")



    #Cria e exibe mapa - A FAZER

    play = False
    
