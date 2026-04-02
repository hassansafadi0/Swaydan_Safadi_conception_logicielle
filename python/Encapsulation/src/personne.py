class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        if not value or not value.strip():
            raise ValueError("Le nom ne peut pas être vide.")
        self._nom = value.strip()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (0 <= value <= 100):
            raise ValueError("L'âge doit être compris entre 0 et 100.")
        self._age = value

    def __str__(self):
        return f"Personne: {self._nom}, {self._age} ans"