import os
from dotenv import load_dotenv
import chatgpt
import tela
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def criar_pergunta(assunto, tipo, dificuldade, pergunta_exemplo):
    return chatgpt.criar_pergunta(
        OPENAI_API_KEY,
        assunto,
        tipo,
        dificuldade,
        pergunta_exemplo
    )

tela.criar_tela(criar_pergunta)