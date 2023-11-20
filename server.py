import socket
import threading     

clients = []

def show_message(message, conn):
    for client in clients:
        try:
            if(client != conn):
                client.send(message.encode())
        except:
            clients.remove(client)
            
def client_thread(conn, addr):
    print(f"Connected by {addr}")
    while True:
        message = conn.recv(1024).decode()
        if not message:
            break
        print(f"Received from {addr}: {message}")
        show_message(message, conn)
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen()
    print('server started')

    while True:
        conn, addr = server.accept()
        clients.append(conn)
        thread = threading.Thread(target=client_thread, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
    
    