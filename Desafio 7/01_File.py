"""
referencia: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# 1-Abra o arquivo do diretorio atual "foo.txt"
# Printe todo o conteudo do arquivo , então feche o arquivo
arquivo = open('foo.txt','r')
for linha in arquivo:
    print(linha)
arquivo.close()
# 2- Crie um arquivo chamado "bar.txt" 
# Abra o arquivo e conte quanta vezes a palavra "sir" aparece 
# Escreva no arquivo que voce criou quantas palavras foram encontradas
# Feche o arquivo

arquivo_2 = open('bar.txt','w')

count = 0

arquivo = open('foo.txt','r')

for linha in arquivo:
    for palavra in linha.split():
        if "sir" in palavra: 
            count +=1
            
arquivo.close()
arquivo_2.write("A palavra 'sir' aparece " + str(count) + " vezes.")
arquivo_2.close()