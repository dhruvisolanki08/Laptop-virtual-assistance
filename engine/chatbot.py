from langchain_ollama import OllamaLLM
from engine.command import *

model = OllamaLLM(model="llama3")

def Chat(prompt):
    response = model.invoke(input=prompt)
    speak(response)


