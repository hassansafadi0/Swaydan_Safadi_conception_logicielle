# main.py - demo that shows all 6 design patterns working together

from modeles.etudiant import Etudiant
from patterns.singleton import ScolariteManager
from patterns.factory import PersonneFactory
from patterns.strategy import MentionStandard, MentionSevere, TriParMoyenne, TriParNom
from patterns.decorator import EtudiantBoursierDecorator, EtudiantDelegueDecorator
from patterns.adapter import LegacyCoursSystem, CoursAdapter


def main():
    print("\n===== DEMO TP : SYSTEME DE GESTION ACADEMIQUE MULTI-PATTERNS =====\n")

    # 1. Singleton - only one instance of ScolariteManager
    manager1 = ScolariteManager()
    manager2 = ScolariteManager()
    print(f"Singleton ScolariteManager : {manager1 is manager2}")  # True

    # 2. Factory Method - create students and professors through the factory
    etu1 = PersonneFactory.creer_personne(
        "etudiant",
        nom="Alice",
        age=21,
        numero_etudiant="E2026001",
        strategie_mention=MentionStandard(),
    )

    etu2 = PersonneFactory.creer_personne(
        "etudiant",
        nom="Karim",
        age=22,
        numero_etudiant="E2026002",
        strategie_mention=MentionSevere(),
    )

    prof1 = PersonneFactory.creer_personne(
        "professeur",
        nom="Dr Martin",
        age=45,
        specialite="Mathématiques",
    )

    print(prof1.afficher())

    # 4. Adapter - convert legacy string data into Cours objects
    legacy = LegacyCoursSystem()
    adapter = CoursAdapter(legacy)

    cours1 = adapter.convertir_en_cours("Analyse;Dr Martin")
    cours2 = adapter.convertir_en_cours("Programmation Python;Mme Dupont")

    etu1.ajouter_cours(cours1)
    etu1.ajouter_cours(cours2)
    etu2.ajouter_cours(cours2)

    # 6. Observer - the manager subscribes when we add the students
    # after this, every new grade will trigger a notification
    manager1.ajouter_etudiant(etu1)
    manager1.ajouter_etudiant(etu2)

    print("\n--- Ajout des notes ---")
    etu1.ajouter_note(15)
    etu1.ajouter_note(17)
    etu2.ajouter_note(12)
    etu2.ajouter_note(14)

    # 5. Strategy - change the mention calculation at runtime
    print("\n--- Strategy : calcul de mention ---")
    print(f"{etu1.nom} -> mention = {etu1.calculer_mention()}")

    # switch Alice to the strict grading strategy
    etu1.set_strategie_mention(MentionSevere())
    print(f"{etu1.nom} après changement de stratégie -> mention = {etu1.calculer_mention()}")

    # 3. Decorator - add extra roles without modifying the Etudiant class
    print("\n--- Decorator : enrichissement dynamique ---")

    # Alice is both a scholarship student and a class delegate
    etu1_decore = EtudiantDelegueDecorator(
        EtudiantBoursierDecorator(etu1, 250.0)
    )
    print(etu1_decore.afficher())

    # Karim is just a delegate
    etu2_decore = EtudiantDelegueDecorator(etu2)
    print(etu2_decore.afficher())

    # final display
    print("\n--- Liste des étudiants ---")
    for e in manager1.lister_etudiants():
        print(e.afficher())

    print(f"\nMoyenne générale de la scolarité = {manager1.moyenne_generale():.2f}")

    # sorting strategies
    print("\n--- Strategy : tri des étudiants ---")

    etudiants_tries = TriParMoyenne().trier(manager1.lister_etudiants())
    print("Triés par moyenne (descendant) :")
    for e in etudiants_tries:
        print(f"  {e.nom}: {e.moyenne:.2f}")

    etudiants_tries = TriParNom().trier(manager1.lister_etudiants())
    print("Triés par nom (alphabétique) :")
    for e in etudiants_tries:
        print(f"  {e.nom}")


if __name__ == "__main__":
    main()
