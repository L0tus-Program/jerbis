import requests
from bs4 import BeautifulSoup
import openai
import json

def scraping(url):
    print("Entrou no webscraping")
    response = requests.get(url)
    
    if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida (status code 200)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontrar todas as tags de texto desejadas
        tags_texto = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span'])  # Adicione mais tags se necessário
        
        # Concatenar o conteúdo das tags encontradas
        conteudo = '\n'.join(tag.get_text(strip=True) for tag in tags_texto)
        
        
        if conteudo:
            #print(conteudo)
            
            # Abre o arquivo JSON para obter a chave da API do OpenAI
            with open('src.json', 'r') as file:
                src = json.load(file)
            
            # Define a chave da API do OpenAI
            API_KEY = src['key']
            openai.api_key = API_KEY
            
            # Modelo e texto para resumo no ChatGPT
            modelo = "gpt-3.5-turbo-0613"
            resume = conteudo
            
            # Envie a mensagem para o GPT-3.5-turbo e obtenha a resposta
            persona = "Me de as notícias desta página web, não precisa das apresentações de quem é o dono do site, quero apenas as notícias e informações."
            response_gpt = openai.ChatCompletion.create(
                model=modelo,
                messages=[
                    {"role": "system", "content": persona},
                    {"role": "user", "content": resume}
                ]
            )
            
            # Exibe o resumo gerado pelo ChatGPT
            print("Resumo do ChatGPT:", response_gpt.choices[0].message['content'].strip())
            
        else:
            print("Nenhuma tag <body> encontrada na página")
    else:
        print(f"Erro ao fazer a requisição. Status code: {response.status_code}")









#url = "https://conteudos.xpi.com.br/morning-call/"
#scraping(url)
