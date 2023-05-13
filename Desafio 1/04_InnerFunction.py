# Criar uma função externa que irá aceitar dois parametros, a e b
# Crie uma função interna dentro da função externa que irá retornar a soma os parametros a e b 
# Na função externa, adicione 5 ao retorno da funcao interna e escreva na tela este valor
def soma(a,b) :
    print('Somando A e B')
    print(a + b)
    return a+b

def funcao(a,b) : 
    
    soma_com_5 = soma(a,b) + 5.0
    print('Somando com 5 tambem')
    print(soma_com_5)
    
print("Digite os valores a serem somados")
x, y = map(float, input().split())
 
funcao(x,y)    