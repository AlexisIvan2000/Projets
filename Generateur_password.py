import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print ("Bienvenue sur le générateur de mots de passe")
nbre_lettres=int(input("Combien de lettres voulez vous dans votre mot de passe?\n "))
nbre_symboles=int(input(f"Combien symboles voulez vous?\n"))
nbre_nombres=int(input(f"Combien de nombres voulez vous?\n"))
mot_passe = ""
choix = "n"

while choix != "o":
    # Nouvelle génération
    mot_passe_liste = (
        random.choices(letters, k=nbre_lettres) +
        random.choices(symbols, k=nbre_symboles) +
        random.choices(numbers, k=nbre_nombres)
    )
    random.shuffle(mot_passe_liste)
    mot_passe = ''.join(mot_passe_liste)

    print(f"\nVotre mot de passe est : {mot_passe}")
    choix = input('Voulez-vous garder ce mot de passe ? "o" pour oui, "n" pour non\n').lower()

print("Mot de passe validé ✅")