from tkinter import Frame, Button, Canvas, NW

from .globalVariables import win_bg, pwd, WIDTH, HEIGHT, getGlobalVariable
from .helper import deny_focus, set_innerfocus, get_points
from .sidebar import Sidebar
from .header import Header
from .main_body import Main
from .createTransparenting import createTransparentImage


class Adminpickpage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.text_widget = ''
        self.top_level_flag = False
        self.new_reg_info = []

        self.grid_rowconfigure(1, weight=1, uniform=True)
        self.grid_columnconfigure(1, weight=1, uniform=True)

        self.sidebar = Sidebar(self, bg='yellow', width=250, bd=0)
        self.sidebar.grid(row=0, rowspan=2, column=0, sticky="nsew", pady=2)

        self.header = Header(self, height=30, bd=0)
        self.header.grid(row=0, column=1, sticky='nsew', padx=1, pady=2)
        self.canvas = Canvas(self.header, bd=0, bg=win_bg, height=70, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_rectangle(10, 10, 20, 20, fill="orange", tags="rectangle", outline='orange')
        self.canvas.bind("<Configure>", self.resize_canvas_objects)

        self.main_body = Main(self, bg='red', bd=0)
        self.main_body.grid(row=1, column=1, sticky='nsew', padx=2, pady=1)

        self.shadow_color1 = win_bg
        self.list = []

        #
        # for i in range(5):
        #     self.button = Button(self.canvas, text=str(i), bd=1)
        #
        #
        #     self.list.append(i)
        #     self.button.grid(row=0, column=i, sticky='ew', padx=1)
        #
        # self.canvas.grid_columnconfigure(tuple(self.list), weight=1, uniform=True)
        # self.canvas.grid_rowconfigure(tuple(self.list), weight=1, uniform=True)
        #

        # self.frame.grid_columnconfigure(2, weight=1, uniform=True)

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

