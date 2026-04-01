package heritage;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CoursTest {

    @Test
    void testCreation() {
        Cours c = new Cours("POO", "Prof");

        assertEquals("POO", c.getNomCours());
    }
}