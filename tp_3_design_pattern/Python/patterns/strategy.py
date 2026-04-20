# strategy.py - Strategy pattern
# two types of strategies: mention calculation and student sorting
# the student can switch their mention strategy whenever we want

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from modeles.etudiant import Etudiant


# Mention calculation strategies

class ICalculMention(ABC):
    """Interface for all mention strategies."""

    @abstractmethod
    def calculer(self, moyenne: float) -> str:
        pass


class MentionStandard(ICalculMention):
    """Normal grading: Tres Bien >= 16, Bien >= 14, etc."""

    def calculer(self, moyenne: float) -> str:
        if moyenne >= 16:
            return "Très Bien"
        elif moyenne >= 14:
            return "Bien"
        elif moyenne >= 12:
            return "Assez Bien"
        elif moyenne >= 10:
            return "Passable"
        return "Ajourné"


class MentionSevere(ICalculMention):
    """Strict grading: thresholds are 1 point higher than standard."""

    def calculer(self, moyenne: float) -> str:
        if moyenne >= 17:
            return "Très Bien"
        elif moyenne >= 15:
            return "Bien"
        elif moyenne >= 13:
            return "Assez Bien"
        elif moyenne >= 10:
            return "Passable"
        return "Ajourné"


# Sorting strategies

class IStrategieTri(ABC):
    """Interface for all sorting strategies."""

    @abstractmethod
    def trier(self, etudiants: List["Etudiant"]) -> List["Etudiant"]:
        pass


class TriParMoyenne(IStrategieTri):
    """Sorts students by average (highest first)."""

    def trier(self, etudiants: List["Etudiant"]) -> List["Etudiant"]:
        return sorted(etudiants, key=lambda e: e.moyenne, reverse=True)


class TriParNom(IStrategieTri):
    """Sorts students by name (A to Z)."""

    def trier(self, etudiants: List["Etudiant"]) -> List["Etudiant"]:
        return sorted(etudiants, key=lambda e: e.nom)
