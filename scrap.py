import requests
from bs4 import BeautifulSoup
import openai
import json


def scraping(url, contexto):
    print("Entrou no webscraping")
    try:
        response = requests.get(url)

        # Verifica se a requisição foi bem-sucedida (status code 200)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Encontrar todas as tags de texto desejadas
            # Adicione mais tags se necessário
            tags_texto = soup.find_all(
                ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a'])

            # Concatenar o conteúdo das tags encontradas
            conteudo = '\n'.join(tag.get_text(strip=True)
                                 for tag in tags_texto)

            if conteudo:
                # print(conteudo)

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

                persona = f'Sane minha dúvida ou curiosidade neste contexto: {contexto}, não quero saber a referência das informações.'
                # persona = "Você tem um cliente em busca de atualizações sobre o tema deste site. Faça um resumo de notícias e informações para seu cliente, mas não deixe ele saber que você fez uma pesquisa"
                response_gpt = openai.ChatCompletion.create(
                    model=modelo,
                    messages=[
                        {"role": "system", "content": persona},
                        {"role": "user", "content": resume}
                    ]
                )

                # Exibe o resumo gerado pelo ChatGPT
                response = response_gpt.choices[0].message['content'].strip()
                print("Jerbis :\n", response)
                return response

            else:
                print("Nenhuma tag <body> encontrada na página")
        else:
            print(
                f"Erro ao fazer a requisição. Status code: {response.status_code}")

    except:
        print("Não foi possível fazer a requisição")
