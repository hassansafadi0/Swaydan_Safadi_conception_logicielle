package polymorphisme;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class EtudiantTest {

    @Test
    void testEtudiantEstUnePersonne() {
        Etudiant e = new Etudiant("Alice", 21, "E01", 14.5);
        assertTrue(e instanceof Personne);
    }

    @Test
    void testAfficherDetailsEtudiant() {
        Etudiant e = new Etudiant("Alice", 21, "E01", 14.5);
        e.ajouterCours(new Cours("Math", "Prof"));

        String resultat = e.afficherDetails();

        assertTrue(resultat.contains("Alice"));
        assertTrue(resultat.contains("Moyenne"));
        assertTrue(resultat.contains("Math"));
    }
}