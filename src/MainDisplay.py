import sys
import tkinter
import tkinter.scrolledtext
import datetime
from src.FileIO import FileIO


class MainDisplay:

    def __init__(self):
        self.__io = FileIO()
        width = 300
        height = 200
        self.__historyList = list()
        self.window = tkinter.Tk()
        self.window.title("Disturbed Counter")
        self.window.geometry(f"{width}x{height}")

    def start(self):
        self.__add_button()
        self.__add_history_display_area()
        self.window.mainloop()

    def __add_button(self):
        topFrame = tkinter.Frame(self.window)
        topFrame.pack()

        self.disturbed_button = tkinter.Button(topFrame, height = 2, text = u"Being disturbed",
                                               command = lambda : [self.__register(), self.__button_style_update(self.disturbed_button)])
        self.disturbed_button.pack(side = tkinter.LEFT, padx = 10, pady = 10)

        self.not_disturbed_button = tkinter.Button(topFrame, height = 2, text = u"Not being disturbed", state = tkinter.DISABLED,
                                                   command = lambda : [self.__register(), self.__button_style_update(self.not_disturbed_button)])
        self.not_disturbed_button.pack(side = tkinter.LEFT, padx = 10)

    def __add_history_display_area(self):
        bottomFrame = tkinter.LabelFrame(self.window, text = "History")
        bottomFrame.pack(expand = 1, fill = tkinter.BOTH, padx = 10)

        self.__scrolled_text = tkinter.scrolledtext.ScrolledText(master = bottomFrame)
        self.__scrolled_text.pack()

    def __register(self):
        now = datetime.datetime.now()
        text = str(now) + "\n"
        self.__io.write(text)
        self.__scrolled_text.insert("1.0", text)

    def __button_style_update(self, button: tkinter.Button):
        if button["text"] == "Being disturbed":
            self.disturbed_button.configure(state = tkinter.DISABLED)
            self.not_disturbed_button.configure(state = tkinter.NORMAL)
        else:
            self.disturbed_button.configure(state = tkinter.NORMAL)
            self.not_disturbed_button.configure(state = tkinter.DISABLED)
        self.window.update()


disp = MainDisplay()
disp.start()
