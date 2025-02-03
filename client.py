import socket


def send_data(data):
    host = '127.0.0.1'
    port = 34191  # Use an appropriate localhost port: see https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers for known used ports

    # Specify IPv4 and TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(2)  # Avoid long waiting times if the server isn't running

    try:
        client.connect((host, port))
        client.sendall(data.encode('utf-8'))
        client.close()
        print("Data sent successfully")
    except (socket.error, socket.timeout):
        print("Server is not running")


if __name__ == '__main__':
    while True:
        data = input("Enter data to send: ")

        if data.lower() == "test":  # Test with large data
            data = str({f"key{i}": i for i in range(300)})

        send_data(data)
        print()
