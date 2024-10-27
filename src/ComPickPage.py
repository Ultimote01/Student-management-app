class Commpickpage(Frame):
    verify=''
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        heading = Label(self, text="WRITE EXAM", font='Bookman-Old-Style 16 bold')
        heading.place(x=200, y=70)
        heading.configure(foreground='white')
        heading.configure(background='#989492')
        self.label = Label(self, text='', width=7, bg='white', fg='black', font='Bookman-Old-Style 12 bold')
        self.label.place(x=1100, y=15)
        # logout the user and send their current score to the server
        logout_btn = ttk.Button(self, text='Log out',
                                cursor='hand2', command=lambda: logout_timer(controller,verify))
        logout_btn.place(x=1200, y=15)
        self.control=controller
        self.math_btn = Button(self, text="MATH", width=15, font='Bookman-Old-Style 12 bold', bd=0, bg='white',
                      cursor='hand2',command=lambda: self.create_toplevel('math'))
        self.math_btn.place(x=200, y=300)
        self.english_btn = Button(self, text="ENGLISH", width=15, font='Bookman-Old-Style 12 bold', bd=0, bg='white',
                             cursor='hand2',command=lambda: self.create_toplevel('english'))
        self.english_btn.place(x=200, y=400)
        self.busstudy_btn = Button(self, text="BUS STUDIES", width=15, font='Bookman-Old-Style 12 bold', bd=0, bg='white',
                              cursor='hand2',command=lambda: controller.show_frame(Commerce))
        self.busstudy_btn.place(x=200, y=500)

        back_btn = Button(self, text="BACK", bd=0, bg='white',fg='black', font='Bookman-Old-Style 12 normal',
                          cursor='hand2',command=lambda: self.back(controller))
        back_btn.place(x=200, y=650)

        def verify(data):
            info = data

            if info:
                for j in info:
                    if j == 'updated':
                        if current_minute == 0 and current_seconds == 0:
                            messagebox.showinfo('', 'You\'ve been logged out.')
                            Math.verify(data)
                            English.verify(data)
                            self.control.show_frame(Userlandpage)
                        else:
                            messagebox.showinfo('', 'You\'ve logged out successfully.')
                            Math.verify(data)
                            English.verify(data)
                            self.control.show_frame(Userlandpage)
                    else:
                        messagebox.showerror('', 'Try again.')
        Commpickpage.verify=verify

        self.math_btn.bind("<Enter>", lambda event: on_enter({'math_btn': self.math_btn}))
        self.english_btn.bind("<Enter>", lambda event: on_enter({'english_btn': self.english_btn}))
        self.busstudy_btn.bind("<Enter>", lambda event: on_enter({'busstudy_btn': self.busstudy_btn}))
        back_btn.bind("<Enter>", lambda event: on_enter({'back_btn': back_btn}))
        self.math_btn.bind("<Leave>", lambda event: on_leave({'math_btn': self.math_btn}))
        self.english_btn.bind("<Leave>", lambda event: on_leave({'english_btn': self.english_btn}))
        self.busstudy_btn.bind("<Leave>", lambda event: on_leave({'busstudy_btn': self.busstudy_btn}))
        back_btn.bind("<Leave>", lambda event: on_leave({'back_btn': back_btn}))


        self.configure(background='#989492')
        deny_focus(self.children)

    def create_toplevel(self,page):
        try:
            if page == 'math':
                if Math.top_level_object:
                    Math.top_level_object.focus()
                    Math.top_level_object.deiconify()

                else:
                    math = Math(self, '')
                    object_dict1['math'] = math
                    math.update_widget()
                    math.top_level.deiconify()
                    math.top_level.focus()

            elif page == 'english':
                if English.top_level_object:
                    English.top_level_object.focus()
                    English.top_level_object.deiconify()
                else:
                    english = English(self, '')
                    object_dict1['math'] = english
                    english.update_widget()
                    english.top_level.deiconify()
                    english.top_level.focus()

        except Exception as e:
            print(e)

    def back(self, controller):
        logout_timer(controller, Commpickpage.verify)
        if controller:
            controller.show_frame(Userlandpage)
        deny_focus(self.children)