# Brandon CHan
# chanbz@uci.edu
# 12383908
import socket
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
  HOST = server
  PORT = port

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((server, port))
    
  pass



