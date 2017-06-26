import webserver


def main():
    webserver.app.run(host="0.0.0.0", port=80)


if __name__ == '__main__':
    main()

