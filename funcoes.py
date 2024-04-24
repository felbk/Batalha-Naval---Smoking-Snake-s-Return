#funções para facilitar a organização
from Basededados import*
import random

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

#confere se posição ja foi atacada
def ja_foi_atacado(col,linha,mapa):
    if mapa[linha][col]=="A" or mapa[linha][col]=="D" :
        return True
    else:
        return False

#Aloca nas na posiç~eos correta da cpu, no tabuleiro.
def aloca_navios_para_cpu(mapa,lista):
    for bloco in lista:
        saida = []
        linha = random.randint(0,len(mapa)-1)
        coluna = random.randint(0,len(mapa[linha])-1)
        orientacao = random.choice(['h', 'v'])  
        while posicao_suporta(mapa,bloco,linha,coluna,orientacao) != True:
            linha = random.randint(0,len(mapa)-1)
            coluna = random.randint(0,len(mapa[linha])-1)
            orientacao = random.choice(['h', 'v'])          
        for i in range(len(mapa)):
            linhasaida = []
            linha_em_analise = mapa[i]
            for j in range(len(mapa[i])):
                elemento_em_analise = linha_em_analise[j]
                if orientacao == 'v':
                    if j == coluna and i in range(linha,linha+bloco):
                            linhasaida.append('N')
                    else:
                        linhasaida.append(elemento_em_analise)
                if orientacao == 'h':
                    if j in range(coluna,coluna+bloco) and i == linha:
                        linhasaida.append('N')
                    else:
                        linhasaida.append(elemento_em_analise)
            saida.append(linhasaida)
        mapa = saida
    return mapa


def aloca_navios_para_player(mapa,lista,mapacpu,cpu,player):
    for bloco in lista:
        saida = []
        colorir('cyan','\n Alocando navio de tamanho {}\n'.format(bloco),True)
        # insere valores de linha coluna e orientação COM VERIFICAÇÃO
        linha = input_valida_linha()

        coluna = ALFABETO.find(input("Informe a letra: ").upper())
        while not coluna < len(mapa):
            colorir("red","Coluna inválida, digite a letra novamente: ",False)
            coluna = ALFABETO.find(input("").upper())

        orientacao = input("Digite a orientação (v (vertical) ou h (horizontal))").lower()
        while orientacao not in ['v','h']:
            colorir("red","Orientação inválida, digite v ou h : ",False)
            orientacao = input("").lower()

        #analisa se pode alocar
        while posicao_suporta(mapa,bloco,linha,coluna,orientacao) != True:
            colorir('red',"Não foi possível alocar nessa posição, tente novamente:",True)

             # insere valores de linha coluna e orientação COM VERIFICAÇÃO
            linha = input_valida_linha()

            coluna = ALFABETO.find(input("Informe a letra: ").upper())
            while not coluna < len(mapa):
                colorir("red","Coluna inválida, digite a letra novamente: ",False)
                coluna = ALFABETO.find(input("").upper())

            orientacao = input("Digite a orientação (v (vertical) ou h (horizontal))").lower()
            while orientacao not in ['v','h']:
                colorir("red","Orientação inválida, digite v ou h : ",False)
                orientacao = input("").lower()

                    
        for i in range(len(mapa)):
            linhasaida = []
            linha_em_analise = mapa[i]
            for j in range(len(mapa[i])):
                elemento_em_analise = linha_em_analise[j]
                if orientacao == 'v':
                    if j == coluna and i in range(linha,linha+bloco):
                            linhasaida.append('N')
                    else:
                        linhasaida.append(elemento_em_analise)
                if orientacao == 'h':
                    if j in range(coluna,coluna+bloco) and i == linha:
                        linhasaida.append('N')
                    else:
                        linhasaida.append(elemento_em_analise)
            saida.append(linhasaida)
        mapa = saida
        mostra_jogo(mapacpu,mapa,cpu,player,len(mapa))
    return mapa

def input_valida_linha():
    linha = input("Informe o número: ")
    if linha not in numeros:
        invalido= True
    else:
        linha = int(linha)-1
        invalido = False
    while invalido:
        colorir("red","Linha inválida, digite o número da linha novamente: ",False)
        linha = input("")
        if linha not in numeros:
            invalido= True
        else:
            linha = int(linha)-1
            invalido = False
    return linha

   
    
    

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
    return random.choice(listp)

#Registra ataque e mostra o mapa   
def registra_ataque(let,num,mapa):
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
                    retorno = 'A'
                elif elemento_em_analise == "N":
                    linhasaida.append("D")
                    retorno = 'D'
            else:
                #copia celula
                linhasaida.append(elemento_em_analise)
        saida.append(linhasaida)
    return [saida,retorno]


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
def colorir(cor= "cor",texto="Texto",quebralinha=True or False):
    if quebralinha:
        print('{0}{1}{2}'.format(CORES[cor],texto,CORES['reset']))
    else:
        print('{0}{1}{2}'.format(CORES[cor],texto,CORES['reset']), end="")
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


def mostra_jogo(mapacpu,mapaplayer,cpu,player,n):
    texto=" COMPUTADOR - "+cpu
    colorir('red',texto,False)

    tam = n*3 +6
    texto = " "*(tam - len(texto))
    print(texto,end="")

    texto= " JOGADOR - "+player
    colorir('blue',texto,True)

    col=''
    for i in range (n):
        col+=" "+ALFABETO[i]+' '
    col= ' '*2+col+' '*2
    texto = col+' '*2 + col
    print(texto)

    for i in range(1,n+1):
        if i<10:
            texto=' '+str(i)
            print(texto,end="")
        else:
            texto= str(i)
            print(texto,end="")
        for j in range(0,n):
            printa_situacao_celula(mapacpu[i-1][j],'cpu')

        if i<10:
            texto=str(i)+" "
            print(texto,end="")
        else:
            texto= str(i)
            print(texto,end="")
        texto = " "*2
        print(texto,end="")

        if i<10:
            texto=' '+str(i)
            print(texto,end="")
        else:
            texto= str(i)
            print(texto,end="")
        for j in range(0,n):
            printa_situacao_celula(mapaplayer[i-1][j],'player')

        if i<10:
            texto=str(i)+" "
            print(texto)
        else:
            texto= str(i)
            print(texto)
    texto = col+' '*2 + col
    print(texto)
    return



