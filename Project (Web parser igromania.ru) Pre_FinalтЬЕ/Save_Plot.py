from tkinter import *
from Par_mod.plotting_module import plotting_plot
from tkinter import messagebox

class Save_Plot:
    def __init__(self, parent3, width = 400, height = 400, title = 'Parsing'):
        self.root = Toplevel(parent3)
        self.root['bg'] = 'gray8'  # цвет фона
        self.root.title(title)
        self.root.geometry(f'{width}x{height}')  # размер окна

        self.plot_type = ''
        self.info_auth_sec = []

        self.frame = Frame(self.root, bg='gray8')
        self.frame1 = Frame(self.root, bg='gray8')
        self.frame2 = Frame(self.root, bg='gray8')

        self.text_path = Label(self.frame, text = 'Path:', bg='gray8', fg='white',font='Consolas, 20')
        self.path = Entry(self.frame, font='Consolas, 20')
        self.title = Label(self.frame, text = 'Tytle:', bg='gray8', fg='white', font='Consolas, 20')
        self.t = Entry(self.frame, font='Consolas, 20')
        self.x_label = Label(self.frame, text = 'X label:', bg='gray8', fg='white',font='Consolas, 20')
        self.x = Entry(self.frame, font='Consolas, 20')
        self.y_label = Label(self.frame, text = 'Y label:', bg='gray8', fg='white', font='Consolas, 20')
        self.y = Entry(self.frame, font='Consolas, 20')
        self.btn3_1 = Button(self.frame1, height=1, width=10, text='Save', bg='gray8', font='Consolas, 20',
                             command=self.save_plot)  # saving

    def draw_win_1(self):  # реализация функцийй и кнопок
        self.frame.place(relx=0, rely=0.05, relwidth=0.7, relheight=0.7)
        self.frame1.place(relx=0.51, rely=0.85, relwidth=0.7, relheight=0.7)

        self.text_path.grid(row=0, column=0)
        self.path.grid(row=0, column=1)

        self.title.grid(row=1, column=0)
        self.t.grid(row=1, column=1)

        self.x_label.grid(row=2, column=0)
        self.x.grid(row=2, column=1)

        self.y_label.grid(row=3, column=0)
        self.y.grid(row=3, column=1)

        self.btn3_1.pack()

        self.grab_focus3()

    def grab_focus3(self):
        self.root.focus_set()

    def run(self):
        self.draw_win_1()

    def save_plot(self):
        title = self.t.get()
        x_lab = self.x.get()
        y_lab = self.y.get()

        if title == '':
            title = None
        elif x_lab == '':
            x_lab = None
        elif y_lab == '':
            y_lab = None
        plotting_plot(self.info_auth_sec, self.path.get(), self.plot_type, title, x_lab, y_lab)
        messagebox.showinfo(message='Saved')

