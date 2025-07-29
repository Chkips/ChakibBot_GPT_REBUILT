 # main.py
from agent_gpt import Agent
from api import app

def run_console():
    agent = Agent()
    print(f"=== Bienvenue dans l’interface console de {agent.name} ===")
    nom = input("Quel est ton nom ? ")
    while True:
        msg = input(f"{nom} ➤ ")
        if msg.lower() in ["exit", "quitter"]:
            print("Au revoir !")
            break
        reponse = agent.respond(msg)
        print(f"{agent.name} ➤ {reponse}")

if __name__ == "__main__":
    print("Choisis le mode de lancement :")
    print("1. Console")
    print("2. API Flask")
    choix = input("Ton choix (1/2) : ")

    if choix == "1":
        run_console()
    elif choix == "2":
        print("Lancement de l’API Flask...")
        app.run(debug=True)
    else:
        print("Choix invalide.")
