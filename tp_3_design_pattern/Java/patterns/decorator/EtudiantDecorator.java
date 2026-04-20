package patterns.decorator;

// base decorator - just passes the call to the wrapped component
public abstract class EtudiantDecorator implements IEtudiantComponent {

    protected IEtudiantComponent etudiantComponent;

    public EtudiantDecorator(IEtudiantComponent etudiantComponent) {
        this.etudiantComponent = etudiantComponent;
    }

    @Override
    public String afficher() {
        return etudiantComponent.afficher();
    }
}
