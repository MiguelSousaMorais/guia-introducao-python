# Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos lados de um triângulo, 
# e se forem verificar se é um triângulo equilátero, isóscele ou escaleno. 
# Se eles não formarem um triângulo, escrever uma mensagem.

x,y,z = map(int,input().split())

if ((x + y > z) & (x + z > y) & (y + z > x)) :
    
    if (x == y == z):
        print("É um triângulo equilátero!")
    
    elif (x == y or x == z or y == z):
        print("É um triângulo isósceles!")
    
    else:
        print("É um triângulo escaleno!")
else:
   
    print("Os valores informados não formam um triângulo.")