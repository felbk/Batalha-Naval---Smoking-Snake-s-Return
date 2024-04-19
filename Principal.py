
from Basededados import* #Importa variaveis fixas da base de dados
from funcoes import *
import time
play = True


while play:
    
    #cabeçalho de inicio
    tituloinicio= "!!!!!Batalha Naval - Smoking Snake's Return!!!!!"
    tituloinicio= "="*len(tituloinicio)+'\n'+tituloinicio + "\n"+'_'*len(tituloinicio)
    colorir("green","\n \n"+tituloinicio + "\n")

    # Cpu escolhe pais e aloca frotas - A FAZER


    # Texto de carregamento
    time.sleep(1)
    print('\nIniciando jogo\n ')
    time.sleep(0.8)
    print('{} está alocando seus navios para a batalha'.format('Brasil'),end='')
    time.sleep(0.8)
    for i in range(2):
        print('.',end='')
        time.sleep(1)
    print('.\n ')
    time.sleep(2)
    colorir('green','!! {} JÁ ESTÁ PRONTO PARA A BATALHA !!\n '.format("BRASIL"))

    #Jogador escolhe País - A FAZER
    time.sleep(0.5)
    colorir("yellow","\n|Analisando as Frotas disponíveis pelo mundo|\n ")
    time.sleep(1.5)
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
    
