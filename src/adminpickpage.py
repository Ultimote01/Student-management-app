from tkinter import  Frame,Button,Canvas,NW




from .globalVariables import win_bg,pwd,WIDTH,HEIGHT,getGlobalVariable
from .helper import  deny_focus,set_innerfocus,get_points
from  .sidebar import Sidebar
from .header import Header
from .main_body import  Main
from .createstudent import Createstudent
from .createTransparenting import createTransparentImage

class Adminpickpage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.text_widget = ''
        self.top_level_flag = False
        self.new_reg_info = []
        self.grid_rowconfigure(0, weight=1, uniform=True)
        self.grid_columnconfigure(0, weight=1, uniform=True)

        self.top_layer_frame=Frame(self,width=300,height=400,bg='yellow')
        self.top_layer_frame.grid(row=0,column=0,sticky='nw')


        #lower_layer_frame holds the grid layout
        self.lower_layer_frame=Frame(self, height=600,width=1200)
        self.lower_layer_frame.grid(row=0, rowspan=5, column=0, columnspan=3, sticky='nsew')

        self.lower_layer_frame.grid_rowconfigure(1, weight=1, uniform=True)
        self.lower_layer_frame.grid_columnconfigure(1, weight=1, uniform=True)





        self.header=Header(self.lower_layer_frame,height=30,bd=0)
        self.header.grid(row=0,column=1,sticky='nsew',padx=1,pady=2)

        self.header.canvas.create_rectangle(10, 10, 20, 20, fill="orange", tags="rectangle", outline='orange')
        self.header.canvas.bind("<Configure>", self.resize_canvas_objects)

        self.main_body=Main(self.lower_layer_frame, bg=win_bg,bd=0)
        self.main_body.grid(row=1,column=1,sticky='nsew',padx=2,pady=1)

        self.dashboard_page = Frame(self.main_body, height=200, bg='blue')
        self.dashboard_page.grid(row=0,column=1,sticky='nsew',padx=2,pady=1)

        self.createstudent_page=Frame(self.main_body,width=300,height=200, bg='red')
        self.createstudent_page.grid(row=0,column=1,sticky='nsew',padx=2,pady=1)

        self.editstudent_page = Frame(self.main_body, width=300, height=200, bg='yellow')
        self.editstudent_page.grid(row=0,column=1,sticky='nsew',padx=2,pady=1)

        self.showallstudent_page = Frame(self.main_body, width=300, height=200, bg='grey')
        self.showallstudent_page.grid(row=0,column=1,sticky='nsew',padx=2,pady=1)

        self.sidebar = Sidebar(self.lower_layer_frame,self, bg='yellow', width=250, bd=0)
        self.sidebar.grid(row=0, rowspan=2, column=0, sticky="nsew", pady=2)

        # self.main_body.show_frame(self.dashboard_page)




        self.shadow_color1 = win_bg
        self.list = []



        self.show_frame(self.lower_layer_frame)
        self.configure(bg='white')

        def on_enter(rec):
            self.back_btn.configure(bg='#b08454')

        def on_leave(rec):
            self.back_btn.configure(bg='#3a3939')

        def on_canvas_click(event):
            if not isinstance(event, str):
                clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
                for item_id in clicked_items:
                    tags = event.widget.gettags(item_id)  # Get all tags associated with the item
                    xem = tags[0] if 's' not in tags[0] else ''
                    self.notify_btn_canvas.itemconfigure(xem, fill='#b08454')
                    self.widgets_canvas.itemconfigure(xem, fill='#b08454')

                    if 's' in tags[0]:
                        # create activefill for buttons when text is clicked
                        tag = tags[0].replace('s', '')
                        self.notify_btn_canvas.itemconfigure(tag, fill='#b08454')
                        self.widgets_canvas.itemconfigure(tag, fill='#b08454')




    def resize_canvas_objects(self, event):
        # we'll make the rectangle 1/2 the height of the canvas, with
        # a 10 pixel border

        canvas = event.widget


        x0, y0 = (10, 10)
        x1, y1 = (event.width - 10, event.height // 2)
        canvas.coords("rectangle", x0, y0, x1, y1)
        canvas.configure(scrollregion=canvas.bbox("all"))



    def show_frame(self,page):
         page.tkraise()
