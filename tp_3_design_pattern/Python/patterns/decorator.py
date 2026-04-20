# decorator.py - Decorator pattern
# lets us add extra info to a student (like scholarship or class delegate)
# without changing the original Etudiant class

from abc import ABC, abstractmethod


class IEtudiantComponent(ABC):
    """Interface shared by the real student and its decorators."""

    @abstractmethod
    def afficher(self) -> str:
        pass


class EtudiantDecorator(IEtudiantComponent):
    """Base decorator that just passes the call to the wrapped component."""

    def __init__(self, etudiant_component: IEtudiantComponent):
        self._etudiant_component = etudiant_component

    def afficher(self) -> str:
        return self._etudiant_component.afficher()


class EtudiantBoursierDecorator(EtudiantDecorator):
    """Adds scholarship info to the student display."""

    def __init__(self, etudiant_component: IEtudiantComponent, montant_bourse: float):
        super().__init__(etudiant_component)
        self._montant_bourse = montant_bourse

    def afficher(self) -> str:
        return (
            super().afficher()
            + f" | Statut: Boursier ({self._montant_bourse} EUR)"
        )


class EtudiantDelegueDecorator(EtudiantDecorator):
    """Adds class delegate status to the student display."""

    def afficher(self) -> str:
        return super().afficher() + " | Statut: Délégué de classe"
