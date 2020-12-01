import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


class PostCrawled:

    def __init__(self, titulo, emoticono, contenido, imagen):
        self.titulo = titulo
        self.emoticono = emoticono
        self.contenido = contenido
        self.imagen = imagen


class PostExtractor:

    @staticmethod
    def extrae_info():
        urlbase = "http://python.beispiel.programmierenlernen.io/index.php"
        posts = []

        while urlbase != "":

            mi_doc = requests.get(urlbase)
            doc_final = BeautifulSoup(mi_doc.text, "html.parser")
            time.sleep(1)

            for card in doc_final.select(".card"):
                titulo = card.select(".card-title span")[1].text
                emoticono = card.select_one(".emoji").text
                contenido = card.select_one(".card-text").text
                imagen = urljoin(urlbase, card.select_one("img").attrs["src"])

                crawled = PostCrawled(titulo, emoticono, contenido, imagen)
                posts.append(crawled)

            botonsiguiente = doc_final.select_one(".navigation .btn")

            if botonsiguiente:                                                          
                rutasabsolutas = urljoin(urlbase, botonsiguiente.attrs["href"])
                urlbase = rutasabsolutas
                print(rutasabsolutas)

            else:
                urlbase = ""

        return posts


unPost = PostExtractor()
Lista_Posts = unPost.extrae_info()

for elPost in Lista_Posts:
    print(elPost.emoticono)
    print(elPost.titulo)
    print(elPost.contenido)
    print(elPost.imagen)
    print("<---------------------------HASTA AQUÍ--------------------------------------------->")

# print(Lista_Posts).
# REPASAR TEMA CRAWLERS Y EN ESPECIAL EL VIDEO 55.
