package encapsulation;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Etudiant extends Personne {
    private final String numeroEtudiant;
    private double moyenne;
    private final List<Cours> listeCours;

    public Etudiant(String nom, int age, String numeroEtudiant, double moyenne) {
        super(nom, age);
        this.numeroEtudiant = numeroEtudiant;
        this.listeCours = new ArrayList<>();
        setMoyenne(moyenne);
    }

    public String getNumeroEtudiant() {
        return numeroEtudiant;
    }

    public double getMoyenne() {
        return moyenne;
    }

    public void setMoyenne(double moyenne) {
        if (moyenne < 0 || moyenne > 20) {
            throw new IllegalArgumentException("La moyenne doit être comprise entre 0 et 20.");
        }
        this.moyenne = moyenne;
    }

    public List<Cours> getListeCours() {
        return Collections.unmodifiableList(listeCours);
    }

    public void ajouterCours(Cours cours) {
        listeCours.add(cours);
    }

    @Override
    public String toString() {
        StringBuilder coursStr = new StringBuilder();
        if (listeCours.isEmpty()) {
            coursStr.append("Aucun");
        } else {
            for (int i = 0; i < listeCours.size(); i++) {
                coursStr.append(listeCours.get(i).getNomCours());
                if (i < listeCours.size() - 1) {
                    coursStr.append(", ");
                }
            }
        }

        return super.toString()
                + " | ID: " + numeroEtudiant
                + " | Moyenne: " + moyenne
                + " | Cours: " + coursStr;
    }
}