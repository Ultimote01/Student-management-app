from tkinter import Frame


class DeleteStudent(Frame):
    s_process=''
    verifyupdate=''
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.count = 0
        heading = Label(self, text="DELETE STUDENT", font='Bookman-Old-Style 16 normal')
        heading.place(x=200, y=70)
        heading.configure(foreground='white')
        heading.configure(background='#989492')

        user = Label(self, text="Enter Matric No.", font='Bookman-Old-Style 12 normal')
        user.place(x=200, y=100)
        user.configure(foreground='white')
        user.configure(background='#989492')
        user_entry = Entry(self, width=30, bd=1)
        user_entry.place(x=320, y=100)
        logout_btn = ttk.Button(self, text='Log out',
                                cursor='hand2', command=lambda: controller.show_frame(Adminlandpage))
        logout_btn.place(x=1200, y=15)
        self.flag=False
        self.widgets_objx={}
        self.widgets_obj={}

        def on_enter(rec):
            if rec == "activate":
                self.submit_btn.config(bg='#695348',foreground='white')
                self.submit_btn.configure(cursor="hand2")

            elif rec == "activate2":
                self.back_btn.configure(bg='#b08454')
                self.back_btn.configure(cursor="hand2")

        def on_leave(rec):
            if rec == "deactivate":
                self.submit_btn.configure(bg='white',foreground="black")

            elif rec == "deactivate2":
                self.back_btn.configure(bg='red')

        def check(data):
            student = {}
            module2.Animation.toplevel.grab_release()
            student = data
            self.student = student
            module2.Animation.toplevel.destroy()
            num = user_entry.get()
            if num in student:
                if not self.flag:
                    matric = Label(self, text="1. Matric No.:", font=('Bookman-Old-Style 12 normal', 15))
                    matric.place(x=200, y=190)
                    matric.configure(foreground='white', background='#989492')
                    matricshow = Label(self, text=num, font=('Bookman-Old-Style 12 normal', 15))
                    matricshow.place(x=320, y=190)
                    matricshow.configure(foreground='white', background='#989492', padx=15)

                    firstname = Label(self, text="2. First Name:", font=('Bookman-Old-Style 12 normal', 15))
                    firstname.place(x=200, y=220)
                    firstname.configure(foreground='white', background='#989492')
                    firstnameshow = Label(self, text=student[num][0], font=('Bookman-Old-Style 12 normal', 15))
                    firstnameshow.place(x=320, y=220)
                    firstnameshow.configure(foreground='white', background='#989492', padx=15)

                    lastname = Label(self, text="3. Last Name:", font=('Bookman-Old-Style 12 normal', 15))
                    lastname.place(x=200, y=250)
                    lastname.configure(foreground='white', background='#989492')
                    lastnameshow = Label(self, text=student[num][1], font=('Bookman-Old-Style 12 normal', 15))
                    lastnameshow.place(x=320, y=250)
                    lastnameshow.configure(foreground='white', background='#989492', padx=15)

                    password = Label(self, text="4. Password:", font=('Bookman-Old-Style 12 normal', 15))
                    password.place(x=200, y=280)
                    password.configure(foreground='white', background='#989492')
                    passwordshow = Label(self, text=student[num][2], font=('Bookman-Old-Style 12 normal', 15))
                    passwordshow.place(x=320, y=280)
                    passwordshow.configure(foreground='white', background='#989492', padx=15)
                    self.widgets_objx = {'matricshow': matricshow, 'firstnameshow': firstnameshow,
                    'lastnameshow': lastnameshow,'passwordshow': passwordshow}
                    self.widgets_obj={'user_entry':user_entry,'matricshow': matricshow,'matric': matric,'firstnameshow': firstnameshow,
                    'firstname':firstname,'lastnameshow': lastnameshow,'lastname': lastname,
                    'password':password,'passwordshow':passwordshow}
                else:
                    self.widgets_objx['matricshow'].config(text=num)

                    for i ,x in zip(self.widgets_objx,range(len(student[num]))):
                        if not i == 'matricshow':
                            self.widgets_objx[i].config(text=student[num][x-1])

                def yes(data):
                    module2.Animation.toplevel.grab_release()
                    res = data
                    module2.Animation.toplevel.destroy()

                    if res['updated'] == 'Deleted':
                         messagebox.showinfo("Sucess", "Student Deleted")
                         for i in self.widgets_obj:
                            if i == 'user_entry':
                                 self.widgets_obj[i].delete(0,END)
                            else:
                                self.widgets_obj[i].destroy()
                         self.flag=False
                    else:
                        messagebox.showerror('Error',res['info'])

                DeleteStudent.verifyupdate=yes
                def no(num=None):
                    if num == 1:
                        for i in self.widgets_obj:
                            if i == 'user_entry':
                                self.widgets_obj[i].delete(0, END)
                            else:
                                self.widgets_obj[i].destroy()
                        self.flag=False
                if not self.flag:
                    ques = Label(self, text="Are you sure you want to delete?", font='Bookman-Old-Style 12 normal')
                    ques.place(x=200, y=310)
                    yes_btn = ttk.Button(self, text="Yes",
                                     command=lambda: self.submit_call(user_entry.get().strip() + ',' + 'delete', 'yes'))
                    yes_btn.place(x=220, y=340)
                    no_btn = ttk.Button(self, text="No",
                                    command=lambda: no(num=1))
                    no_btn.place(x=320, y=340)

                    self.flag = True
                    self.widgets_obj['ques']=ques
                    self.widgets_obj['yes']=yes_btn
                    self.widgets_obj['no']=no_btn
            else:
                messagebox.showinfo("Error", "Student does not exist")

        DeleteStudent.s_process=check
        self.submit_btn = Button(self, text="Check", bd=0, bg='white', font='Bookman-Old-Style 12 normal',
                                 command=lambda : self.submit_call(user_entry.get().strip(),'check'))
        self.submit_btn.configure(cursor='hand2')
        user_entry.bind("<Return>", lambda event: self.submit_call(user_entry.get().strip(),'check'))
        self.submit_btn.bind("<Enter>", lambda event: on_enter(rec="activate"))
        self.submit_btn.bind("<Leave>", lambda event: on_leave(rec="deactivate"))
        self.submit_btn.bind("<Return>", lambda event: check())
        self.submit_btn.focus_set()
        self.submit_btn.place(x=290, y=130)


        self.back_btn = Button(self, text="BACK", bd=0, bg='red', font='Bookman-Old-Style 12 normal',
                          command=lambda: self.back(controller,user_entry))
        self.back_btn.bind("<Enter>", lambda event: on_enter(rec="activate2"))
        self.back_btn.bind("<Leave>", lambda event: on_leave(rec="deactivate2"))
        self.back_btn.place(x=200, y=500)
        self.back_btn.configure(foreground='white')

        self.configure(background=win_bg)
        deny_focus(self.children)

    def submit_call(self, info,type):

        variable=''
        if type == 'check':
            variable=DeleteStudent.s_process
        elif type == 'yes':
            variable=DeleteStudent.verifyupdate

        if variable :
            asyncio.run(tcp_echo_client(self, '{}#u/894#{}'.format('delete student', info),
                                        variable))

    def logout(self, controller):

        if self.widgets_obj:
            for i in self.widgets_obj:
                if i == 'user_entry':
                    self.widgets_obj[i].delete(0, END)
                else:
                    self.widgets_obj[i].destroy()
            self.flag=False



    def back(self,controller,user_entry):
        if controller:
            user_entry.delete(0,END)
            controller.show_frame(Adminpickpage)
            deny_focus(self.children)

