from src.personne import Personne
from src.cours import Cours


class Etudiant(Personne):
    def __init__(self, nom: str, age: int, numero_etudiant: str, moyenne: float):
        super().__init__(nom, age)
        self.__numero_etudiant = numero_etudiant
        self.moyenne = moyenne
        self.__liste_cours = []

    @property
    def numero_etudiant(self) -> str:
        return self.__numero_etudiant

    @property
    def moyenne(self) -> float:
        return self.__moyenne

    @moyenne.setter
    def moyenne(self, valeur: float):
        if valeur < 0 or valeur > 20:
            raise ValueError("La moyenne doit être comprise entre 0 et 20.")
        self.__moyenne = valeur

    @property
    def liste_cours(self):
        return tuple(self.__liste_cours)

    def ajouter_cours(self, cours: Cours):
        self.__liste_cours.append(cours)

    def afficher_details(self) -> str:
        cours_str = ", ".join(c.nom_cours for c in self.__liste_cours) if self.__liste_cours else "Aucun"
        return (
            f"Etudiant: {self.nom}, {self.age} ans, "
            f"ID: {self.numero_etudiant}, "
            f"Moyenne: {self.moyenne}, "
            f"Cours: {cours_str}"
        )

    def __str__(self):
        return self.afficher_details()

    def __repr__(self):
        return (
            f"Etudiant({self.nom!r}, {self.age!r}, "
            f"{self.numero_etudiant!r}, {self.moyenne!r})"
        )