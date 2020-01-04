import datetime


class TaskEntry:
    def __init__(self):
        self.__start_time
        self.__end_time

    @property
    def start_time(self):
        return self.__start_time

    @property
    def end_time(self):
        return self.__end_time

    def start_task(self):
        if self.__end_time != None:
            raise Exception("start_task cannot be called after calling complete_task.")
        self.__start_time = datetime.datetime.now()

    def complete_task(self):
        if self.__start_time == None:
            raise Exception("complete_task cannot be called before calling start_task.")
        self.__end_time = datetime.datetime.now()