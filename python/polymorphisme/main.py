from src.cours import Cours
from src.etudiant import Etudiant
from src.enseignant  import Enseignant


def main():
    e = Etudiant("Alice", 21, "E001", 15.5)
    e.ajouter_cours(Cours("Math", "Dr Martin"))
    e.ajouter_cours(Cours("Algo", "Mme Dupont"))

    ens = Enseignant("Karim", 45, "Programmation", 3500.0)

    personnes = [e, ens]

    print("=== Polymorphisme ===")
    for personne in personnes:
        print(personne.afficher_details())


if __name__ == "__main__":
    main()