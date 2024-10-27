from tkinter import *


class Userlandpage(Frame):
    s_process=''
    student={}
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.count = 0
        self.one = 0
        self.boelean = False
        self.controller=controller
        self.animate = ''
        self.animate_canvas = ''
        self.parent=parent
        self.Frame_login = Canvas(self, bg=win_bg, highlightbackground=win_bg, highlightcolor=win_bg, bd=0)
        self.Frame_login.place(x=200, y=120, width=500, height=400)
        radius = 10
        x1, y1, x2, y2 = 40, 155, 270, 185
        self.create_rounded_rec(self.Frame_login, 1, 1, 500, 400, 70, 0, 'rectangle')
        self.create_rounded_rec(self.Frame_login, x1, y1, x2, y2, radius, 1, 'entry')

        heading = Label(self.Frame_login, text="USER LOGIN", font='Arial 35 bold')
        heading.place(x=40, y=30)
        heading.configure(foreground='black',background='#d0c5c1')

        user = Label(self.Frame_login, text="Username", font='Bookman-Old-Style 15 bold')
        user.place(x=40, y=110)
        user.configure(foreground='black', background='#d0c5c1')

        self.user_entry = Entry(self.Frame_login, bd=0, font=('Bookman-Old-Style bold',14))
        self.user_entry.place(x=45, y=158)

        password = Label(self.Frame_login, text="password", font='Bookman-Old-Style 15 bold')
        password.place(x=40, y=200)
        password.configure(foreground='black',background='#d0c5c1')

        self.password_entry = Entry(self.Frame_login, bd=0, font=('Bookman-Old-Style bold',13),state="normal",show='*')
        self.password_entry.configure(bg='white')
        self.password_entry.place(x=45, y=240)
        self.create_rounded_rec(self.Frame_login, x1, 235, x2, 265, radius, 2, 'entry')

        self.image1 = Image.open(pwd+"eye_1.png")
        self.resized_image1 = self.image1.resize((25, 17), Image.BICUBIC)
        self.photo1 = ImageTk.PhotoImage(self.resized_image1)

        self.show_password = Button(self.Frame_login, bd=0, image=self.photo1, width=25, height=21,
                                    command=lambda: self.show_passwordd1())
        self.show_password.place(x=238, y=238)
        self.repo = Button(self.Frame_login , text='Forget password?',fg='black',bg='#d0c5c1',background='#d0c5c1',
                              font=('Bookman-Old-Style bold', 14),border=0,command= lambda : self.recovery())
        self.repo.place(x=225, y=279)

        #enroll_label=ttk.Label(self,text='Not a student?\nClick the botton below to register.',font='Times 17 bold',
        #                       background=win_bg)
        #enroll_label.place(x=1000,y=25)
        #enrool_btn=ttk.Button(self,text='REGISTER', command= lambda : self.create_profile(controller))
        #enrool_btn.place(x=1000,y=80)

        #global bg_img
        #imagex = Image.open(pwd+ "college_image2.jpg")
        #bg_img = ImageTk.PhotoImage(imagex.resize((1000, 1000), Image.BICUBIC))

        #ani_label = Label(self, width=600, height=650, image=prom)
        #ani_label.place(x=740, y=50)

        self.student=''
        self.user=''
        self.contro=controller

        def entry():
            self.password_entry.bind("<Return>", lambda event: self.submit_call())


        def on_enter(rec):

            self.show_password.configure(cursor="hand2")
            self.repo.configure(cursor="hand2")


        def login(res_data):
            if 'done' in res_data:
                with open('server_response.json', 'r') as file:
                    student = json.load(file)
            else:
                student= res_data

            self.student=student
            Userlandpage.student=student

            self.user = self.user_entry.get()
            self.password = self.password_entry.get()
            if self.user in student:
                if student[self.user][2] == self.password:
                    if student[self.user][12] == 'True':
                        if student[self.user][18] != '0:0':
                            self.count = 0
                            if self.animate:
                                self.animate.destroy()
                            self.top_level()
                        elif student[self.user][18] == '0:0':
                            messagebox.showinfo('', "Session Expired.")
                    elif student[self.user][12] == 'False':
                        messagebox.showinfo("Error", "Login denied.")
                    elif not student[self.user][12]:
                        messagebox.showinfo("Pending", "Registration in progress.")
                elif student[self.user][2] != self.password:
                    if self.count < 3:
                        messagebox.showinfo("Error", "Please input correct  password")
                    elif self.count > 3 and self.count < 6:
                        if self.boelean == False:
                            x = messagebox.askquestion('Forgotten password?', "Do you want to reset password?")
                            if x == 'yes':
                                recover = self.recovery()
                                if recover == int(self.user_entry.get()):
                                    self.boelean= True
                                    self.count = 3
                        else:
                            messagebox.showinfo('Error', "Please input correct password")
                    elif self.count == 6:
                        self.count = 0
                        self.boelean=False
                        self.back(controller)
                    self.count += 1

            elif student and 'connection error' in [i for i in student.keys()]:
                messagebox.showinfo("Error", student['connection error'])

            elif student and 'error' == ''.join([i for i in student.keys()]):
                 messagebox.showinfo("Error", student['error'])

            elif student and self.user_entry.get() not in student:
                messagebox.showinfo("Error", "Please input correct  username and password")

        Userlandpage.s_process=login
        Frame.bind(self, "<Enter>", lambda event: entry())
        self.repo.bind("<Enter>", lambda event: on_enter(rec=None))
        self.show_password.bind("<Enter>", lambda event: on_enter(rec=None))

        # submit button
        self.create_rounded_rec(self.Frame_login, 40, 310, 110, 350, radius, 3, 'submit', text='Submit')


        # Back button
        self.Frame_login1 = Canvas(self, bg=win_bg, highlightbackground=win_bg, highlightcolor=win_bg)
        self.Frame_login1.place(x=220, y=560, width=100, height=50)
        self.create_rounded_rec(self.Frame_login1, 3, 2, 70, 35, radius + 6, 4, 'back', text='Back')

        self.configure(background=win_bg)
        deny_focus(self.children)

    def create_profile(self,controller):
        global voucher_pass
        res=messagebox.askquestion('Registration','To register you need a voucher Number\nIf you don\'t have one yet,'
        'click \'No\' to requset for a voucher number  otherwise click \'Yes\'')
        if res == 'yes':
            res1=simpledialog.askinteger("Validate voucher", 'Enter voucher pin')

            if str(res1)[:3] == '527':
                voucher_pass=str(res1)
                object_dict[Createstudent].matricno.config(text='Voucher No')
                object_dict[Createstudent].logout_btn.place(x=1200,y=-100)
                controller.show_frame(Createstudent,'forward')
            elif res1 and str(res1)[:3] != '527':
                messagebox.showerror('error','Pin is incorrect.')
            else:
                pass
        else:
            pass

    def top_level(self):
        self.password_entry.unbind("<Return>")
        text="You have five Question to answer in each course,each question has 10 marks.\n" \
             "   The options will be displayed beneath the questions.\n      Choose your answers correctly.\n Time:2hrs Goodluck.."
        self.pop_up=Toplevel(self)
        self.pop_up.overrideredirect(True)
        self.pop_up.geometry("750x500+300+70")
        self.pop_up.focus()
        frame=Frame(self.pop_up,bg='lightgrey')
        frame.pack(fill='both',expand=True)
        heading=Label(self.pop_up,text="WELCOME!!!\n\n{}   {}".format(self.student[self.user][0],self.student[self.user][1]),
                      fg='black',font='Arial 20 bold',bg='lightgrey')
        heading1=Label(self.pop_up,text=text,fg='red',bg='lightgrey',font='Bookman-Old-Style 16 normal')
        heading.place(x=250,y=20)
        heading1.place(x=5, y=150)
        back_btn=Button(frame,text='LOGOUT',command=self.back1,cursor='hand2')
        proceed=Button(frame,text='PROCEED',command=self.access,cursor='hand2')
        back_btn.place(x=120,y=400)
        proceed.place(x=460,y=400)
        back_btn.bind("<Enter>", lambda event: on_enter({'usertlback_btn':back_btn}))
        proceed.bind("<Enter>", lambda event: on_enter({'usertlproceed':proceed}))
        back_btn.bind("<Leave>", lambda event: on_leave({'usertlback_btn':back_btn}))
        proceed.bind("<Leave>", lambda event: on_leave({'usertlproceed':proceed}))
        self.pop_up.bind("<Return>",lambda event:self.access())
        self.pop_up.grab_set()


    def access(self):
        global matricno,exam_no,exam_no1,total_score

        self.pop_up.grab_release()
        self.pop_up.destroy()
        matricno=self.user
        exam_no1 = 0
        exam_no = 0
        total_score=0
        def session_timer():
            global current_seconds, current_minute, matricno, session_time_flag, permit
            if not session_time_flag:
                matricno = ''.join(self.student.keys())
                time = self.student[self.user][18].split(':')
                if int(time[1]) == 0:
                    if int(time[0]) > 0:
                        current_minute = int(time[0]) - 1
                else:
                    current_minute = int(time[0])
                current_seconds = 60 if int(time[1]) == 0 else int(time[1])
                session_time_flag = True
                permit = False
            #session_time()

        if 'Science' in self.student[self.user]:
            self.contro.show_frame(Sciencepickpage, self.user)
            if int(self.student[self.user][13]) == 0:
                object_dict[Sciencepickpage].math_btn.config(state='normal')
            elif int(self.student[self.user][13]) > 0:
                object_dict[Sciencepickpage].math_btn.config(state='disabled')
            if int(self.student[self.user][14]) == 0:
                object_dict[Sciencepickpage].english_btn.config(state='normal')
            elif int(self.student[self.user][14]) > 0:
                object_dict[Sciencepickpage].english_btn.config(state='disabled')
            self.exam_processor('math')
            self.exam_processor('english')

            session_timer()
        elif 'Commerce' in self.student[self.user]:
            self.contro.show_frame(Commpickpage, self.user)
            if int(self.student[self.user][13]) == 0:
                object_dict[Commpickpage].math_btn.config(state='normal')
            elif int(self.student[self.user][13]) > 0:
                object_dict[Commpickpage].math_btn.config(state='disabled')
            if int(self.student[self.user][14]) == 0:
                object_dict[Commpickpage].english_btn.config(state='normal')
            elif int(self.student[self.user][14]) > 0:
                object_dict[Commpickpage].english_btn.config(state='disabled')
            self.exam_processor('math')
            self.exam_processor('english')

            session_timer()
        elif 'Art' in self.student[self.user]:
            self.contro.show_frame(Artpickpage, self.user)
            if int(self.student[self.user][13]) == 0:
                object_dict[Artpickpage].math_btn.config(state='normal')
            elif int(self.student[self.user][13]) > 0:
                object_dict[Artpickpage].math_btn.config(state='disabled')
            if int(self.student[self.user][14]) == 0:
                object_dict[Artpickpage].english_btn.config(state='normal')
            elif int(self.student[self.user][14]) > 0:
                object_dict[Artpickpage].english_btn.config(state='disabled')
            self.exam_processor('math')
            self.exam_processor('english')

            session_timer()

        self.user_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.password_entry.unbind("<Return>")
        self.password_entry.configure(show="*")
        self.password_entry.bind("<Return>", lambda event: self.submit_call())
    def exam_processor(self,filex):
        global exam_json

        if filex == 'math':
             exam_json1 = {}
             if filex == 'math':
                 with open(f'{filex}_questions.json', 'r') as file:
                     files = json.load(file)

                     # code ensures that each student answers questions
                     # this code will be implemented at the server side
                 exam_json['math_quest'] = {i: files['Questions'][i] for i, j in
                                            zip(files['Questions'], range(len(files['Questions']))) if j < 5}
                 exam_json['math_opt'] = {i: files['Options'][i] for i, j in
                                          zip(files['Options'], range(len(files['Options']))) if j < 5}
                 exam_json['math_ans'] = {i: files['Ans'][i] for i, j in
                                          zip(files['Ans'], range(len(files['Ans']))) if j < 5}

                 exam_json1['math_quest'] = {i: files['Questions'][i] for i in files['Questions']
                                             if i not in exam_json['math_quest']}

                 exam_json1['math_opt'] = {i: files['Questions'][i] for i in files['Options']
                                             if i not in exam_json['math_opt']}

                 exam_json1['math_ans'] = {i: files['Ans'][i] for i in files['Ans']
                                           if i not in exam_json['math_ans']}
        elif filex == 'english':
             exam_json1 = {}

             with open(f'{filex}_questions.json', 'r') as file:
                 files = json.load(file)

                 # code ensures that each student answers questions
                 # this code will be implemented at the server side
             exam_json['english_quest'] = {i: files['Questions'][i] for i, j in
                                           zip(files['Questions'], range(len(files['Questions']))) if j < 5}
             exam_json['english_opt'] = {i: files['Options'][i] for i, j in
                                         zip(files['Options'], range(len(files['Options']))) if j < 5}
             exam_json['english_ans'] = {i: files['Ans'][i] for i, j in
                                         zip(files['Ans'], range(len(files['Ans']))) if j < 5}

             exam_json1['english_quest'] = {i: files['Questions'][i] for i in files['Questions']
                                            if i not in exam_json['english_quest']}

             exam_json1['english_opt'] = {i: files['Questions'][i] for i in files['Options']
                                          if i not in exam_json['english_opt']}

             exam_json1['english_ans'] = {i: files['Ans'][i] for i in files['Ans']
                                          if i not in exam_json['english_ans']}

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
                tcp_echo_client(self, '{}#u/894#{}'.format('edit student', recovery.strip()),
                                confirm_id))
            async_thread.daemon = True
            async_thread.start()

    def show_passwordd1(self):

        if self.one == 0:
            self.password_entry.configure(show="")
            self.one+=1
        elif self.one == 1:
            self.password_entry.configure(show="*")
            self.one-=1

    def active_rectangle(self,event,value):

        clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)  # Get all tags associated with the item
            if value  == 'enter':
                if 's' not in tags[0]:
                    self.Frame_login.config(cursor='hand2')
                    self.Frame_login.itemconfigure(tags[0],fill='#695348')
                elif 's' in tags[0]:
                    self.Frame_login.itemconfigure(tags[0].replace('s',''), fill='#695348')
                    self.Frame_login.config(cursor='hand2')
            elif value == 'clicked':
                if 's' not in tags[0]:
                    self.Frame_login.itemconfigure(tags[0],fill='#b8b589')
                elif 's' in tags[0]:
                    self.Frame_login.itemconfigure(tags[0].replace('s',''), fill='#b8b589')
            elif value == 'enter1':
                if 's' not in tags[0]:
                    self.Frame_login1.itemconfigure(tags[0], fill='#695348')
                    self.Frame_login1.config(cursor='hand2')
                elif 's' in tags[0]:
                    self.Frame_login1.config(cursor='hand2')
                    self.Frame_login1.itemconfigure(tags[0].replace('s', ''), fill='#695348')

            elif value == 'clicked1':
                if 's' not in tags[0]:
                    self.Frame_login1.itemconfigure(tags[0], fill='#b8b589')
                elif 's' in tags[0]:
                    self.Frame_login1.itemconfigure(tags[0].replace('s', ''), fill='#b8b589')


    def nonactive_rectangle(self,event,value):

        clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)  # Get all tags associated with the item
            if value == 'leave':
                if 's' not in tags[0]:
                    self.Frame_login.config(cursor='')
                    self.Frame_login.itemconfigure(tags[0], fill='#696564')

            elif value == 'buttonrelease':
                if 's' not in tags[0]:
                    self.Frame_login.itemconfigure(tags[0], fill='#696564')
                    self.submit_call()
                elif 's' in tags[0]:
                    self.Frame_login.itemconfigure(tags[0].replace('s', ''), fill='#696564')
                    self.submit_call()

            elif value == 'leave1':
                if 's' not in tags[0]:
                    self.Frame_login1.config(cursor='')
                    self.Frame_login1.itemconfigure(tags[0], fill='#696564')

            elif value == 'buttonrelease1':
                if 's' not in tags[0]:
                    self.Frame_login1.itemconfigure(tags[0], fill='#696564')
                    self.back(self.controller)
                elif 's' in tags[0]:
                    self.Frame_login1.itemconfigure(tags[0].replace('s', ''), fill='#696564')
                    self.back(self.controller)

    def create_rounded_rec(self, canvas, x1, y1, x2, y2, radius, tag, type, text='', ):

        points = [x1 + radius, y1, x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1, x2, y1, x2,
                  y1 + radius,
                  x2, y1 + radius, x2, y1 + radius, x2, y2 - radius, x2, y2 - radius, x2, y2, x2 - radius, y2,
                  x2 - radius, y2,
                  x2 - radius, y2, x1 + radius, y2, x1 + radius, y2, x1, y2, x1, y2 - radius, x1, y2 - radius, x1,
                  y2 - radius, x1,
                  y1 + radius, x1, y1 + radius, x1, y1]
        if type == 'entry':
            item = canvas.create_polygon(points, fill='white', outline="#989492", smooth=True,
                                         tags=f"tag{tag}", width=2)
        elif type == 'submit':
            item = canvas.create_polygon(points, fill='#696564', outline="", smooth=True, tags=f"tag{tag}")
            text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill='white',
                                      font='Bookman-Old-Style 12 normal',
                                      tags=f"tags{tag}")
            canvas.tag_bind(item, "<Enter>", lambda event: self.active_rectangle(event, 'enter'))
            canvas.tag_bind(item, "<Leave>", lambda event: self.nonactive_rectangle(event, 'leave'))
            canvas.tag_bind(text, "<Enter>", lambda event: self.active_rectangle(event, 'enter'))
            canvas.tag_bind(text, "<Leave>", lambda event: self.nonactive_rectangle(event, 'leave'))
            canvas.tag_bind(item, "<Button-1>", lambda event: self.active_rectangle(event, 'clicked'))
            canvas.tag_bind(text, "<Button-1>", lambda event: self.active_rectangle(event, 'clicked'))
            canvas.tag_bind(item, "<ButtonRelease-1>", lambda event: self.nonactive_rectangle(event, 'buttonrelease'))
            canvas.tag_bind(text, "<ButtonRelease-1>", lambda event: self.nonactive_rectangle(event, 'buttonrelease'))

        elif type == 'back':
            item = canvas.create_polygon(points, fill='#696564', outline="", smooth=True, tags=f"tag{tag}")
            text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill='white',
                                      font='Bookman-Old-Style 12 normal', tags=f"tags{tag}")
            canvas.tag_bind(item, "<Enter>", lambda event: self.active_rectangle(event, 'enter1'))
            canvas.tag_bind(item, "<Leave>", lambda event: self.nonactive_rectangle(event, 'leave1'))
            canvas.tag_bind(text, "<Enter>", lambda event: self.active_rectangle(event, 'enter1'))
            canvas.tag_bind(text, "<Leave>", lambda event: self.nonactive_rectangle(event, 'leave1'))
            canvas.tag_bind(item, "<Button-1>", lambda event: self.active_rectangle(event, 'clicked1'))
            canvas.tag_bind(text, "<Button-1>", lambda event: self.active_rectangle(event, 'clicked1'))
            canvas.tag_bind(item, "<ButtonRelease-1>", lambda event: self.nonactive_rectangle(event, 'buttonrelease1'))
            canvas.tag_bind(text, "<ButtonRelease-1>", lambda event: self.nonactive_rectangle(event, 'buttonrelease1'))

        elif type == 'rectangle':

            item = canvas.create_polygon(points, fill='#d0c5c1', outline="#d0c5c1", smooth=True,
                                         tags=f"tag{tag}", width=3)

    def submit_call(self):

        self.animate = Toplevel(self.parent, screen='')
        self.animate_canvas = Canvas(self.animate, width=WIDTH, height=HEIGHT, bg="white",
                                     highlightbackground='white', bd=0)
        wid = Tk.winfo_x(self.parent) + 500
        hei = Tk.winfo_y(self.parent) + 200
        display_animation(self.animate, self.animate_canvas, f'400x250+{wid}+{hei}')
        async_thread = async_Thread(
            tcp_echo_client(self, '{}#u/894#{}'.format('user login', self.user_entry.get().strip()),
                            Userlandpage.s_process))
        async_thread.daemon = True
        async_thread.start()


    def back1(self):
        self.pop_up.grab_release()
        self.pop_up.destroy()
        self.password_entry.configure(show="*")
        self.password_entry.bind("<Return>", lambda event: self.submit_call())


    def back(self,controller):
        self.user_entry.delete(0, END),self.password_entry.delete(0,END),self.password_entry.unbind("<Return>")
        controller.show_frame(Landingpage,'backward')
        self.password_entry.configure(show="*")
        deny_focus(self.children)
