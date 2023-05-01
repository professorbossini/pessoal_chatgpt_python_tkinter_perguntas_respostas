import os
from dotenv import load_dotenv
import chatgpt
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
print(
    chatgpt.criar_pergunta(
      OPENAI_API_KEY,
      'java',
      'alternativa',
      'médio'
    )
)