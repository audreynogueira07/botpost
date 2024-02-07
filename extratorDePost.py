import re
import requests
from bs4 import BeautifulSoup
import chardet

# Inicia uma sessão que pode manter cookies e cabeçalhos através de múltiplas solicitações
session = requests.Session()

def extrair_dados(url):
    # Configura cabeçalhos que imitam um navegador real
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com/',
        'DNT': '1',  # Do Not Track Request Header
    }
    response = session.get(url, headers=headers)
    
    # Detecta a codificação da resposta
    detected_encoding = chardet.detect(response.content)['encoding']
    content = response.content.decode(detected_encoding) if detected_encoding else response.text
    
    soup = BeautifulSoup(content, 'html.parser')
    
    titulo = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'Título não encontrado'
    texto = ' '.join([p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)])
    
    return {
        'titulo': titulo,
        'texto': texto,
    }

# Exemplo de uso
url = input("Cole o URL do artigo que deseja extrair dados: ")
dados = extrair_dados(url)
print(dados)
