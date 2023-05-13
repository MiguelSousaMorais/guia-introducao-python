# Escreva uma função para encontrar o maior entre 3 numeros

#def Max(a,b,c):

print('Digite na tela os 3 números a serem comparados\n')
x,y,z = map(float, input().split())
if(x>y) :
    maior = x
else :
    maior = y

if(maior < z) :
    maior = z

print("O maior número dentre os comparados é o:\n",maior)
    