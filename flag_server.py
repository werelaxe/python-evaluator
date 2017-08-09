import socket
from ipaddress import IPv4Address
from subprocess import check_output

BUFFER_SIZE = 10240


def start_flag_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as process_socket:
        process_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        process_socket.bind(("localhost", port))
        while True:
            data, addr = process_socket.recvfrom(BUFFER_SIZE)
            if IPv4Address(addr[0]).is_loopback:
                data = check_output("./gen_flag")
            else:
                data = b"It is a private server. Not for evil hackers!"
            process_socket.sendto(data, addr)
