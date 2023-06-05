"""
Para este exercicio, voce tem uma lista de dicionarios. Cada dicionario
tem as seguintes chaves:
 - lat: inteiro representando o valor de latitude
 - lon: inteiro representando o valor de longitude
 - name: nome do local
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Adicione um novo local a lista
# YOUR CODE HERE
novo_local = {
    "lat": 90,
    "lon": 90,
    "name": "novo local"
}
waypoints.append(novo_local)

# Modifique o dicionario com nome "a place" para uma longitude
# de valor -130 e mude seu nome para "not a real place"

for local in waypoints:
    if (local["name"] == "a place"):
        local["name"] = "not a real place"
        local["lon"] = -130
        
    

# YOUR CODE HERE

# Crie um loop que escreva na tela todos os valores dos dicionarios da lista
# YOUR CODE HERE
for local in waypoints:
    print("Nome =",local["name"], "\nlongitude =", local["lon"],"\n Latitude =", local["lat"])