📽️ API-Consulta-Filmes-TMDB
Olá! Me chamo Felipe e vou te contar passo a passo como desenvolvi essa API. Esse projeto foi muito importante na minha jornada como desenvolvedor Python, pois foi a primeira vez que criei uma API REST usando Flask e consumindo dados de uma API externa — a TMDb (The Movie Database).

🚀 O que essa API faz?
Ela busca informações de filmes pelo título e retorna os dados em formato JSON.
Exemplo de acesso:
http://127.0.0.1:5000/movies/search?title=Filme

📝 Como desenvolvi (passo a passo)
Configurei o ambiente Python

Criei um novo projeto e instalei as bibliotecas necessárias, principalmente o Flask e requests.

Montei a estrutura da API com Flask

Implementei uma rota /movies/search que recebe o título do filme como parâmetro na URL.

Fiz a integração com a API do TMDb

Usei a biblioteca requests para fazer uma requisição GET para o TMDb, passando o título do filme e a minha API Key.

Tratei os dados recebidos

Recebi os dados em JSON, filtrei as informações mais importantes (como nome, sinopse e data de lançamento) e organizei para retornar na minha API.

Implementei tratamento de erros

Adicionei verificações para casos de título não encontrado ou erro de requisição, garantindo que a API não quebre.

Teste no navegador e no Postman

Testei o funcionamento acessando a URL no navegador e via Postman, conferindo se os dados estavam corretos e organizados.

Publiquei no GitHub

Subi o projeto no meu repositório do GitHub para compartilhar com outros desenvolvedores.

📚 O que eu aprendi:
Criar rotas e endpoints usando Flask.

Utilizar a biblioteca requests para consumir APIs externas.

Trabalhar com dados em JSON.

Fazer tratamento de erros em APIs.

Publicar projetos no GitHub.

📷 Dica!
Adicionei uma imagem no repositório mostrando a API funcionando no navegador e no Postman. Recomendo fazer o mesmo!

📢 Feedback
Se quiser, clone o projeto, teste e me envie sugestões. Vou adorar saber o que achou!
