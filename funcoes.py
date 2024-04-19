#funções para facilitar a organização
from Basededados import*

def cria_mapa():
    return
    
def aloca_navio():
    return
    
def aloca_se_possivel():
    return
    
def foi_derrotado():
    return
    
def sorteia_cpu():
    return
    
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




    


    

    
