import os

def verifica_anagrama_simples(entrada, palavras):
    
    for i in range(len(palavras)):
        anagrama = True
        if len(palavras[i]) != len(entrada):
            anagrama = False
        else:
            for x in range(len(entrada)):
                if entrada[x] not in  palavras[i]:
                    anagrama = False
                if palavras[i][x] not in entrada :
                    anagrama = False
           

        if anagrama:
            print(palavras[i])

def verifica_anagrama_complexo(entrada, palavras):
    resultado = []
    for i in range(len(palavras)):
        anagrama = True
        if len(palavras[i]) > len(entrada):
            anagrama = False
        else:
            
            for x in range(len(palavras[i])):
                if palavras[i][x] not in entrada:
                    anagrama = False
                else:
                    if entrada.count(palavras[i][x]) != palavras[i].count(palavras[i][x]):
                        anagrama = False 
                    else:
                        num_letras += len(palavras[i])

        if anagrama:
            resultado.append(palavras[i])
    
    return resultado
    

def organizar_palavras(entrada,resultado):
    frase = ''
    soma = 0
    #while soma <= len(entrada):
    #    for 
    return frase


def main():
    diretorio = os.path.dirname(__file__)
    with open(f"{diretorio}\\words.txt", 'r') as file:
        texto = file.read()

    palavras = texto.split('\n')
    entrada = ''
    while entrada != '0':
        os.system("cls")

        entrada = input("Digite uma palavra ou frase para buscarmos anagramas\nDigite 0 para Sair\n ->").upper()

        resultado = verifica_anagrama_complexo(entrada, palavras)
        
        frase = organizar_palavras(entrada, resultado)

        print(frase)

        input("------ ENTER ------")

        
            
main()
