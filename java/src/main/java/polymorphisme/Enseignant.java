package polymorphisme;

public class Enseignant extends Personne {
    private String matiere;
    private double salaire;

    public Enseignant(String nom, int age, String matiere, double salaire) {
        super(nom, age);
        setMatiere(matiere);
        setSalaire(salaire);
    }

    public String getMatiere() {
        return matiere;
    }

    public void setMatiere(String matiere) {
        if (matiere == null || matiere.trim().isEmpty()) {
            throw new IllegalArgumentException("La matière ne peut pas être vide.");
        }
        this.matiere = matiere.trim();
    }

    public double getSalaire() {
        return salaire;
    }

    public void setSalaire(double salaire) {
        if (salaire < 0) {
            throw new IllegalArgumentException("Le salaire ne peut pas être négatif.");
        }
        this.salaire = salaire;
    }

    @Override
    public String afficherDetails() {
        return "Enseignant: " + getNom()
                + ", " + getAge() + " ans"
                + ", Matière: " + matiere
                + ", Salaire: " + salaire;
    }

    @Override
    public String toString() {
        return afficherDetails();
    }
}