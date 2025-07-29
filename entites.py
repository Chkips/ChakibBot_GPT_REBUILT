class Question:
    def __init__(self, id, question, reponse):
        self.id = id
        self.question = question
        self.reponse = reponse

    def afficher(self):
        return f"Q: {self.question} → R: {self.reponse}"

class Utilisateur:
    def __init__(self, nom):
        self.nom = nom
        self.historique = []

    def ajouter_message(self, message):
        self.historique.append(message)

    def afficher_historique(self):
        return self.historique

class Session:
    def __init__(self, utilisateur):
        self.utilisateur = utilisateur
        self.questions_posees = []

    def enregistrer_question(self, question):
        self.questions_posees.append(question)

    def nb_questions_posees(self):
        return len(self.questions_posees)