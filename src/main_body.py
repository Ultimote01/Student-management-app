from tkinter import Frame


class Main(Frame):

    def __init__(self,parent,**kwargs):

        Frame.__init__(self,parent)

        self.configure(cnf=kwargs)



    def show_frame(self,page):
        page.tkraise()