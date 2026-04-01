package heritage;

public class Main {
    public static void main(String[] args) {

        Cours c1 = new Cours("Math", "Dr Martin");
        Cours c2 = new Cours("Algo", "Mme Dupont");

        Etudiant e = new Etudiant("Alice", 21, "E01", 15.5);

        e.ajouterCours(c1);
        e.ajouterCours(c2);

        System.out.println(e);

        for (Cours c : e.getListeCours()) {
            System.out.println(c);
        }
    }
}