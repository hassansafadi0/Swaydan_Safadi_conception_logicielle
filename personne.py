class personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def afficher_info(self):
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Âge: {self.age}")