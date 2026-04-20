# singleton.py - Singleton pattern
# ScolariteManager holds the global list of all students
# there can only be one instance of it in the whole app
# it also implements IObserver so it gets notified when grades are added

from __future__ import annotations

import threading
from typing import List, TYPE_CHECKING

from patterns.observer import IObserver

if TYPE_CHECKING:
    from modeles.etudiant import Etudiant


class ScolariteManager(IObserver):
    """The main manager for all students. Only one instance can exist (Singleton)."""

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # check again after locking to be safe with threads
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._etudiants: List[Etudiant] = []
        return cls._instance

    def ajouter_etudiant(self, etudiant: "Etudiant") -> None:
        """Adds a student and automatically subscribes to their notifications."""
        self._etudiants.append(etudiant)
        etudiant.attacher(self)

    def lister_etudiants(self) -> List["Etudiant"]:
        return self._etudiants

    def moyenne_generale(self) -> float:
        """Calculates the overall average of all students."""
        if not self._etudiants:
            return 0.0
        return sum(e.moyenne for e in self._etudiants) / len(self._etudiants)

    # this method is called automatically when a student gets a new grade
    def update(self, etudiant: "Etudiant", evenement: str) -> None:
        print(f"[ScolariteManager] Notification reçue : {evenement} pour {etudiant.nom}")
        print(f"[ScolariteManager] Nouvelle moyenne de {etudiant.nom} = {etudiant.moyenne:.2f}")
        print(f"[ScolariteManager] Moyenne générale actuelle = {self.moyenne_generale():.2f}")
