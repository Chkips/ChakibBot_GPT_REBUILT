import streamlit as st
from agent_gpt import Agent

# Configuration de la page
st.set_page_config(page_title="ChakibBot GPT", page_icon="🤖")
st.title("🤖 ChakibBot GPT – Interface Streamlit")

# Initialisation de l’agent
agent = Agent()

# Entrée utilisateur
message = st.text_input("💬 Pose ta question ici :", "")

# Traitement du message
if st.button("Envoyer") and message.strip():
    with st.spinner("ChakibBot réfléchit..."):
        reponse = agent.respond(message)
        st.success(reponse)

        # Historique (bonus)
        if "historique" not in st.session_state:
            st.session_state.historique = []
        st.session_state.historique.append((message, reponse))

# Affichage de l’historique
if "historique" in st.session_state and st.session_state.historique:
    st.markdown("### 🕘 Historique de la session")
    for msg, rep in reversed(st.session_state.historique):
        st.markdown(f"**Toi :** {msg}")
        st.markdown(f"**ChakibBot :** {rep}")
        st.markdown("---")