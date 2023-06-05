#   Faça um programa que leia uma frase pelo teclado e mostre:
#       - Quantas vezes aparece a letra 'A'
#       - Em que posição ela aparece a primeira vez
#       - Em que posição ela aparece a última vez
count = 0
pos_letras = 0
aux = 0

print("Insira a frase: ")
frase = input()

for letra in frase:
    pos_letras +=1 
    print("Analisando a letra", letra)
    if letra == 'a' or letra == 'A': 
        count += 1
        if (count == 1):
            print("A primeira ocorrencia foi na pos", pos_letras)
        ultima_letra = pos_letras
        

print("A letra 'a' apareceu", count, "vezes")
print("A ultima aparição foi na pos: " ,ultima_letra)

