import sqlite3
from types import DynamicClassAttribute
import pyautogui
import time
import threading
import keyboard  # Certifique-se de ter instalado a biblioteca keyboard

# Flag para controlar a execução da reprodução
continue_running = True

def replay_actions():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('actions.db')
    c = conn.cursor()

    # Ler todas as ações salvas
    c.execute("SELECT action_type, x, y, button, pressed, timestamp FROM actions ORDER BY timestamp ASC")
    actions = c.fetchall()

    last_timestamp = 0  # Inicializa o último timestamp para o cálculo do primeiro intervalo
    for action in actions:
        if not continue_running:  # Verifica se deve parar a execução
            break
        action_type, x, y, button, pressed, timestamp = action
        interval = timestamp - last_timestamp
        time.sleep(interval)  # Espera o intervalo de tempo correto entre as ações
        
        if action_type == 'click' and pressed:
            pyautogui.click(x=x, y=y)
        elif action_type == 'scroll':
            pyautogui.scroll(DynamicClassAttribute, x=x, y=y)
        elif action_type == 'press' and pressed:
            if button.startswith('Key.'):
                key = button.split('.', 1)[1]
                if key == 'space':
                    pyautogui.press('space')
                elif key == 'enter':
                    pyautogui.press('enter')
                elif key == 'backspace':
                    pyautogui.press('backspace')
                elif key == 'shift':
                    pass  # Não há ação direta para shift sozinho
                elif key == 'esc':
                    pyautogui.press('esc')
                # Outros casos especiais podem ser adicionados aqui
            else:
                # Aqui, verificamos se a ação é para digitar uma interrogação usando shift
                if button == '?':
                    pyautogui.hotkey('shift', '/')
                else:
                    pyautogui.write(button)
        
        last_timestamp = timestamp

    # Fechar a conexão com o banco de dados após executar as ações
    conn.close()

def on_esc_press(event):
    global continue_running
    if event.name == 'esc':
        continue_running = False

# Registra o evento de pressionar a tecla "Esc"
keyboard.on_press(on_esc_press)

# Executa a reprodução das ações em uma thread separada
replay_thread = threading.Thread(target=replay_actions)
replay_thread.start()

# Aguarda a thread de reprodução terminar
replay_thread.join()
