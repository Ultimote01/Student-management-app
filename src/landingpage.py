from tkinter import Frame,Canvas,Button,NW
from PIL import ImageTk, Image, ImageDraw, ImageFont
import tkinter as  tk


from .roundedButton import   createRoundedButton
from .adminlandpage import Adminlandpage
from .userlandpage import  Userlandpage
from .helper import get_points,resource_path,draw_image_in_text,rounded_image,rounded_image_with_mask





class Landingpage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller=controller
        self.canvas = Canvas(self,width=4000, height=4000,bd=0,highlightthickness=0)



        self.image_open=Image.open(resource_path("_images\\college_imagev1.jpg")).resize((1370,749))
        self.photo1 = ImageTk.PhotoImage(self.image_open)
        self.bg_image=self.canvas.create_image(0,0, image=self.photo1, anchor=NW,tags="tagi3")
        self.canvas.tag_bind(self.bg_image, "<Enter>", lambda event: self.active_rectangle(event, 'enter'))


        self.adminIconImage=Image.open(resource_path( "_images\\admin.png"))
        self.adminIcon=ImageTk.PhotoImage(self.adminIconImage)

        self.usersIconImage= Image.open( resource_path("_images\\user.png"))
        self.usersImage = ImageTk.PhotoImage(self.usersIconImage)


        createRoundedButton(self.canvas,390,500,490,530,15,0,self.active_rectangle,
                self.nonactive_rectangle,text="Admin",image=self.adminIcon,fill='#696564',outline='')


        createRoundedButton(self.canvas, 690, 500, 790, 530, 15, 1, self.active_rectangle,
            self.nonactive_rectangle, text="Users",image=self.usersImage,fill='#696564',outline='')

        font_path="\\users\\Nathan\\documents\\adrip1.ttf"
        self.logo_image = draw_image_in_text("W\n  E\n     S",font_path, font_size=100,image='',text_cord=(60,0),
            image_size=(500,500),background_color_rgba=(225,225,255,0)
        ).resize((200,180),Image.BICUBIC)

        self.logo_photo=ImageTk.PhotoImage(self.logo_image)

        """This line creates the school logo"""
        createRoundedButton(self.canvas, 480, 300, 580, 400, 20, 2, self.active_rectangle,
         self.nonactive_rectangle,width=5, text="", image=self.logo_photo, fill='white', outline='black',bind_widget=False)




        self.canvas.pack(fill='both',expand=True)

    def active_rectangle(self, event, value ):


        clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag

        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)  # Get all tags associated with the item
            if value == 'enter':

                if 's' not in tags[0]:

                    if "3" not in tags[0]:
                        self.canvas.config(cursor='hand2')
                        self.canvas.itemconfigure(tags[0].replace('i',''), fill='#695348')



                    if  "3" in tags[0]:
                        self.canvas.itemconfigure('tag0', fill='#696564')
                        self.canvas.itemconfigure('tag1', fill='#696564')


                elif 's' in tags[0]:
                    self.canvas.itemconfigure(tags[0].replace('s', ''), fill='#695348')
                    self.canvas.config(cursor='hand2')

                elif "i" in tags[0]:
                    self.canvas.config(cursor='hand2')


            elif value == 'clicked':
                if 's' not in tags[0]:
                    self.canvas.itemconfigure(tags[0].replace('i',''), fill='#b8b589')

                elif 's' in tags[0]:
                    self.canvas.itemconfigure(tags[0].replace('s', ''), fill='#b8b589')




    def nonactive_rectangle(self, event, value, ):

        clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)  # Get all tags associated with the item
            if value == 'leave':
                if 's' not in tags[0]:
                    self.canvas.config(cursor='')
                    self.canvas.itemconfigure(tags[0].replace('i',''), fill='#696564')

                elif "i" in tags[0]:
                    self.canvas.config(cursor='hand2')


            elif value == 'buttonrelease':
                if 's' not in tags[0]:
                    self.canvas.itemconfigure(tags[0].replace('i',''), fill='#696564')

                elif 's' in tags[0]:
                    self.canvas.itemconfigure(tags[0].replace('s', ''), fill='#696564')

                if "0" in tags[0]:
                    self.controller.show_frame(Adminlandpage,route='forward')
                elif "1" in tags[0]:

                    self.controller.show_frame(Userlandpage, route='forward')



    def resize_widgets(self,width,height):


        global photo
        radius=15
        width_0=(width//3)+20
        height_0=(height//2)+125

        width_1=(width//3)+170
        height_1=(height//2)+125

        image=self.image_open.resize((width,height), Image.BICUBIC)
        photo = ImageTk.PhotoImage(image)
        self.canvas.itemconfigure("tagi3", image=photo)
        self.canvas.coords("tag0",get_points(width_0,height_0,
                                             width_0+100,height_0+30,radius))
        self.canvas.coords("tags0",((width_0+(width_0+100))/2,(height_0+(height_0+30))/2))
        self.canvas.coords("tagi0", width_0+1,height_0+1)

        self.canvas.coords("tag1", get_points(width_1, height_1,
                                              width_1 + 100, height_1 + 30, radius))
        self.canvas.coords("tags1", ((width_1 + (width_1 + 100)) / 2, (height_1 + (height_1 + 30)) / 2))
        self.canvas.coords("tagi1", width_1 + 1, height_1 + 1)

        self.canvas.coords("tag2",get_points((width//3)+80,(height//2)-50,(width//3)+180,(height//2)+50,radius+5))
        self.canvas.coords("tagi2",(width//3)+80,(height//2)-50)





