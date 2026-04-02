package encapsulation;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class CoursTest {

    @Test
    void testCreationCours() {
        Cours c = new Cours("POO", "Prof X");
        assertEquals("POO", c.getNomCours());
        assertEquals("Prof X", c.getProfesseurResponsable());
    }
}