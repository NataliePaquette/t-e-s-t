# import libraries
import customtkinter as ctk
from panels import *
from settings import *
from question_add_dq import *

def set_text(entry , text):
    entry.delete(0,ctk.END)
    entry.insert(0,text)
    return

class Menu(ctk.CTkTabview):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky='news', rowspan=2)
        self.add('Main')
        self.add('Export')
        # widgets
        self.MF = MainFrame(self.tab('Main'))
        self.EF = ExportFrame(self.tab('Export'))


class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.parent = parent
        self.pack(expand=True, fill='both')
        self.question_button = ctk.CTkButton(self, text='Add Question' , command=self.add_question_start)
        self.question_button.pack(fill='x', pady=4, padx=4)

        self.add_question_b = ctk.CTkFrame(self , fg_color=DARK_GREY)
        self.add_question_b.rowconfigure((1 , 2) , weight=1 , uniform='a')
        self.add_question_b.columnconfigure(0 , weight=1 , uniform='a')

        self.qestion_FrameButton_descriptive = ctk.CTkButton(self.add_question_b , text='Open Add Window' , command = self.open_dq)
        self.qestion_FrameButton_cancel = ctk.CTkButton(self.add_question_b , text='cancel' , command=self.add_question_canceled)
        self.qestion_FrameButton_descriptive.grid(row = 1 , column = 0 , sticky = 'news' , pady=4, padx=4)
        self.qestion_FrameButton_cancel.grid(row = 2 , column = 0 , sticky = 'news' , pady=4, padx=4 , columnspan = 2)





        self.subject_button = ctk.CTkButton(self, text='Add Subject' , command= self.add_subject_start)
        self.subject_button.pack(fill='x', pady=4, padx=4)

        self.add_subject_frame = ctk.CTkFrame(self , fg_color=DARK_GREY)
        self.LabelFrame = ctk.CTkLabel(self.add_subject_frame , text='Add New Subject')
        self.LabelFrame.pack(fill='x', pady=4, padx=4)
        
        self.ButtonFrame = ctk.CTkFrame(self.add_subject_frame , fg_color=DARK_GREY)
        self.ButtonFrame.rowconfigure(0 , weight=1 , uniform='a')
        self.ButtonFrame.columnconfigure((0 , 1) , weight=1 , uniform='a')
        

        self.FrameEntry = ctk.CTkEntry(self.add_subject_frame , justify='right')
        self.FrameButton_save = ctk.CTkButton(self.ButtonFrame , text='save' , command=self.add_subject_saved)
        self.FrameButton_cancel = ctk.CTkButton(self.ButtonFrame , text='cancel' , command=self.add_subject_canceled)

        self.FrameEntry.pack(fill='x', pady=4, padx=4)
        self.ButtonFrame.pack(fill='x', pady=4, padx=4)

        self.FrameButton_save.grid(row = 0 , column = 0 , sticky = 'news' , pady=4, padx=4)
        self.FrameButton_cancel.grid(row = 0 , column = 1 , sticky = 'news' , pady=4, padx=4)

        self.FrameEntry.configure(font = ('B yekan' , 14))
        self.FrameEntry.bind('<Control-v>' , command=lambda:self.FrameEntry.event_generate("<<Paste>>"))
        self.FrameEntry.bind('<Control-V>' , command=lambda:self.FrameEntry.event_generate("<<Paste>>"))

        self.delete_button = ctk.CTkButton(self, text='Delete' , command=self.parent.master.parent.delete_b)
        self.delete_button.pack(fill='x', pady=4, padx=4)
        self.back_button = ctk.CTkButton(self, text='back' , command=self.parent.master.parent.back_subject)
        self.back_button.pack(fill='x', pady=4, padx=4)
        self.SubjectEntry = ButtonWithEntry(self , 'Subject Name')
        self.SubjectEntry.pack(fill='x', pady=4, padx=4)
    def add_subject_start(self):
        self.add_question_canceled()
        self.subject_button.pack_forget()
        self.delete_button.pack_forget()
        self.SubjectEntry.pack_forget()
        self.back_button.pack_forget()
        self.add_subject_frame.pack(fill='x', pady=4, padx=4)
        self.delete_button.pack(fill='x', pady=4, padx=4)
        self.back_button.pack(fill='x', pady=4, padx=4)
        self.SubjectEntry.pack(fill='x', pady=4, padx=4)
    def add_subject_canceled(self):
        set_text(self.FrameEntry , '')
        self.add_subject_frame.pack_forget()
        self.delete_button.pack_forget()
        self.SubjectEntry.pack_forget()
        self.back_button.pack_forget()
        self.subject_button.pack(fill='x', pady=4, padx=4)
        self.delete_button.pack(fill='x', pady=4, padx=4)
        self.back_button.pack(fill='x', pady=4, padx=4)
        self.SubjectEntry.pack(fill='x', pady=4, padx=4)
    def add_subject_saved(self):
        self.parent.master.parent.add_subject_db(self.FrameEntry.get())
        self.add_subject_frame.pack_forget()
        self.delete_button.pack_forget()
        self.SubjectEntry.pack_forget()
        self.back_button.pack_forget()
        self.subject_button.pack(fill='x', pady=4, padx=4)
        self.delete_button.pack(fill='x', pady=4, padx=4)
        self.back_button.pack(fill='x', pady=4, padx=4)
        self.SubjectEntry.pack(fill='x', pady=4, padx=4)
        set_text(self.FrameEntry , '')
    


    def add_question_start(self):
        self.add_subject_canceled()
        self.question_button.pack_forget()
        self.subject_button.pack_forget()
        self.delete_button.pack_forget()
        self.SubjectEntry.pack_forget()
        self.back_button.pack_forget()
        self.add_question_b.pack(fill='x', pady=4, padx=4)
        self.subject_button.pack(fill='x', pady=4, padx=4)
        self.delete_button.pack(fill='x', pady=4, padx=4)
        self.back_button.pack(fill='x', pady=4, padx=4)
        self.SubjectEntry.pack(fill='x', pady=4, padx=4)

    def add_question_canceled(self):
        self.subject_button.pack_forget()
        self.add_question_b.pack_forget()
        self.delete_button.pack_forget()
        self.SubjectEntry.pack_forget()
        self.back_button.pack_forget()
        self.question_button.pack(fill='x', pady=4, padx=4)
        self.subject_button.pack(fill='x', pady=4, padx=4)
        self.delete_button.pack(fill='x', pady=4, padx=4)
        self.back_button.pack(fill='x', pady=4, padx=4)
        self.SubjectEntry.pack(fill='x', pady=4, padx=4)
    
    def open_dq(self):
        global dqw
        dqw = DQ_window(self ,'add')
        self.add_question_canceled()

        


        


class ExportFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.pack(expand=True, fill='both')
        ctk.CTkButton(self, text='Export').pack(fill='x', pady=4, padx=4)

class ButtonWithEntry(ctk.CTkFrame):
    def __init__(self , parent , text):
        super().__init__(master=parent , fg_color=DARK_GREY)
        self.parent = parent
        self.rowconfigure((0 , 1 , 2) , weight=1 , uniform='a')
        # self.var = ctk.StringVar()
        # self.var.trace('w' , lambda _ , *__ : config_text(self.FrameEntry))
        self.FrameLabel = ctk.CTkLabel(self , text=text)
        self.FrameEntry = ctk.CTkEntry(self , justify='right')
        self.FrameButton = ctk.CTkButton(self , text='save' , command=lambda : self.CSN(self.FrameEntry.get()))
        self.FrameLabel.pack(fill='x', pady=4, padx=4)
        self.FrameEntry.pack(fill='x', pady=4, padx=4)
        self.FrameButton.pack(fill='x', pady=4, padx=4)
        self.FrameEntry.configure(font = ('B yekan' , 14))
        self.FrameEntry.bind('<Control-v>' , command=lambda:self.FrameEntry.event_generate("<<Paste>>"))
        self.FrameEntry.bind('<Control-V>' , command=lambda:self.FrameEntry.event_generate("<<Paste>>"))

    def MainPage(self):
        set_text(self.FrameEntry , 'Main')
        self.FrameEntry.configure(state = 'disabled')
        self.FrameButton.configure(state = 'disabled')
        self.parent.back_button.configure(state = 'disabled')
    def AnotherPage(self , text):
        self.parent.back_button.configure(state = 'normal')
        self.FrameEntry.configure(state = 'normal')
        self.FrameButton.configure(state = 'normal')
        set_text(self.FrameEntry , text)
    def CSN(self , nn):
        self.parent.parent.master.parent.ChangeSubjectName(nn)