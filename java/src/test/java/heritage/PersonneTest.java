package heritage;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PersonneTest {

    @Test
    void testCreation() {
        Personne p = new Personne("Ali", 20);

        assertEquals("Ali", p.getNom());
    }
}