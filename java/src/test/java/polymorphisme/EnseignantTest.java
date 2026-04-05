package polymorphisme;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class EnseignantTest {

    @Test
    void testEnseignantEstUnePersonne() {
        Enseignant ens = new Enseignant("Karim", 45, "IA", 3500.0);
        assertTrue(ens instanceof Personne);
    }

    @Test
    void testAfficherDetailsEnseignant() {
        Enseignant ens = new Enseignant("Karim", 45, "IA", 3500.0);
        String resultat = ens.afficherDetails();

        assertTrue(resultat.contains("Karim"));
        assertTrue(resultat.contains("IA"));
        assertTrue(resultat.contains("Salaire"));
    }
}