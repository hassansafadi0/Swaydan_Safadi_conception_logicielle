package patterns.strategy;

import java.util.ArrayList;
import java.util.List;
import modeles.Etudiant;

// sorts students by name (A to Z)
public class TriParNom implements IStrategieTri {

    @Override
    public List<Etudiant> trier(List<Etudiant> etudiants) {
        List<Etudiant> copie = new ArrayList<>(etudiants);
        copie.sort((e1, e2) -> e1.getNom().compareTo(e2.getNom()));
        return copie;
    }
}
