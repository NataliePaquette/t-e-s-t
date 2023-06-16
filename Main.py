# import libraries
import customtkinter as ctk
from menu import *
from table import Table
import json
import os
import shutil

## Json
# save program data into json file
def save():
    global data_base
    with open(db_path , "w") as file:
        json.dump(data_base , file)
    import_data_base()

# set data base dict
data_base = {"data" : {'MAIN' : {'kids' : []}},
             "uid" : 0}
## make DB folder
# Get the current directory
current_directory = os.getcwd()

# Define the name of the new folder
new_folder_name = "~EEDB"

# Join the current directory path with the new folder name
new_folder_path = os.path.join(current_directory, new_folder_name)

# Check if the folder already exists
if not os.path.exists(new_folder_path):
    # Create the new folder
    os.mkdir(new_folder_path)
db_path = f"{new_folder_path}/DataBase.json"

# check if json file is empty
with open(db_path , "a+") as file:
    file.seek(0)
    if (len(file.readlines()) == 0):
        json.dump(data_base , file)

# import data from json file
def import_data_base():
    global data_base
    with open(db_path) as file:
        data_base = json.load(file)
import_data_base()
save()
# id generator
def make_uid(mode):
    return_var = f"{mode}-{data_base['uid']}"
    data_base['uid'] += 1
    save()
    return return_var




# App
class App(ctk.CTk):
    def __init__(self):
        # setup
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('ExamEase')
        self.minsize(800, 500)

        # layout
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=9, uniform='a')
        self.columnconfigure(0, weight=2, uniform='a')
        self.columnconfigure(1, weight=8, uniform='a')

        self._menu_ = Menu(self)


        # widgets
        frame = ctk.CTkFrame(self)
        frame.grid(row=1, column=1, sticky="nsew" , padx = 5)
        frame.rowconfigure(0, weight=1, uniform='a')
        frame.columnconfigure(0, weight=1, uniform='a')
        frame.columnconfigure(1, weight=1, uniform='a')
        self._table_ = Table(frame)

        # path
        self.path_label = ctk.CTkLabel(self , text='Loading')
        self.path_label.grid(row=0, column=1, sticky="nsew" , padx = 5)

        # main
        self.online = 'MAIN'
        self.path = 'MAIN'
        self.path_label.configure(text = self.path)
        self._menu_.MF.SubjectEntry.MainPage()
        self.reload()
        

        # run
        self.mainloop()

    # functions
    def reload(self):
        id = self.online
        self._table_.table1.clear()
        self._table_.table2.clear()
        for i in data_base['data'][id]['kids']:
            if i.split('-')[0] == 's':
                self._table_.table2.add_item(data_base['data'][i]['title'] , i)
            elif i.split('-')[0] == 'dq':
                self._table_.table1.add_item(data_base['data'][i]['title'] , i , data_base['data'][i]['select'])
    def open_subject(self, id):
        self._menu_.MF.SubjectEntry.AnotherPage(data_base['data'][id]['title'])
        self.online = id
        self.path += f"/{data_base['data'][id]['title']}"
        self.path_label.configure(text = self.path)
        self.reload()
    def back_subject(self):
        temp = self.path.split('/')
        self.online = data_base['data'][self.online]['parent']
        if self.online == 'MAIN':
            self.online = 'MAIN'
            self.path = 'MAIN'
            self.path_label.configure(text = self.path)
            self._menu_.MF.SubjectEntry.MainPage()
        else:
            self._menu_.MF.SubjectEntry.AnotherPage(data_base['data'][self.online]['title'])
            self.path = ""
            for i in temp[:-1]:
                self.path += f"/{i}"
            self.path_label.configure(text = self.path)
        self.reload()
    def open_question(self, id):
        global dqw
        dqw = DQ_window(self ,'edit' , id)

    def changeStat_Database(self, id):
        data_base['data'][id]['select'] = not(data_base['data'][id]['select'])

    
    def ChangeSubjectName(self , new_name):
        data_base['data'][self.online]['title'] = new_name
        save()
        self.reload()
        
    def add_subject_db(self , name):
        uid = make_uid('s')
        data_base['data'][self.online]['kids'].append(uid)
        data_base['data'][uid] = {
            'title' : name,
            'parent' : self.online,
            'kids' : []
        }
        save()
        self.reload()

    def add_d_question_db(self , name , text , ans , Q_img , ANS_img , select : bool):
        uid = make_uid('dq')
        data_base['data'][self.online]['kids'].append(uid)
        data_base['data'][uid] = {
            'title' : name,
            'text' : text,
            'answer' : ans,
            'img' : Q_img,
            'answer_img' : ANS_img,
            'select' : select,
            'parent' : self.online
        }
        save()
        self.reload()
    def change_d_question_db(self , name , text , ans , Q_img , ANS_img , select : bool , uid):
        if '~EEDB' in data_base['data'][uid]['img'] and data_base['data'][uid]['img'] != Q_img:
            self.delete_file(data_base['data'][uid]['img'])
        if '~EEDB' in data_base['data'][uid]['answer_img'] and data_base['data'][uid]['answer_img'] != ANS_img:
            self.delete_file(data_base['data'][uid]['answer_img'])
        data_base['data'][uid] = {
            'title' : name,
            'text' : text,
            'answer' : ans,
            'img' : Q_img,
            'answer_img' : ANS_img,
            'select' : select
        }
        save()
        self.reload()
    
    def delete_db(self , uid , kk = False):
        data_base['data'].pop(uid , None)
        if not(kk):
            data_base['data'][self.online]['kids'].remove(uid)
        save()
    def delete_b(self , kill_kids = False , id = None):
        if not(kill_kids):
            items = self._table_.table1.get_checked_items() + self._table_.table2.get_checked_items()
        else:
            items = data_base['data'][id]['kids']
        for i in items:
            if i.split('-')[0] == 's':
                self.delete_b(True , i)
            self.delete_db(i , kill_kids)
        self.reload()
    def get_db(self , uid):
        return data_base['data'][uid]
    def copy_file(self ,from_path):
        global new_folder_path
        uid = make_uid('img')
        # Specify the source file and destination path
        source_file = from_path
        destination_path = new_folder_path
        new_file_name = uid + '.' + source_file.split('.')[-1]

        # Construct the new file path with the desired name
        new_file_copy_path = os.path.join(destination_path, new_file_name)

        # Use shutil.copy() to copy the file with the new name
        shutil.copy(source_file, new_file_copy_path)
        return new_file_copy_path
    def delete_file(self , path):
        # Specify the path to the file you want to delete
        file_path = path
        # Check if the file exists
        if os.path.exists(file_path):
            # Delete the file
            os.remove(file_path)
app = App()
