from src.etudiant import Etudiant
from src.personne import Personne
from src.cours import Cours


def test_heritage():
    e = Etudiant("Alice", 21, "E01", 14.5)

    assert isinstance(e, Personne)


def test_liste_cours_vide():
    e = Etudiant("Alice", 21, "E01", 14.5)
    assert e.liste_cours == []


def test_ajout_cours():
    e = Etudiant("Alice", 21, "E01", 14.5)
    c = Cours("Math", "Prof")

    e.ajouter_cours(c)

    assert len(e.liste_cours) == 1


def test_str_etudiant():
    e = Etudiant("Alice", 21, "E01", 14.5)
    e.ajouter_cours(Cours("Math", "Prof"))

    result = str(e)

    assert "Alice" in result
    assert "Math" in result