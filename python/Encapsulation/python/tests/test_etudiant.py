import pytest
from src.etudiant import Etudiant
from src.personne import Personne
from src.cours import Cours


def test_heritage():
    e = Etudiant("Alice", 21, "E01", 14.5)
    assert isinstance(e, Personne)


def test_moyenne_invalide():
    with pytest.raises(ValueError):
        Etudiant("Alice", 21, "E01", 25)


def test_setter_moyenne_invalide():
    e = Etudiant("Alice", 21, "E01", 14.5)
    with pytest.raises(ValueError):
        e.moyenne = -2


def test_ajout_cours():
    e = Etudiant("Alice", 21, "E01", 14.5)
    c = Cours("Math", "Prof")
    e.ajouter_cours(c)
    assert len(e.liste_cours) == 1


def test_numero_etudiant_lecture_seule():
    e = Etudiant("Alice", 21, "E01", 14.5)
    with pytest.raises(AttributeError):
        e.numero_etudiant = "E99"


def test_liste_cours_non_modifiable_directement():
    e = Etudiant("Alice", 21, "E01", 14.5)
    with pytest.raises(AttributeError):
        e.liste_cours.append(Cours("Math", "Prof"))


def test_str_etudiant():
    e = Etudiant("Alice", 21, "E01", 14.5)
    e.ajouter_cours(Cours("Math", "Prof"))
    resultat = str(e)
    assert "Alice" in resultat
    assert "Math" in resultat