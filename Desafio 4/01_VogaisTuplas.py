#   Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#   Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

frutas = ('banana', 'abacate', 'pera', 'uva', 'abacaxi')

vogais = ('a','e','i','o','u')

for palavra in frutas:
    print('Vogais da palavra', palavra, ':')
    for letra in palavra:
        if letra in vogais:
            print(letra)
  
