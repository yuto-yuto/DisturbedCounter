import tkinter as tk
from tkinter import ttk
from datetime import *


class MainDisplay(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        width = 400
        height = 200

        self.title("Disturbed Counter")
        self.geometry(f"{width}x{height}")
        self.minsize(width = width, height = height)

        self.__add_button()
        self.__add_history_display_area()

    def __add_button(self):
        topFrame = tk.Frame(self)
        topFrame.pack()

        self.disturbed_button = tk.Button(topFrame, height = 2, text = u"Being disturbed",
                                          command = lambda: [self.__add_task_entry(),
                                                             self.__button_style_update(self.disturbed_button)])
        self.disturbed_button.pack(side = tk.LEFT, padx = 10, pady = 10)

        self.not_disturbed_button = tk.Button(topFrame, height = 2, text = u"Not being disturbed",
                                              state = tk.DISABLED,
                                              command = lambda: [self.__finish_task(),
                                                                 self.__button_style_update(
                                                                     self.not_disturbed_button)])
        self.not_disturbed_button.pack(side = tk.LEFT, padx = 10)

    def __add_history_display_area(self):
        bottomFrame = tk.LabelFrame(self, text = "History")
        bottomFrame.pack(expand = 1, fill = tk.BOTH)

        self.__tree_view = ttk.Treeview(bottomFrame, height = 2)
        self.__tree_view["columns"] = ("No", "Start", "End")

        self.__tree_view.heading("No", text = "No")
        self.__tree_view.heading("Start", text = "Start")
        self.__tree_view.heading("End", text = "End")

        self.__tree_view.column("No", width = 30)
        self.__tree_view.column("Start", width = 185)
        self.__tree_view.column("End", width = 185)

        self.__tree_view["show"] = "headings"
        self.__tree_view.pack(expand = 1, fill = tk.BOTH)

        scrollbar = ttk.Scrollbar(self.__tree_view, orient = "vertical", command = self.__tree_view.yview)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        self.__tree_view.configure(yscrollcommand = scrollbar.set)

    def __add_task_entry(self):
        entry_number = len(self.__tree_view.get_children()) + 1
        self.__last_entry = (entry_number, datetime.now(), "")
        self.__last_id = self.__tree_view.insert("", 0, values = self.__last_entry)

    def __finish_task(self):
        self.__tree_view.set(self.__last_id, "End", datetime.now())

    def __button_style_update(self, button: tk.Button):
        if button["text"] == "Being disturbed":
            self.disturbed_button.configure(state = tk.DISABLED)
            self.not_disturbed_button.configure(state = tk.NORMAL)
        else:
            self.disturbed_button.configure(state = tk.NORMAL)
            self.not_disturbed_button.configure(state = tk.DISABLED)
