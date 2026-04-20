# personne.py - abstract class Personne and its child class Professeur

from abc import ABC, abstractmethod


class Personne(ABC):
    """Abstract class that represents a person in the system."""

    def __init__(self, nom: str, age: int):
        self._nom = nom
        self._age = age

    @property
    def nom(self) -> str:
        return self._nom

    @property
    def age(self) -> int:
        return self._age

    @abstractmethod
    def afficher(self) -> str:
        """Returns a text description of the person."""
        pass


class Professeur(Personne):
    """A professor with a specialty."""

    def __init__(self, nom: str, age: int, specialite: str):
        super().__init__(nom, age)
        self.specialite = specialite

    def afficher(self) -> str:
        return (
            f"Professeur(nom={self.nom}, age={self.age}, "
            f"specialite={self.specialite})"
        )
