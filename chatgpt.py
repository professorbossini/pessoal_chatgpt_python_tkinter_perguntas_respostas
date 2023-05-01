import openai

def criar_pergunta(
  OPENAI_API_KEY,
  assunto,
  tipo,
  dificuldade,
  questao_exemplo = None
):
  openai.api_key = OPENAI_API_KEY
  assunto = f'Elabore uma questão sobre {assunto}'
  tipo = f'Ela deve ser {tipo}'
  dificuldade = f'Seu nível de dificuldade deve ser {dificuldade}'
  questao_exemplo = f'Utilize esta questão como exemplo: {questao_exemplo}.' if questao_exemplo != None else ''
  prompt = f'{assunto}.{tipo}.{dificuldade}.{questao_exemplo}'
  resposta = openai.Completion.create(
    engine='text-davinci-003',
    prompt = prompt,
    max_tokens=150
  )
  return resposta.choices[0].text.strip()
