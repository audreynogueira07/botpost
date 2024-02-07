import pyautogui
import time

# Aguarda um tempo para você mover o mouse para a posição desejada
print("Mova o mouse para a posição desejada e aguarde 5 segundos...")
time.sleep(5)  # Aguarda 5 segundos

# Obtém e imprime as coordenadas atuais do mouse
posicao_atual = pyautogui.position()
print(f"A posição atual do mouse é: {posicao_atual}")
