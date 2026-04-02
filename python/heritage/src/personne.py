class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"Personne: {self.nom}, {self.age} ans"

    def __repr__(self):
        return f"Personne({self.nom!r}, {self.age!r})"
