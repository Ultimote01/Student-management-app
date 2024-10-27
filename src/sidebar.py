from tkinter import Frame,Canvas,NW,CURRENT
from PIL import  ImageTk


from .globalVariables import win_bg
from .helper import rounded_image_with_mask,rounded_image
from .roundedButton import createRoundedButton



class Sidebar(Frame):

    def __init__(self,parent,adminpickpage,**kwargs):
        Frame.__init__(self,parent)
        self.adminpickpage=adminpickpage
        self.canvas=Canvas(self,bg=win_bg,width=250,bd=0,highlightthickness=0)
        self.canvas.pack(fill='both',expand=True)
        self.profile_image=rounded_image_with_mask(200,200,120,
                            "_images\\user_avatar_male.jpg",)

        self.background_image=rounded_image(241,330,10,outline_width=0,
                                             foreground=(255,255,255,240))

        self.profile_photo=ImageTk.PhotoImage(self.profile_image)
        self.background_photo=ImageTk.PhotoImage(self.background_image)

        self.canvas.create_image(5, 5, image=self.background_photo, anchor=NW, tag="tagz0")



        self.canvas.create_oval(15,10,221.8,215,width=5,tags='tago1',outline='#3d4eb0')
        self.canvas.create_image(18,12.5,image=self.profile_photo,anchor=NW,tag="tagi1")

        self.admin='Nathaniel Anyebo'.upper()
        self.position="Lecturer".upper()

        self.canvas.create_text(15,260,text=f"USERNAME:   {self.admin}",font='Bookman-Old-Style 10 bold',
                                anchor="w")

        self.canvas.create_text(15, 285, text=f"POSITION:   {self.position}", font='Bookman-Old-Style 8 bold',
                                anchor="w")

        self.canvas.create_text(15.5, 302, text="Ratings", font='Bookman-Old-Style 7 bold',
                                anchor="w")


        self.canvas.bind("<Enter>",lambda event :self.active_rectangle(event,'canvas'))

        for i in range(5):
            self.canvas.create_text(60+(i*15), 308, text="* ", font='Bookman-Old-Style 17 bold',
                                anchor="w",fill="grey",tags=f"tagRating{i}")

        self.button_color='#f6f4f4'
        self.button_outline='#fefefe'
        self.button_bk_color = '#f6f4f4'
        self.button_font_color = 'black'
        self.active_bt_background = '#3955f6'
        self.active_bt_foreground = 'white'
        self.clicked_button_bg = '#b8b589'
        self.clicked_button_fg = 'white'


        createRoundedButton(self.canvas, 12,414,241,454,9,2,self.active_rectangle,
        self.nonactive_rectangle,'Dashboard',fill=self.button_bk_color,text_color=self.button_font_color,text_coordX=(16+60),
        font='Bookman-Old-Style 15 bold',outline=self.button_outline)

        createRoundedButton(self.canvas, 12, 464, 241, 504, 9, 3, self.active_rectangle,
        self.nonactive_rectangle, 'Createstudent', fill=self.button_bk_color, text_color=self.button_font_color,
        text_coordX=(16 + 75),font='Bookman-Old-Style 15 bold', outline=self.button_outline)

        createRoundedButton(self.canvas, 12, 514, 241, 554, 9, 4, self.active_rectangle,
        self.nonactive_rectangle, 'Editstudent', fill=self.button_bk_color, text_color=self.button_font_color,
        text_coordX=(16 + 60), font='Bookman-Old-Style 15 bold', outline=self.button_outline)

        createRoundedButton(self.canvas, 12, 564, 241, 604, 9, 5, self.active_rectangle,
        self.nonactive_rectangle, 'Showallstudent', fill=self.button_bk_color, text_color=self.button_font_color,
        text_coordX=(16 + 75), font='Bookman-Old-Style 15 bold', outline=self.button_outline)


        self.configure(cnf=kwargs)


    def render_sidebar(self,event):

        if event.width < 600 :
            self.grid_forget()

        elif event.width > 600:

            self.grid(row=0,rowspan=2,column=0,sticky="nsew",pady=2)




    def active_rectangle(self, event, value):

        clicked_items = event.widget.find_withtag(CURRENT)  # Get item IDs associated with the clicked tag
        for i in range(2, 6):
            self.canvas.itemconfigure(f"tag{i}", fil=self.button_bk_color)
            self.canvas.itemconfigure(f"tags{i}", fill=self.button_font_color)

        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)  # Get all tags associated with the item
            if value == 'enter':
                if 's' not in tags[0] and "i" not in tags[0] and "l" not in tags[0]:
                    self.canvas.config(cursor='hand2')
                    self.canvas.itemconfigure(tags[0], fill=self.active_bt_background)
                    self.canvas.itemconfigure(tags[0].replace(tags[0][-1], 's') + tags[0][-1],
                                                        fill=self.active_bt_foreground)




                elif 's' in tags[0]:
                    self.canvas.itemconfigure(tags[0].replace('s', ''), fill=self.active_bt_background)
                    self.canvas.itemconfigure(tags[0], fill=self.active_bt_foreground)
                    self.canvas.config(cursor='hand2')


            elif value == 'clicked':
                if 's' not in tags[0]:
                    self.canvas.itemconfigure(tags[0], fill=self.clicked_button_bg)
                    self.canvas.itemconfigure(tags[0][:-1]+"s"+tags[0][-1], fill=self.clicked_button_fg)


                elif 's' in tags[0]:
                    self.canvas.itemconfigure(tags[0], fill=self.clicked_button_fg)
                    self.canvas.itemconfigure(tags[0].replace('s', ''), fill=self.clicked_button_bg)



    def nonactive_rectangle(self, event, value):

        clicked_items = event.widget.find_withtag(CURRENT)  # Get item IDs associated with the clicked tag
        for i in range(2, 6):
            self.canvas.itemconfigure(f"tag{i}", fil=self.button_bk_color)
            self.canvas.itemconfigure(f"tags{i}", fill=self.button_font_color)

        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)  # Get all tags associated with the item
            if value == 'leave':
                if 's' not in tags[0] and "l" not in tags[0]:
                    self.canvas.config(cursor='')
                    self.canvas.itemconfigure(tags[0], fill=self.button_bk_color)
                    self.canvas.itemconfigure(tags[0].replace(tags[0][-1], 's') + tags[0][-1],
                                                        fill=self.button_font_color)
                elif "l" in tags[0]:
                    self.canvas.config(cursor='')


            elif value == 'buttonrelease':

                if 's' not in tags[0]:
                    self.canvas.itemconfigure(tags[0], fill=self.active_bt_background)
                    self.canvas.itemconfigure(tags[0][:-1] + "s" + tags[0][-1], fill=self.active_bt_foreground)

                elif 's' in tags[0]:
                    self.canvas.itemconfigure(tags[0], fill=self.active_bt_foreground)
                    self.canvas.itemconfigure(tags[0].replace('s', ''), fill=self.active_bt_background)


                if str(2) in tags[0]:
                    print(self.adminpickpage)
                    self.adminpickpage.main_body.show_frame(self.adminpickpage.dashboard_page)





