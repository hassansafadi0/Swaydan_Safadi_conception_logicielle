package modeles;

import java.util.ArrayList;
import java.util.List;

import patterns.observer.IObserver;
import patterns.observer.ISubject;
import patterns.strategy.ICalculMention;
import patterns.strategy.MentionStandard;
import patterns.decorator.IEtudiantComponent;

// the student class - inherits from Personne
// implements ISubject (Observer pattern) so it can notify when grades are added
// implements IEtudiantComponent (Decorator pattern) so it can be decorated
public class Etudiant extends Personne implements ISubject, IEtudiantComponent {

    private String numeroEtudiant;
    private double moyenne;
    private List<Cours> cours;
    private List<Double> notes;
    private List<IObserver> observers;
    private ICalculMention strategieMention;

    public Etudiant(String nom, int age, String numeroEtudiant,
                    double moyenne, ICalculMention strategieMention) {
        super(nom, age);
        this.numeroEtudiant = numeroEtudiant;
        this.moyenne = moyenne;
        this.strategieMention = (strategieMention != null)
                ? strategieMention
                : new MentionStandard();
        this.cours = new ArrayList<>();
        this.notes = new ArrayList<>();
        this.observers = new ArrayList<>();
    }

    public String getNumeroEtudiant() {
        return numeroEtudiant;
    }

    public double getMoyenne() {
        return moyenne;
    }

    public List<Cours> getCours() {
        return cours;
    }

    public void ajouterCours(Cours cours) {
        this.cours.add(cours);
    }

    // Strategy pattern - change the mention calculation at runtime
    public void setStrategieMention(ICalculMention strategieMention) {
        this.strategieMention = strategieMention;
    }

    public String calculerMention() {
        return strategieMention.calculer(moyenne);
    }

    // when a grade is added, we recalculate the average and notify observers
    public void ajouterNote(double note) {
        if (note < 0 || note > 20) {
            throw new IllegalArgumentException(
                    "La note doit être comprise entre 0 et 20.");
        }
        notes.add(note);

        double somme = 0;
        for (double n : notes) {
            somme += n;
        }
        moyenne = somme / notes.size();

        notifier("note_ajoutee");
    }

    @Override
    public String afficher() {
        StringBuilder nomsCours = new StringBuilder();
        if (cours.isEmpty()) {
            nomsCours.append("Aucun cours");
        } else {
            for (int i = 0; i < cours.size(); i++) {
                nomsCours.append(cours.get(i).getNomCours());
                if (i < cours.size() - 1) {
                    nomsCours.append(", ");
                }
            }
        }

        return "Etudiant(nom=" + nom
                + ", age=" + age
                + ", num=" + numeroEtudiant
                + ", moyenne=" + String.format("%.2f", moyenne)
                + ", mention=" + calculerMention()
                + ", cours=[" + nomsCours + "])";
    }

    // Observer pattern methods
    @Override
    public void attacher(IObserver observer) {
        if (!observers.contains(observer)) {
            observers.add(observer);
        }
    }

    @Override
    public void detacher(IObserver observer) {
        observers.remove(observer);
    }

    @Override
    public void notifier(String evenement) {
        for (IObserver obs : observers) {
            obs.update(this, evenement);
        }
    }
}
