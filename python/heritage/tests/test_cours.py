from src.cours import Cours


def test_creation_cours():
    c = Cours("POO", "Prof X")

    assert c.nom_cours == "POO"
    assert c.professeur_responsable == "Prof X"


def test_str_cours():
    c = Cours("POO", "Prof X")
    assert "POO" in str(c)