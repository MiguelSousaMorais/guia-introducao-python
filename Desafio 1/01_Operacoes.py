# Construa um programa que receba como entrada três valores inteiros. Ao final imprima a soma, multiplicação e divisão deste itens.
print("Digite os três números que vão passar pelas operações")
a, b, c = map(int, input().split())

soma = a + b + c
multiplicacao = a * b * c
divisao = a/b/c
print(soma,multiplicacao,divisao)

# Escreva um programa que leia um número e apresente a raiz quadrada deste número.

x = int(input('Digite o número para encontrarmos sua raiz: '))

print(x**0.5)


