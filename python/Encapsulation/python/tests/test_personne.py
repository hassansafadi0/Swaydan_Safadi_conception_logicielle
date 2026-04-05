import pytest
from src.personne import Personne


def test_creation_personne():
    p = Personne("Ali", 20)
    assert p.nom == "Ali"
    assert p.age == 20


def test_nom_vide_interdit():
    with pytest.raises(ValueError):
        Personne("", 20)


def test_age_negatif_interdit():
    with pytest.raises(ValueError):
        Personne("Ali", -1)


def test_age_superieur_a_100_interdit():
    with pytest.raises(ValueError):
        Personne("Ali", 101)


def test_modification_age_valide():
    p = Personne("Ali", 20)
    p.age = 35
    assert p.age == 35