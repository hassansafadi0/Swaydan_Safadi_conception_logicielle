from src.etudiant import Etudiant
from src.cours import Cours

def test_afficher_details_etudiant():
    e = Etudiant("Alice", 21, "E01", 14.5)
    e.ajouter_cours(Cours("Math", "Prof"))

    result = e.afficher_details()

    assert "Alice" in result
    assert "Moyenne" in result