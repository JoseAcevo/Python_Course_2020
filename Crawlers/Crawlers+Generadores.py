import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time


class PostCrawled:
    """Clase encargada de crear objetos de tipo PostCrawled."""

    def __init__(self, titulo, emoticono, contenido, imagen):
        self.titulo = titulo
        self.emoticono = emoticono
        self.contenido = contenido
        self.imagen = imagen


class PostExtractor:

    @staticmethod
    def extrae_info():
        """Método encargado de extraer la info de la página."""

        urlbase = "http://python.beispiel.programmierenlernen.io/index.php"

        while urlbase != "":

            mi_doc = requests.get(urlbase)
            doc_final = BeautifulSoup(mi_doc.text, "html.parser")
            time.sleep(2)

            for card in doc_final.select(".card"):
                titulo = card.select(".card-title span")[1].text
                emoticono = card.select_one(".emoji").text
                contenido = card.select_one(".card-text").text
                imagen = urljoin(urlbase, card.select_one("img").attrs["src"])

                yield PostCrawled(titulo, emoticono, contenido, imagen)

            botonsiguiente = doc_final.select_one(".navigation .btn")

            if botonsiguiente:
                rutasabsolutas = urljoin(urlbase, botonsiguiente.attrs["href"])
                urlbase = rutasabsolutas
                print(rutasabsolutas)

            else:
                urlbase = ""


unPost = PostExtractor()
Lista_Posts = unPost.extrae_info()

contador = 0

for elPost in Lista_Posts:
    if contador == 12:
        break
    contador += 1
    print(elPost.emoticono)
    print(elPost.titulo)
    print(elPost.contenido)
    print(elPost.imagen)
    print("<---------------------------HASTA AQUÍ--------------------------------------------->")
