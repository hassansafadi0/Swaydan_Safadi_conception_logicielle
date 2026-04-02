package encapsulation;

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

    @Test
    void testMoyenneInvalide() {
        assertThrows(IllegalArgumentException.class,
                () -> new Etudiant("Alice", 21, "E01", 25));
    }

    @Test
    void testSetterMoyenneInvalide() {
        Etudiant e = new Etudiant("Alice", 21, "E01", 14.5);
        assertThrows(IllegalArgumentException.class, () -> e.setMoyenne(-3));
    }

    @Test
    void testNumeroLectureSeule() {
        Etudiant e = new Etudiant("Alice", 21, "E01", 14.5);
        assertEquals("E01", e.getNumeroEtudiant());
    }
}