import requests
from bs4 import BeautifulSoup


def importar_h1():
    try:
        link = input("escreva o site: ")

        resposta = requests.get(link)
        conteudo = resposta.content

        site = BeautifulSoup(conteudo, "html.parser")
        tag = site.find("h1")
        print(tag.text)

    except AttributeError:
        print("Sem tag h1")

    except:
        print("Houve algum erro com o seu link.")


importar_h1()
