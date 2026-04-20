import java.util.List;

import modeles.Etudiant;
import modeles.Professeur;
import modeles.Cours;

import patterns.singleton.ScolariteManager;
import patterns.factory.PersonneFactory;
import patterns.strategy.*;
import patterns.decorator.*;
import patterns.adapter.LegacyCoursSystem;
import patterns.adapter.CoursAdapter;

// main demo - shows all 6 design patterns working together
public class Main {

    public static void main(String[] args) {
        System.out.println("\n===== DEMO TP : SYSTEME DE GESTION ACADEMIQUE MULTI-PATTERNS =====\n");

        // 1. Singleton - only one instance of ScolariteManager
        ScolariteManager manager1 = ScolariteManager.getInstance();
        ScolariteManager manager2 = ScolariteManager.getInstance();
        System.out.println("Singleton ScolariteManager : " + (manager1 == manager2));

        // 2. Factory Method - create students and professors through the factory
        Etudiant etu1 = (Etudiant) PersonneFactory.creerPersonne(
                "etudiant", "Alice", 21,
                "E2026001", 0.0, new MentionStandard(), null
        );

        Etudiant etu2 = (Etudiant) PersonneFactory.creerPersonne(
                "etudiant", "Karim", 22,
                "E2026002", 0.0, new MentionSevere(), null
        );

        Professeur prof1 = (Professeur) PersonneFactory.creerPersonne(
                "professeur", "Dr Martin", 45,
                null, null, null, "Mathématiques"
        );

        System.out.println(prof1.afficher());

        // 4. Adapter - convert legacy string data into Cours objects
        LegacyCoursSystem legacy = new LegacyCoursSystem();
        CoursAdapter adapter = new CoursAdapter(legacy);

        Cours cours1 = adapter.convertirEnCours("Analyse;Dr Martin");
        Cours cours2 = adapter.convertirEnCours("Programmation Python;Mme Dupont");

        etu1.ajouterCours(cours1);
        etu1.ajouterCours(cours2);
        etu2.ajouterCours(cours2);

        // 6. Observer - the manager subscribes when we add the students
        // after this, every new grade triggers a notification
        manager1.ajouterEtudiant(etu1);
        manager1.ajouterEtudiant(etu2);

        System.out.println("\n--- Ajout des notes ---");
        etu1.ajouterNote(15);
        etu1.ajouterNote(17);
        etu2.ajouterNote(12);
        etu2.ajouterNote(14);

        // 5. Strategy - change the mention calculation at runtime
        System.out.println("\n--- Strategy : calcul de mention ---");
        System.out.println(etu1.getNom() + " -> mention = " + etu1.calculerMention());

        // switch Alice to the strict grading strategy
        etu1.setStrategieMention(new MentionSevere());
        System.out.println(etu1.getNom()
                + " après changement de stratégie -> mention = "
                + etu1.calculerMention());

        // 3. Decorator - add extra roles without modifying the Etudiant class
        System.out.println("\n--- Decorator : enrichissement dynamique ---");

        // Alice is both a scholarship student and a class delegate
        IEtudiantComponent etu1Decore = new EtudiantDelegueDecorator(
                new EtudiantBoursierDecorator(etu1, 250.0)
        );
        System.out.println(etu1Decore.afficher());

        // Karim is just a delegate
        IEtudiantComponent etu2Decore = new EtudiantDelegueDecorator(etu2);
        System.out.println(etu2Decore.afficher());

        // final display
        System.out.println("\n--- Liste des étudiants ---");
        for (Etudiant e : manager1.listerEtudiants()) {
            System.out.println(e.afficher());
        }

        System.out.println("\nMoyenne générale de la scolarité = "
                + String.format("%.2f", manager1.moyenneGenerale()));

        // sorting strategies
        System.out.println("\n--- Strategy : tri des étudiants ---");

        List<Etudiant> triesMoyenne = new TriParMoyenne().trier(manager1.listerEtudiants());
        System.out.println("Triés par moyenne (descendant) :");
        for (Etudiant e : triesMoyenne) {
            System.out.println("  " + e.getNom() + ": " + String.format("%.2f", e.getMoyenne()));
        }

        List<Etudiant> triesNom = new TriParNom().trier(manager1.listerEtudiants());
        System.out.println("Triés par nom (alphabétique) :");
        for (Etudiant e : triesNom) {
            System.out.println("  " + e.getNom());
        }
    }
}
