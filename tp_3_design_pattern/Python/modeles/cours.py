# cours.py - represents a course (unite d'enseignement)


class Cours:
    """A course with a name and the professor who teaches it."""

    def __init__(self, nom_cours: str, professeur: str):
        self.nom_cours = nom_cours
        self.professeur = professeur

    def __str__(self) -> str:
        return f"{self.nom_cours} (Prof: {self.professeur})"
