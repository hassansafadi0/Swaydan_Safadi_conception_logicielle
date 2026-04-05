from src.personne import Personne


class Enseignant(Personne):
    def __init__(self, nom: str, age: int, matiere: str, salaire: float):
        super().__init__(nom, age)
        self.matiere = matiere
        self.salaire = salaire

    @property
    def matiere(self) -> str:
        return self.__matiere

    @matiere.setter
    def matiere(self, valeur: str):
        if valeur is None or not valeur.strip():
            raise ValueError("La matière ne peut pas être vide.")
        self.__matiere = valeur.strip()

    @property
    def salaire(self) -> float:
        return self.__salaire

    @salaire.setter
    def salaire(self, valeur: float):
        if valeur < 0:
            raise ValueError("Le salaire ne peut pas être négatif.")
        self.__salaire = valeur

    def afficher_details(self) -> str:
        return (
            f"Enseignant: {self.nom}, {self.age} ans, "
            f"Matière: {self.matiere}, "
            f"Salaire: {self.salaire}"
        )

    def __str__(self):
        return self.afficher_details()

    def __repr__(self):
        return (
            f"Enseignant({self.nom!r}, {self.age!r}, "
            f"{self.matiere!r}, {self.salaire!r})"
        )