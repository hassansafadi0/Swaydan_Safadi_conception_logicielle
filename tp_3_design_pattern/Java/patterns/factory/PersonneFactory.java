package patterns.factory;

import modeles.Personne;
import modeles.Etudiant;
import modeles.Professeur;
import patterns.strategy.ICalculMention;
import patterns.strategy.MentionStandard;

// Factory Method pattern - creates students or professors
// the client just tells us what type it wants, we handle the rest
public class PersonneFactory {

    public static Personne creerPersonne(String typePersonne, String nom, int age,
                                         String numeroEtudiant, Double moyenne,
                                         ICalculMention strategieMention,
                                         String specialite) {

        if (typePersonne.equalsIgnoreCase("etudiant")) {
            return new Etudiant(
                    nom,
                    age,
                    numeroEtudiant,
                    moyenne != null ? moyenne : 0.0,
                    strategieMention != null ? strategieMention : new MentionStandard()
            );

        } else if (typePersonne.equalsIgnoreCase("professeur")) {
            return new Professeur(nom, age, specialite);
        }

        throw new IllegalArgumentException("Type de personne inconnu : " + typePersonne);
    }
}
