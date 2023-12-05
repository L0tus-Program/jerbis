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


def mandar_um_recado(nome, recado):
    print("Rodando a funcao")
    enviar_recado = {
        "nome": nome,
        "recado": recado,
    }
    print("Verifiquei o tempo e esta sol")
    return json.dumps(enviar_recado)



def enviar_email_gpt(ideia, destinatario):
    try:
        print("Entrou email")
        egpt.enviar_email(ideia,destinatario)
    except:
        pass
# Passo 1, manda o texto pro modelo e prepara a funcao caso ela seja chamada

def webscrap(url):
    print("Webscrap")
    scraping(url)


def run_conversation():
    while True:
        mensagem = input("User : ")
        if mensagem.lower() in ['sair', 'exit']:
            print("Encerrando chat...")
            break
        # print("Recebido:", mensagem)
        #response = openai.ChatCompletion.create( # api antiga
        response = openai.ChatCompletion.create( 
            model=modelo,
            messages=[{"role": "user", "content": mensagem}],
            functions=[
                {
                    "name": "enviar_email_gpt",
                    "description": "Enviar um e-mail para alguem",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "ideia": {
                                "type": "string",
                                "description": "Você é o bot da OPENAAI e deve sempre se chamar assim nos e-mails. Construa o texto do e-mail com base nesta ideia. O texto que você gerar será enviado imediatamente para o e-mail do destinatário, portanto deve estar devidamente preparado para isto.Como o texto será enviado diretamente ao contato final, não deve haver variáveis não preenchidas como por exemplo [Seu Nome],[data], etc.",
                            },
                            "destinatario": {"type": "string", "description": "Destinatario do e-mail"}
                        },
                        "required": ["nome", "recado"],
                    }
                },
                {
                    "name": "webscrap",
                    "description" : "Acessar um site e ver seu conteúdo",
                    "parameters": {
                        "type": "object",
                        "properties":{
                            "url":{
                                "type":"string",
                                "description": "URL completa para enviar para a função de webscrapping"
                            },
                        },
                        "required":["url"],
                    },


                }

            ],
            function_call="auto",
        )

        first_response = response["choices"][0]["message"] 

        
        print("Jerbis: ", first_response['content'])

        # Passo 2, verifica se o modelo quer chamar uma funcao
        if first_response.get("function_call"):
            function_name = first_response["function_call"]["name"]
            function_args = json.loads(first_response["function_call"]["arguments"])

            print("")
            print("Detectou uma função", function_name, function_args)
            print("")

            # Passo 3, chama a funcao
            # Detalhe: a resposta em JSON do modelo pode não ser um JSON valido
            if function_name == "enviar_email_gpt":
                function_response = enviar_email_gpt(
                    ideia=function_args.get("ideia"),
                    destinatario=function_args.get("destinatario"),
                )
            if function_name == "webscrap":
                function_response = webscrap(
                    url=function_args.get("url")
                    
                )
            else:
                print("Nao achei a funcao pedida")




if __name__ == '__main__':
    print("Iniciando Jerbis. Digite 'sair' ou 'exit' para encerrar.")
    run_conversation()