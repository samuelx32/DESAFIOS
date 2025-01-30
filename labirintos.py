import time
import os
import readchar as rc

def visualizador(matriz):
    str_matriz = ""
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            str_matriz += matriz[l][c] + " "

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
                matriz[x-1][y] = "+"
                x -= 1
            elif matriz[x-1][y] == "S":
                parar = True
        elif mov == "s":
            if matriz[x+1][y] == " ":
                matriz[x][y] = " "
                matriz[x+1][y] = "+"
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


matriz = [["x","x","x","x","x","x"," "," "," ","x"," "," "," ","x","x","x","x"," "," "," "],
          ["E",">"," "," "," ","x"," ","x"," "," "," ","x"," ","x"," ","-","-","-","-","-"],
          ["x","x","x","x"," ","x"," ","x"," ","x","x"," "," "," "," ","-","-","-","-","-"],
          [" "," "," "," "," "," "," ","x"," ","x"," "," ","x"," ","-","-","-","-","-","-"],
          [" ","x","x","x","x","x","x","x"," ","x"," "," ","x","-","-","-","-","-","-","-"],
          [" ","x"," "," "," "," "," ","x"," ","x"," "," ","x","-","-","-","-","-","-","-"],
          [" ","x","x","x","x","x"," ","x"," ","x"," "," ","x","-","-","-","-","-","-","-"],
          [" ","x"," "," "," "," "," "," "," ","x"," "," ","x","-","-","-","-","-","-","-"],
          [" ","x","x","x","x","x","x","x"," ","x"," "," ","-","-","-","-","-","-","-","-"],
          [" "," ","x"," "," "," "," "," "," ","x"," "," ","x","-","-","-","-","-","-","-"],
          ["x"," ","x"," ","x","x"," ","x","x","x"," "," ","x","-","-","-","-","-","-","-"],
          ["x"," ","x"," "," "," "," ","x"," "," "," "," ","x","-","-","-","-","-","-","-"],
          ["x"," ","x"," ","x","x"," "," ","x"," "," "," "," "," "," ","x"," ","-","-","-"],
          ["x"," ","x"," ","x"," ","x"," ","x","x","x","x","x","x"," ","x"," "," "," ","x"],
          ["x"," ","x"," ","x"," "," "," "," "," ","x"," "," ","x"," ","x"," ","x"," ","x"],
          ["x"," ","x"," ","x","x","x"," ","x"," ","x"," ","x","x"," ","x"," ","x"," ","x"],
          [" "," ","x"," ","x"," ","x"," ","x"," "," "," ","x"," "," ","x"," ","x"," ","x"],
          ["x","x","x"," ","x"," ","x"," ","x"," ","x"," ","x","x","x","x"," ","x"," ","x"],
          ["x"," "," "," "," "," ","x"," "," "," ","x"," ","x"," "," "," "," ","x"," ","S"],
          ["x","x","x","x","x","x","x","x","x","x","x"," "," "," ","x","x","x","x","x","x"]
    ]

parar = False
x,y = 1,1
while(parar == False):
    os.system("cls")
    visualizador(matriz)
    print("""
        W    
    A   S   D     <- MOVIMENTAÇÃO
""")
    mov = ""
    while mov not in {"a","s","w","d"}:
        mov = rc.readchar()
    
    
    matriz,parar,x,y = movimentar(mov,matriz,x,y)

for i in range(15):
    os.system("cls")
    if i % 2 != 0:
        print("""
            **                    ** 
                **  PARABÉNS  **
            **                    **  

        """)
    else:
        print("""
                              
                    PARABÉNS  
              

        """)
    time.sleep(0.2)
    
    
  