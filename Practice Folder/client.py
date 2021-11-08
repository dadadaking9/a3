import socket


PORT = 2020
HOST = "127.0.0.1"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
	client.connect((HOST, PORT))

	print("client connected to {HOST} on {PORT}")

	while True:
		msg = input("Enter message to send: ")

		client.sendall(msg.encode('utf-8'))
		srv_msg = client.recv(4096)

		print("Response",srv_msg.decode('utf-8'))
