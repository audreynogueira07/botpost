from pynput import mouse, keyboard
import threading
import sqlite3
import queue
import time

# Cria uma fila para comunicação entre threads
actions_queue = queue.Queue()
start_time = time.time()  # Registra o tempo de início

def on_click(x, y, button, pressed):
    timestamp = time.time() - start_time  # Tempo decorrido desde o início
    actions_queue.put(('click', x, y, str(button), pressed, timestamp))

def on_scroll(x, y, dx, dy):
    timestamp = time.time() - start_time
    actions_queue.put(('scroll', x, y, dx, dy, timestamp))

def on_press(key):
    timestamp = time.time() - start_time
    try:
        key_value = key.char  # Para caracteres imprimíveis
    except AttributeError:
        key_value = str(key)  # Para teclas especiais
    if key == keyboard.Key.esc:
        global recording
        recording = False
        actions_queue.put(('stop', None, None, None, None, timestamp))
        return False
    actions_queue.put(('press', None, None, key_value, True, timestamp))

def on_release(key):
    timestamp = time.time() - start_time
    key_value = str(key)
    actions_queue.put(('release', None, None, key_value, False, timestamp))

def process_actions_from_queue():
    conn = sqlite3.connect('actions.db')
    c = conn.cursor()
    
    # Certifique-se de que a tabela 'actions' existe
    c.execute('''CREATE TABLE IF NOT EXISTS actions
                 (action_type TEXT, x INTEGER, y INTEGER, button TEXT, pressed BOOLEAN, timestamp REAL)''')
    conn.commit()
    
    # Exclui todas as entradas existentes para garantir que o novo macro não tenha dados antigos
    c.execute("DELETE FROM actions")
    conn.commit()

    while True:
        action = actions_queue.get()
        if action[0] == 'stop':
            break
        c.execute("INSERT INTO actions (action_type, x, y, button, pressed, timestamp) VALUES (?, ?, ?, ?, ?, ?)", action)
        conn.commit()
    
    conn.close()


recording = True

def record():
    with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener_mouse, \
         keyboard.Listener(on_press=on_press, on_release=on_release) as listener_keyboard:
        listener_mouse.join()
        listener_keyboard.join()

# Inicia a gravação em uma thread separada
thread = threading.Thread(target=record)
thread.start()

# Processa ações da fila na thread principal
process_actions_from_queue()

# Aguarda a thread de gravação terminar
thread.join()
