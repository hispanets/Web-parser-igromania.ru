from tkinter import *
import Par_mod.save_to_csv as stc
from tkinter import messagebox

# save data

class Download:
    def __init__(self, parent3, width, height, title = 'Parsing'):
        self.root = Toplevel(parent3)
        self.root['bg'] = 'gray8'  # цвет фона
        self.root.title(title)
        self.root.geometry(f'{width}x{height}')  # размер окна

        self.item_lst = []

        self.frame = Frame(self.root, bg='gray8')
        self.frame1 = Frame(self.root, bg='gray8')

        self.title = Label(self.frame, text='Choose a save path', font='Consolas, 20', bg='gray8', fg='white')  # текст
        self.save = Entry(self.frame, font='Consolas, 20')  # ввод url
        self.btn3_1 = Button(self.frame1, height=1, width=10, text='Save', font='Consolas, 20', bg='gray8',
                             fg='white', command=self.save_info)  # saving

    def draw_win_1(self):  # реализация функцийй и кнопок
        self.frame.place(relx=0.15, rely=0.25, relwidth=0.7, relheight=0.7)
        self.frame1.place(relx=0.51, rely=0.85, relwidth=0.7, relheight=0.7)
        self.title.pack()
        self.save.pack()
        self.btn3_1.pack()

        self.grab_focus3()

    def grab_focus3(self):
        self.root.focus_set()

    def run(self):
        self.draw_win_1()

    def save_info(self):
        stc.save_file(self.item_lst, self.save.get())
        messagebox.showinfo(message='Saved')
