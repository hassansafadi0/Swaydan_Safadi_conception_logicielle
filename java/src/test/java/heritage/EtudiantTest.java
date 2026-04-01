package heritage;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class EtudiantTest {

    @Test
    void testHeritage() {
        Etudiant e = new Etudiant("Alice", 21, "E01", 14.5);

        assertTrue(e instanceof Personne);
    }

    @Test
    void testAjoutCours() {
        Etudiant e = new Etudiant("Alice", 21, "E01", 14.5);
        Cours c = new Cours("Math", "Prof");

        e.ajouterCours(c);

        assertEquals(1, e.getListeCours().size());
    }
}