# import libraries
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from settings import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

class Menu(ctk.CTkTabview):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.parent = parent
        self.grid(row=0, column=0, sticky='news', rowspan=2)
        self.add('Main')
        self.add('Images')
        # widgets
        self.main_menu = MainMenu(self.tab('Main'))
        self.img_menu = ImageMenu(self.tab('Images'))
        

class DQ_window(ctk.CTkToplevel):
    def __init__(self ,parent, mode , uid = ''):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('800x500')
        self.title('Add descriptive question')
        self.minsize(800, 500)
        self.start_tm()
        self.uid = uid
        self.parent = parent
        self.mode = mode
        self.tmp_db = {
            'title' : '',
            'text' : '',
            'answer' : '',
            'img' : '',
            'answer_img' : '',
            'select' : False
        }
        

        # layout
        self.rowconfigure(0, weight=1, uniform='a')
        self.columnconfigure(0, weight=3, uniform='a')
        self.columnconfigure(1, weight=7, uniform='a')
        # menu
        self.image_menu = Menu(self)
        self.main_menu = TextInputs(self)
        # edit
        if self.mode == 'edit':
            uid_db = self.parent.get_db(self.uid)

            self.tmp_db['title'] = uid_db['title']
            self.main_menu.set_name_text(self.tmp_db['title'])

            self.tmp_db['text'] = uid_db['text']
            self.main_menu.set_text_text(self.tmp_db['text'])

            self.tmp_db['answer'] = uid_db['answer']
            self.main_menu.set_answer_text(self.tmp_db['answer'])

            self.tmp_db['img'] = uid_db['img']
            if self.tmp_db['img']:
                self.image_menu.img_menu.e_qi(self.tmp_db['img'])

            self.tmp_db['answer_img'] = uid_db['answer_img']
            if self.tmp_db['answer_img']:
                self.image_menu.img_menu.e_ai(self.tmp_db['answer_img'])
            
            self.tmp_db['select'] = uid_db['select']
            self.image_menu.main_menu.select_set(self.tmp_db['select'])
    def stop(self):
        self.destroy()
    def save(self):
        self.tmp_db['select'] = self.image_menu.main_menu.check_select.get()
        self.main_menu.save_things()
        if self.mode == 'edit':
            if not('~EEDB' in self.tmp_db['img']) and self.tmp_db['img']:
                self.tmp_db['img'] = self.parent.copy_file(self.tmp_db['img'])
            if not('~EEDB' in self.tmp_db['answer_img']) and self.tmp_db['answer_img']:
                self.tmp_db['answer_img'] = self.parent.copy_file(self.tmp_db['answer_img'])
            if self.mode == 'add':
                self.parent.add_d_question_db(self.tmp_db['title'] , self.tmp_db['text'] , self.tmp_db['answer'] , self.tmp_db['img'] , self.tmp_db['answer_img'] , self.tmp_db['select'])
            else :
                self.parent.change_d_question_db(self.tmp_db['title'] , self.tmp_db['text'] , self.tmp_db['answer'] , self.tmp_db['img'] , self.tmp_db['answer_img'] , self.tmp_db['select'] , self.uid)
        else:
            if not('~EEDB' in self.tmp_db['img']) and self.tmp_db['img']:
                self.tmp_db['img'] = self.parent.parent.master.parent.copy_file(self.tmp_db['img'])
            if not('~EEDB' in self.tmp_db['answer_img']) and self.tmp_db['answer_img']:
                self.tmp_db['answer_img'] = self.parent.parent.master.parent.copy_file(self.tmp_db['answer_img'])
            if self.mode == 'add':
                self.parent.parent.master.parent.add_d_question_db(self.tmp_db['title'] , self.tmp_db['text'] , self.tmp_db['answer'] , self.tmp_db['img'] , self.tmp_db['answer_img'] , self.tmp_db['select'])
            else :
                self.parent.parent.master.parent.change_d_question_db(self.tmp_db['title'] , self.tmp_db['text'] , self.tmp_db['answer'] , self.tmp_db['img'] , self.tmp_db['answer_img'] , self.tmp_db['select'] , self.uid)
        self.stop()
    def stop_tm(self):
        self.attributes('-topmost' , False)
    def start_tm(self):
        self.attributes('-topmost' , True)


