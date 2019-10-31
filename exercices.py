#exercice 1------------------------------------------------------
pizzas=["reine","sicilienne","4 saisons","margarita","vesuve","calzone"]
for pizza in pizzas[:3]:
    print(pizza)
for pizza in pizzas[2:5]:
    print(pizza)
for pizza in pizzas[3:]:
    print(pizza)
#Exercice 2-----------------------------------------------------------
friends_pizzas=pizzas[:]
pizzas.append("chorizo")
friends_pizzas.append("pescatore")
print("Mes pizzas originales sont",pizzas)
print("Les pizzas préférées de mon ami sont",friends_pizzas)
#Exercice 3------------------------------------------------------------
buffet=("riz","soja","viande","poisson","frites")
for aliment in buffet:
    print(aliment)
    #buffet[0]="salade" # OK rejected
    buffet = ("riz", "soja", "viande", "saumon", "pates")
for aliment in buffet:
    print(aliment)