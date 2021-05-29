def read_string_from_socket(connection):
    return connection.recv(2048)


def process_client_connection(connection):

    print(connection)
    while True:
        # read message
        message = read_string_from_socket(connection)

        print "Message received = ", message
        sys.stdout.flush()

        # Your logic goes here
        # write message back to clinet
        # write_string_to_socket(connection, message)
        connection.send(message)

        if message == "END":
            break
