import zmq

context = zmq.Context()
zeromqClient = context.socket(zmq.REQ)
zeromqClient.connect("tcp://127.0.0.1:5555")
zeromqClient.send_json({"Action": "Sub", "Topic":"ds2", "Port": "4545"})
msg = zeromqClient.recv_json()
print(msg)



