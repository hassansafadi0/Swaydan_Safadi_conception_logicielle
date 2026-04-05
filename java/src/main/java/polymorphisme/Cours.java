package polymorphisme;

public class Cours {
    private String nomCours;
    private String professeurResponsable;

    public Cours(String nomCours, String professeurResponsable) {
        this.nomCours = nomCours;
        this.professeurResponsable = professeurResponsable;
    }

    public String getNomCours() {
        return nomCours;
    }

    public String getProfesseurResponsable() {
        return professeurResponsable;
    }

    @Override
    public String toString() {
        return "Cours: " + nomCours + " - Prof: " + professeurResponsable;
    }
}