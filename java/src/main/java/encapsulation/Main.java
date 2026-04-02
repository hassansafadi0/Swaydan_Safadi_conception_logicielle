package encapsulation;

public class Main {
    public static void main(String[] args) {
        Cours c1 = new Cours("Math", "Dr Martin");
        Cours c2 = new Cours("Algo", "Mme Dupont");

        Etudiant e = new Etudiant("Alice", 21, "E001", 15.5);
        e.ajouterCours(c1);
        e.ajouterCours(c2);

        System.out.println("=== Avant modification invalide ===");
        System.out.println(e);

        System.out.println("\n=== Test encapsulation ===");
        try {
            e.setMoyenne(25);
        } catch (IllegalArgumentException erreur) {
            System.out.println("Erreur capturée : " + erreur.getMessage());
        }

        System.out.println("\n=== Après tentative invalide ===");
        System.out.println(e);
    }
}