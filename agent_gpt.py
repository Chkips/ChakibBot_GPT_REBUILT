from memory import Memory
from openai import OpenAI

# ✅ Clé API fournie par Chakib
import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Agent:
    def __init__(self, name="ChakibBot"):
        self.name = name
        self.memory = Memory()

    def respond(self, message: str) -> str:
        if not message.strip():
            return "Tu peux reformuler ? Je n’ai pas compris 😅"

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tu es un assistant amical nommé ChakibBot."},
                    {"role": "user", "content": message}
                ]
            )
            self.memory.add(message)
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Désolé, une erreur s’est produite avec GPT : {e}"