class ImageMenu(ctk.CTkFrame):
    def __init__(self , parent):
        super().__init__(master=parent , fg_color='transparent')
        self.parent = parent
        self.pack(expand=True, fill='both')
        self.img_frame = ctk.CTkFrame(self , fg_color=DARK_GREY)
        self.img_frame.pack(fill='x', pady=4, padx=4)
        self.img_label = ctk.CTkLabel(self.img_frame , text='Nothing is here')
        self.img_label.pack(fill='x', pady=4, padx=4)
        self.open_question_image = ctk.CTkButton(self.img_frame, text='Select question image' , command=self.qi)
        self.open_question_image.pack(fill='x', pady=4, padx=4)
        self.delete_img_img = ctk.CTkButton(self.img_frame , text='Delete' , command=self.qid)
        self.open_img_img = ctk.CTkButton(self.img_frame , text='Open' , command= self.open_qi)

        self.ans_frame = ctk.CTkFrame(self , fg_color=DARK_GREY)
        self.ans_frame.pack(fill='x', pady=4, padx=4)
        self.ans_label = ctk.CTkLabel(self.ans_frame , text='Nothing is here')
        self.ans_label.pack(fill='x', pady=4, padx=4)
        self.open_answer_image = ctk.CTkButton(self.ans_frame, text='Select answer image' , command=self.ai)
        self.open_answer_image.pack(fill='x', pady=4, padx=4)
        self.delete_ans_img = ctk.CTkButton(self.ans_frame , text='Delete' , command=self.aid)
        self.open_ans_img = ctk.CTkButton(self.ans_frame , text='Open' , command=self.open_ai)
    def qi(self):
        self.parent.master.parent.stop_tm()
        img = filedialog.askopenfile(mode='r' , filetypes=[('PNG Image Files' , '*.png') , ('JPG Image Files' , '*.jpg')])
        try : 
            self.parent.master.parent.tmp_db['img'] = img.name
            self.img_label.configure(text = img.name.split('/')[-1])
            self.delete_img_img.pack(fill='x', pady=4, padx=4)
            self.open_img_img.pack(fill='x', pady=4, padx=4)
        except : 
            messagebox.showwarning('Select Image' , "You didn't select any image!")
        self.parent.master.parent.start_tm()
    def ai(self):
        self.parent.master.parent.stop_tm()
        img = filedialog.askopenfile(mode='r' , filetypes=[('PNG Image Files' , '*.png') , ('JPG Image Files' , '*.jpg')])
        try : 
            self.parent.master.parent.tmp_db['answer_img'] = img.name
            self.ans_label.configure(text = img.name.split('/')[-1])
            self.delete_ans_img.pack(fill='x', pady=4, padx=4)
            self.open_ans_img.pack(fill='x', pady=4, padx=4)
        except : 
            messagebox.showwarning('Select Image' , "You didn't select any image!")
        self.parent.master.parent.start_tm()
    def qid(self):
        self.parent.master.parent.tmp_db['img'] = ''
        self.img_label.configure(text = 'Nothing is here')
        self.delete_img_img.pack_forget()
        self.open_img_img.pack_forget()
    def aid(self):
        self.parent.master.parent.tmp_db['answer_img'] = ''
        self.ans_label.configure(text = 'Nothing is here')
        self.delete_ans_img.pack_forget()
        self.open_ans_img.pack_forget()
    # edit_funcs
    def e_qi(self , path):
        img = path
        self.parent.master.parent.tmp_db['img'] = img
        self.img_label.configure(text = img.split('/')[-1].split('\\')[-1])
        self.delete_img_img.pack(fill='x', pady=4, padx=4)
        self.open_img_img.pack(fill='x', pady=4, padx=4)

    def e_ai(self , path):
        img = path
        self.parent.master.parent.tmp_db['answer_img'] = img
        self.ans_label.configure(text = img.split('/')[-1].split('\\')[-1])
        self.delete_ans_img.pack(fill='x', pady=4, padx=4)
        self.open_ans_img.pack(fill='x', pady=4, padx=4)
    
    def open_qi(self):
        Image.open(self.parent.master.parent.tmp_db['img']).show()
    def open_ai(self):
        Image.open(self.parent.master.parent.tmp_db['answer_img']).show()


class MainMenu(ctk.CTkFrame):
    def __init__(self , parent):
        super().__init__(master=parent , fg_color='transparent')
        self.parent = parent
        self.pack(expand=True, fill='both')
        self.selection_var = ctk.BooleanVar()
        self.check_select = ctk.CTkCheckBox(self , text='select' , onvalue=True , offvalue=False , variable=self.selection_var)
        self.check_select.pack(fill='x', pady=4, padx=4)
        self.open_question_image = ctk.CTkButton(self, text='Save' , command= self.parent.master.parent.save)
        self.open_question_image.pack(fill='x', pady=4, padx=4)
        self.open_answer_image = ctk.CTkButton(self, text='Cancel' , command=self.parent.master.parent.stop)
        self.open_answer_image.pack(fill='x', pady=4, padx=4)

    def select_set(self , thing : bool):
        self.selection_var.set(value=thing)

