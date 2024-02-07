from pynput import mouse, keyboard
import pyautogui
import threading
import time

actions = []
recording = True  # Variável de controle para continuar ou parar a gravação

def on_click(x, y, button, pressed):
    if pressed and recording:
        actions.append(('click', x, y))

def on_press(key):
    global recording
    if key == keyboard.Key.esc:  # Use a tecla Esc para parar a gravação
        recording = False  # Isso sinaliza para parar a gravação
        return False  # Retorna False para parar os listeners
    if recording:
        try:
            actions.append(('press', key.char))
        except AttributeError:
            actions.append(('press', key))

def record():
    with mouse.Listener(on_click=on_click) as listener_mouse, \
         keyboard.Listener(on_press=on_press) as listener_keyboard:
        listener_mouse.join()
        listener_keyboard.join()

def replay():
    for action in actions:
        if action[0] == 'click':
            pyautogui.click(x=action[1], y=action[2])
        elif action[0] == 'press':
            if action[1] == 'esc':  # Ignora a tecla Esc usada para parar a gravação
                continue
            pyautogui.press(action[1])
        time.sleep(0.1)  # Pequena pausa entre ações

# Inicia a gravação em uma thread separada para não bloquear o script principal
thread = threading.Thread(target=record)
thread.start()

# Aguarde a thread de gravação terminar (indicando que a gravação parou)
thread.join()

# Agora que a gravação parou, chame replay para reproduzir as ações
replay()
