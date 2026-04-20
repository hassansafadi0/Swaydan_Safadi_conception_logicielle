# adapter.py - Adapter pattern
# the old system gives us course data as a simple string like "Math;Dr Martin"
# the adapter converts that string into a proper Cours object

from modeles.cours import Cours


class LegacyCoursSystem:
    """Simulates an old system that returns course data as a raw string."""

    def lire_cours(self, raw_data: str) -> str:
        return raw_data


class CoursAdapter:
    """Converts the legacy string format into a proper Cours object."""

    def __init__(self, legacy_system: LegacyCoursSystem):
        self._legacy_system = legacy_system

    def convertir_en_cours(self, raw_data: str) -> Cours:
        """Takes a string like 'CoursName;Professor' and returns a Cours object."""
        donnees = self._legacy_system.lire_cours(raw_data)
        morceaux = donnees.split(";")

        if len(morceaux) != 2:
            raise ValueError(
                "Format legacy invalide. Format attendu : 'NomCours;Professeur'"
            )

        nom_cours = morceaux[0].strip()
        professeur = morceaux[1].strip()
        return Cours(nom_cours, professeur)
