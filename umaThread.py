import threading
import time

def umaThread():
    print("Tarefa iniciada...")
    time.sleep(1)  
    print("Tarefa concluída.")

thread = threading.Thread(target=umaThread)
thread.start()


thread.join()
