# Web Scraping do Blog MercadoEdu

Este é um projeto de web scraping que extrai informações de artigos do blog MercadoEdu (http://blog.mercadoedu.com.br) e cria um arquivo JSON contendo os dados coletados.

## Funcionamento

O script Python utiliza as bibliotecas `requests` e `BeautifulSoup` para fazer solicitações HTTP às páginas do blog, analisar o HTML e extrair informações específicas dos elementos DOM. Em seguida, as informações dos artigos (título, link, descrição e data) são organizadas em um formato JSON e gravadas em um arquivo.


## Como Usar

1. Faça o download ou clone este repositório.

2. Abra o arquivo `main.py` em um editor de código Python.

3. Execute o script `main.py`.

Isso iniciará o web scraping e criará um arquivo JSON chamado `articles_Mercadoedu.json` contendo os dados extraídos.

## Personalização

Se a estrutura do site http://blog.mercadoedu.com.br mudar, você pode precisar ajustar o código para se adequar à nova estrutura.

