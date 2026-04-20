package patterns.strategy;

import java.util.ArrayList;
import java.util.List;
import modeles.Etudiant;

// sorts students by average (highest first)
public class TriParMoyenne implements IStrategieTri {

    @Override
    public List<Etudiant> trier(List<Etudiant> etudiants) {
        List<Etudiant> copie = new ArrayList<>(etudiants);
        copie.sort((e1, e2) -> Double.compare(e2.getMoyenne(), e1.getMoyenne()));
        return copie;
    }
}
