from src.cours import Cours

def test_creation_cours():
    c = Cours("Math", "Prof")
    assert c.nom_cours == "Math"