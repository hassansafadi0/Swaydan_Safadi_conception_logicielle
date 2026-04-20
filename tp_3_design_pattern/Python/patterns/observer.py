# observer.py - Observer pattern
# when a grade is added to a student, the ScolariteManager gets notified

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modeles.etudiant import Etudiant


class IObserver(ABC):
    """Any object that wants to receive notifications."""

    @abstractmethod
    def update(self, etudiant: "Etudiant", evenement: str) -> None:
        pass


class ISubject(ABC):
    """Any object that can send notifications to observers."""

    @abstractmethod
    def attacher(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def detacher(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notifier(self, evenement: str) -> None:
        pass
