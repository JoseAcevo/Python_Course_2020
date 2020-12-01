"""Prueba y ejemplo de web-Scraping con python y BeautifulSoup"""
# Importación de los módulos necesarios para la prueba.

import requests
import csv
from bs4 import BeautifulSoup

# Guardado en una variable de la url de la web a scrapear.

urlbase = 'http://quotes.toscrape.com/'

# Ejecución del método (get) de la librería requests.

Response_object = requests.get(urlbase)

# Analisis sintáctico del archivo html obtenido.

html_doc = BeautifulSoup(Response_object.text, 'html.parser')

# Extracción de todas "citas" y "autores" del archivo almacenado en la variable (html_doc).

quotes_html = html_doc.find_all('span', class_="text")
authors_html = html_doc.find_all('small', class_="author")

# Creación de una lista para almacenar las citas ("quotes")

quotes = []

for quote in quotes_html:
    quotes.append(quote.text)

# Creación de una lista para almacenar los autores de las citas (authors)

authors = []

for author in authors_html:
    authors.append(author.text)

# Para hacer el test: Combinar y mostrar las entradas de ambas listas.

for t in zip(quotes, authors):
    print(t)


with open("authorsandquotes.csv", "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes, authors))


