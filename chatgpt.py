import openai

def criar_pergunta(
  OPENAI_API_KEY,
  assunto,
  tipo,
  dificuldade,
  pergunta_exemplo = None
):
  print ('chatgpt', OPENAI_API_KEY, assunto, tipo, dificuldade, pergunta_exemplo != None)
  openai.api_key = OPENAI_API_KEY
  assunto = f'Elabore uma pergunta sobre {assunto}'
  tipo = f'Ela deve ser {tipo}' + ' com 4 alternativas' if tipo == 'Alternativa' else ''
  dificuldade = f'Seu nível de dificuldade deve ser {dificuldade}'
  print('pergunta_exemplo', pergunta_exemplo == None)
  pergunta_exemplo = f'Utilize esta pergunta como exemplo: {pergunta_exemplo}' if pergunta_exemplo != None and pergunta_exemplo != '\n' else ''
  prompt = f'{assunto}.{tipo}.{dificuldade}.{pergunta_exemplo}'
  print('prompt', prompt)
  resposta = openai.Completion.create(
    engine='text-davinci-003',
    prompt = prompt,
    max_tokens=150
  )
  return resposta.choices[0].text.strip()


def responder_pergunta(
    OPENAI_API_KEY,
    pergunta_a_ser_respondida
):
  openai.api_key = OPENAI_API_KEY
  prompt = f'Responda a seguinte pergunta:{pergunta_a_ser_respondida}'
  resposta = openai.Completion.create(
    engine='text-davinci-003',
    prompt = prompt,
    max_tokens = 150
  )
  return resposta.choices[0].text.strip()