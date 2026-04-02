from src.personne import Personne


def test_creation_personne():
    p = Personne("Ali", 20)

    assert p.nom == "Ali"
    assert p.age == 20


def test_str_personne():
    p = Personne("Ali", 20)
    assert "Ali" in str(p)