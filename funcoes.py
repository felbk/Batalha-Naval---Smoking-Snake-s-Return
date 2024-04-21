#funções para facilitar a organização
from Basededados import*
from random import *


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
    for letra in range(len(cria_mapa(10))):


    return
    
def aloca_se_possivel():
    return
    
def foi_derrotado(matriz):
    for linha in matriz:
        for i in linha:
            if i == 'N':
                return False
    return True
    
def sorteia_cpu(dici):
    listp =[]
    for pais in dici:
        listp.append(pais)
    return choice(listp)

    
def valida_entradas():
    return
        
def sorteia_ataque():
    return
    
def registra_ataque():
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
#Nome formatado corretamente
def formatarPais(texto):
    texto= texto.strip().upper()
    for pais,lista in verificaPais.items():
        if texto in lista:
            return pais
        
    




    


    

    
