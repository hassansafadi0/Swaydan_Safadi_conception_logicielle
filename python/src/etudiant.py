from .personne import Personne
from .cours import Cours


class Etudiant(Personne):
    def __init__(self, nom: str, age: int, numero_etudiant: str, moyenne: float):
        super().__init__(nom, age)  # obligatoire
        self.numero_etudiant = numero_etudiant
        self.moyenne = moyenne
        self.liste_cours = []

    def ajouter_cours(self, cours: Cours):
        self.liste_cours.append(cours)

    def __str__(self):
        cours_str = ", ".join(c.nom_cours for c in self.liste_cours) if self.liste_cours else "Aucun"
        return (
            f"{super().__str__()} | "
            f"ID: {self.numero_etudiant} | "
            f"Moyenne: {self.moyenne} | "
            f"Cours: {cours_str}"
        )

    def __repr__(self):
        return (
            f"Etudiant({self.nom!r}, {self.age!r}, "
            f"{self.numero_etudiant!r}, {self.moyenne!r})"
        )