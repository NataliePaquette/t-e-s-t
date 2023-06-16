# import libraries
import customtkinter as ctk
from settings import *


class Panel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', pady=4, ipady=8)
        ctk.CTkEntry(self).pack(fill='x', pady=4)
