import threading
import time

class myThread(threading.Thread): 
    def __init__ (self,threadID,name,counter): 
        threading.Thread.__init__(self) 
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self): 
        print("Iniciando" + self.name)  # Obtenha o bloqueio para sincronizar 
        threadLock.acquire () 
        print_time (self.name, self.counter, 3) # Bloqueio gratuito para liberar o próximo 
        threadLock.release () 

def print_time (threadName, delay, counter) : 
        while counter: 
            time.sleep (delay)
            print ("% s:% s"% (threadName, time.ctime (time.time ()))) 
            counter -= 1 
            
threadLock = threading.Lock () 
threads = [] # Criar novo 

thread1 = myThread (1, "Thread-1", 1) 
thread2 = myThread (2, "Thread-2", 2) # Iniciar novo 

thread1.start () 
thread2.start () # Adicionar threads a listthreads de thread. acrescentar 

threads.append(thread1)
threads.append (thread2) # Aguarde que todos os threads sejam concluídos para t nos threads: 

for t in threads:
    t.join () 
print ("Saindo do thread principal")
