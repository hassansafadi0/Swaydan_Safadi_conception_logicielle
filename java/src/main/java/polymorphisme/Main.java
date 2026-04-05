package polymorphisme;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Etudiant e = new Etudiant("Alice", 21, "E001", 15.5);
        e.ajouterCours(new Cours("Math", "Dr Martin"));
        e.ajouterCours(new Cours("Algo", "Mme Dupont"));

        Enseignant ens = new Enseignant("Karim", 45, "Programmation", 3500.0);

        List<Personne> personnes = new ArrayList<>();
        personnes.add(e);
        personnes.add(ens);

        System.out.println("=== Polymorphisme ===");
        for (Personne p : personnes) {
            System.out.println(p.afficherDetails());
        }
    }
}