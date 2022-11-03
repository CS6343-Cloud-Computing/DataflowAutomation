import zmq

context = zmq.Context()
zeromqClient = context.socket(zmq.SUB)
zeromqClient.connect("tcp://127.0.0.1:4545")
# zeromqClient.send_json({"Action": "Sub", "Topic":"ds1", "Port": "4545"})
msg = zeromqClient.recv_string()
print(msg)



