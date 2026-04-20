package patterns.decorator;

// adds scholarship info to the student display
public class EtudiantBoursierDecorator extends EtudiantDecorator {

    private double montantBourse;

    public EtudiantBoursierDecorator(IEtudiantComponent etudiantComponent,
                                     double montantBourse) {
        super(etudiantComponent);
        this.montantBourse = montantBourse;
    }

    @Override
    public String afficher() {
        return super.afficher()
                + " | Statut: Boursier (" + montantBourse + " EUR)";
    }
}
