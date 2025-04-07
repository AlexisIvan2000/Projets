import random 
amis=["Alexis","Gaetan","Jordy","Djibril"]
print("Qui paiera l'addtion pour  toute la table? 🤑")
print("Veuillez placer vos cartes dans le bocales")
index=random.randrange(len(amis))
if amis[index] == "Alexis":
    print(f"Le serveur a choisi la carte de {amis[index]} ! \nAlexis va devoir payer l'addition... 😅")
elif amis[index]== "Gaetan":
    print(f"Le serveur a choisi la carte de {amis[index]} ! \nGaetan, c'est ton tour de payer. On compte sur toi ! 💸")
elif amis[index] == "Jordy":
     print(f"Le serveur a choisi la carte de {amis[index]} ! \nJordy va devoir payer cette fois ! 🎉")
elif amis[index] == "Djibril":
    print(f"Le serveur a choisi la carte de {amis[index]} ! \nDjibril, à toi de régler l'addition, mon ami ! 😎")
