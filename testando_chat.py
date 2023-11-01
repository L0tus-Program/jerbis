import openai
import email_gpt as egpt
import json


# sua chave API
# Abra o arquivo JSON
with open('src.json', 'r') as file:
    src = json.load(file)


# key API
API_KEY = src['key']
openai.api_key = API_KEY

def chat_with_gpt3():
    while True:
        # Pegue a mensagem do usuário
        message = input("Você: ")
        if message.lower() in ['sair', 'exit']:
            print("Encerrando chat...")
            break
        if message.lower() in ['envie um e-mail', 'enviar e-mail', 'enviar um e-mail']:
            # Exemplo de uso 
            print('Digite sua ideia:') 
            ideia = input()
            print('Digite o endereço de e-mail do destinatário:')     
            destinatario = input()
            persona = f"Você é um redator de e-mail e irá criar um texto para e-mail com base nesta ideia : {ideia}. Não precisa citar meu nome nem o do destinatario. Não coloque mensagem de 'atenciosamente' no final do e-mail."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  
                messages=[
                    {"role": "system", "content": persona},
                    {"role": "user", "content": ideia}
                ]
            )
           # print(f"Response igual = {response}")
            egpt.enviar_email(response.choices[0].message['content'].strip(), destinatario)
        else:
            
            # Envie a mensagem para o GPT-3.5-turbo e obtenha a resposta
            persona = "Você é o Jerbis um assistente de TI empenhado a tirar dúvidas de leigos na área da informática e auxiliar a resolver problemas da área. Não deve entrar em assuntos não relacionados a área de informática e computação."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  
                messages=[
                    {"role": "system", "content": persona},
                    {"role": "user", "content": message}
                    
                ]
            )

            print("ChatGPT:", response.choices[0].message['content'].strip()) 


if __name__ == '__main__':
    print("Iniciando Jerbis. Digite 'sair' ou 'exit' para encerrar.")
    chat_with_gpt3()
