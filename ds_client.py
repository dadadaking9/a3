# Brandon CHan
# chanbz@uci.edu
# 12383908
import socket
import json
import ds_protocol
def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  HOST = '168.235.86.101'
  PORT = 3021
  message = None # In the case no message is passed through, don't send a post
  
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client: # client is using ipv4 and is TCP [sockstream]
    client.connect((HOST, PORT)) # Connect to the server

    send = client.makefile('w') # Write the info
    recv = client.makefile('r') # Read the info

    print("client connected to {HOST} on {PORT}")
    send.write(ds_protocol.join(username, password) + '\r\n')
    send.flush()
    srv_msg = recv.readline()
    server_response = json.loads(srv_msg)
    token = server_response['response']['token']
    print("Response:", srv_msg,) #DELETE | This tells us the server's response
    send.write(ds_protocol.post(token, message) + '\r\n') # This might break if 
    send.flush()
    srv_msg = recv.readline()
    server_response = json.loads(srv_msg)
    print(server_response)


#send('168.235.86.101', 3021, 'dadadaking9', 'adgjl123', 'hello fellow suffering students', 'crying compsci student')

