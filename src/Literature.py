class Literature(Frame):
    verify = ''

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        logout_btn = ttk.Button(self, text='Log out',
                                cursor='hand2', command=lambda: logout_timer(controller, verify))
        logout_btn.place(x=1200, y=15)

        self.label = Label(self, text='', width=7, bg='white', fg='black', font='Bookman-Old-Style 12 bold')
        self.label.place(x=1100, y=15)
        self.control = controller
        self.configure(background='#989492')

        back_btn = Button(self, text="BACK", bd=0, bg='white', fg='black', font='Bookman-Old-Style 12 normal',
                          cursor='hand2', command=lambda: self.back(controller))
        back_btn.place(x=200, y=650)

        def verify():
            module2.Animation.toplevel.grab_release()
            info = clientThread.loader()
            clientThread.s_response = ''
            module2.Animation.toplevel.destroy()
            if info:
                for j in info:
                    if j == 'updated':
                        if current_minute == 0 and current_seconds == 0:
                            messagebox.showinfo('', 'You\'ve been logged out.')
                            self.control.show_frame(Userlandpage)
                        else:
                            messagebox.showinfo('', 'You\'ve logged out successfully.')
                            self.control.show_frame(Userlandpage)
                    else:
                        messagebox.showerror('', 'Try again.')

        Literature.verify = verify

    def back(self, controller):
        if controller:
            controller.show_frame(Artpickpage)





