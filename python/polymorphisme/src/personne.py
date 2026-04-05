class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, valeur: str):
        if valeur is None or not valeur.strip():
            raise ValueError("Le nom ne peut pas être vide.")
        self.__nom = valeur.strip()

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, valeur: int):
        if valeur < 0 or valeur > 100:
            raise ValueError("L'âge doit être compris entre 0 et 100.")
        self.__age = valeur

    def afficher_details(self) -> str:
        return f"{self.nom}, {self.age} ans"

    def __str__(self):
        return self.afficher_details()

    def __repr__(self):
        return f"Personne({self.nom!r}, {self.age!r})"