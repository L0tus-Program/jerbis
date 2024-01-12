import openai
import json
import email_gpt as egpt
from scrap import scraping
import sqlite3
import speech_recognition as sr
import pyttsx3
from utils import *
from datetime import datetime


# Abra o arquivo JSON
with open('src.json', 'r') as file:
    src = json.load(file)


# key API
API_KEY = src['key']
openai.api_key = API_KEY


modelo = "gpt-3.5-turbo-0613"

data_hora_atual = datetime.now()

historico = []  # Lista para armazenar o histórico de mensagens


def enviar_email_gpt(ideia, destinatario):
    try:
        print("Entrou email")
        egpt.enviar_email(ideia, destinatario)
    except:
        pass


def webscrap(url, contexto):
    # print("Webscrap")
    global historico
    req = scraping(url, contexto)
    # print(type(req))
    # print(type(historico))
    historico.append(str(req))  # Adiciona a mensagem ao histórico


def ouvir_microfone():
    microfone = sr.Recognizer()

    # Usando microfone
    with sr.Microphone() as source:
        # Chama o algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)
        print("Voz - USER :\n")

        audio = microfone.listen(source, timeout=5)

    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print("User : ", frase)

        return frase
    except sr.UnknownValueError:
        print("Não entendi")
        return "Erro"


def run_conversation(comando_de_voz):
    global historico
    conn = sqlite3.connect('jerbis.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * from Mensagens")
    dados = cursor.fetchall()

    for row in dados:
        # print(row)
        # Adiciona o segundo elemento de cada linha à lista
        historico.append(row[1])

    while True:
        # Obtendo a data e hora atuais
        data_hora_atual = datetime.now()
        if comando_de_voz == True:
            mensagem = ouvir_microfone()
        else:
            mensagem = input("User : ")

        # print(historico)
        concat = "User : " + mensagem
        historico.append(concat)  # Adiciona a mensagem ao histórico
        if mensagem.lower() in ['sair', 'exit']:
            # Conexão com o banco de dados
            conn = sqlite3.connect('jerbis.db')
            cursor = conn.cursor()

            # Excluir todos os dados existentes na tabela
            cursor.execute("DELETE FROM Mensagens")
            conn.commit()
            # print(historico)
            # Inserir os novos dados da lista na tabela
            for mensagem in historico:
                # print("Inserindo no BD: ",mensagem)
                query = f"INSERT INTO Mensagens (mensagem) VALUES('{mensagem}')"

                # Substitua 'nome_da_coluna' pelo nome real da coluna
                cursor.execute(query)
                conn.commit()
            conn.close()

            print("Encerrando chat...")
            break
        # print("Recebido:", mensagem)
        # response = openai.ChatCompletion.create( # api antiga
        # Filtra os valores None do histórico
        historico_filtrado = [msg for msg in historico if msg is not None]
        persona = "Seu nome é Jerbis,você é um assistente virtual criado por mim e que ainda está em desenvolvimento, estamos testando novas funcionalidades. Você deve ser um especialista em qualquer assunto que conversarmos, principalmente no ramo de tecnologia. Lembre-se de que junto da ultima mensagem você sempre receberá o histórico inteiro das mensagens, então quando eu questioinar algo de mensagens anteriores você pode consultar a mesma mensagem."

        response = openai.ChatCompletion.create(
            model=modelo,
            messages=[
                {"role": "system", "content": persona},
                {"role": "user",  "content": '\n'.join(historico_filtrado)}],
            temperature=0.8,
            functions=[
                {
                    "name": "enviar_email_gpt",
                    "description": "Enviar um e-mail para alguem",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "ideia": {
                                "type": "string",
                                "description": "Construa o texto do e-mail com base nesta ideia. O texto que você gerar será enviado imediatamente para o e-mail do destinatário, portanto deve estar devidamente preparado para isto.Como o texto será enviado diretamente ao contato final, não deve haver variáveis não preenchidas como por exemplo [Seu Nome],[data], etc.",
                            },
                            "destinatario": {"type": "string", "description": "Destinatario do e-mail"}
                        },
                        "required": ["nome", "recado"],
                    }
                },
                {
                    "name": "webscrap",
                    "description": "Acessar um site e ver seu conteúdo",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "url": {
                                "type": "string",
                                "description": "URL completa para enviar para a função de webscrapping, caso a pergunta seja a respeito de economia ou mercado financeiro tente acessar a infomoney"
                            },
                            "contexto": {
                                "type": "string",
                                "description": "Minha dúvida, curiosidade ou coisa que eu quero saber."
                            },
                        },
                        "required": ["url", "contexto"],
                    },


                },
                {
                    "name": "lembretes",
                    "description": "Adicionar um lembrete na minha agenda",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "time": {
                                "type": "integer",
                                "description": "Timer em segundos até o momento que devo ser lembrado de algo"
                            },
                            "lembrete": {
                                "type": "string",
                                "description": "Base do que eu preciso ser lembrado"
                            }
                        },
                        "required": ["time", "lembrete"],
                    },
                }

            ],
            function_call="auto",
        )

        first_response = response["choices"][0]["message"]

        if first_response['content'] == None:
            pass
        else:
            print("\nJerbis: ", first_response['content'], "\n")
            concat = "Jerbis : " + str(first_response['content'])
            audio_resposta = str(first_response['content'])
            engine = pyttsx3.init()
            engine.say(audio_resposta)
            engine.runAndWait()
            historico.append(concat)

        # verifica se o modelo quer chamar uma funcao
        if first_response.get("function_call"):
            function_name = first_response["function_call"]["name"]
            function_args = json.loads(
                first_response["function_call"]["arguments"])

            print("Detectou uma função", function_name, function_args)

            # chama a funcao
            # Detalhe: a resposta em JSON do modelo pode não ser um JSON valido
            if function_name == "enviar_email_gpt":
                function_response = enviar_email_gpt(
                    ideia=function_args.get("ideia"),
                    destinatario=function_args.get("destinatario"),
                )
            elif function_name == "webscrap":
                function_response = webscrap(
                    url=function_args.get("url"),
                    contexto=function_args.get("contexto")

                )

            elif function_name == "lembretes":

                function_response = lembretes(
                    time=function_args.get("time"),
                    lembrete=function_args.get("lembrete"),
                )
            else:
                print("Nao achei a funcao pedida")


if __name__ == '__main__':
    conn = sqlite3.connect('jerbis.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Mensagens
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 mensagem TEXT )''')
    conn.commit()
    conn.close()

    print("Iniciando Jerbis. Digite 'sair' ou 'exit' para encerrar.")
    # Configurações
    comando_de_voz = True
    run_conversation(comando_de_voz)
