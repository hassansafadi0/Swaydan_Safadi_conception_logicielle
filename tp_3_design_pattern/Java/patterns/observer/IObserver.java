package patterns.observer;

import modeles.Etudiant;

// Observer pattern - any object that wants to get notifications
public interface IObserver {
    void update(Etudiant etudiant, String evenement);
}
