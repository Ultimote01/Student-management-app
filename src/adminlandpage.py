import tkinter as tk
from PIL import Image,ImageTk
from tkinter import Frame,Canvas,Label,END,Tk,Toplevel,NW
from .createstudent import Createstudent
from .animationFunctions import display_animation
from .createTransparenting import createTransparentImage



from .globalVariables import win_bg,pwd,WIDTH,HEIGHT,getGlobalVariable
from .helper import  deny_focus,set_innerfocus,get_points,resource_path,rounded_image,hexToDecimal
from .adminpickpage import Adminpickpage
from .form import  Form




class Adminlandpage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.one = 0
        self.count = 0
        self.boelean = False
        self.admin = {}
        self.controller = controller
        self.recent_rouunded_button=''
        self.border_color="#989492"
        self.font_color="black"
        self.rounded_bg="#feaa50"
        self.button_bk_color="white"
        self.button_font_color='black'
        self.active_bt_background='#3955f6'
        self.active_bt_foreground='white'
        self.clicked_button_bg='#b8b589'
        self.clicked_button_fg = 'white'

        self.form=Form(self, bg=win_bg, highlightbackground=win_bg, highlightcolor=win_bg, bd=0)




        radius = 10
        x1, y1, x2, y2 = 40, 155, 270, 185

        r,g,b=hexToDecimal(self.rounded_bg)
        self.rounded_image=rounded_image(500,400,30,foreground=(r,g,b,100),outline_width=0)
        self.rounded_photo=ImageTk.PhotoImage(self.rounded_image)

        bk_rounded_img=self.form.canvas.create_image(1,1,image=self.rounded_photo,anchor=NW,tags='tagi0')
        self.form.canvas.tag_bind(bk_rounded_img, "<Enter>",
                                  lambda  event :self.active_rectangle(event,'enter'))


        self.form.create_rounded_rec( x1, y1, x2, y2, radius, 1, 'entry',self.active_rectangle,
                                      self.nonactive_rectangle,outline=self.border_color,fill='white')

        self.animate = ''
        self.animate_canvas = ''
        self.widget_obj = {}

        self.shadow_color1=win_bg



        self.dpCanvas = Canvas(self,  bd=0, highlightthickness=0)

        self.transparent_image_tk=createTransparentImage(607, 669,"#181a26",15)
        self.dpCanvas.create_image(0,0,anchor=tk.NW, image=self.transparent_image_tk,tags="tagi0")
        self.dpCanvas.place(x=731, y=40, width=613, height=660)


        self.form.canvas.create_text(45,60,text="ADMIN LOGIN",font='Arial 35 bold',anchor='w',tags='tagl0',
                                     fill=self.font_color)


        self.widget_obj['canvas'] = self.form.getCanvas()

        self.widget_obj['drawline'] = self.form.drawline




        self.form.canvas.create_text(45, 135, text="USERNAME", font='Arial 15 bold', anchor='w',tags='tagl1',
                                     fill=self.font_color)



        self.user_entry =self.form.createWidget('self.user_entry',"entry",bd=0,
                                                font=('Bookman-Old-Style bold', 13, ))
        self.form.childrenLayout('self.user_entry',"place",x=45, y=159)



        self.form.canvas.create_text(45, 220, text="PASSWORD", font='Arial 15 bold', anchor='w', tags='tagl2',
                                     fill=self.font_color)



        self.password_entry = self.form.createWidget("self.passoword_entry","entry", bd=0,
        font=('Bookman-Old-Style bold', 13), state="normal", show='*',bg='white')
        self.form.childrenLayout("self.passoword_entry", "place", x=45, y=239)


        self.form.create_rounded_rec( x1, 235, x2, 265, radius, 2, 'entry',
                            self.active_rectangle,self.nonactive_rectangle,outline=self.border_color,fill='white')

        self.image1 = Image.open( resource_path("_images\\eye_1.png"))
        self.resized_image1 = self.image1.resize((25, 25), Image.BICUBIC)
        self.photo1 = ImageTk.PhotoImage(self.resized_image1)


        self.show_password = self.form.createWidget('self.show_password','button', bd=0,
        image=self.photo1, width=25, height=17,command=lambda: self.show_passwordd())
        self.show_password.place(x=238, y=238)


        #retrieve password
        retrive_password=self.form.canvas.create_text(200, 280, text="Forget Password?", font='Arial 11 bold', anchor='w', tags='tagl3',
                                     fill=self.font_color)

        self.form.canvas.tag_bind(retrive_password,"<ButtonRelease-1>",
                                  lambda event : self.nonactive_rectangle(event,'buttonrelease'))

        self.form.canvas.tag_bind(retrive_password, "<Enter>",
                                  lambda event: self.active_rectangle(event, 'enter'))

        self.form.canvas.tag_bind(retrive_password, "<Leave>",
                                  lambda event: self.nonactive_rectangle(event, 'leave'))



        image = Image.open(resource_path("_images\\emoji.jpg"))
        resized_image = image.resize((320, 200), Image.BICUBIC)
        self.photo9 = ImageTk.PhotoImage(resized_image)


        # create school library image
        global prom
        imagex = Image.open(resource_path("_images\\college_image2.jpg"))
        prom = ImageTk.PhotoImage(imagex.resize((1000, 800), Image.BICUBIC))

        ani_label = Label(self, width=600, height=650, image=prom)
        ani_label.place(x=740, y=50)


        admin_access=tk.Button(self,text="Admin Access",
                    command=lambda: controller.show_frame(Adminpickpage, route='forward'), takefocus=False)
        admin_access.place(x=300, y=540)
        self.admin = {}

        def entry():
            self.password_entry.bind("<Return>", lambda event: self.submit_call())

        def on_enter(rec):

            self.show_password.configure(cursor="hand2")


        # This is to verify admin login from server side
        def verify(res_data):
            global processing_flag, show_all_student_flag

            admin = {}
            if 'done' in res_data:
                with open('server_response.json', 'r') as file:
                    admin = json.load(file)
            else:
                admin = res_data
            self.admin = admin
            if admin and self.user_entry.get() in admin:
                stored_pass, user_pass = [admin[self.user_entry.get()][2]] + [admin[self.user_entry.get()][3]], \
                    self.password_entry.get()
                admin[self.user_entry.get()][2] = self.password_entry.get().strip() if self.auth_login(stored_pass,
                                                                                                       user_pass) else ''
                if admin[self.user_entry.get()][2] == self.password_entry.get():
                    self.count = 0
                    self.widget_obj['drawline'](self.Frame_login, 'clickedout', flag=True)
                    wid = Tk.winfo_x(self.parent) + 500
                    hei = Tk.winfo_y(self.parent) + 200
                    animation_function(self, self.photo9, "!WeLCOME {}".format(admin[self.user_entry.get()][0]),
                                       controller.show_frame, 'Adminlandpage', f'320x300+{wid}+{hei}',
                                       font=('Bookman-Old-Style 17 bold'), )

                    object_dict[Createstudent].matricno.config(text='Matric No.')
                    self.user_entry.delete(0, END)
                    self.password_entry.delete(0, END)

                    self.password_entry.config(show="*")
                    self.password_entry.unbind("<Return>")
                    object_dict[Createstudent].logout_btn.place(x=1200, y=15)



                elif admin[self.user_entry.get()][1] != self.password_entry.get():
                    self.destroy_animate()
                    if self.count <= 3:
                        messagebox.showinfo("Error", "Please input correct  password")
                    elif self.count > 3 and self.count < 6:
                        if self.boelean == False:
                            messagebox.showinfo('Forgotten password?', "Do you want to reset password?\n"
                                                                       "Click on Forget password to reset password")
                        else:
                            messagebox.showinfo("Error", "Please input correct  password")
                    elif self.count == 6:
                        self.count = 0
                        self.boelean = False
                        self.back(controller)
                    self.count += 1
                else:
                    self.destroy_animate()
                    messagebox.showinfo("Error", "Please input correct Admin username and password")
            elif admin and 'connection error' in [i for i in admin.keys()]:
                self.destroy_animate()
                messagebox.showerror("Error", admin['connection error'])
            elif admin and 'error' == ''.join([i for i in admin.keys()]):
                self.destroy_animate()
                messagebox.showinfo("Error", admin['error'])
            elif admin and self.user_entry.get() not in admin:
                self.destroy_animate()
                messagebox.showinfo("Error", "Please input correct Admin username and password")

        # we create a variable of the function verify to use in other classes
        Adminlandpage.s_process = verify

        # we create a key command method
        Frame.bind(self, "<Enter>", lambda event: entry())

        self.show_password.bind("<Enter>", lambda event: on_enter(rec=None))
        # self.retrieve.bind("<Enter>", lambda event: on_enter(rec=None))

        # submit button
        self.form.create_rounded_rec( 40, 330, 110, 360, radius, 3, 'submit',
            self.active_rectangle,self.nonactive_rectangle,text='Submit',fill=self.button_bk_color,outline="",
                                      text_color=self.button_font_color,font=('Bookman-Old-Style 10 bold'))


        # # back button
        self.form.create_rounded_rec(260, 330, 330, 360, radius, 4, 'back',
        self.active_rectangle, self.nonactive_rectangle, text='Back', fill=self.button_bk_color,outline="",
                                     text_color=self.font_color, font=('Bookman-Old-Style 10 bold'))




        self.configure(background=win_bg)
        deny_focus(self.children)

    def auth_login(self, user_data, password):

        if user_data:
            stored_salt = user_data[1].encode('utf-8')
            stored_password = user_data[0].encode('utf-8')[2:]

            # Hash the entered password using the stored salt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), stored_salt)

            # Compare the computed hash with the stored hash
            if hashed_password == stored_password:
                return True  # Authentication successful
        return False  # Authentication failed
    


    def active_rectangle(self, event, value):


        clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)  # Get all tags associated with the item
            if value == 'enter':

                if 's' not in tags[0] and "i" not in tags[0] and "l" not in tags[0]:
                    self.form.getCanvas().config(cursor='hand2')
                    self.form.getCanvas().itemconfigure(tags[0], fill=self.active_bt_background)
                    self.recent_rouunded_button=tags[0]
                    self.form.getCanvas().itemconfigure(tags[0].replace(tags[0][-1], 's') + tags[0][-1],
                                                        fill=self.active_bt_foreground)



                elif 's' in tags[0]:
                    self.form.getCanvas().itemconfigure(tags[0].replace('s', ''), fill=self.active_bt_background)
                    self.form.getCanvas().itemconfigure(tags[0], fill=self.active_bt_foreground)
                    self.form.getCanvas().config(cursor='hand2')
                    self.recent_rouunded_button = tags[0].replace('s', '')

                elif 'l' in tags[0]:
                    self.form.getCanvas().config(cursor='hand2')

                if "i" in tags[0]:
                    self.form.getCanvas().itemconfigure(self.recent_rouunded_button, fill=self.button_bk_color)
                    r_e_t=self.recent_rouunded_button[-1] if self.recent_rouunded_button else '' #recent entered text
                    self.form.getCanvas().itemconfigure(self.recent_rouunded_button.replace(r_e_t, 's') + r_e_t,
                                                        fill=self.button_font_color)
                    self.form.getCanvas().config(cursor='')


            elif value == 'clicked':
                if 's' not in tags[0]:
                    self.form.getCanvas().itemconfigure(tags[0], fill=self.clicked_button_bg)
                    self.form.getCanvas().itemconfigure(tags[0][:-1]+"s"+tags[0][-1], fill=self.clicked_button_fg)

                elif 's' in tags[0]:
                    self.form.getCanvas().itemconfigure(tags[0], fill=self.clicked_button_fg)
                    self.form.getCanvas().itemconfigure(tags[0].replace('s', ''), fill=self.clicked_button_bg)



    def nonactive_rectangle(self, event, value):

        clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)  # Get all tags associated with the item
            if value == 'leave':
                if 's' not in tags[0] and "l" not in tags[0]:
                    self.form.getCanvas().config(cursor='')
                    self.form.getCanvas().itemconfigure(tags[0], fill=self.button_bk_color)
                    self.form.getCanvas().itemconfigure(tags[0].replace(tags[0][-1],'s')+tags[0][-1],
                                                        fill=self.button_font_color)
                elif "l" in tags[0]:
                    self.form.getCanvas().config(cursor='')


            elif value == 'buttonrelease':

                for i in range(3, 5):
                    self.form.getCanvas().itemconfigure(f"tag{i}", fil=self.button_bk_color)
                    self.form.getCanvas().itemconfigure(f"tags{i}", fill=self.button_font_color)

                if 's' not in tags[0] :

                    # self.submit_call()
                    self.back(self.controller)

                elif 's' in tags[0]:

                    # self.submit_call()
                    self.back(self.controller)



    def submit_call(self):
        wid = Tk.winfo_x(self.parent) + 500
        hei = Tk.winfo_y(self.parent) + 200
        self.animate = Toplevel(self.parent, screen='')
        self.animate_canvas = Canvas(self.animate, width=WIDTH, height=HEIGHT, bg="white",
                                     highlightbackground='white', bd=0)
        display_animation(self.animate, self.animate_canvas, f'400x250+{wid}+{hei}')
        async_thread = async_Thread(
            tcp_echo_client(self, '{}#u/894#{}'.format('admin login', self.user_entry.get().strip()),
                            Adminlandpage.s_process))
        async_thread.daemon = True
        async_thread.start()

    # fucnftion to reset password
    def recovery(self):

        recovery = simpledialog.askstring("Reset", 'Enter username', )

        if recovery:
            def confirm_id(res_data):
                res_adx = ''
                if 'done' in res_data:
                    with open('server_response.json', 'r') as file:
                        res_adx = json.load(file)
                else:
                    res_adx = res_data

                if recovery == list(res_adx.keys())[0]:
                    data = res_adx[list(res_adx.keys())[0]]
                    messagebox.showinfo("Success", 'Link to reset your password has been sent to email')
                    self.boelean = True
                    self.count = 3
                elif "connection error" in list(res_adx.keys()):
                    messagebox.showerror("error", res_adx[list(res_adx.keys())[0]])
                elif "error" in list(res_adx.keys()):
                    messagebox.showerror("error", res_adx[list(res_adx.keys())[0]])
                else:
                    messagebox.showerror("error", "username not found")

            async_thread = async_Thread(
                tcp_echo_client(self, '{}#u/894#{}'.format('admin login', recovery.strip()),
                                confirm_id))
            async_thread.daemon = True
            async_thread.start()

    def show_passwordd(self):

        if self.one == 0:
            self.password_entry.configure(show="")
            self.one += 1
        elif self.one == 1:
            self.password_entry.configure(show="*")
            self.one -= 1

    def backgroud_process(self):

        # this thread loads  unverified student information
        b_thread = dameon_Trhead(
            tcp_echo_client(object_dict[Adminpickpage], '{}#u/894#{}'.format('unverified_student', '0'),
                            object_dict[Adminpickpage].bk_update, new_reg=True))
        b_thread.daemon = True
        b_thread.start()

        # this thread load all students infomation from the server
        async_thread = async_Thread(
            tcp_echo_client(object_dict[ShowAllStudents], '{}#u/894#{}'.format('Showallstudents', '0'),
                            ShowAllStudents.s_process, sas_flag=True))
        async_thread.daemon = True
        async_thread.start()

    def back(self, controller):
        global object_dict
        from .landingpage import Landingpage

        self.user_entry.delete(0, END), self.password_entry.delete(0, END), self.password_entry.unbind("<Return>")
        self.password_entry.configure(show="*")

        if controller:
            controller.show_frame(Landingpage, route='backward')
            # self.widget_obj['drawline'](self.form, 'clickedout', flag=True)
            deny_focus(self.children)
            set_innerfocus(getGlobalVariable('object_dict')[Landingpage].children)

        if 'Animation' in getGlobalVariable('object_dict').keys():
            getGlobalVariable('object_dict')['Animation'].toplevel.destroy()

    def destroy_animate(self):
        try:
            self.animate.destroy()
        except:
            pass


    def resize_widgets(self,event):

        global reducer ,rounded_photo

        # print(event.widget, self.form.canvas.winfo_reqwidth())

        if event.width < 500:
            #canvas

            self.form.formLayout('place', x=(event.width // 5) - 74, y=120, width=event.width-10,
                                 height=400)
            self.rounded_image=self.rounded_image.resize((event.width-20,400),Image.BICUBIC)
            rounded_photo = ImageTk.PhotoImage(self.rounded_image)

            self.form.canvas.itemconfigure('tagi0',
                                    image=rounded_photo)

            if event.width <375:
                self.rounded_image = self.rounded_image.resize((event.width , 400), Image.BICUBIC)
                rounded_photo = ImageTk.PhotoImage(self.rounded_image)

                self.form.canvas.itemconfigure('tagi0',
                                               image=rounded_photo)



        else :
            self.rounded_image = self.rounded_image.resize((500, 400), Image.BICUBIC)
            rounded_photo = ImageTk.PhotoImage(self.rounded_image)

            self.form.canvas.itemconfigure('tagi0',
                                           image=rounded_photo)
            self.form.formLayout('place', x=(event.width // 5) - 74, y=120, width=500, height=400)
            self.dpCanvas.place(x=731, y=40, width=613, height=660)



    def light_mode(self):
        self.border_color = "#989492"
        self.font_color = "black"
        self.button_bk_color = "white"
        self.button_font_color = 'black'
        self.active_bt_background = '#3955f6'
        self.active_bt_foreground = 'white'

    def handle_canvas_event(self,event):
        print(event.width)


reducer=0