class TextInputs(ctk.CTkFrame):
    def __init__(self , parent):
        super().__init__(master=parent , fg_color='transparent')
        self.parent = parent
        self.columnconfigure((0 , 1) , weight=1 , uniform='a')
        self.rowconfigure(0 , weight=1 , uniform='a')
        self.rowconfigure(1 , weight=6 , uniform='a')
        # name

        self.name_frame = ctk.CTkFrame(self , fg_color=DARK_GREY)
        self.name_frame.columnconfigure(0 , weight=3 , uniform='a')
        self.name_frame.columnconfigure(1 , weight=7 , uniform='a')
        self.name_frame.rowconfigure(0 , weight=1 , uniform='a')
        self.name_frame_label = ctk.CTkLabel(self.name_frame , text='Question name')
        self.name_frame_box = ctk.CTkEntry(self.name_frame)
        self.name_frame_box.configure(font = ('B yekan' , 14))
        self.name_frame_box.bind('<Control-v>' , command=lambda:self.name_frame_box.event_generate("<<Paste>>"))
        self.name_frame_box.bind('<Control-V>' , command=lambda:self.name_frame_box.event_generate("<<Paste>>"))
        self.name_frame_label.grid(row=0, column=0, sticky="nsew" , padx = 5)
        self.name_frame_box.grid(row=0, column=1, sticky="nsew" , padx = 5 , pady = 5)
        self.name_frame.grid(column = 0 , row = 0 , sticky="nsew" , padx = 5 , pady = 5 , columnspan = 2)

        # text

        self.text_frame = ctk.CTkFrame(self , fg_color=DARK_GREY)
        self.text_frame.rowconfigure(0 , weight=1 , uniform='a')
        self.text_frame.rowconfigure(1 , weight=9 , uniform='a')
        self.text_frame.columnconfigure(0 , weight=1 , uniform='a')
        self.text_frame_label = ctk.CTkLabel(self.text_frame , text='Question text')
        self.text_frame_box = ctk.CTkTextbox(self.text_frame)
        self.text_frame_box.configure(font = ('B yekan' , 14))
        self.text_frame_box.bind('<Control-v>' , command=lambda:self.text_frame_box.event_generate("<<Paste>>"))
        self.text_frame_box.bind('<Control-V>' , command=lambda:self.text_frame_box.event_generate("<<Paste>>"))
        self.text_frame_label.grid(row=0, column=0, sticky="nsew" , padx = 5)
        self.text_frame_box.grid(row=1, column=0, sticky="nsew" , padx = 5 , pady = 5)
        self.text_frame.grid(column = 0 , row = 1 , sticky="nsew" , padx = 5 , pady = 5)



        # ans
        self.answer_frame = ctk.CTkFrame(self , fg_color=DARK_GREY)
        self.answer_frame.rowconfigure(0 , weight=1 , uniform='a')
        self.answer_frame.rowconfigure(1 , weight=9 , uniform='a')
        self.answer_frame.columnconfigure(0 , weight=1 , uniform='a')
        self.answer_frame_label = ctk.CTkLabel(self.answer_frame , text='Answer text')
        self.answer_frame_box = ctk.CTkTextbox(self.answer_frame)
        self.answer_frame_box.configure(font = ('B yekan' , 14))
        self.answer_frame_box.bind('<Control-v>' , command=lambda:self.answer_frame_box.event_generate("<<Paste>>"))
        self.answer_frame_box.bind('<Control-V>' , command=lambda:self.answer_frame_box.event_generate("<<Paste>>"))
        self.answer_frame_label.grid(row=0, column=0, sticky="nsew" , padx = 5)
        self.answer_frame_box.grid(row=1, column=0, sticky="nsew" , padx = 5 , pady = 5)
        self.answer_frame.grid(column = 1 , row = 1 , sticky="nsew" , padx = 5 , pady = 5)

        self.grid(row=0, column=1, sticky="nsew" , padx = 5)

    def save_things(self):
        self.parent.tmp_db['title'] = self.name_frame_box.get()
        self.parent.tmp_db['text'] = self.text_frame_box.get('1.0' , ctk.END)
        self.parent.tmp_db['answer'] = self.answer_frame_box.get('1.0' , ctk.END)
    
    def set_name_text(self , text):
        self.name_frame_box.delete(0,ctk.END)
        self.name_frame_box.insert(0,text)
    def set_text_text(self , text):
        self.text_frame_box.delete('1.0',ctk.END)
        self.text_frame_box.insert('1.0',text)
    def set_answer_text(self , text):
        self.answer_frame_box.delete('1.0',ctk.END)
        self.answer_frame_box.insert('1.0',text)
