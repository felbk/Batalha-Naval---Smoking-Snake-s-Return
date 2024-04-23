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
 
def aloca_navio(,,):
    return
    
#verifica se é possivel alocar naquela posição:
def posicao_suporta(mapa,blocos,linha,coluna,orient):
    if orient == 'v':
        if linha >= len(mapa) or linha+blocos > len(mapa):
            return False
        for i in range(linha,linha+blocos):
            if mapa[i][coluna] == "N" :
                return False
    else:
        if coluna >= len(mapa[linha]) or coluna+blocos > len(mapa[linha]):
            return False
        for i in range(coluna,coluna+blocos):
            if mapa[linha][i] == "N" or i >= len(mapa[linha]):
                return False
    return True

#Aloca nais na posição correta, no tabuleiro
def aloca_navios(mapa,lista):
    for bloco in lista:
        linha = random.randint(0,len(mapa)-1)
        coluna = random.randint(0,len(mapa[linha])-1)
        orientacao = random.choice(['h', 'v'])  
        while posicao_suporta(mapa,bloco,linha,coluna,orientacao) != True:
            linha = random.randint(0,len(mapa)-1)
            coluna = random.randint(0,len(mapa[linha])-1)
            orientacao = random.choice(['h', 'v'])          
        cont_linha = -1
        cont_coluna = -1
        for i in range(len(mapa)):
            cont_linha +=1
            if i == linha:
                for j in range(len(mapa[i])):
                    cont_coluna +=1
                    if j == coluna:
                        if orientacao == 'v':
                            for k in range(bloco):
                                mapa[linha+k][j] = 'N'
                        if orientacao == 'h':
                            for l in range(bloco):
                                mapa[linha][j+l] = 'N' 
    return mapa

#Cria lista de blocos a serem colocados
def lista_de_blocos(Pais):
    saida=[]
    for navio in PAISES[Pais]:
        for i in range(PAISES[Pais][navio]):
            saida.append(CONFIGURACAO[navio])
    return saida



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

def sorteia_ataque():
    return

#Registra ataque e mostra o mapa   
def registra_ataque(let,num,mapa):
    let = ALFABETO.find(let.upper())
    saida=[]
    for nlinha in range(len(mapa)):
        linhasaida= []
        linha_em_analise= mapa[nlinha]
        for ncol in range (len(mapa[nlinha])):
            elemento_em_analise = linha_em_analise[ncol]
            if nlinha == num and ncol == let :
                #registra ataque
                if elemento_em_analise == " ":
                    linhasaida.append("A")
                elif elemento_em_analise == "N":
                    linhasaida.append("D")
            else:
                #copia celula
                linhasaida.append(elemento_em_analise)
        saida.append(linhasaida)
    return saida


#Verifica situação da celular da cpu e jogador e printa
def printa_situacao_celula(elem,jogador):
    if jogador == 'cpu':
        if elem == ' ':
            print('   ',end="")
        elif elem == 'N':
            print('   ',end="")
        elif elem == 'A':
            print('{0}███{1}'.format(CORES['blue'],CORES['reset']),end="")
        elif elem == 'D':
            print('{0}███{1}'.format(CORES['red'],CORES['reset']),end="")
    else:
        if elem == ' ':
            print('   ',end="")
        elif elem == 'N':
            print('{0}███{1}'.format(CORES['green'],CORES['reset']),end="")
        elif elem == 'A':
            print('{0}███{1}'.format(CORES['blue'],CORES['reset']),end="")
        elif elem == 'D':
            print('{0}███{1}'.format(CORES['red'],CORES['reset']),end="")
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


    

