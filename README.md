# IMBD to JSON

## Descrição
<p>Código escrito em Python para buscar por um filme e retornas as informações do mesmo em um aquivo JSON, utilizando a API "The Movie DB" (https://developer.themoviedb.org/reference/intro/getting-started) e o pacote Cinemagoer (https://cinemagoer.github.io/).</p>

## Como Usar (passo a passo)
1. Instalar as dependências contidas no arquivo [requirements.txt](https://github.com/thosijulio/IMDBtoJSON/blob/main/requirements.txt)
2. Criar uma key de acesso a API The Movie DB e adiciona-la ao enviroment (.env), como consta no exemplo [.env.example](https://github.com/thosijulio/IMDBtoJSON/blob/main/.env.example)
3. Executar o arquivo main.py passando movie_title (o primeiro filme encontrado será retornado), ou imdb_movie_id e tmdb_movie_id.

Após a execução do código (leva por volta de dois minutos para recuperar todas as informações), será gerado um arquivo na raíz projeto (movieInfo.json), contendo todas as informações sobre o filme buscado.
