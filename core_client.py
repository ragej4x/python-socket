    # Receive data from the server
    data = receive_data_from_server()
    
    def receive_data_from_server():
      # Set up the socket
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.bind(("localhost", 8000))
      sock.listen(1)
      conn, addr = sock.accept()

      # Receive data
      data = conn.recv(1024)  # receive up to 1024 bytes

      # Close the connection
      conn.close()

      return data
