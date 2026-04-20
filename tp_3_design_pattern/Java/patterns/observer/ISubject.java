package patterns.observer;

// Observer pattern - any object that can send notifications
public interface ISubject {
    void attacher(IObserver observer);
    void detacher(IObserver observer);
    void notifier(String evenement);
}
