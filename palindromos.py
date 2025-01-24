palavras = ["tenet","amadeus","teste","sonnos"]

for palavra in palavras:
    palindromo = True
    letras = len(palavra)
    
    for i in range(int(letras/2)):
        if palavra[i] != palavra[letras - (i + 1)]:
            palindromo = False
    
                
    if not palindromo:    
        print (f"{palavra} -> Não é palindromo")
    else:
        print (f"{palavra} -> É palindromo")