import openai
import json
import email_gpt as egpt
from scrap import scraping


# Abra o arquivo JSON
with open('src.json', 'r') as file:
    src = json.load(file)


# key API
API_KEY = src['key']
openai.api_key = API_KEY


modelo = "gpt-3.5-turbo-0613"
historico = []  # Lista para armazenar o histórico de mensagens

def lembretes(time, lembrete):
    print("Entrou lembrete")
    print(time)
    print(lembrete)

# Função para interagir com o ChatGPT
def chatGPT(message):
    global historico
    historico.append(message)  # Adiciona a mensagem ao histórico

    # Envia o histórico completo para o ChatGPT
    response = openai.ChatCompletion.create(
        model=modelo,
        messages=[{"role": "user", "content": '\n'.join(historico)}],
       # function_call="auto",
    )

    first_response = response["choices"][0]["message"]
    print("Jerbis: ", first_response['content'])
    historico.append(first_response['content'])  # Adiciona a resposta ao histórico
    return first_response['content']

# Função para executar a conversa
def run_conversation():
    while True:
        mensagem = input("User : ")
        if mensagem.lower() in ['sair', 'exit']:
            print("Encerrando chat...")
            break
        
        chatGPT(mensagem)

if __name__ == '__main__':
    print("Iniciando Jerbis. Digite 'sair' ou 'exit' para encerrar.")
    run_conversation()