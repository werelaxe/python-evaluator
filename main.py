from concurrent.futures import ProcessPoolExecutor
import webserver
import flag_server


def main():
    with ProcessPoolExecutor(2) as task_handler:
        task_handler.submit(flag_server.start_flag_server, 1234)
        task_handler.submit(webserver.start_web_server)


if __name__ == '__main__':
    main()

