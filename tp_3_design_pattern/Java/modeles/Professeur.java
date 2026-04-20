package modeles;

// a professor with a specialty, inherits from Personne
public class Professeur extends Personne {

    private String specialite;

    public Professeur(String nom, int age, String specialite) {
        super(nom, age);
        this.specialite = specialite;
    }

    public String getSpecialite() {
        return specialite;
    }

    @Override
    public String afficher() {
        return "Professeur(nom=" + nom + ", age=" + age
                + ", specialite=" + specialite + ")";
    }
}
