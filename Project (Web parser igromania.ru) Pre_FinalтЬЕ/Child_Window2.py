from tkinter import *
from Save_Plot import Save_Plot


class Win2:
    def __init__(self, parent1, width, height, title='Parsing'):
        self.root = Toplevel(parent1)
        self.root['bg'] = 'gray8'  # цвет фона
        self.root.title(title)
        self.root.geometry(f'{width}x{height}')  # размер окна

        self.info_igr = []

        self.info_author_section = []

        self.frame = Frame(self.root, bg='gray8')
        self.frame1 = Frame(self.root, bg='gray8')
        self.frame2 = Frame(self.root, bg='gray8')

        self.plot_kind = ''

        self.analyze_text = Text(self.frame2, width=20, height=10, font='Consolas 15')

        self.title = Label(self.frame, text='Plotting', font='Consolas, 20', bg='gray8', fg='white')  # текст

        self.blSt1 = BooleanVar()
        self.blSt2 = BooleanVar()
        self.blSt3 = BooleanVar()
        self.blSt4 = BooleanVar()
        self.blSt5 = BooleanVar()

        self.cb2_1 = Checkbutton(self.frame, height=1, width=10, text='Line', bg='brown4', fg='white',
                                 font='Consolas, 20', variable=self.blSt1)
        self.cb2_2 = Checkbutton(self.frame, height=1, width=10, text='Box', bg='brown4', fg='white',
                                 font='Consolas, 20', variable=self.blSt2)
        self.cb2_3 = Checkbutton(self.frame, height=1, width=10, text='Histogram', bg='brown4', fg='white',
                                 font='Consolas, 20', variable=self.blSt3)
        self.cb2_4 = Checkbutton(self.frame, height=1, width=10, text='Area', bg='brown4', fg='white',
                                 font='Consolas, 20', variable=self.blSt4)
        self.cb2_5 = Checkbutton(self.frame, height=1, width=10, text='Pie', bg='brown4', fg='white',
                                 font='Consolas, 20', variable=self.blSt5)
        self.btn2_1 = Button(self.frame1, height=1, width=10, text='Save plot', bg='brown4',
                             font='Consolas, 20', command=self.create_save_win)  # сохранение файла

    def draw_win_1(self):  # реализация функцийй и кнопок
        self.frame.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.7)
        self.frame1.place(relx=0.5, rely=0.7, relwidth=0.7, relheight=0.7)
        self.frame2.place(relx = 0, rely = 0.15, relwidth=0.7, relheight=0.7)
        self.title.pack()
        self.cb2_1.pack()
        self.cb2_2.pack()
        self.cb2_3.pack()
        self.cb2_4.pack()
        self.cb2_5.pack()
        self.btn2_1.pack()


        self.analyze_text.insert(0.0, self.info_author_section)
        self.analyze_text.pack()

        self.grab_focus2()
        #self.text_info.insert()

    def grab_focus2(self):
        self.root.focus_set()

    def run(self):
        self.draw_win_1()

    def create_save_win(self):
        btn_ind = 1
        ind = 1
        for BoolState in (self.blSt1, self.blSt2, self.blSt3, self.blSt5, self.blSt5):
            if BoolState.get():
                btn_ind = ind
            ind += 1

        if btn_ind == 1:
            self.plot_kind = 'line'
        elif btn_ind == 2:
            self.plot_kind = 'bar'
        elif btn_ind == 3:
            self.plot_kind = 'hist'
        elif btn_ind == 4:
            self.plot_kind = 'area'
        elif btn_ind == 5:
            self.plot_kind = 'pie'

        sp_win = Save_Plot(self.root)
        sp_win.plot_type = self.plot_kind
        sp_win.info_auth_sec = self.info_author_section
        sp_win.run()
