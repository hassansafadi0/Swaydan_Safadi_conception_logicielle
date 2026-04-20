# etudiant.py - the Student class
# it inherits from Personne and uses Observer, Decorator and Strategy patterns

from __future__ import annotations

from typing import List

from modeles.personne import Personne
from modeles.cours import Cours
from patterns.observer import ISubject, IObserver
from patterns.decorator import IEtudiantComponent
from patterns.strategy import ICalculMention, MentionStandard


class Etudiant(Personne, ISubject, IEtudiantComponent):
    """Represents a student in the academic system."""

    def __init__(
        self,
        nom: str,
        age: int,
        numero_etudiant: str,
        moyenne: float = 0.0,
        strategie_mention: ICalculMention | None = None,
    ):
        super().__init__(nom, age)
        self.numero_etudiant = numero_etudiant
        self._moyenne = moyenne
        self._cours: List[Cours] = []
        self._notes: List[float] = []
        self._observers: List[IObserver] = []
        # if no strategy is given, we use the standard one
        self._strategie_mention = strategie_mention or MentionStandard()

    @property
    def moyenne(self) -> float:
        return self._moyenne

    @property
    def cours(self) -> List[Cours]:
        return self._cours

    def ajouter_cours(self, cours: Cours) -> None:
        self._cours.append(cours)

    # Strategy pattern - we can change the mention calculation at runtime
    def set_strategie_mention(self, strategie: ICalculMention) -> None:
        self._strategie_mention = strategie

    def calculer_mention(self) -> str:
        return self._strategie_mention.calculer(self._moyenne)

    def ajouter_note(self, note: float) -> None:
        if note < 0 or note > 20:
            raise ValueError("La note doit être comprise entre 0 et 20.")
        self._notes.append(note)
        self._moyenne = sum(self._notes) / len(self._notes)
        # notify all observers that a new grade was added
        self.notifier("note_ajoutee")

    def afficher(self) -> str:
        noms_cours = (
            ", ".join(c.nom_cours for c in self._cours)
            if self._cours
            else "Aucun cours"
        )
        return (
            f"Etudiant(nom={self.nom}, age={self.age}, num={self.numero_etudiant}, "
            f"moyenne={self.moyenne:.2f}, mention={self.calculer_mention()}, "
            f"cours=[{noms_cours}])"
        )

    # Observer pattern methods
    def attacher(self, observer: IObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detacher(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notifier(self, evenement: str) -> None:
        for obs in self._observers:
            obs.update(self, evenement)
