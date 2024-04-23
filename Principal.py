
from Basededados import* #Importa variaveis fixas da base de dados
from funcoes import *
import pygame # para tocar musica
import random

import time
play = True


while play:
    pygame.mixer.init()
    pygame.mixer.music.load('mp3.mp3')
    pygame.mixer.music.play(15)
    
    #cabeçalho de inicio
    tituloinicio= "!!!!Batalha Naval - Smoking Snake's Return!!!!"
    tituloinicio= '╔'+"═"*len(tituloinicio)+'╗'+'\n'+'║'+tituloinicio + '║'+"\n"+'╚'+"═"*len(tituloinicio)+'╝'
    colorir("green","\n \n"+tituloinicio + "\n",True)

    
    # Cpu escolhe pais e aloca frotas 
    

    
    cpu = sorteia_cpu(PAISES) # definição provisória manual da cpu

    # Texto de carregamento
    time.sleep(1)
    print('\nIniciando jogo\n ')
    time.sleep(1)
    print('\nSeu oponente será: ',end="")
    colorir("red",cpu + "\n",True)
    time.sleep(0.8)
    colorir('yellow','{} está alocando seus navios para a batalha'.format(cpu),False)
    time.sleep(0.8)
    for i in range(2):
        colorir("yellow",'.',False)
        time.sleep(1)
    colorir('yellow','.\n ',True)
    time.sleep(2)
    colorir('green','!! {} JÁ ESTÁ NO CAMPO DE BATALHA !!\n '.format(cpu.upper()),True)
    time.sleep(0.5)
    colorir("green",frase_de_efeito[cpu],True)
    time.sleep(1.5)

    #Jogador escolhe País 
    time.sleep(0.5)
    colorir("yellow","\n|Analisando as Frotas disponíveis pelo mundo|\n ",True)
    time.sleep(1.5)
         #printa Tabela de paises
    for inf,val in PAISES.items():
        colorir('cyan',inf+':',True)
        time.sleep(0.2)
        for inf2 , val2 in val.items():
            colorir('black',"     "+inf2+': '+str(val2),True)
            time.sleep(0.3)
    print("\n ")
    #Escolha do país
    paisIn = input("Escolha seu país: ")
    #Validação do país
    while verificarPais(paisIn)==False :  
        colorir('red','O valor inserido não está na lista de países, tente novamente:',True)
        paisIn = input("")
    time.sleep(0.5)
    player = formatarPais(paisIn)
    if player != cpu:
        colorir('cyan','\n Você escolheu {}, hora de alocar seus navios!! \n'.format(player),True)
    else:
        colorir('cyan','\n Você também escolheu {}? Ok, teremos uma guerra civil hora de alocar seus navios!! \n'.format(player),True)
    #Cria e exibe mapa 
    mapa_player = cria_mapa(10)
    mapa_cpu = cria_mapa(10) 
    time.sleep(0.6)
    mostra_jogo(mapa_cpu,mapa_player,cpu,player,10)
    #Alocar navios - 
    mapa =aloca_navios_para_player(mapa_player,lista_de_blocos(player),mapa_cpu,cpu,player)

    '''quemjoga = random.choice(0,1)
    while not foi_derrotado(mapa_cpu) and not foi_derrotado(mapa_player):
        if quemjoga == 0:
            #cpu ataca


        else:
             #player ataca
        
        mostra_jogo(mapa_cpu,mapa_player,cpu,player,10)'''




    pygame.mixer.music.stop()
    play = False
    
