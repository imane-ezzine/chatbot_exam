import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

class Chatbot:
    def __init__(self):
        # Configuration de l'API Gemini
        genai.configure(api_key="AIzaSyDhJBopXsxkJAMoG6iv6GduIZEl8nNpCrY")
        
        # Initialiser le modèle de langage
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.7,
            google_api_key="AIzaSyDhJBopXsxkJAMoG6iv6GduIZEl8nNpCrY"
        )
        
        # Initialiser la mémoire de conversation
        self.memory = ConversationBufferMemory(return_messages=True)
        
        # Créer la chaîne de conversation
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            verbose=True
        )
    
    def get_response(self, user_input: str) -> str:
        """
        Obtenir une réponse du chatbot pour l'entrée utilisateur
        
        Args:
            user_input (str): Message de l'utilisateur
            
        Returns:
            str: Réponse du chatbot
        """
        try:
            response = self.conversation.predict(input=user_input)
            return response
        except Exception as e:
            return f"Une erreur s'est produite: {str(e)}"
    
    def clear_memory(self):
        """Effacer l'historique de la conversation"""
        self.memory.clear()