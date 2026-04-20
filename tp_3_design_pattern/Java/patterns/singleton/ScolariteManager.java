package patterns.singleton;

import java.util.ArrayList;
import java.util.List;

import modeles.Etudiant;
import patterns.observer.IObserver;

// Singleton pattern - only one instance of this class can exist
// it manages all students and gets notified when grades are added
public class ScolariteManager implements IObserver {

    private static ScolariteManager instance;
    private List<Etudiant> etudiants;

    // private constructor so nobody can create new instances
    private ScolariteManager() {
        etudiants = new ArrayList<>();
    }

    // returns the single instance, creates it if it doesn't exist yet
    public static synchronized ScolariteManager getInstance() {
        if (instance == null) {
            instance = new ScolariteManager();
        }
        return instance;
    }

    // adds a student and subscribes to their notifications automatically
    public void ajouterEtudiant(Etudiant etudiant) {
        etudiants.add(etudiant);
        etudiant.attacher(this);
    }

    public List<Etudiant> listerEtudiants() {
        return etudiants;
    }

    // calculates the overall average of all students
    public double moyenneGenerale() {
        if (etudiants.isEmpty()) return 0.0;

        double somme = 0;
        for (Etudiant e : etudiants) {
            somme += e.getMoyenne();
        }
        return somme / etudiants.size();
    }

    // called automatically when a student gets a new grade
    @Override
    public void update(Etudiant etudiant, String evenement) {
        System.out.println("[ScolariteManager] Notification reçue : "
                + evenement + " pour " + etudiant.getNom());
        System.out.println("[ScolariteManager] Nouvelle moyenne de "
                + etudiant.getNom() + " = "
                + String.format("%.2f", etudiant.getMoyenne()));
        System.out.println("[ScolariteManager] Moyenne générale actuelle = "
                + String.format("%.2f", moyenneGenerale()));
    }
}
