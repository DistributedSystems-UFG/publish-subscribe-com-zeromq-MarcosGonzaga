import zmq
from constPS import * #-

context = zmq.Context()
s_combined = context.socket(zmq.SUB)  # cria um único socket de assinante combinado
p_combined = "tcp://" + HOST + ":" + PORT  # como e onde comunicar
s_combined.connect(p_combined)  # conecta ao servidor combinado
s_combined.setsockopt_string(zmq.SUBSCRIBE, "TIME")
s_combined.setsockopt_string(zmq.SUBSCRIBE, "STOCK")
s_combined.setsockopt_string(zmq.SUBSCRIBE, "EVENT")
s_combined.setsockopt_string(zmq.SUBSCRIBE, "CHAT")

for i in range(5):  # Cinco iterações
    combined_data = s_combined.recv()   # recebe uma mensagem
    print("Mensagem Recebida:", bytes.decode(combined_data))
