package encapsulation;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PersonneTest {

    @Test
    void testCreationPersonne() {
        Personne p = new Personne("Ali", 20);

        assertEquals("Ali", p.getNom());
        assertEquals(20, p.getAge());
    }

    @Test
    void testNomVideInterdit() {
        assertThrows(IllegalArgumentException.class, () -> new Personne("", 20));
    }

    @Test
    void testAgeNegatifInterdit() {
        assertThrows(IllegalArgumentException.class, () -> new Personne("Ali", -1));
    }

    @Test
    void testAgeSuperieurA100Interdit() {
        assertThrows(IllegalArgumentException.class, () -> new Personne("Ali", 101));
    }
}