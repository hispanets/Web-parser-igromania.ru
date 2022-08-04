from tkinter import *
from Child_Window1 import Win1
from tkinter import messagebox
import Par_mod.parse_page as pp
import Par_mod.save_to_csv as stc

class Win:
    def __init__(self, width, height, title='Parsing'):
        self.root = Tk()
        self.root['bg'] = 'gray8'  # цвет фона
        self.root.title(title)
        self.root.geometry(f'{width}x{height}')  # размер окна

        self.igr_info = []

        self.frame = Frame(self.root, bg='gray8')

        self.title = Label(self.frame, text='Enter URL', font='Consolas, 20', bg='gray8', fg='white')  # текст
        self.text = Label(self.frame, text='Parsing...', font='Consolas, 20', bg='gray8', fg='white')
        self.url = Entry(self.frame, font='Consolas, 20')  # ввод url
        self.lbl_num_page = Label(self.frame, text='Enter number of pages for parsing:', font='Consola 20',\
                                  fg='white', bg='gray8')
        self.entr_num_page = Entry(self.frame, font='Consola 20')

        self.btn1 = Button(self.frame, height=1, width=10, text='Parsing', bg='brown4', font='Consolas, 20', \
                           command=self.create_child1)  # кнопка для перехода в следующее окно

    def draw_win(self):     # реализация функцийй и кнопок
        self.frame.place(relx=0.15, rely=0.25, relwidth=0.7, relheight=0.7)
        self.title.pack()
        self.url.pack()
        self.lbl_num_page.pack()
        self.entr_num_page.pack()
        self.btn1.pack(expand=1)

    def run(self):      # запуск стартового окна
        self.draw_win()
        self.root.mainloop()

    # Creating first window
    def create_child1(self, width=500, height=300, title='Parsing'):
        link = self.url.get()

        Flag = True
        try:
            num_page = int(self.entr_num_page.get())
            link.index('igromania.ru')
            link.index('www.')
            link.index('https://')

            if link.find('hard') == -1 and link.find('news') == -1 and link.find('articles') == -1 \
                    and link.find('kino') == -1 and link.find('videos') == -1:
                Flag = False
        except ValueError:
            messagebox.showerror('Error', 'Please, enter correct URl')
            Flag = False

        if Flag:
            self.igr_info = pp.parse(link, num_page)
            stc.save_file(self.igr_info, 'Files/igromania_data.csv')

            win1 = Win1(self.root, width, height, title)
            win1.info_lst = self.igr_info
            win1.run()
        else:
            messagebox.showerror('Error', 'Invalid section of web page')

