from .TaskEntry import TaskEntry


class DisturbedCounter:
    def __init__(self):
        self.__is_started = False
        self.entries = list(TaskEntry)

    @property
    def count(self):
        return len(self.entries)

    def register_start_time(self):
        if self.__is_started == True:
            raise Exception("register_start_time has already been called.")
        self.__is_started = True

        self.__newEntry = TaskEntry()
        self.__newEntry.start_task()
        self.entries.append(self.__newEntry)

    def register_end_time(self):
        if self.__is_started == False:
            raise Exception("register_end_time is called before calling register_start_time.")
        self.__is_started = False
        self.__newEntry.complete_task()

