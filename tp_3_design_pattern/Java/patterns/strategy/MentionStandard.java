package patterns.strategy;

// normal grading scale
public class MentionStandard implements ICalculMention {

    @Override
    public String calculer(double moyenne) {
        if (moyenne >= 16) return "Très Bien";
        else if (moyenne >= 14) return "Bien";
        else if (moyenne >= 12) return "Assez Bien";
        else if (moyenne >= 10) return "Passable";
        return "Ajourné";
    }
}
