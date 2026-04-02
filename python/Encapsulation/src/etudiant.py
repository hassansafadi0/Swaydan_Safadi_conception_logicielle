from .personne import Personne
from .cours import Cours
from typing import List

class Etudiant(Personne):
    def __init__(self, nom: str, age: int, numero_etudiant: str, moyenne: float):
        super().__init__(nom, age)
        self.numero_etudiant = numero_etudiant
        self.moyenne = moyenne
        self.liste_cours: List[Cours] = []

    @property
    def moyenne(self):
        return self._moyenne

    @moyenne.setter
    def moyenne(self, value):
        if not (0 <= value <= 20):
            raise ValueError("La moyenne doit être comprise entre 0 et 20.")
        self._moyenne = value

    def ajouter_cours(self, cours: Cours):
        self.liste_cours.append(cours)

    def __str__(self):
        cours_str = ", ".join(c.nom_cours for c in self.liste_cours) if self.liste_cours else "Aucun"
        return f"{super().__str__()} | ID: {self.numero_etudiant} | Moyenne: {self._moyenne} | Cours: {cours_str}"