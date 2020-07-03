import zmq
import numpy as np
import sys
array = ['weather', 'game', 'food', 'tv', 'shopping']
while True:
    t = sys.argv[1]
    t = array[int(t)]
    print('the topic I want to receive is {}'.format(t))
    topic = t.encode()
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://127.0.0.1:5559")
    sendTime = time.time()
    subscriber.setsockopt(zmq.SUBSCRIBE, topic)
    [topic, meaasge] = subscriber.recv_multipart()
    recTime = time.time()
    logFile = '/home/xujuan/Desktop/cs6381/timeLog.txt'
    f = open(logFile, "a")
    f.write("My topic is {}, my sending time and receive time is {}/{}\n".format(topic, sendTime, recTime))
    f.close()
    print('the topic I received is{}: value is {}'.format(topic, meaasge))

