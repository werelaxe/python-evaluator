from eval_server import EvalServer
from time import sleep


def main():
    server = EvalServer()
    server.eval("10000 ** 100")
    print(server.get_result("10000 ** 100"))
    sleep(3)
    print(server.get_result("10000 ** 100"))

if __name__ == '__main__':
    main()
