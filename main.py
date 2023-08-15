import requests
from bs4 import BeautifulSoup
import json

class Scrapy:
    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.result = []

    def scrape_articles(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup.find_all("div", class_="blog-card group")
        return []

    def get_links_from_articles(self):
        for indice in range(self.pages):
            url = f"http://blog.mercadoedu.com.br/page/{indice}/"
            articles = self.scrape_articles(url)

            if not articles:
                break

            for article in articles:
                title = article.find(
                    "h2", class_="blog-card-title").text.strip()
                link = article.a["href"]
                description = article.find(
                    "div", class_="blog-card-excerpt").text.strip()
                date = article.find(
                    "ul", class_='blog-card-meta').find("li", class_="blog-card-date").text.strip()
                article_data = {title: {"link": link,
                                        "description": description, "date": date}}
                self.result.append(article_data)

        return self.result

    def create_json(self):
        obj_json = json.dumps(self.get_links_from_articles(),
                              ensure_ascii=False, indent=4)

        with open("articles_Mercadoedu.json", "w", encoding="utf-8") as file:
            file.write(obj_json)


if __name__ == "__main__":
    teste = Scrapy(15)
    teste.create_json()
