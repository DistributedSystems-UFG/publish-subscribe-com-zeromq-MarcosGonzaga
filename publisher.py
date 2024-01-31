import zmq, time
from constPS import * #-

context = zmq.Context()
s_time = context.socket(zmq.PUB)        # cria um socket de publicador para o horário
p_time = "tcp://0.0.0.0:"+ PORT     # como e onde comunicar
s_time.bind(p_time)                          # associa o socket ao endereço

s_stock = context.socket(zmq.PUB)        # cria um socket de publicador para preços de ações
p_stock = "tcp://0.0.0.0:"+ PORT      # como e onde comunicar
s_stock.bind(p_stock)                          # associa o socket ao endereço

s_events = context.socket(zmq.PUB)       # cria um socket de publicador para eventos do sistema
p_events = "tcp://0.0.0.0:"+ PORT  # como e onde comunicar
s_events.bind(p_events)                   # associa o socket ao endereço

s_chat = context.socket(zmq.PUB)       # cria um socket de publicador para mensagens de chat
p_chat = "tcp://0.0.0.0:"+ PORT  # como e onde comunicar
s_chat.bind(p_chat)                   # associa o socket ao endereço

while True:
    time.sleep(5)                    # aguarda 5 segundos
    msg_time = str.encode("TIME " + time.asctime())
    s_time.send(msg_time)  # publica o horário atual

    stock_price = {"symbol": "XYZ", "price": 50.0}  # Dados fictícios da ação XYZ
    msg_stock = str.encode(f"STOCK {stock_price['symbol']} {stock_price['price']}")
    s_stock.send(msg_stock)  # publica o preço da ação

    system_event = {"event_type": "ALERT", "message": "High CPU Usage"}  # Evento fictício de alto uso de CPU
    msg_events = str.encode(f"EVENT {system_event['event_type']} {system_event['message']}")
    s_events.send(msg_events)  # publica o evento do sistema

    chat_message = {"user": "Alice", "message": "Hello, everyone!"}  # Mensagem de chat fictícia
    msg_chat = str.encode(f"CHAT {chat_message['user']} {chat_message['message']}")
    s_chat.send(msg_chat)  # publica a mensagem de chat
