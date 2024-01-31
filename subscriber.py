import zmq
from constPS import * #-

context = zmq.Context()
s_time = context.socket(zmq.SUB)          # cria um socket de assinante para o horário
p_time = "tcp://"+ HOST +":"+ PORT    # como e onde comunicar
s_time.connect(p_time)                     # conecta ao servidor de horário
s_time.setsockopt_string(zmq.SUBSCRIBE, "TIME")  # assina mensagens com prefixo "TIME"

s_stock = context.socket(zmq.SUB)          # cria um socket de assinante para preços de ações
p_stock = "tcp://"+ HOST +":"+ PORT    # como e onde comunicar
s_stock.connect(p_stock)                     # conecta ao servidor de preços de ações
symbol_to_subscribe = "XYZ"
s_stock.setsockopt_string(zmq.SUBSCRIBE, f"STOCK {symbol_to_subscribe}")  # assina mensagens relacionadas à ação XYZ

s_events = context.socket(zmq.SUB)          # cria um socket de assinante para eventos do sistema
p_events = "tcp://"+ HOST +":"+ PORT  # como e onde comunicar
s_events.connect(p_events)                     # conecta ao servidor de eventos do sistema
event_type_to_subscribe = "ALERT"
s_events.setsockopt_string(zmq.SUBSCRIBE, f"EVENT {event_type_to_subscribe}")  # assina mensagens de eventos do tipo ALERT

s_chat = context.socket(zmq.SUB)          # cria um socket de assinante para mensagens de chat
p_chat = "tcp://"+ HOST +":"+ PORT  # como e onde comunicar
s_chat.connect(p_chat)                     # conecta ao servidor de mensagens de chat
user_to_subscribe = "Alice"
s_chat.setsockopt_string(zmq.SUBSCRIBE, f"CHAT {user_to_subscribe}")  # assina mensagens de chat do usuário Alice

for i in range(5):  # Cinco iterações
    time_data = s_time.recv()   # recebe uma mensagem de horário
    stock_data = s_stock.recv()   # recebe uma mensagem de preço da ação
    event_data = s_events.recv()   # recebe uma mensagem de evento do sistema
    chat_data = s_chat.recv()   # recebe uma mensagem de chat

    print("Horário:", bytes.decode(time_data))
    print("Preço da Ação (XYZ):", bytes.decode(stock_data))
    print("Evento do Sistema (ALERT):", bytes.decode(event_data))
    print("Mensagem de Chat (Alice):", bytes.decode(chat_data))
