 # ChakibBot GPT – Agent éducatif intelligent 🤖📘

Ce projet est un agent conversationnel éducatif capable de répondre à des questions de culture générale à partir d’un fichier local (`questions.json`) et, si besoin, de compléter avec GPT-3.5.

## 👨‍💻 Auteurs

- Chakib Rahmani  
- Medjkoune Belkacem  
- Mameri Massinissa  

Projet réalisé en collaboration dans le cadre du cours de Programmation 2 – Collège Boréal.

---

## 👥 Répartition des tâches

- **Chakib Rahmani** : Création de l’architecture du projet, codage principal de l’agent, intégration de l’interface Flask et tests.
- **Medjkoune Belkacem** : Préparation du fichier `questions.json`, aide à la documentation (`README.md`), validation des réponses locales.
- **Mameri Massinissa** : Tests fonctionnels, retours sur l’ergonomie de l’interface, vérification du bon fonctionnement avec GPT-3.5.

Travail réalisé en collaboration via GitHub.

## 📁 Structure du Projet

ChakibBot_GPT_REBUILT/
├── 📄 README.md # Documentation du projet
├── 📄 requirements.txt # Librairies nécessaires
├── 📄 .gitignore # Fichiers à ignorer par Git
├── 📄 main.py # Point d’entrée principal
├── 📄 app.py # Interface web Flask
├── 📄 config.py # Paramètres globaux
│
├── 📁 data/ # Données
│ └── 📄 questions.json # Questions de culture générale
│
├── 📁 templates/ # Pages HTML pour Flask
│ ├── 📄 index.html # Page d'accueil
│ └── 📄 chat.html # Interface de chat
│
├── 📄 agent_gpt.py # Classe de l’agent IA (GPT-3.5)
├── 📄 memory.py # Mémoire locale des échanges
├── 📄 data_manager.py # Gestion du fichier JSON
├── 📄 database.py # Structure pour future base de données
├── 📄 api.py # API Flask (optionnelle)
└── 📄 entities.py # Objets du système (ancien test)