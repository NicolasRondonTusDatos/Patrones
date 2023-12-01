class Rq:
    def get_queue(self):
        return  5

rq = Rq()
class QueueSingleton:
    __instance = None
    __queue = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(QueueSingleton, cls).__new__(cls)
            cls.__queue = rq.get_queue()
        return cls.__instance

    @property
    def queue(self):
        return self.__queue

s = QueueSingleton()
d = QueueSingleton()
print(id(s), id(d))

class Example:
    ...

s = Example()
d = Example()
print(id(s), id(d))