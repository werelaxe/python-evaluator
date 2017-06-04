from concurrent.futures import ProcessPoolExecutor
from string import ascii_letters

ASCII_LETTERS = set(ascii_letters)


def secure_eval(expression):
    if set(expression).intersection(ASCII_LETTERS):
        return "abort"
    try:
        return eval(expression)
    except Exception:
        return "abort"


class EvalServer:
    def __init__(self):
        self._database = {}
        self._client_handler = ProcessPoolExecutor(256)

    def eval(self, expression):
        if expression not in self._database:
            self._database[expression] = self._client_handler.submit(secure_eval, expression)

    def get_result(self, expression):
        if self._database[expression].done():
            return self._database[expression].result()
