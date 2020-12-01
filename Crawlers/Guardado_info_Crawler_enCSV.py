import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv


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

            mi_doc = requests.get(urlbase) # Copias el código de la página guardada en urlbase y lo almacenas en un objeto response (request)
            doc_final = BeautifulSoup(mi_doc.text, "html.parser") # Y lo almacenas en una variable para su estudio.
            time.sleep(2)

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

with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
    postwriter = csv.writer(csvfile, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for mipost in unPost.extrae_info():
        postwriter.writerow([mipost.emoticono, mipost.titulo, mipost.contenido, mipost.imagen])
