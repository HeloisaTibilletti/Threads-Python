import threading
import time

def dezThread(id):
    print(f"Tarefa {id} iniciada.")
    time.sleep(1)
    print(f"Tarefa {id} concluída.")

threads = []

for i in range(1, 11):
    thread = threading.Thread(target=dezThread, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
