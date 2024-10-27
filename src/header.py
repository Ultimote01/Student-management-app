from tkinter import Frame,Canvas

class Header(Frame):

    def __init__(self,parent,**kwargs):
        Frame.__init__(self,parent)
        self.canvas = Canvas(self, bd=0, bg='white', height=70, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.configure(cnf=kwargs)
