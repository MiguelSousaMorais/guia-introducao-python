# Defina a função div que recebe como argumentos dois números naturais  m  e  n  e 
# devolve o resultado da divisão inteira de  m  por  n . 

# div(7,2)
# Esperado: 3

def div(m,n):
    if(n==0) :
        print("Não é possível realizar uma divisão por zero")
    else :
     return m // n   
 
x = int(input("Digite o número a ser dividido\n"))
y = int(input("Digite o divisor\n"))
print("A divisão inteira é:\n",div(x,y))