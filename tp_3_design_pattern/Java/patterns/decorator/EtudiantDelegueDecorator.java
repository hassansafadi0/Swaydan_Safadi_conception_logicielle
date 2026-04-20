package patterns.decorator;

// adds class delegate status to the student display
public class EtudiantDelegueDecorator extends EtudiantDecorator {

    public EtudiantDelegueDecorator(IEtudiantComponent etudiantComponent) {
        super(etudiantComponent);
    }

    @Override
    public String afficher() {
        return super.afficher() + " | Statut: Délégué de classe";
    }
}
