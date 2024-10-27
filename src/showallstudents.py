from tkinter import Frame

class ShowAllStudents(Frame):
    s_process = ''
    student = {}

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.list_box = ''
        self.pop_up = ''
        self.setter = False
        self.flag = False
        self.temp = False
        self.retreat = False
        self.animate = ''
        self.animate_canvas = ''
        self.load_flag = False
        self.controller = controller

        heading = Label(self, text="SHOW ALL STUDENT", font=('Bookman-Old-Style 16 normal', 30),
                        foreground='white', background='#000024')
        heading.place(x=150, y=15)
        self.l = ['', "Matric no:", 'Firstname:', 'Lastname:', 'Password:', 'Phone Number:', 'Courses:', 'Address:',
                  'Country:',
                  'State of origin:', "State:", "City:", "Gender:", "DOB:"]
        logout_btn = ttk.Button(self, text='Log out',
                                cursor='hand2', command=lambda: controller.show_frame(Adminlandpage, shw_temp='showall',
                                                                                      route='logout'))
        logout_btn.place(x=1200, y=15)
        self.widget_obj = {}
        self.binder = ''

        def check(arg):
            global all_student_data
            if self.animate:
                self.animate.destroy()
            student = {}
            try:
                with open('server_response3.json', 'r') as file:
                    student = json.load(file)
            except Exception as e:
                if "No such file or directory" in str(e):
                    student['error'] = 'Internal error, try again later'
            self.temp = True
            ShowAllStudents.student = student

            if student and ''.join([i for i in student.keys()]) not in ["connection error", "error"]:
                if not self.flag:
                    heading1 = Label(self, text=F"TOTAL ({len(student)})", font=('Bookman-Old-Style 16 normal', 20),
                                     foreground='white', background='#000024')
                    heading1.place(x=900, y=19)
                    heading2 = Label(self, text="Search", font=('Bookman-Old-Style 16 normal', 15, 'bold'),
                                     foreground='white', background='#000024')
                    search_entry = Entry(self, width=30)
                    heading2.place(x=623, y=30)
                    search_entry.place(x=700, y=33)

                    # frame to hold the canvas widget
                    frame = tk.Frame(self, bg='black')
                    frame.place(x=150, y=70, anchor='nw')

                    # Create a canvas widget with a scrollbar
                    canvas = tk.Canvas(frame, width=1100, height=660, bg='black', highlightcolor='black',
                                       highlightbackground='black')
                    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
                    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

                    canvas.configure(yscrollcommand=scrollbar.set)

                    # Generate example data
                    data_frame = [i * 550 for i in range(len(student))]
                    data = [[i] + student[i] for i in student]

                    scroll_info = module3.VirtualScroller(canvas, data, scrollbar, data_frame, len(student))

                    search_entry.configure(state="normal")
                    self.pop_up = Toplevel(self, height=200, bg='white', highlightthickness=0.5,
                                           highlightbackground='grey')
                    self.pop_up.overrideredirect(True)
                    s_frame = Frame(self.pop_up, bg='white', height=200)
                    s_frame.place(x=1, y=0, anchor='nw')

                    suggestion_listbox = Listbox(s_frame, width=18, font=10, bd=0)
                    suggestion_listbox.configure(cursor="hand2", selectbackground="black", activestyle="none",
                                                 highlightbackground='white')
                    suggestion_listbox.grid(row=0, column=0)

                    listbox_scrollbar = ttk.Scrollbar(s_frame, orient=tk.VERTICAL,
                                                      command=suggestion_listbox.yview)
                    suggestion_listbox.configure(yscrollcommand=listbox_scrollbar.set)

                    self.pop_up.withdraw()
                    self.list_box = suggestion_listbox
                    self.widget_obj = {'heading1': heading1, 'heading2': heading2, 'search_entry': search_entry,
                                       'canvas': canvas, 'pop_up': self.pop_up, 'scrollbar': scrollbar,
                                       "listboxscrollbar": listbox_scrollbar}
                    self.flag = True

                    if self.binder:
                        self.binder()
                else:

                    self.widget_obj['heading1'].config(text=F"TOTAL ({len(student)})")
                    self.widget_obj['canvas'].config(bg='black')
                    self.widget_obj['scrollbar'].pack(side=tk.RIGHT, fill=tk.Y)
                    # Generate example data
                    data_frame = [i * 550 for i in range(len(student))]
                    data = [[i] + student[i] for i in student]

                    scroll_info = module3.VirtualScroller(self.widget_obj['canvas'], data,
                                                          self.widget_obj['scrollbar'], data_frame, len(student))
                    xii = lambda event: scroll_info._on_canvas_configure(event)



            elif student and 'connection error' in student or 'error' in student:
                for i in student.keys():
                    messagebox.showerror('error', student[i])
            else:
                messagebox.showerror('Error', 'Try again later')

        ShowAllStudents.s_process = check

        # function update list base on search keywords
        def updater(value):
            search_entry = self.widget_obj['search_entry'] if self.widget_obj else ''
            student = ShowAllStudents.student
            if search_entry.get() and student:
                # Generate example data

                data = [[i] + student[i] for i in student if value[0] in student[i] or value[1] in student[i]]
                data_frame = [i * 550 for i in range(len(data))]
                scroll_info = module3.VirtualScroller(self.widget_obj['canvas'], data,
                                                      self.widget_obj['scrollbar'], data_frame, len(student))
                scroll_info._on_canvas_configure()

        def top_level(num=None):
            search_entry = self.widget_obj['search_entry'] if self.widget_obj else ''
            student = ShowAllStudents.student
            x = search_entry.get() if search_entry else ''

            if x and num == 0:
                wid = Tk.winfo_x(controller) + 710
                hei = Tk.winfo_y(controller) + 85
                self.pop_up.geometry(f"+{wid}+{hei}")
                self.pop_up.deiconify()

            elif not x and num == 0:
                self.pop_up.withdraw()

            if num == 1:
                self.pop_up.withdraw()
                search_entry.delete(0, END)
                search_entry.config(state='disabled')

            if num == 2:
                try:
                    search_entry.focus()
                    search_entry.config(state='normal')
                except:
                    pass

            def on_search_changed():
                search_text = search_entry.get()
                suggestions = get_suggestions(search_text)
                update_suggestion_list(suggestions)

            def get_suggestions(search_text):

                if search_text:
                    suggestions = [[i] + student[i] for i in student]
                    filtered_suggestions = []
                    filtered_suggestions1 = ''
                    for i in suggestions:
                        i = [str(x) for x in i if x]

                        for j in i:
                            if not search_text.isnumeric() and search_text.lower() in j.lower():
                                if not i in filtered_suggestions:
                                    filtered_suggestions.append(i)
                            elif search_text.lower() not in (' '.join(i)).lower():
                                filtered_suggestions1 = search_text
                            elif search_text.isnumeric():
                                filtered_suggestions1 = search_text

                    return filtered_suggestions, filtered_suggestions1

            def update_suggestion_list(suggestions):
                filtered = []
                if suggestions and suggestions[0]:
                    self.list_box.delete(0, END)

                    def filter_search(sequence):
                        if [sequence[1], sequence[2]] not in filtered:
                            filtered.append([sequence[1], sequence[2]])

                    list(filter(filter_search, suggestions[0]))

                    for suggestion in filtered:
                        self.list_box.insert(END, [suggestion[0], suggestion[1]])

                    if len(filtered) < 6:
                        self.pop_up.configure(height=(len(filtered) * 20), width=182)
                        self.widget_obj['listboxscrollbar'].grid_remove()
                    else:
                        self.pop_up.configure(height=196, width=182)
                        self.widget_obj['listboxscrollbar'].grid(row=0, column=1, sticky='nsew')

                elif suggestions and suggestions[1]:
                    self.list_box.delete(0, END)
                    self.list_box.insert(END, 'No match found')

                    self.pop_up.configure(height=20, width=180)
                    self.widget_obj['listboxscrollbar'].grid_remove()

                if not search_entry.get() and student:
                    # Generate example data
                    data_frame = [i * 550 for i in range(len(student))]
                    data = [[i] + student[i] for i in student]

                    scroll_info = module3.VirtualScroller(self.widget_obj['canvas'], data,
                                                          self.widget_obj['scrollbar'], data_frame, len(student))
                    scroll_info._on_canvas_configure()

                def update_scrolled_text():
                    selected = self.list_box.curselection()
                    if selected:
                        self.pop_up.withdraw()
                        if self.list_box.get(selected) != 'No match found':
                            updater(self.list_box.get(selected))

                if suggestions:
                    self.list_box.bind("<ButtonRelease-1>", lambda event: update_scrolled_text())

            if num < 1:
                on_search_changed()

        def event_place(event):
            if event.y < 0:
                self.pop_up.withdraw()

        def binder():
            self.widget_obj['search_entry'].bind("<KeyRelease>", lambda event: top_level(num=0))
            self.widget_obj['search_entry'].bind("<ButtonRelease-1>", lambda event: top_level(num=2))
            self.parent.bind("<Leave>", event_place)
            self.widget_obj['canvas'].bind("<Button-1>", lambda event: top_level(num=1))
            self.bind("<Button-1>", lambda event: top_level(num=1))

        self.binder = binder

        def on_enter(rec):
            if rec == "activate":
                self.refresh_btn.config(bg='#695348')


            elif rec == "activate2":
                self.back_btn.configure(bg='#b08454')
                self.back_btn.configure(cursor="hand2")

        def on_leave(rec):
            if rec == "deactivate":
                self.refresh_btn.configure(bg='#696564')

            elif rec == "deactivate2":
                self.back_btn.configure(bg='#3a3939')

        self.refresh_btn = Button(self, text='Reload', bg='#696564', font='Bookman-Old-Style 12 normal', cursor='hand2',
                                  fg='white', command=self.refresh_page)
        self.refresh_btn.place(x=1100, y=15)
        self.refresh_btn.bind("<Enter>", lambda event: on_enter(rec="activate"))
        self.refresh_btn.bind("<Leave>", lambda event: on_leave(rec="deactivate"))
        self.back_btn = Button(self, text="<", bd=0, bg='#696564', font=('Bookman-Old-Style normal', 20),
                               height=0, width=1, command=lambda: self.back(controller))

        self.back_btn.place(x=50, y=500)
        self.back_btn.configure(foreground='white')
        self.back_btn.bind("<Enter>", lambda event: on_enter(rec="activate2"))
        self.back_btn.bind("<Leave>", lambda event: on_leave(rec="deactivate2"))
        self.back_btn.bind("<Button-1>", lambda event: top_level(num=2))

        self.configure(background=win_bg)
        deny_focus(self.children)

    def refresh_page(self):
        self.load_flag = True
        self.animate = Toplevel(self.parent, screen='')
        self.animate_canvas = Canvas(self.animate, width=WIDTH, height=HEIGHT, bg="white",
                                     highlightbackground='white', bd=0)
        wid = Tk.winfo_x(self.parent) + 500
        hei = Tk.winfo_y(self.parent) + 200
        display_animation(self.animate, self.animate_canvas, f'400x250+{wid}+{hei}')
        async_thread = async_Thread(
            tcp_echo_client(object_dict[ShowAllStudents], '{}#u/894#{}'.format('Showallstudents', '0'),
                            ShowAllStudents.s_process, sas_flag=True))
        async_thread.daemon = True
        async_thread.start()

    def back(self, controller):
        try:
            self.pop_up.withdraw()
            self.widget_obj['search_entry'].delete(0, END)

        except:
            pass
        if controller:
            self.retreat = True
            controller.show_frame(Adminpickpage, 'backward')
            deny_focus(self.children)

    def logout(self, type):
        num = 0

        self.list = 0
        if 'pop_up' in self.widget_obj:
            self.widget_obj['pop_up'].withdraw()
        if 'scroll_text' in self.widget_obj:
            self.widget_obj['scroll_text'].delete(1.0, END)
        if 'heading1' in self.widget_obj:
            self.widget_obj['heading1'].config(text=F"TOTAL {''}")
        if 'search_entry' in self.widget_obj:
            self.widget_obj['search_entry'].delete(0, END)
        if 'student' in self.widget_obj:
            self.widget_obj['student'] = {}
        if "canvas" in object_dict[ShowAllStudents].widget_obj:
            object_dict[ShowAllStudents].widget_obj['canvas'].delete('all')
            object_dict[ShowAllStudents].widget_obj['canvas'].config(bg="#000024", highlightbackground='#000024')
        if "scrollbar" in object_dict[ShowAllStudents].widget_obj:
            object_dict[ShowAllStudents].widget_obj["scrollbar"].place(x=0, y=-100)

        self.tpy_flag = False
