import random

value = ['pierre', 'feuille', 'ciseaux']

pierre = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

feuille = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

ciseaux = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


while True:
    choix_input = input('Faites votre choix : "0" pour pierre, "1" pour feuille, "2" pour ciseaux, ou "q" pour quitter :\n')

    if choix_input.lower() == 'q':
        print("Merci d'avoir joué ! À bientôt 👋")
        break

    if not choix_input.isdigit():
        print("Entrée invalide. Veuillez entrer un chiffre (0, 1, 2) ou 'q' pour quitter.")
        continue

    choix_joueur = int(choix_input)

    if choix_joueur not in [0, 1, 2]:
        print("Choix invalide !!! Veuillez choisir 0, 1 ou 2.")
        continue

    print(f"\nVous avez choisi {value[choix_joueur]}")
    if choix_joueur == 0:
        print(pierre)
    elif choix_joueur == 1:
        print(feuille)
    elif choix_joueur == 2:
        print(ciseaux)

    choix_ordinateur = random.randrange(3)
    print(f"\nL'ordinateur a choisi {value[choix_ordinateur]}")
    if choix_ordinateur == 0:
        print(pierre)
    elif choix_ordinateur == 1:
        print(feuille)
    elif choix_ordinateur == 2:
        print(ciseaux)

    print("********** Résultat **********")
    if choix_joueur == choix_ordinateur:
        print("Match nul 🤝")
    elif (choix_joueur == 0 and choix_ordinateur == 2) or \
         (choix_joueur == 1 and choix_ordinateur == 0) or \
         (choix_joueur == 2 and choix_ordinateur == 1):
        print("🎉 Vous remportez la partie !")
    else:
        print("😢 Vous avez perdu. Dommage !")

    print("\n-----------------------------\n")
