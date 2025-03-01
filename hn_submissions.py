import requests
import plotly.express as px
from operator import itemgetter

# Obtém os IDs das postagens mais populares
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)

# Lista de IDs das principais postagens
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:5]:  # Obtendo apenas as 5 primeiras
    # Obtém os detalhes de cada postagem
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    
    if r.status_code != 200:
        continue  # Pula para o próximo ID caso haja erro
    
    response_dict = r.json()

    # Verifica se os campos necessários existem antes de acessá-los
    if 'title' in response_dict and 'descendants' in response_dict and 'by' in response_dict:
        owner = response_dict['by']
        owner_link = f"https://news.ycombinator.com/user?id={owner}"  # Criando link manualmente

        submission_dict = {
            'title': response_dict["title"],
            'comments': response_dict['descendants'],
            'author': owner,
            'author_link': owner_link,
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}"
        }
        submission_dicts.append(submission_dict)

# Ordena os artigos pelo número de comentários em ordem decrescente
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Criando listas para os gráficos
submission_titles = [f"<a href='{sub['hn_link']}' target='_blank'>{sub['title']}</a>" 
                     for sub in submission_dicts]  # Agora os títulos são links clicáveis
submission_comments = [sub['comments'] for sub in submission_dicts]
authors = [sub['author'] for sub in submission_dicts]  # Lista com os nomes dos autores
author_links = [sub['author_link'] for sub in submission_dicts]  # Lista com os links dos autores

# Alterando o hover_data para exibir "Author: [Nome]" e o link do perfil
hover_text = [f"Author: {author}<br><a href='{link}' target='_blank'>Profile Link</a>" 
              for author, link in zip(authors, author_links)]  # Exibe "Author" e link

# Criando gráfico
title = "Most Active Discussions in Hacker News"
labels = {'x': 'Discussion Name', 'y': 'Number Of Comments'}

fig = px.bar(
    x=submission_titles, 
    y=submission_comments, 
    title=title, 
    labels=labels, 
    hover_name=hover_text  # Exibe "Author: [Nome]" e o link para o perfil
)

fig.show()
