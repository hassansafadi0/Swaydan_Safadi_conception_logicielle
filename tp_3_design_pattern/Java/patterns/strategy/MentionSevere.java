package patterns.strategy;

// strict grading scale - thresholds are 1 point higher
public class MentionSevere implements ICalculMention {

    @Override
    public String calculer(double moyenne) {
        if (moyenne >= 17) return "Très Bien";
        else if (moyenne >= 15) return "Bien";
        else if (moyenne >= 13) return "Assez Bien";
        else if (moyenne >= 10) return "Passable";
        return "Ajourné";
    }
}
