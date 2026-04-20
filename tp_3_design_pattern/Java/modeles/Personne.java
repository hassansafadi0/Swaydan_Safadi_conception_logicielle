package modeles;

// abstract class for any person in the system
public abstract class Personne {

    protected String nom;
    protected int age;

    public Personne(String nom, int age) {
        this.nom = nom;
        this.age = age;
    }

    public String getNom() {
        return nom;
    }

    public int getAge() {
        return age;
    }

    // each subclass will have its own way to display info
    public abstract String afficher();
}
