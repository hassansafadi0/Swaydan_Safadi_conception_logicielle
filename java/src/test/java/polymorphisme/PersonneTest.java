package polymorphisme;

import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class PersonneTest {

    @Test
    void testAfficherDetailsPersonne() {
        Personne p = new Personne("Ali", 20);
        String resultat = p.afficherDetails();
        assertTrue(resultat.contains("Ali"));
        assertTrue(resultat.contains("20"));
    }

    @Test
    void testPolymorphismeDansListe() {
        Etudiant e = new Etudiant("Alice", 21, "E01", 14.5);
        Enseignant ens = new Enseignant("Karim", 45, "IA", 3500.0);

        List<Personne> personnes = new ArrayList<>();
        personnes.add(e);
        personnes.add(ens);

        assertTrue(personnes.get(0).afficherDetails().contains("Moyenne"));
        assertTrue(personnes.get(1).afficherDetails().contains("Salaire"));
    }
}