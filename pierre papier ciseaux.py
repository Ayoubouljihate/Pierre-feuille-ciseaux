from random import choice


COUP = ("Pierre", "Feuille", "Ciseaux")


while input("Jouez (joue/joue pas): ") != "joue pas":


    print("Le jeu du: Pierre - Feuille - Ciseaux")


    a = int(input("Choisissez un chiffre:\n0: Pierre\n1: Feuille\n2: Ciseaux\n-> "))
    b = choice(range(3))

    print("{} VS {}".format(COUP[a], COUP[b]))
    if a == b:
        print("Égalité")
    elif (a>b and b+1==a) or (a<b and a+b==2):
        print("Vous gagnez")
    else:
        print("Vous perdez")
else:
    print("Bye Bye")