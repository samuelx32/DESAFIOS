# Qualquer célula viva com menos de 2 vizinhos vivos morre (solidão).
# Qualquer célula viva com 2 ou 3 vizinhos vivos continua viva.
# Qualquer célula viva com mais de 3 vizinhos vivos morre (superpopulação).
# Qualquer célula morta com exatamente 3 vizinhos vivos se torna viva (reprodução).

# Vizinhos = Linha Atual, Linha + 1 e Linha - 1, coluna atual, coluna + 1, coluna - 1
# [linha][coluna + 1] -- [linha][coluna - 1]
# [linha + 1][coluna] -- [linha + 1][coluna + 1] -- [linha + 1][coluna - 1]
# [linha - 1][coluna] -- [linha - 1][coluna + 1] -- [linha - 1][coluna - 1]
import time
import os

def visualizador(matriz):
    str_matriz = ""
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            str_matriz += matriz[l][c] + " "

        str_matriz += "\n"

    print(str_matriz)

def aplicar_mudancas(matriz,mudancas):
    for x in range(len(mudancas)):
        matriz[mudancas[x][0]][mudancas[x][1]] = mudancas[x][2]
    
    return matriz

def verificador(matriz):
    pos = 0
    mudancas = []
    parar = True
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            contador_mortos = 0
            contador_vivos = 0
            pos += 1
            if l + 1 <= len(matriz) - 1:
                if matriz[l+1][c] == "-":
                    contador_mortos += 1
                else:
                    contador_vivos += 1
                    parar = False
            if l - 1 >= 0:
                if matriz[l-1][c] == "-":
                    contador_mortos += 1
                else:
                    contador_vivos += 1
                    parar = False


            if c + 1 <= len(matriz[l]) - 1:
                if matriz[l][c+1] == "-" :
                    contador_mortos += 1
                else:
                    contador_vivos += 1
                    parar = False

                if l + 1 <= len(matriz) - 1:
                    if matriz[l+1][c+1] == "-":
                        contador_mortos += 1
                    else:
                        contador_vivos += 1
                        parar = False
                if l - 1 >= 0:
                    if matriz[l-1][c+1] == "-":
                        contador_mortos += 1
                    else:
                        contador_vivos += 1
                        parar = False

            if c - 1 >= 0:
                if matriz[l][c-1] == "-" :
                    contador_mortos += 1
                else:
                    contador_vivos += 1
                    parar = False
                
                if l + 1 <= len(matriz) - 1:
                    
                    if matriz[l+1][c-1] == "-":
                        contador_mortos += 1
                    else:
                        contador_vivos += 1
                        parar = False
                
                if l - 1 >= 0:
                    if matriz[l-1][c-1] == "-":
                        contador_mortos += 1
                    else:
                        contador_vivos += 1
                        parar = False
          
            if matriz[l][c] == 'x':
                if contador_vivos > 3:
                    mudancas.append([l,c,'-'])
                if contador_vivos <= 1:
                    mudancas.append([l,c,'-'])

            if matriz[l][c] == '-':
                if contador_vivos == 3:
                    mudancas.append([l,c,'x'])

    os.system("cls")
    visualizador(matriz)
    matriz = aplicar_mudancas(matriz,mudancas)
    time.sleep(0.1)
    
    return matriz,parar
            
                
                


def main():
    matriz = [["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","x","-","-","-","-","x","-","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","x","x","x","-","-","-","x","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","-","x","-","-","x","x","x","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","x","x","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","x","x","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","x","x","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","x","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","-","-","-","x","-","-","-","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","-","-","-","-","x","x","x","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","-","-","-","-","x","x","x","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"],
          ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]
    ]
    parar = False
    while(parar == False):
        matriz,parar = verificador(matriz)

op = input("Iniciar?(y/n)")
if op == "y":
    main()