#funções para facilitar a organização
from Basededados import*
from random import *

#Cria tabuleiro do jogo
def cria_mapa(N):
    mapa = []
    linha = []
    meio = ' '
    i =0
    j=0
    while j<N:
        linha.append(meio)
        j+=1
    while i<N:
        mapa.append(linha)
        i+=1
    return mapa
 
def aloca_navio(letra,num,orine):
    return
    
def aloca_se_possivel():
    return

#Verifica se algum jogador foi derrotado   
def foi_derrotado(matriz):
    for linha in matriz:
        for i in linha:
            if i == 'N':
                return False
    return True

#Sorteia o paia da CPU 
def sorteia_cpu(dici):
    listp =[]
    for pais in dici:
        listp.append(pais)
    return choice(listp)

    
def valida_entradas():
    return
        
def sorteia_ataque():
    return
    
def registra_ataque(let,num,mapa):
    let = ALFABETO.find(let.upper())
    if mapa[num][let] == ' ':
        mapa[num][let] = "A"
    return mapa

#Verifica situação da celular da cpu e jogador
def situacao_celula(elem,jogador):
    if jogador == 'cpu':
        if elem == ' ':
            print(' ',end="")
        elif elem == 'N':
            print(' ',end="")
        elif elem == 'A':
            print('{0}█{1}'.format(CORES['blue'],CORES['reset']),end="")
        elif elem == 'D':
            print('{0}█{1}'.format(CORES['red'],CORES['reset']),end="")
    else:
        if elem == ' ':
            print(' ',end="")
        elif elem == 'N':
            print('{0}█{1}'.format(CORES['green'],CORES['reset']),end="")
        elif elem == 'A':
            print('{0}█{1}'.format(CORES['blue'],CORES['reset']),end="")
        elif elem == 'D':
            print('{0}█{1}'.format(CORES['red'],CORES['reset']),end="")
    return 
#Printa uma string colorida
def colorir(cor,texto):
    print('{0}{1}{2}'.format(CORES[cor],texto,CORES['reset']))
    return
#Verifica nome do país
def verificarPais(texto):
    texto = texto.strip().upper()
    for pais,lista in verificaPais.items():
        if texto in lista:
            return True
    return False

#Verifica se há letra no tabuleiro
def verifica_letracord(letra, tam):
    if letra.upper() in ALFABETO[:len(tam)]:
        return True
    else:
        return False

#Nome formatado corretamente
def formatarPais(texto):
    texto= texto.strip().upper()
    for pais,lista in verificaPais.items():
        if texto in lista:
            return pais

    


    

    
