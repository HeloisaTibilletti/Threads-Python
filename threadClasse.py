import threading
import time

class threadClasse(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

    def run(self):
        print(f"Thread {self.id} iniciada.")
        time.sleep(1) 
        print(f"Thread {self.id} concluída.")

threads = []
for i in range(1, 11):
    thread = threadClasse(i)
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()
