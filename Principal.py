
from Basededados import* #Importa variaveis fixas da base de dados
from funcoes import *
import pygame # para tocar musica
import random 

import time
play = True
t = 0.1

while play:
    pygame.mixer.init()
    pygame.mixer.music.load('mp3.mp3')
    pygame.mixer.music.play(15)
    
    #cabeçalho de inicio
    tituloinicio= "!!!!Batalha Naval - Smoking Snake's Return!!!!"
    tituloinicio= '╔'+"═"*len(tituloinicio)+'╗'+'\n'+'║'+tituloinicio + '║'+"\n"+'╚'+"═"*len(tituloinicio)+'╝'
    colorir("green","\n \n"+tituloinicio + "\n",True)

    
    # Cpu escolhe pais e aloca frotas 
    mapa_cpu = cria_mapa(10) 
    cpu = sorteia_cpu(PAISES)
    mapa_cpu = aloca_navios_para_cpu(mapa_cpu,lista_de_blocos(cpu))
    
    

    # Texto de carregamento
    time.sleep(1 *t)
    print('\nIniciando jogo\n ')
    time.sleep(1 *t)
    print('\nSeu oponente será: ',end="")
    colorir("red",cpu + "\n",True)
    time.sleep(0.8 *t)
    colorir('yellow','{} está alocando seus navios para a batalha'.format(cpu),False)
    time.sleep(0.8 *t)
    for i in range(2):
        colorir("yellow",'.',False)
        time.sleep(1 *t)
    colorir('yellow','.\n ',True)
    time.sleep(2 *t)
    colorir('green','!! {} JÁ ESTÁ NO CAMPO DE BATALHA !!\n '.format(cpu.upper()),True)
    time.sleep(0.5 *t)
    colorir("green",frase_de_efeito[cpu],True)
    time.sleep(1.5 *t)

    #Jogador escolhe País 
    time.sleep(0.5 *t)
    colorir("yellow","\n|Analisando as Frotas disponíveis pelo mundo|\n ",True)
    time.sleep(1.5 *t)
         #printa Tabela de paises
    for inf,val in PAISES.items():
        colorir('cyan',inf+':',True)
        time.sleep(0.2 *t)
        for inf2 , val2 in val.items():
            colorir('black',"     "+inf2+': '+str(val2),True)
            time.sleep(0.3 *t)
    print("\n ")
    #Escolha do país
    paisIn = input("Escolha seu país: ")
    #Validação do país
    while verificarPais(paisIn)==False :  
        colorir('red','O valor inserido não está na lista de países, tente novamente:',True)
        paisIn = input("")
    time.sleep(0.5 *t)
    player = formatarPais(paisIn)
    if player != cpu:
        colorir('cyan','\n Você escolheu {}, hora de alocar seus navios!! \n'.format(player),True)
    else:
        colorir('cyan','\n Você também escolheu {}? Ok, teremos uma guerra civil hora de alocar seus navios!! \n'.format(player),True)
    #Cria e exibe mapa.
    mapa_player = cria_mapa(10)
   
    time.sleep(0.6 *t)
    
    mostra_jogo(mapa_cpu,mapa_player,cpu,player,10)

    #Alocar navios - 
    colorir('yellow',"\n gostaria de alocar seus navios automaticamente? (s ou n):", False)
    autoaloc = input("").strip().upper()
    if 'S' == autoaloc:
        mapa_player = aloca_navios_para_cpu(mapa_player,lista_de_blocos(player))
    else:
        mapa_player =aloca_navios_para_player(mapa_player,lista_de_blocos(player),mapa_cpu,cpu,player)
    time.sleep(2 *t)
    mostra_jogo(mapa_cpu,mapa_player,cpu,player,10)
    colorir('green','\n!! {} CHEGOU AO CAMPO DE BATALHA !!\n '.format(player.upper()),True)
    time.sleep(0.5 *t)
    colorir("green",frase_de_efeito[player],True)
    time.sleep(1.5 *t)
    
    quemjoga = random.randint(0,1)
    sorteador = [cpu,player]
    sorteado = sorteador[quemjoga]
    colorir("red","\n{} começa atacando:\n".format(sorteado),True)

    while not foi_derrotado(mapa_cpu) and not foi_derrotado(mapa_player):
        if quemjoga == 0:

            #cpu ataca
            lsort = random.randint(0,len(mapa_player)-1)
            csort = random.randint(0,len(mapa_player)-1)
            while ja_foi_atacado(csort,lsort,mapa_player):
                lsort = random.randint(0,len(mapa_player)-1)
                csort = random.randint(0,len(mapa_player)-1)

            reg = registra_ataque(csort,lsort,mapa_player)
            mapa_player = reg[0]
            retorno = reg[1]
            time.sleep(0.5 *t)

            quemjoga = 1
            


        else:

             #player ataca
            # insere valores de linha coluna  COM VERIFICAÇÃO
            linha = int(input("Informe o número: "))-1
            while not linha < len(mapa_player):
                colorir("red","Linha inválida, digite o número da linha novamente: ",False)
                linha = int(input(""))-1

            coluna = ALFABETO.find(input("Informe a letra: ").upper())
            while not coluna < len(mapa_player):
                colorir("red","Coluna inválida, digite a letra novamente: ",False)
                coluna = ALFABETO.find(input("").upper())

            while ja_foi_atacado(coluna,linha,mapa_cpu):
                # insere valores de linha coluna  COM 
                colorir('red','\n Ja foi atacado, insira outros valores:',True)
                linha = int(input("Informe o número: "))-1
                while not linha < len(mapa_player):
                    colorir("red","Linha inválida, digite o número da linha novamente: ",False)
                    linha = int(input(""))-1

                coluna = ALFABETO.find(input("Informe a letra: ").upper())
                while not coluna < len(mapa_player):
                    colorir("red","Coluna inválida, digite a letra novamente: ",False)
                    coluna = ALFABETO.find(input("").upper())
            reg = registra_ataque(coluna,linha,mapa_cpu)
            mapa_cpu = reg[0]
            retorno = reg[1]
            time.sleep(0.5 *t)
        
            quemjoga= 0
        
        mostra_jogo(mapa_cpu,mapa_player,cpu,player,10)
        if retorno == "A":
            colorir('blue','ÁGUA !! Foi por pouco... \n',True)
        else:
            colorir('red','BOOM !! ACERTOU EM CHEIO!! \n',True)
        




    pygame.mixer.music.stop()
    play = False
    
