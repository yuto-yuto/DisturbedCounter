import os


class FileIO:
    __filename = os.path.dirname(__file__) + "/history.csv"

    def write(self, content):
        with open(FileIO.__filename, mode="a") as fs:
            fs.write(content)

    def read_history(self):
        with open(FileIO.__filename) as fs:
            return fs.readlines()

