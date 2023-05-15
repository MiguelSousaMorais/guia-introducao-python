# Os números de Fibonacci são representados pela sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... ]
# onde cada valor é calculado pela soma dos dois anteriores. 
# Faça um programa que gere e imprima os primeiros 10 valores desta sequência utilizando for ou while.
# Definindo as variáveis iniciais da sequência de Fibonacci
a, b = 0, 1

# Imprimindo os primeiros 10 valores da sequência de Fibonacci
i = 0
while (i < 10):
    print(a)
    aux = a
    a = b
    b = aux + b
    i += 1
