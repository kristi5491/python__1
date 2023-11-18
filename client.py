import socket

def send_message():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    while True:
        message = input("Your message: ")
        if message.lower() == 'quit':
            break
        client.send(message.encode())

    client.close()

if __name__ == "__main__":
    send_message()