import requests
from bs4 import BeautifulSoup
import openai
import json

def scraping(url):
    print("Entrou no webscraping")
    response = requests.get(url)
    
    if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida (status code 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.find('body')  # Obtém somente a tag <body>
        
        if content:
            html_limpo = content.prettify()
            
            # Abre o arquivo JSON para obter a chave da API do OpenAI
            with open('src.json', 'r') as file:
                src = json.load(file)
            
            # Define a chave da API do OpenAI
            API_KEY = src['key']
            openai.api_key = API_KEY
            
            # Modelo e texto para resumo no ChatGPT
            modelo = "gpt-3.5-turbo-0613"
            resume = html_limpo
            
            # Envie a mensagem para o GPT-3.5-turbo e obtenha a resposta
            persona = "Escreva um pequeno resumo sobre o conteúdo desta página web"
            response_gpt = openai.ChatCompletion.create(
                model=modelo,
                messages=[
                    {"role": "system", "content": persona},
                    {"role": "user", "content": resume}
                ]
            )
            
            # Exibe o resumo gerado pelo ChatGPT
            print("Resumo do ChatGPT:", response_gpt.choices[0].resume['content'].strip())
            
        else:
            print("Nenhuma tag <body> encontrada na página")
    else:
        print(f"Erro ao fazer a requisição. Status code: {response.status_code}")









#url = "https://www.messeminvestimentos.com.br/"
#scraping(url)
