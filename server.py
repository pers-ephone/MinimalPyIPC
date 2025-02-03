import socket
import threading


class Server:
    host = '127.0.0.1'
    port = 34191  # Use an appropriate localhost port: see https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers for known used ports

    def __init__(self):
        # Specify IPv4 and TCP
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)  # Allow max 5 connection attempts waiting in queue

        self.running = True

        self.thread = threading.Thread(target=self.listen_for_connections, daemon=True)
        self.thread.start()

    def listen_for_connections(self):
        while self.running:
            client, _ = self.server.accept()

            # Read data
            data = b""
            chunk = client.recv(1024)  # Read up to 1024 bytes of data
            while chunk:  # Continue reading until no more data is received
                data += chunk
                chunk = client.recv(1024)

            self.process_data(data.decode())
            client.close()

    def process_data(self, data):
        print("Data received:", data)

    def stop(self):
        self.running = False
        self.server.close()


if __name__ == '__main__':
    server = Server()
    import time
    import random
    while True:
        time.sleep(1)
        print("doing stuff", random.randint(1, 100))  # main thread isn't blocked
    # input("Press Enter to stop the server...")
    # server.stop()
