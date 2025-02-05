import time
import os
import readchar as rc


def parabens():
    for i in range(15):
        os.system("cls")
        if i % 2 != 0:
            print("""
                                      
                    **  PARABÉNS  **
                                      

            """)
        else:
            print("""
                                
                        PARABÉNS  
                

            """)
        time.sleep(0.2)

def visualizador(matriz):
    str_matriz = ""
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            str_matriz += matriz[l][c] + " "

        str_matriz += "\n"

    print(str_matriz)

def visualizador_hard(matriz,x,y):
    str_matriz = ""
    for l in range(len(matriz)):
        
        for c in range(len(matriz[l])):
            if c == 0 or c == (len(matriz[l])-1) or l == 0 or l == (len(matriz)-1):
                str_matriz += matriz[l][c] + " "
            elif (l >= x-3 and l <= x+3) and (c >= y-3 and c <= y+3):
                str_matriz += matriz[l][c] + " "
            else:
                str_matriz += " " + " "

        str_matriz += "\n"

    print(str_matriz)



def movimentar(mov,matriz,x,y):
    parar = False
    try:
        if mov == "d":
            if matriz[x][y+1] == " ":
                matriz[x][y] = " "
                matriz[x][y+1] = ">"
                y += 1
            elif matriz[x][y+1] == "S":
                parar = True
                
        elif mov == "w":
            if matriz[x-1][y] == " ":
                matriz[x][y] = " "
                matriz[x-1][y] = "^"
                x -= 1
            elif matriz[x-1][y] == "S":
                parar = True
        elif mov == "s":
            if matriz[x+1][y] == " ":
                matriz[x][y] = " "
                matriz[x+1][y] = "v"
                x += 1
            elif matriz[x+1][y] == "S":
                parar = True
        elif mov == "a":
            if matriz[x][y-1] == " ":
                matriz[x][y] = " "
                matriz[x][y-1] = "<"
                y -= 1
            elif matriz[x][y-1] == "S":
                parar = True
    except:
        return matriz,parar,x,y

    return matriz,parar,x,y




def main(matriz):
    parar = False
    x,y = 1,1
    while(parar == False):
        os.system("cls")
        visualizador_hard(matriz,x,y)
        print("""
            W    
        A   S   D     <- MOVIMENTAÇÃO
    """)
        mov = ""
        while mov not in {"a","s","w","d"}:
            mov = rc.readchar()
        
        
        matriz,parar,x,y = movimentar(mov,matriz,x,y)


    parabens()

if __name__ == '__main__':
    labirinto = [
    ["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","|"],
    ["E",">"," ","|"," ","|","-","-","-","|"," "," "," "," "," ","|","-","-","-","|"],
    ["|","-"," ","|"," "," "," "," "," ","|"," ","-"," ","-"," ","|"," "," "," ","|"],
    ["|"," "," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|","-","-"," ","|"],
    ["|"," ","-","|"," ","|"," ","|"," "," "," ","|"," ","|"," "," "," "," ","|","|"],
    ["|"," "," ","|"," ","|"," "," ","-","-","-","|"," ","|","-","-","-","-","-","|"],
    ["|","-"," ","|"," ","|","-","-"," "," "," ","|"," ","|"," "," "," "," "," ","|"],
    ["|"," "," "," "," "," "," ","|","-","-","-","|"," ","|"," ","|","-","-"," ","|"],
    ["|","-","-","-","-","-"," ","|"," "," "," ","|"," "," "," ","|"," "," "," ","|"],
    ["|"," "," "," ","|"," "," "," ","-","|","-","|","-","-","-","|","-"," ","-","|"],
    ["|"," ","-"," ","|"," ","-","|"," ","|"," "," "," "," "," "," "," "," "," ","|"],
    ["|"," ","|"," "," "," "," "," "," ","|","-","-","-","|"," ","-","|","-"," ","|"],
    ["|"," ","|","-","-","-","-","-"," ","|"," ","|"," ","|"," "," ","|"," "," ","|"],
    ["|"," "," "," "," "," ","|"," "," "," "," ","-"," ","|"," ","|"," "," "," ","|"],
    ["|"," ","-","-","-"," ","|","-","-","|"," ","|"," "," "," ","|","-"," "," ","|"],
    ["|"," "," "," "," "," "," "," "," ","|","-","-","-","|"," ","|"," "," "," ","|"],
    ["|","-","-","-","-","-","-","-"," ","|"," "," "," "," "," ","|"," ","|","-","|"],
    ["|"," "," "," "," "," "," "," "," ","|","-","-","|"," "," ","|"," ","|"," ","|"],
    ["|","-"," ","-","-","-","-","-","-","|"," "," "," "," ","-","|","-","|"," ","|"],
    ["|"," "," "," "," ","|"," "," "," "," "," ","|"," "," "," "," "," "," "," ","|"],
    ["|","-","-","-","-","-","S","-","-","-","-","-","-","-","-","-","-","-","-","|"],
    ]

    main(labirinto)

    
  