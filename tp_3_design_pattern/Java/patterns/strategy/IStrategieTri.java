package patterns.strategy;

import java.util.List;
import modeles.Etudiant;

// Strategy pattern - interface for sorting students
public interface IStrategieTri {
    List<Etudiant> trier(List<Etudiant> etudiants);
}
