# CSCI 355/655
# Summer 2022
# Assignment 1 - Socket Programming
# Gabriel Rubio Alvarado


""" In this assignment, we will first look at IP and port addresses, and then inter-computer
communications known as socket programming. The combination of IP Address (32 bits) and Port Address (16 bits)
form the Socket Address used in socket programming. """

import socket
import sys

sys.stdout = open("Assignment_1_console.txt", "w")


def get_host_info():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    print("My computer's name is:", hostname)
    print("My computer's IP Address is", ip_addr)
    octets = ip_addr.split('.')
    ip_addr_bin = ''
    for octet in octets:
        ip_addr_bin += (("0" * 8) + bin(int(octet))[2:])[-8:]

    print("My computer's IP Address in Binary is: ", ip_addr_bin, len(ip_addr_bin))
    print("My computer's IP Address Class is: ", get_addr_class(ip_addr_bin))


def connect_to_server(host_name, port, do_receive, send_msg=None):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed with error %s" % (err))

    try:
        host_ip = socket.gethostbyname(host_name)
    except socket.gaierror:
        print("there was an error resolving the host")
        sys.exit()

    socket_add = (host_ip, port)
    s.connect(socket_add)
    print("The socket has successfully connected to", host_name, "at address", host_ip, "at", get_port_type(port),
          "port", port)

    if do_receive:
        conn = socket.create_connection(socket_add)
        if send_msg:
            conn.send(send_msg.encode())
        message = conn.recv(4096)
        print(message.decode("utf-8"))


def get_port_type(port):
    if 0 <= port < 1024:
        return "Well-Known"
    elif 1024 <= port < 49152:
        return "Registered"
    elif 49152 <= port < 65536:
        return "Dynamic"


def get_addr_class(ip_addr_bin):
    if ip_addr_bin[0:1] == '0':
        return 'A'
    elif ip_addr_bin[0:2] == '10':
        return 'B'
    elif ip_addr_bin[0:3] == '110':
        return 'C'
    elif ip_addr_bin[0:4] == '1110':
        return 'D'
    elif ip_addr_bin[0:4] == '1111':
        return 'E'


def main():
    get_host_info()
    connect_to_server('www.google.com', 80, False)
    connect_to_server('djxmmx.net', 17, True)
    connect_to_server('ut1-wwv.nist.gov', 13, True)
    connect_to_server('localhost', 12347, True)


if __name__ == "__main__":
    main()
    sys.stdout.close()
