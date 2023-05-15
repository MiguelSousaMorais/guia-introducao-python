# Escreva uma função que receba um numero pelo entrada e retorna se aquele numero é primo ou não 
def primos(x):
    if x <= 1:
        return False
    for i in range(2, int(x/2) ):
        if x % i == 0:
            return False
    return True

print(primos(int(input("Digite o número para a verificação:"))))