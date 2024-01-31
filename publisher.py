import zmq, time
from constPS import * #-

context = zmq.Context()
s_combined = context.socket(zmq.PUB)    # cria um único socket de publicador combinado
p_combined = "tcp://0.0.0.0:" + PORT    # como e onde comunicar
s_combined.bind(p_combined)              # associa o socket ao endereço

while True:
    time.sleep(5)                        # aguarda 5 segundos

    msg_time = str.encode("TIME " + time.asctime())
    s_combined.send(msg_time)  # publica o horário atual

    stock_price = {"symbol": "XYZ", "price": 50.0}  
    msg_stock = str.encode(f"STOCK {stock_price['symbol']} {stock_price['price']}")
    s_combined.send(msg_stock)  # publica o preço da ação

    system_event = {"event_type": "ALERT", "message": "High CPU Usage"}  
    msg_events = str.encode(f"EVENT {system_event['event_type']} {system_event['message']}")
    s_combined.send(msg_events)  # publica o evento do sistema

    chat_message = {"user": "Alice", "message": "Hello, everyone!"}  
    msg_chat = str.encode(f"CHAT {chat_message['user']} {chat_message['message']}")
    s_combined.send(msg_chat)  # publica a mensagem de chat
