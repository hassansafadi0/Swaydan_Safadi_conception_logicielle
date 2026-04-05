from src.cours import Cours
from src.etudiant import Etudiant


def main():
    c1 = Cours("Math", "Dr Martin")
    c2 = Cours("Algo", "Mme Dupont")

    e = Etudiant("Alice", 21, "E001", 15.5)
    e.ajouter_cours(c1)
    e.ajouter_cours(c2)

    print("=== Avant modification invalide ===")
    print(e)

    print("\n=== Test encapsulation ===")
    try:
        e.moyenne = 25
    except ValueError as erreur:
        print("Erreur capturée :", erreur)

    print("\n=== Après tentative invalide ===")
    print(e)


if __name__ == "__main__":
    main()