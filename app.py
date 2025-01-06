import streamlit as st
from chatbot_logic import Chatbot

def main():
    st.title("Mon Chatbot avec Gemini")
    
    # Initialiser le chatbot
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = Chatbot()
    
    # Zone de saisie utilisateur
    user_input = st.text_input("Votre message:", key="user_input")
    
    # Bouton pour effacer l'historique
    if st.button("Effacer l'historique"):
        st.session_state.chatbot.clear_memory()
        st.session_state.messages = []
    
    # Initialiser l'historique des messages
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Traiter l'entrée utilisateur
    if user_input:
        # Obtenir la réponse du chatbot
        response = st.session_state.chatbot.get_response(user_input)
        
        # Ajouter les messages à l'historique
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Afficher l'historique des messages
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write(f"Vous: {message['content']}")
        else:
            st.write(f"Assistant: {message['content']}")

if __name__ == "__main__":
    main()
