# Uma empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. 
# Se o valor da venda de um corretor for maior que R$ 50.000.00 a comissão será de 12% do valor vendido. 
# Se o valor da venda do corretor estiver entre R$ 30.000.00 e R$ 50.000.00 (incluindo extremos) a comissão será de 9.5%. Em qualquer outro caso, a comissão será de 7%. 
# Escreva um programa que calcule a comissão de um vendedor baseado no valor de suas vendas.

valor_vendas = int(input("Digite o valor das vendas: "))
comissao = 0

def valor_comissao(a) :
    if(a>50000.00) :
        return a/100*12
    elif(30000.00<=a<=50000.00):
        return a/100*9.5
    else :
        return a/100*7

comissao = valor_comissao(valor_vendas)

print(comissao)