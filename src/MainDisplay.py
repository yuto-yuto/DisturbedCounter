import sys
import tkinter
import tkinter.scrolledtext
import datetime


class MainDisplay:

    def __init__(self):
        width = 300
        height = 200
        self.__historyList = list()
        self.window = tkinter.Tk()
        self.window.title("Disturbed Counter")
        self.window.geometry(f"{width}x{height}")

    def start(self):
        self.__add_disturbed_button()
        self.__add_history_display_area()
        self.window.mainloop()

    def __add_disturbed_button(self):
        topFrame = tkinter.Frame(self.window)
        topFrame.pack()

        button = tkinter.Button(topFrame, text = u"Being disturbed")
        button.bind("<Button-1>", self.__register)
        button.pack(side = tkinter.TOP, pady = 20)

    def __add_history_display_area(self):
        bottomFrame = tkinter.LabelFrame(self.window, text = "History", bd = 2, relief = tkinter.SUNKEN)
        bottomFrame.pack(expand = 1, fill = tkinter.BOTH, padx = 10)

        self.__history = tkinter.scrolledtext.ScrolledText(master = bottomFrame)
        self.__history.pack(padx = 10)

    def __register(self, event):
        now = datetime.datetime.now()
        self.__historyList.insert(0, now)
        self.__history.insert("1.0", str(now) + "\n")

disp = MainDisplay()
disp.start()
