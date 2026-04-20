package patterns.adapter;

import modeles.Cours;

// Adapter pattern - converts string like "Math;Dr Martin" into a Cours object
public class CoursAdapter {

    private LegacyCoursSystem legacySystem;

    public CoursAdapter(LegacyCoursSystem legacySystem) {
        this.legacySystem = legacySystem;
    }

    public Cours convertirEnCours(String rawData) {
        String donnees = legacySystem.lireCours(rawData);
        String[] morceaux = donnees.split(";");

        if (morceaux.length != 2) {
            throw new IllegalArgumentException(
                    "Format legacy invalide. Format attendu : 'NomCours;Professeur'");
        }

        String nomCours = morceaux[0].trim();
        String professeur = morceaux[1].trim();

        return new Cours(nomCours, professeur);
    }
}
