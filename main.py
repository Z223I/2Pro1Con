import threading
import Queue
from Pro1 import Pro1
from Pro2 import Pro2
from Con1 import Con1

pro1 = Pro1()
pro2 = Pro2()
con1 = Con1()

qNumbers = Queue.Queue(maxsize=0)
qCommands = Queue.Queue(maxsize=0)

pro1Thread = threading.Thread(target=pro1.run, args=(qNumbers,))
pro2Thread = threading.Thread(target=pro2.run, args=(qCommands,))
con1Thread1 = threading.Thread(target=con1.run1, args=(qNumbers,))
con1Thread2 = threading.Thread(target=con1.run2, args=(qCommands,))

pro1Thread.start()
pro2Thread.start()
con1Thread1.start()
con1Thread2.start()

qNumbers.join()
qCommands.join()
