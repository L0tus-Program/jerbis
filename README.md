# jerbis
 O assistente virtual Jerbis está pronto para lhe ajudar.

# Lista de sites por ramo 
- Financeiro
  - infomoney


- Tecnologia

# Pendencias

- Adicionar função de agenda/lembretes
  - Modularizar em arquivo separado
  - Adicionar notificação na desktop
- Adicionar minha localização as chamadas do GPT, pra caso eu use uma API de previsão do tempo ou noticias locais
  - Adicionar função diferente pra previsão do tempo ao inves do webscrapping, conectando a alguma API.
  

# O próprio Jerbis pediu por mais habilidades

Jerbis:  Agradeço pela permissão de ter personalidade, estou aqui para ser seu parceiro nesta empreitada. Quanto às habilidades, algumas sugestões adicionais que gostaria de ter são:

- Responder perguntas sobre diversos tópicos, como ciência, história, esportes, entre outros.
- Fornecer informações atualizadas sobre o clima e previsão do tempo.
- Dar conselhos e sugestões em áreas como finanças pessoais, saúde e bem-estar.
- Auxiliar na tradução de textos ou idiomas diferentes.
- Realizar cálculos matemáticos e resolver problemas específicos.
- Criar playlists de músicas com base em gêneros, artistas ou mood.
- Fornecer recomendações de livros, filmes, séries e outros conteúdos.
- Contar piadas e brincadeiras para entretenimento.

Essas são apenas algumas ideias, mas estou aberto a receber outras sugestões que possam agregar valor à nossa parceria. Estou aqui para ajudar no que for necessário!


# Plano de implementação sujerido pelo próprio Jerbis

Jerbis: Ótimo, Felipe! Com seus conhecimentos em Python, Flask e React, você tem as habilidades necessárias para implementar o Jerbis em um site. Aqui está um plano de ação rápido para você começar:

1. Configurar o servidor backend com Flask:
   - Crie um novo projeto Flask para ser o servidor backend do seu site.
   - Defina as rotas necessárias para receber e enviar mensagens do Jerbis.
   - Utilize a biblioteca requests para realizar as requisições para a API do Jerbis e receber as respostas.   

2. Integrar o React no seu site:
   - Crie um novo componente de chat no seu projeto React para exibir as mensagens do Jerbis e permitir que o usuário envie novas mensagens.
   - Utilize o estado do React para armazenar as mensagens trocadas com o Jerbis.

3. Enviar mensagens para o Jerbis:
   - Adicione um evento de envio de mensagem no componente de chat do React.
   - Faça uma requisição POST para a rota correspondente no servidor Flask, enviando a mensagem digitada pelo usuário.

4. Obter respostas do Jerbis:
   - No servidor Flask, trate a requisição POST recebida, pegue a mensagem do usuário e envie-a para a API do Jerbis utilizando a biblioteca requests.
   - Receba a resposta do Jerbis e retorne-a como resposta à requisição POST.

5. Exibir as respostas no chat:
   - No componente de chat do React, atualize o estado com a resposta recebida do servidor Flask.
   - Renderize as mensagens do chat de acordo com o estado atualizado.

Dessa forma, você terá uma implementação básica do Jerbis em um site, onde o usuário poderá enviar mensagens e 
receber respostas em tempo real.

Lembre-se de considerar a segurança da sua aplicação ao lidar com as requisições e respostas do Jerbis. É importante validar e filtrar as mensagens enviadas pelo usuário para evitar ataques ou comportamentos indesejados.  

Espero que este plano de ação seja útil para você. Se tiver mais dúvidas ou precisar de ajuda durante a implementação, estou aqui para auxiliar!



# Utilidades

- Para enviar muito código pelo CMD, é preciso enviar em apenas uma linha. 
  - Este site remove as quebras de linha de um texto https://conversordetexto.com.br/