from src.personne import Personne

def test_afficher_details_personne():
    p = Personne("Ali", 20)
    result = p.afficher_details()

    assert "Ali" in result
    assert "20" in result