import requests
from bs4 import BeautifulSoup


def pruebas(url: str):
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup.prettify())


if __name__ == "__main__":
    pruebas("http://archive.stsci.edu/missions/k2/")
