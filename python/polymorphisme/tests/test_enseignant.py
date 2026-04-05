from src.enseignant import Enseignant

def test_afficher_details_enseignant():
    e = Enseignant("Karim", 40, "IA", 3000)

    result = e.afficher_details()

    assert "Karim" in result
    assert "Salaire" in result