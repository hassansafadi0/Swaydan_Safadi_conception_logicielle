from src.cours import Cours
from src.etudiant import Etudiant


def main():
    c1 = Cours("Math", "Dr Martin")
    c2 = Cours("Algo", "Mme Dupont")

    e = Etudiant("Alice", 21, "E001", 15.5)

    e.ajouter_cours(c1)
    e.ajouter_cours(c2)

    print(e)

    for c in e.liste_cours:
        print(c)


if __name__ == "__main__":
    main()