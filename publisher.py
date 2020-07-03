import time
import zmq
import numpy as np
import sys
class Pub():
    def __init__(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.connect("tcp://127.0.0.1:5560")
        #return self.socket
    def sendMsg(self, topic, val):
        self.topic = topic.encode()
        self.val = val.encode()
        self.socket.send_multipart([self.topic,  self.val])

array = ['weather', 'game', 'food', 'tv', 'shopping']
p = Pub()
i = sys.argv[1]
i = int(i)
topic = array[i]
val = 'I am sending {}'.format(topic)
while True:
    p.sendMsg(topic, val)
    time.sleep(1)

# pubs = []
# for i in range(10):
#     p = Pub()
#     pubs.append(p)
# print(pubs)
# while True:
#     for _ in pubs:
#         i = np.random.randint(1,10)
#         topic = str(i)
#         val = str(i)
#         _.sendMsg(topic, val)
#         print(topic)
#         time.sleep(1)
