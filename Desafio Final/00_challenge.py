filmes = []


x = 1

print("\nVamos organizar os filmes que você já assitiu por nome, data e nota.")
print("Evite a utilização de caracteres especiais, acentos e 'ç'.\n")

while (x):
    aux = input("Digite:\n '1' se você quer inserir um novo filme.\n '2' se quer ver os filmes inseridos em determinado gênero.\n '3' para buscar um filme inserido pelo nome.\n '4' para encerrar o programa\n\n")

    if aux == str(4):
        x = 0 

    if aux == str(1):
        nome = input("Digite o nome do filme\n")
        data = input("Digite a data de visualização\n")
        nota = input("Digite a nota do filme\n") 
        genero = input("Digite o genero do filme\n") 
        
        if (genero.lower() == "aventura"):
                        
            novo_filme = {
            "nome": nome,
            "data": data,
            "nota": nota
            }
            
            filmes.append(novo_filme)
            arquivo = open('aventura.txt','a')
            arquivo.write("\nFilme: " + nome + 
                          "\nData: " + data 
                          + "\n Nota: " + nota + "\n---\n")
            arquivo.close()

        
        if (genero.lower() == "comedia"):
                        
            novo_filme = {
            "nome": nome,
            "data": data,
            "nota": nota
            }
            
            filmes.append(novo_filme)
            arquivo = open('comedia.txt','a')
            arquivo.write("\nFilme: " + nome + 
                          "\nData: " + data + "\n Nota: " + nota + "\n---\n")
            arquivo.close()
        
        if (genero.lower() == "acao"):
                        
            novo_filme = {
            "nome": nome,
            "data": data,
            "nota": nota
            }
            
            filmes.append(novo_filme)
            arquivo = open('acao.txt','a')
            arquivo.write("\nFilme: " + nome + 
                          "\nData: " + data + "\n Nota: " + nota + "\n---\n")
            arquivo.close()
            
        if (genero.lower() == "drama"):
                        
            novo_filme = {
            "nome": nome,
            "data": data,
            "nota": nota
            }
            
            filmes.append(novo_filme)
            arquivo = open('drama.txt','a')
            arquivo.write("\nFilme: " + nome + 
                          "\nData: " + data + "\n Nota: " + nota + "\n---\n")
            arquivo.close()
            
        if (genero.lower() == "terror"):
                        
            novo_filme = {
            "nome": nome,
            "data": data,
            "nota": nota
            }
            
            filmes.append(novo_filme)
            arquivo = open('terror.txt','a')
            arquivo.write("\nFilme: " + nome + 
                          "\nData: " + data + "\n Nota: " + nota + "\n---\n")
            arquivo.close()
            
        if (genero.lower() == "fantasia"):
                        
            novo_filme = {
            "nome": nome,
            "data": data,
            "nota": nota
            }
            
            filmes.append(novo_filme)
            arquivo = open('fantasia.txt','a')
            arquivo.write("\nFilme: " + nome + 
                          "\nData: " + data + "\n Nota: " + nota + "\n---\n")
            arquivo.close()                
    

    if aux == str(2):
        genero = input("\nDigite o gênero desejado:\n")
        
        if genero.lower() == "aventura":
            arquivo = open('aventura.txt','r')
            for linha in arquivo:
                print(linha)
        
        if genero.lower() == "comedia":
            arquivo = open('comedia.txt','r')
            for linha in arquivo:
                print(linha)
        
        if genero.lower() == "acao":
            arquivo = open('acao.txt','r')
            for linha in arquivo:
                print(linha)                
        
        if genero.lower() == "drama":
            arquivo = open('drama.txt','r')
            for linha in arquivo:
                print(linha)
        
        if genero.lower() == "terror":
            arquivo = open('terror.txt','r')
            for linha in arquivo:
                print(linha)
        
        if genero.lower() == "fantasia":
            arquivo = open('fantasia.txt','r')
            for linha in arquivo:
                print(linha)                        
                
    
    if aux == str(3):
        pesquisa = input("\nDigite o nome do filme:\n")   
                 
        for filme in filmes:
            if (filme["nome"] == pesquisa ):
                print("\nVocê assistiu este filme em:", filme["data"])
                print("A nota dada para este filme foi:", filme["nota"],"\n")
        