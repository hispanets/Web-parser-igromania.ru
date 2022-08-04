from tkinter import *
from Child_Window2 import Win2
from Download_window import Download
import Par_mod.analyzing_data as ad
import Window


class Win1:
    def __init__(self, parent, width, height, title='Parsing'):
        self.root = Toplevel(parent)
        self.root['bg'] = 'gray8'  # цвет фона
        self.root.title(title)
        self.root.geometry(f'{width}x{height}')  # размер окна

        self.info_lst = []
        self.frame = Frame(self.root, bg='gray8')
        self.frame1 = Frame(self.root, bg='gray8')
        self.frame2 = Frame(self.root, bg='gray8')

        self.title = Label(self.frame, text='Analyse data by', font='Consolas, 20', bg='gray8', fg='white')  # текст
        self.btn_Section = Button(self.frame, height=1, width=10, text='Section',
                                  font='Consolas, 20', command=self.create_child_with_section_data)  # 1 вариант чекбокса
        self.btn_Author = Button(self.frame, height=1, width=10, text='Author',
                                 font='Consolas, 20', command=self.create_child_with_author_data)  # 2 варианта чекбокса
        """self.btn_ShowStat = Button(self.frame1, height=1, width=10, text='Show statistic', bg='brown4',
                                   font='Consolas, 20', command=self.create_child2)  # открытие 3 окна"""
        self.btn_SaveData = Button(self.frame2, height=1, width=10, text='Save data', bg='brown4',
                                   font='Consolas, 20', command=self.create_download)  # сохранение файла

    def draw_win_1(self):  # реализация функцийй и кнопок
        self.frame.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.7)
        #self.frame1.place(relx=0.5, rely=0.7, relwidth=0.7, relheight=0.7)
        self.frame2.place(relx=0, rely=0.27, relwidth=0.7, relheight=0.7)
        self.title.pack()
        self.btn_Section.pack()
        self.btn_Author.pack()
        #self.btn_ShowStat.pack()
        self.btn_SaveData.pack()

        self.grab_focus1()

    def grab_focus1(self):
        self.root.focus_set()
        # self.root.wait_window()

    def create_child_with_author_data(self, width=500, height=500, title='Parsing'):    # создание второго дочернего окна
        # print(self.info_lst)
        info = ad.analyze_by_author('Files/igromania_data.csv')
        win2 = Win2(self.root, width, height, title)
        win2.info_igr = self.info_lst
        win2.info_author_section = info
        win2.run()

    def create_child_with_section_data(self, width=500, height=500, title='Parsing'):
        info = ad.analyze_by_section('Files/igromania_data.csv')
        win2 = Win2(self.root, width, height, title)
        win2.info_igr = self.info_lst
        win2.info_author_section = info
        win2.run()

    def create_download(self, width=500, height=500, title='Saving'):    # создание второго дочернего окна
        download_win = Download(self.root, width, height, title)
        download_win.item_lst = self.info_lst
        download_win.run()

    def run(self):
        self.draw_win_1()
