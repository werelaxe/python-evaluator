from concurrent.futures import ProcessPoolExecutor
import resource


MAX_PROCESSES_COUNT = 256
MEMORY_LIMIT_IN_MEGABYTES = 60
MEMORY_LIMIT_IN_BYTES = MEMORY_LIMIT_IN_MEGABYTES * 1024 * 1024


def smart_eval(expression):
    resource.setrlimit(resource.RLIMIT_AS, (MEMORY_LIMIT_IN_BYTES,) * 2)
    try:
        return eval(expression)
    except Exception:
        return BaseException


class EvalServer:
    def __init__(self):
        self._database = {}
        self._client_handler = ProcessPoolExecutor(MAX_PROCESSES_COUNT)

    def eval(self, expression):
        if expression not in self._database:
            future_object = self._client_handler.submit(smart_eval, expression)
            self._database[expression] = future_object

    def get_result(self, expression):
        if self._database[expression].done():
            return self._database[expression].result()

    def __str__(self):
        attrs = filter(lambda x: "__" not in x, dir(self))
        return "\n".join("{} = {}".format(attr, getattr(self, attr)) for attr in attrs)

    def database(self):
        return self._database
