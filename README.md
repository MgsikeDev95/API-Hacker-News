How to Use/Como usar em pt ao fim Download the files:

**1**-On the GitHub repository page, click the "Code" button and then select "Download ZIP". Extract the ZIP file to a folder on your computer. Install Python:

**2**- If you don't have Python installed, you can download and install it from the official website: https://www.python.org/downloads/. Make sure to check the option "Add Python to PATH" during the installation process. Install dependencies:

**3**-Install dependencies: The script uses the plotly library to create the visualization. To install it, open your terminal or command prompt and run: bash pip install plotly

**4**-Run the script: Execute the script by running the following command in your terminal or command prompt: bash python python_repos_visual.py

**Como Usar Baixe os arquivos:**

**1**-Na página do repositório no GitHub, clique no botão "Code" e depois selecione "Download ZIP". Extraia o arquivo ZIP para uma pasta no seu computador. Instale o Python:

**2**-Se você ainda não tem o Python instalado, pode baixá-lo e instalá-lo a partir do site oficial: https://www.python.org/downloads/. Certifique-se de marcar a opção "Add Python to PATH" durante o processo de instalação.

**3**-Instale as dependências: O script usa a biblioteca plotly para criar a visualização. Para instalá-la, abra o terminal ou prompt de comando e execute: bash pip install plotly

**4**-Execute o script: Execute o script rodando o seguinte comando no terminal ou prompt de comando: bash python python_repos_visual.py



This code retrieves and graphically visualizes the five most commented posts on Hacker News. First, it fetches a list of IDs of the most popular posts and then accesses the details of each one to extract information such as the title, link, author, and number of comments. After collecting this data, the list of posts is sorted in descending order based on the number of comments, ensuring that the most active discussions appear at the top.  

With the information organized, the next step is to prepare the data for visualization. Separate lists are created to store the post titles, comment counts, authors, and author profile links. The titles are formatted as clickable links using HTML, allowing users to be redirected to the respective Hacker News post when clicking on a title in the chart. At the same time, a list of hover texts is built to be displayed when hovering over each bar in the chart. This formatting includes the author's name, preceded by the word “Author:”, along with a clickable link to their profile.  

Once the data is prepared, the visualization is configured using the Plotly Express library. The bar chart is generated with post titles as labels on the X-axis and the number of comments on the Y-axis. Additionally, the chart title is set to “Most Active Discussions in Hacker News,” and axis labels are adjusted for better readability. The hover functionality is applied to ensure that when hovering over a bar, the author’s name and a link to their profile are displayed clearly and in an organized manner.  

Finally, the function responsible for rendering the chart is called, allowing the collected data to be presented in a visual and interactive way. The final result is a graphical representation of the most active discussions on Hacker News, enabling users to quickly identify which topics generated the most engagement and access the posts intuitively.


Este código busca e visualiza graficamente as cinco postagens mais comentadas no Hacker News. Primeiramente, ele obtém uma lista de IDs das postagens mais populares e, em seguida, acessa os detalhes de cada uma para extrair informações como título, link, autor e número de comentários. Após coletar esses dados, a lista contendo essas postagens é ordenada de forma decrescente com base no número de comentários, garantindo que as discussões mais ativas apareçam no topo.

Com as informações organizadas, é necessário preparar os dados para a criação do gráfico. Para isso, são criadas listas separadas contendo os títulos das postagens, o número de comentários, os autores e os links dos perfis dos autores. Os títulos são formatados como links clicáveis utilizando HTML, permitindo que, ao clicar em um título no gráfico, o usuário seja redirecionado para a respectiva postagem no Hacker News. Em paralelo, é construída a lista de textos que serão exibidos ao passar o mouse sobre cada barra do gráfico. Essa formatação inclui o nome do autor precedido pela palavra “Author:” e um link clicável para seu perfil.

Uma vez que os dados estejam preparados, a visualização é configurada com a biblioteca Plotly Express. O gráfico de barras é gerado utilizando os títulos das postagens como rótulos no eixo X e o número de comentários no eixo Y. Além disso, o título do gráfico é definido como “Most Active Discussions in Hacker News”, e os rótulos dos eixos são ajustados para melhorar a compreensão da visualização. A configuração do hover é aplicada para garantir que, ao passar o mouse sobre uma barra, seja exibido o nome do autor e o link para seu perfil de maneira clara e organizada.

Por fim, a função responsável por renderizar o gráfico é chamada, permitindo que os dados coletados sejam apresentados de forma visual e interativa. O resultado final é uma representação gráfica das discussões mais ativas do Hacker News, permitindo que os usuários identifiquem rapidamente quais tópicos geraram mais engajamento e acessem as postagens de forma intuitiva.
