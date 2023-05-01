import os
from dotenv import load_dotenv
import chatgpt
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

pergunta_exemplo = 'import javax.swing.JOptionPane; public class SomatorioWhile{ public static void main (String [] args){ int n = Integer.parseInt(JOptionPane.showInputDialog("Digite um número")); int i = 1; int soma = 0; while (i <= n){ soma = soma + i % 2 == 0 ? i : 0; i = i + 1; } JOptionPane.showMessageDialog(null, soma); } } I> O programa calcula a soma dos números inteiros pares no intervalo fechado [0, n]. II. Se o usuário digitar um valor ímpar qualquer, o programa produzirá o valor zero. III. Se o usuário digitar o valor 2, o programa produzirá o valor 2. É correto apenas o que se afirma em a) I b) II c) III d) I e II e) II e III'

print(
    chatgpt.criar_pergunta(
      OPENAI_API_KEY,
      'java',
      'alternativa',
      'dificil',
      pergunta_exemplo
    )
)