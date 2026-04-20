# factory.py - Factory Method pattern
# PersonneFactory creates students or professors for us
# so the client code doesn't need to know how to build them

from modeles.personne import Personne, Professeur
from modeles.etudiant import Etudiant
from patterns.strategy import ICalculMention, MentionStandard


class PersonneFactory:
    """Creates Etudiant or Professeur objects based on the type you give it."""

    @staticmethod
    def creer_personne(type_personne: str, **kwargs) -> Personne:
        """
        Creates a person of the given type.
        Use "etudiant" for students, "professeur" for professors.
        """
        type_personne = type_personne.lower()

        if type_personne == "etudiant":
            return Etudiant(
                nom=kwargs["nom"],
                age=kwargs["age"],
                numero_etudiant=kwargs["numero_etudiant"],
                moyenne=kwargs.get("moyenne", 0.0),
                strategie_mention=kwargs.get("strategie_mention", MentionStandard()),
            )

        elif type_personne == "professeur":
            return Professeur(
                nom=kwargs["nom"],
                age=kwargs["age"],
                specialite=kwargs["specialite"],
            )

        raise ValueError(f"Type de personne inconnu : {type_personne}")
