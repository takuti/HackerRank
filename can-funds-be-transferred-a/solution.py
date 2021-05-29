## Use this function to write data to socket
## write_string_to_socket(connection, message) where connection is the socket object and message is string

## Use this function to read data from socket
## def read_string_from_socket(connection) where connection is the socket object

## All global declarations go here
banks = {}

## This function is called only once before any client connection is accepted by the server.
## Read any global datasets or configurations here
def init_server():
    global banks

    print "Reading training set"

    with open('training.txt') as f:
        lines = f.readlines()
        n = int(lines[0].rstrip())
        for l in lines[1:]:
            u, v = map(int, l.rstrip().split(','))
            if u not in banks:
                banks[u] = set()
            banks[u].add(v)
            if v not in banks:
                banks[v] = set()
            banks[v].add(u)

    sys.stdout.flush()



## This function is called everytime a new connection is accepted by the server.
## Service the client here
def process_client_connection(connection):

    while True:
        # read message
        message = read_string_from_socket(connection)

        if message == "END":
            write_string_to_socket(connection, "END")
            break

        a, b, q = map(int, message.rstrip().split(','))
        visited = set()
        to_visit = set([a])

        reached = False
        for _ in range(q-1):  # n-hop
            if reached:
                break

            next_hop = set()
            visited |= to_visit

            # +1 hop from the previous node
            for u in to_visit:
                if reached:
                    break
                if u not in banks:
                    continue

                # +1 hop from the current node
                for v in banks[u]:
                    if v == b:
                        reached = True
                        break
                    if v not in visited:
                        next_hop.add(v)

            to_visit = next_hop

        # write message
        write_string_to_socket(connection, "YES" if reached else "NO")
