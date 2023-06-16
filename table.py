import customtkinter


class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, buttonText, command=None, command2=None, **kwargs):
        super().__init__(master, **kwargs)
        self.buttonText = buttonText
        self.columnconfigure(0, weight=8, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')
        self.command = command
        self.command2 = command2
        self.master = master

        self.checkBox_list = []
        self.button_list = []
        self.checkBox2_list = []
        self.names = []
        self.IDs = []
        self.itemChecked = []

    def add_item(self, itemName, itemID, itemChecked):
        checkBoxList = customtkinter.CTkCheckBox(self, text=itemName)
        checkBoxList.configure(font = ('B nazanin' , 14))
        checkBoxList2 = customtkinter.CTkCheckBox(self, text="", width=5)
        if itemChecked:
            checkBoxList2.select()
        button = customtkinter.CTkButton(self, text=self.buttonText, width=50, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(itemID))
        if self.command2 is not None:
            checkBoxList2.configure(command=lambda: self.command2(itemID))
        checkBoxList.grid(row=len(self.checkBox_list), column=0, pady=(0, 10), sticky="nsew")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=10, sticky="nsew")
        checkBoxList2.grid(row=len(self.checkBox2_list), column=2, pady=(0, 10), sticky="nsew")
        self.checkBox_list.append(checkBoxList)
        self.checkBox2_list.append(checkBoxList2)
        self.button_list.append(button)
        self.names.append(itemName)
        self.IDs.append(itemID)
        self.itemChecked.append(itemChecked)

    def remove_item(self, id):
        ind = self.IDs.index(id)
        self.checkBox2_list[ind].destroy()
        self.checkBox_list[ind].destroy()
        self.button_list[ind].destroy()
        self.checkBox_list.pop(ind)
        self.checkBox2_list.pop(ind)
        self.button_list.pop(ind)
        self.IDs.pop(ind)
        self.itemChecked.pop(ind)
        self.names.pop(ind)

    def clear(self):
        ids = self.IDs.copy()
        for id in ids:
            self.remove_item(id)

    def get_checked_items(self):
        re = []
        for i in range(len(self.checkBox_list)):
            if self.checkBox_list[i].get() == 1:
                re.append(self.IDs[i])
        return re


class ScrollableLabelButtonFrame1(customtkinter.CTkScrollableFrame):
    def __init__(self, master, buttonText, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.buttonText = buttonText
        self.columnconfigure(0, weight=8, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')
        self.command = command
        self.master = master

        self.checkBox_list = []
        self.button_list = []
        self.names = []
        self.IDs = []

    def add_item(self, itemName, itemID):
        checkBoxList = customtkinter.CTkCheckBox(self, text=itemName)
        checkBoxList.configure(font = ('B nazanin' , 14))
        button = customtkinter.CTkButton(self, text=self.buttonText, width=50, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(itemID))
        checkBoxList.grid(row=len(self.checkBox_list), column=0, pady=(0, 10), sticky="nsew")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=10, sticky="nsew")
        self.checkBox_list.append(checkBoxList)
        self.button_list.append(button)
        self.names.append(itemName)
        self.IDs.append(itemID)

    def remove_item(self, id):
        ind = self.IDs.index(id)
        self.checkBox_list[ind].destroy()
        self.button_list[ind].destroy()
        self.checkBox_list.pop(ind)
        self.button_list.pop(ind)
        self.IDs.pop(ind)
        self.names.pop(ind)

    def clear(self):
        ids = self.IDs.copy()
        for id in ids:
            self.remove_item(id)

    def get_checked_items(self):
        re = []
        for i in range(len(self.checkBox_list)):
            if self.checkBox_list[i].get() == 1:
                re.append(self.IDs[i])
        return re


class Table(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.table1 = ScrollableLabelButtonFrame(master, "Edit",
                                                 command=master.master.open_question,
                                                 command2=master.master.changeStat_Database,
                                                 label_text="Questions")
        self.table1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.table2 = ScrollableLabelButtonFrame1(master, "Open",
                                                 command=master.master.open_subject,
                                                 label_text="Subjects")
        self.table2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
