import requests
import pandas as pd

livros = [

    {
        "title": "Phyton, é mais fácil que JAVA",
        "description": "Aprender Python é mais legal",
        "author": 1,
        "gender": 1
    },
    {
        "title": "A grande História do IJJ",
        "description": "O IJJ tem tem uma grande história para contar",
        "author": 2,
        "gender": 2
    },
    {
        "title": "A vida secreta dos QA",
        "description": "Aqui você vai descobrir o que os Qas fazem no seu código programador",
        "author": 3,
        "gender": 3
    },
    {
        "title": "O Ultimo Qa",
        "description": "A ultimo Qa é saga do ultimo guerreiro Qa contra os bugs em produção",
        "author": 4,
        "gender": 4
    }    
]

url = "http://apilivro.jogajuntoinstituto.org/books/"
def cadastrar_livro(livro):
    response = requests.post(url, json=livro)
    if response.status_code == 201:
        livro_nome = livro.get('title')
        print(f"Livro '{livro_nome}' cadastrado com sucesso!")
        response_text = response.text
        print(response_text)
    else:
        print(f"Erro ao cadastrar o livro '{livro['title']}'")   

    
for livro in livros:   
    cadastrar_livro(livro)        



url = "http://apilivro.jogajuntoinstituto.org/books/"

def buscar_livros():
    
    response = requests.get(url)

    livros = response.json() if response.status_code == 200 else []

    nome_arquivo = "todos_os_livros.csv"
    df = pd.DataFrame(livros)
    df.to_csv(nome_arquivo, index=False)

    print(f"Resultados salvos em '{nome_arquivo}'")

buscar_livros()

