import re
import requests
from bs4 import BeautifulSoup
import chardet
import pyautogui
import subprocess
import time
import pyperclip  # Importa o módulo pyperclip


titulo =  input("Cole o titulo: ")
texto =  input("Cole o texto")
# Solicita o URL do usuário

# Copia o título e o texto extraído para a área de transferência
mensagem = f"TITULO ORIGINAL:{titulo} - COM BASE NELE crie um título com seo otimizado, com base nesse texto, CRIE UM TÍTULO QUE CAPTURE A ESSEÊNCIA DO TÍTULO ORIGINAL MAS EM OUTRAS PALAVRAS, NÃO PLAGEIE. Não escreva nada além do título, nem a palavra Título. Apenas o titulo. SEM "" NO TEXTO - faça o texto em portugues"
pyperclip.copy(mensagem)

# Inicia o Microsoft Edge
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
subprocess.Popen([edge_path])
time.sleep(4)

# Navega para a URL especificada
pyautogui.write('https://chat.openai.com/ ')
pyautogui.press('enter')
time.sleep(6)  # Espera a página carregar

# Mudar Versão gpt
pyautogui.click(461, 162)
time.sleep(1)
pyautogui.click(531, 363)
time.sleep(1)
pyautogui.click(795, 948)
time.sleep(3)

# Pressiona ctrl + v para colar o texto copiado
pyautogui.hotkey('ctrl', 'v')


time.sleep(1)

pyautogui.click(1525, 942)

time.sleep(3)

pyautogui.click(1062, 864)

time.sleep(1)

#copiar
# Localiza o botão de enviar na tela usando uma imagem
botao_enviar_posicao = pyautogui.locateCenterOnScreen('prints/copiar.png')
if botao_enviar_posicao:
    pyautogui.click(botao_enviar_posicao)
else:
    print("Botão de copiar não encontrado.")


pyautogui.click(624, 61)


pyautogui.hotkey('ctrl', 't')


pyautogui.write('https://omonoculo.com.br/wp-admin/post-new.php')
pyautogui.press('enter')
time.sleep(2) 

# colar titulo
timeout = 180  # Tempo máximo de espera em segundos
start_time = time.time()

imagem_titulo_pronto_encontrada = False

while (time.time() - start_time) < timeout and not imagem_titulo_pronto_encontrada:
    try:
        posicao_imagem_titulo = pyautogui.locateCenterOnScreen('prints/pronto.png')
        
        if posicao_imagem_titulo:
            pyautogui.hotkey('ctrl', 'v')  # Executa o comando para colar o título
            print("Título colado com sucesso.")
            imagem_titulo_pronto_encontrada = True
            break  # Sai do loop após colar o título com sucesso
        
    except pyautogui.ImageNotFoundException:
        print("Imagem indicativa para colar título não encontrada, tentando novamente em 10 segundos.")
        time.sleep(10)  # Espera 10 segundos antes da próxima tentativa

if not imagem_titulo_pronto_encontrada:
    print(f"Imagem indicativa para colar título não encontrada após esperar {timeout} segundos.")
    
time.sleep(1)
pyautogui.click(232, 16)

time.sleep(1)
pyautogui.click(417, 155)

time.sleep(2)
pyautogui.click(508, 262)


time.sleep(2)
pyautogui.click(717, 948)
#começar texto
mensagem = f"{titulo}\n\n{texto} crie um post com seo otimizado; com parágrafos bem definidos e explicativos, em uma linguagem descontraída e informativa. Não inira o título principal, não insira a palavra introdução e nem conclusão, em vez disso crie títulos em seus lugares, mas nao escreva introdução na introdução nem conclusão na conclusão. o texto deve ser o mais humano possível e sempre visando otimizar o seo para hankear no google para a palavra chave que mais se destaca no texto NÃO INSIRA TÍTULO NA INTRODUÇÃO - faça o texto em portugues - O TEXTO DEVE SER CRIATIVO, MAIS HUMANO POSSÍVEL E SEM PLAGIOS. não escreva a frase 'em resumo' "
pyperclip.copy(mensagem)

pyautogui.hotkey('ctrl', 'v')

time.sleep(1)

pyautogui.click(1525, 942)

time.sleep(3)

pyautogui.click(1062, 864)

time.sleep(1)

timeout = 180  # Tempo máximo de espera em segundos
start_time = time.time()
botao_encontrado = False

while (time.time() - start_time) < timeout and not botao_encontrado:
    try:
        botao_enviar_posicao = pyautogui.locateCenterOnScreen('prints/copiar.png')
        if botao_enviar_posicao:
            pyautogui.click(botao_enviar_posicao)
            botao_encontrado = True
            print("Botão de copiar encontrado e clicado.")
    except pyautogui.ImageNotFoundException:
        print("Botão de copiar não encontrado, tentando novamente em 10 segundos.")
        time.sleep(10)  # Espera 10 segundos antes da próxima tentativa

if not botao_encontrado:
    print(f"Botão de copiar não encontrado após esperar {timeout} segundos.")
    
time.sleep(1)
pyautogui.click(542, 15)

time.sleep(5)
pyautogui.click(496, 312)

for _ in range(5):
    pyautogui.press('down')
    
pyautogui.hotkey('ctrl', 'v')


time.sleep(1)




pyautogui.click(1354, 170)
time.sleep(10)

pyautogui.click(1891, 20)
time.sleep(1)
