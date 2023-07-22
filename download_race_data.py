import os
import requests
from bs4 import BeautifulSoup

def download_pdfs_with_link(url):
    # PDF-Links sammeln
    pdf_links = []
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            if link.get_text().strip() == 'Race Data':
                pdf_links.append(link['href'])

    # PDFs herunterladen
    for pdf_link in pdf_links:
        pdf_name = os.path.basename(pdf_link)
        pdf_path = os.path.join('downloaded_pdfs', pdf_name)

        print(f"Herunterladen von {pdf_link} ...")
        response = requests.get(pdf_link)
        if response.ok:
            with open(pdf_path, 'wb') as file:
                file.write(response.content)
            print(f"{pdf_name} wurde heruntergeladen und gespeichert.")
        else:
            print(f"Fehler beim Herunterladen von {pdf_name}.")

if __name__ == "__main__":
    # URL der Webseite mit den PDF-Links
    url = "https://worldrowing.com/event/2023-world-rowing-under-23-championships/"

    # Erstelle den Ordner "downloaded_pdfs", falls er nicht vorhanden ist
    if not os.path.exists('downloaded_pdfs'):
        os.makedirs('downloaded_pdfs')

    # PDFs herunterladen
    download_pdfs_with_link(url)
