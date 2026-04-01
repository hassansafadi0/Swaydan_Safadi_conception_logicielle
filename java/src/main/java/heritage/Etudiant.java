package heritage;

import java.util.ArrayList;
import java.util.List;

public class Etudiant extends Personne {
    private String numeroEtudiant;
    private double moyenne;
    private List<Cours> listeCours;

    public Etudiant(String nom, int age, String numeroEtudiant, double moyenne) {
        super(nom, age); // obligatoire
        this.numeroEtudiant = numeroEtudiant;
        this.moyenne = moyenne;
        this.listeCours = new ArrayList<>();
    }

    public void ajouterCours(Cours c) {
        listeCours.add(c);
    }

    public List<Cours> getListeCours() {
        return listeCours;
    }

    @Override
    public String toString() {
        return super.toString() +
                " | ID: " + numeroEtudiant +
                " | Moyenne: " + moyenne;
    }
}