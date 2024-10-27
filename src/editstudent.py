from tkinter import Frame,Label,Entry
from .globalVariables import win_bg

class EditStudent(Frame):
    s_process = ''
    verify_update = ''
    clear_widgets = ''

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.count = 0
        self.countZ = 0
        self.widgets_obj = {}
        self.animate = ''
        self.parent = controller  # Tk
        self.animate_canvas = ''
        heading = Label(self, text="EDIT STUDENT", font='Bookman-Old-Style 16 bold')
        heading.place(x=200, y=70)
        heading.configure(foreground='black', background=win_bg)
        # self.d_layer_frame = ''
        #
        # user = Label(self, text="Enter Matric No.", font='Bookman-Old-Style 12 normal')
        # user.place(x=200, y=100)
        # user.configure(foreground='white', background='#000024')
        # user_entry = Entry(self, width=30, bd=1)
        # user_entry.place(x=320, y=100)
        # self.widgets_obj['user_entry'] = user_entry
        # logout_btn = ttk.Button(self, text='Log out',
        #                         cursor='hand2', command=lambda: controller.show_frame(Adminlandpage, route='logout'))
        # logout_btn.place(x=1200, y=15)
        # self.student = {}
        # self.widget_flag = False
        # self.flag = False
        # self.widgets_objx = {}
        # self.option_dicts = {}
        # self.err_label = ''
        # self.new_update = ''
        # self.binding = []
        # image = Image.open(pwd + "emoji2.jpg")
        # resized_image = image.resize((320, 200), Image.BICUBIC)
        # self.photo9 = ImageTk.PhotoImage(resized_image)

    #     def entry():
    #         user_entry.bind("<Return>", lambda event: self.submit_call(user_entry.get().strip(), 'check'))
    #         self.check_btn.bind("<Return>", lambda event: self.submit_call(user_entry.get().strip(), 'check'))
    #
    #     def entry1():
    #         user_entry.unbind("<Return>")
    #         self.check_btn.unbind("<Return>")
    #
    #     def on_enter(rec, variable=None):
    #         if rec == "activate":
    #             self.check_btn.config(bg='#695348')
    #             self.check_btn.configure(cursor="hand2")
    #
    #         elif rec == "activate2":
    #             self.back_btn.configure(bg='#b08454')
    #             self.back_btn.configure(cursor="hand2")
    #         elif rec == 'activate3':
    #             variable.config(bg='#695348')
    #
    #     def on_leave(rec, variable=None):
    #         if rec == "deactivate":
    #             self.check_btn.configure(bg='#696564')
    #
    #         elif rec == "deactivate2":
    #             self.back_btn.configure(bg='#3a3939')
    #
    #         elif rec == "deactivate3":
    #             variable.config(bg='#3a3939')
    #
    #     #  verify student information
    #     def check(data):
    #         global meter
    #         student = {}
    #         if 'done' in data:
    #             with open("server_response.json", 'r') as file:
    #                 student = json.load(file)
    #         else:
    #             student = data
    #         self.student = student
    #         meter = False
    #         num = user_entry.get().strip()
    #
    #         if self.animate:
    #             self.animate.destroy()
    #
    #         if num in student:
    #
    #             if not self.widget_flag:
    #                 self.d_layer_frame = Frame(self, width=470, height=420)
    #                 self.d_layer_frame.place(x=200, y=170)
    #
    #                 d_layer_canvas = Canvas(self.d_layer_frame, width=470, height=420, bd=0,
    #                                         highlightbackground='#989492',
    #                                         highlightcolor='#989492')
    #                 d_layer_canvas.grid(row=0, column=0, sticky="nsew")
    #                 vsb = tk.Scrollbar(self.d_layer_frame, orient="vertical", command=d_layer_canvas.yview)
    #                 vsb.grid(row=0, column=1, sticky="nsew")
    #
    #                 t_layer_frame = Frame(d_layer_canvas, width=1010, height=700, bg='#989492')
    #                 d_layer_canvas.create_window(0, 0, window=t_layer_frame, anchor=tk.NW)
    #                 d_layer_canvas.config(yscrollcommand=vsb.set, scrollregion=d_layer_canvas.bbox("all"))
    #
    #                 matric = Label(t_layer_frame, text="1. Matric No:", font=('Bookman-Old-Style normal', 15))
    #                 matric.place(x=1, y=5)
    #                 matric.configure(foreground='white', background='#989492')
    #                 matricshow = Label(t_layer_frame, text=num, font=('Bookman-Old-Style normal', 15))
    #                 matricshow.place(x=190, y=5)
    #                 matricshow.configure(foreground='white', background='#989492')
    #
    #                 firstname = Label(t_layer_frame, text="2. First Name:", font=('Bookman-Old-Style normal', 15))
    #                 firstname.place(x=1, y=40)
    #                 firstname.configure(foreground='white', background='#989492')
    #                 firstnameshow = Label(t_layer_frame, text=student[num][0], font=('Bookman-Old-Style normal', 15))
    #                 firstnameshow.place(x=190, y=40)
    #                 firstnameshow.configure(foreground='white', background='#989492')
    #
    #                 lastname = Label(t_layer_frame, text="3. Last Name:", font=('Bookman-Old-Style normal', 15))
    #                 lastname.place(x=1, y=75)
    #                 lastname.configure(foreground='white', background='#989492')
    #                 lastnameshow = Label(t_layer_frame, text=student[num][1], font=('Bookman-Old-Style normal', 15))
    #                 lastnameshow.place(x=190, y=75)
    #                 lastnameshow.configure(foreground='white', background='#989492')
    #
    #                 password = Label(t_layer_frame, text="4. Password:", font=('Bookman-Old-Style normal', 15))
    #                 password.place(x=1, y=110)
    #                 password.configure(foreground='white', background='#989492')
    #                 passwordshow = Label(t_layer_frame, text=student[num][2], font=('Bookman-Old-Style normal', 15))
    #                 passwordshow.place(x=190, y=110)
    #                 passwordshow.configure(foreground='white', background='#989492')
    #
    #                 phone_number = Label(t_layer_frame, text="5.Phone Number: ", font=('Bookman-Old-Style normal', 15))
    #                 phone_number.place(x=1, y=145)
    #                 phone_number.configure(foreground='white', background='#989492')
    #                 phone_numbershow = Label(t_layer_frame, text=student[num][3], font=('Bookman-Old-Style normal', 15))
    #                 phone_numbershow.place(x=190, y=145)
    #                 phone_numbershow.configure(foreground='white', background='#989492')
    #
    #                 course = Label(t_layer_frame, text="6. Course:", font=('Bookman-Old-Style normal', 15))
    #                 course.place(x=1, y=180)
    #                 course.configure(foreground='white', background='#989492')
    #                 courseshow = Label(t_layer_frame, text=student[num][4], font=('Bookman-Old-Style normal', 15))
    #                 courseshow.place(x=190, y=180)
    #                 courseshow.configure(foreground='white', background='#989492')
    #
    #                 address = Label(t_layer_frame, text="7 Home Address:", font=('Bookman-Old-Style normal', 15))
    #                 address.place(x=1, y=215)
    #                 address.configure(foreground='white', background='#989492')
    #                 addresshow = Label(t_layer_frame, text=student[num][5], font=('Bookman-Old-Style normal', 15))
    #                 addresshow.place(x=190, y=215)
    #                 addresshow.configure(foreground='white', background='#989492')
    #
    #                 country = Label(t_layer_frame, text="8. Country:", font=('Bookman-Old-Style normal', 15))
    #                 country.place(x=1, y=250)
    #                 country.configure(foreground='white', background='#989492')
    #                 countryshow = Label(t_layer_frame, text=student[num][6], font=('Bookman-Old-Style normal', 15))
    #                 countryshow.place(x=190, y=250)
    #                 countryshow.configure(foreground='white', background='#989492')
    #
    #                 state_of_origin = Label(t_layer_frame, text="9. State of Origin:",
    #                                         font=('Bookman-Old-Style normal', 15))
    #                 state_of_origin.place(x=1, y=285)
    #                 state_of_origin.configure(foreground='white', background='#989492')
    #                 state_of_originshow = Label(t_layer_frame, text=student[num][7],
    #                                             font=('Bookman-Old-Style normal', 15))
    #                 state_of_originshow.place(x=190, y=285)
    #                 state_of_originshow.configure(foreground='white', background='#989492')
    #
    #                 state = Label(t_layer_frame, text="10. State:", font=('Bookman-Old-Style normal', 15))
    #                 state.place(x=1, y=320)
    #                 state.configure(foreground='white', background='#989492')
    #                 stateshow = Label(t_layer_frame, text=student[num][8], font=('Bookman-Old-Style normal', 15))
    #                 stateshow.place(x=190, y=320)
    #                 stateshow.configure(foreground='white', background='#989492')
    #
    #                 city = Label(t_layer_frame, text="11. City:", font=('Bookman-Old-Style normal', 15))
    #                 city.place(x=1, y=355)
    #                 city.configure(foreground='white', background='#989492')
    #                 cityshow = Label(t_layer_frame, text=student[num][9], font=('Bookman-Old-Style normal', 15))
    #                 cityshow.place(x=190, y=355)
    #                 cityshow.configure(foreground='white', background='#989492')
    #
    #                 gender = Label(t_layer_frame, text="12. Gender:", font=('Bookman-Old-Style normal', 15))
    #                 gender.place(x=1, y=390)
    #                 gender.configure(foreground='white', background='#989492')
    #                 gendershow = Label(t_layer_frame, text=student[num][10], font=('Bookman-Old-Style normal', 15))
    #                 gendershow.place(x=190, y=390)
    #                 gendershow.configure(foreground='white', background='#989492')
    #
    #                 date_of_birth = Label(t_layer_frame, text="13. Date of Birth:",
    #                                       font=('Bookman-Old-Style normal', 15))
    #                 date_of_birth.place(x=1, y=425)
    #                 date_of_birth.configure(foreground='white', background='#989492')
    #                 date_of_birthshow = Label(t_layer_frame, text=student[num][11],
    #                                           font=('Bookman-Old-Style normal', 15))
    #                 date_of_birthshow.place(x=190, y=425)
    #                 date_of_birthshow.configure(foreground='white', background='#989492')
    #
    #                 session = Label(t_layer_frame, text="14. Session:", font=('Bookman-Old-Style normal', 15))
    #                 session.place(x=1, y=455)
    #                 session.configure(foreground='white', background='#989492')
    #                 sessionshow = Label(t_layer_frame, text=student[num][12], font=('Bookman-Old-Style normal', 15))
    #                 sessionshow.place(x=190, y=455)
    #                 sessionshow.configure(foreground='white', background='#989492')
    #
    #                 math = Label(t_layer_frame, text="15. Math:", font=('Bookman-Old-Style normal', 15))
    #                 math.place(x=1, y=490)
    #                 math.configure(foreground='white', background='#989492')
    #                 mathshow = Label(t_layer_frame, text=student[num][13], font=('Bookman-Old-Style normal', 15))
    #                 mathshow.place(x=190, y=490)
    #                 mathshow.configure(foreground='white', background='#989492')
    #
    #                 english = Label(t_layer_frame, text="16. English:", font=('Bookman-Old-Style normal', 15))
    #                 english.place(x=1, y=525)
    #                 english.configure(foreground='white', background='#989492')
    #                 englishshow = Label(t_layer_frame, text=student[num][14], font=('Bookman-Old-Style normal', 15))
    #                 englishshow.place(x=190, y=525)
    #                 englishshow.configure(foreground='white', background='#989492')
    #
    #                 self.relative_course = Label(t_layer_frame, text="", font=('Bookman-Old-Style normal', 15))
    #                 self.relative_course.place(x=1, y=560)
    #                 relative_courseshow = Label(t_layer_frame, text='', font=('Bookman-Old-Style normal', 15))
    #                 relative_courseshow.place(x=190, y=560)
    #                 if student[num][4] == 'Art':
    #                     self.relative_course.configure(foreground='white', background='#989492', text='17. Literature')
    #                     relative_courseshow.configure(foreground='white', background='#989492', text=student[num][17])
    #                 elif student[num][4] == 'Science':
    #                     self.relative_course.configure(foreground='white', background='#989492', text='17. Biology')
    #                     relative_courseshow.configure(foreground='white', background='#989492', text=student[num][16])
    #                 elif student[num][4] == 'Commerce':
    #                     self.relative_course.configure(foreground='white', background='#989492', text='17. Commerce')
    #                     relative_courseshow.configure(foreground='white', background='#989492', text=student[num][15])
    #
    #                 time = Label(t_layer_frame, text="18.Auth Time:", font=('Bookman-Old-Style normal', 15))
    #                 time.place(x=1, y=595)
    #                 time.configure(foreground='white', background='#989492')
    #                 timeshow = Label(t_layer_frame, text=student[num][18], font=('Bookman-Old-Style normal', 15))
    #                 timeshow.place(x=190, y=595)
    #                 timeshow.configure(foreground='white', background='#989492')
    #
    #                 total = Label(t_layer_frame, text="19.Total score:", font=('Bookman-Old-Style normal', 15))
    #                 total.place(x=1, y=630)
    #                 total.configure(foreground='white', background='#989492')
    #                 totalshow = Label(t_layer_frame, text=student[num][19], font=('Bookman-Old-Style normal', 15))
    #                 totalshow.place(x=190, y=630)
    #                 totalshow.configure(foreground='white', background='#989492')
    #
    #                 email = Label(t_layer_frame, text="20.Email Address:", font=('Bookman-Old-Style normal', 15))
    #                 email.place(x=1, y=665)
    #                 email.configure(foreground='white', background='#989492')
    #                 emailshow = Label(t_layer_frame, text=student[num][20], font=('Bookman-Old-Style normal', 15))
    #                 emailshow.place(x=190, y=665)
    #                 emailshow.configure(foreground='white', background='#989492')
    #
    #                 def on_mousewheel(event, canvas):
    #                     # Determine the scroll direction (1 for up, -1 for down)
    #                     delta = -1 if event.delta > 0 else 1
    #
    #                     # Perform the scroll
    #                     canvas.yview_scroll(delta, "units")
    #
    #                 self.binding = [t_layer_frame, d_layer_canvas, on_mousewheel]
    #                 self.bind_widgets()
    #
    #                 ask = Label(self, text="What do you want to change?.",
    #                             font='Bookman-Old-Style 12 normal')
    #                 ask.place(x=700, y=167)
    #                 ask.configure(foreground='white', background='#989492')
    #                 ask1 = Label(self, text="Enter info number?", font='Bookman-Old-Style 12 normal', bg='#989492',
    #                              fg='white')
    #                 ask1.place(x=700, y=195)
    #                 ask_entry = Entry(self, width=30, bd=0)
    #                 ask_entry.place(x=900, y=195)
    #                 ask_entry.bind("<Return>", lambda event: verifyupdate())
    #                 self.err_label = Label(self, text='', font='Bookman-Old-Style 12 bold')
    #                 self.err_label.place(x=700, y=390)
    #                 self.err_label.configure(foreground='red', background='#989492')
    #
    #                 self.widgets_obj = {'canvas': self.d_layer_frame, 'ask': ask, 'ask_entry': ask_entry, 'ask1':
    #                     ask1, 'user_entry': user_entry
    #                                     }
    #                 self.widgets_objx = {'matricshow': matricshow, 'firstnameshow': firstnameshow,
    #                                      'lastnameshow': lastnameshow,
    #                                      'passwordshow': passwordshow, 'phone_numbershow': phone_numbershow,
    #                                      'courseshow': courseshow, "addresswhow": addresshow,
    #                                      'countryshow': countryshow, 'state_of_originshow': state_of_originshow,
    #                                      'stateshow': stateshow, 'cityshow': cityshow,
    #                                      'gendershow': gendershow, 'date_of_birth': date_of_birthshow,
    #                                      'session': sessionshow, 'math': mathshow, 'english': englishshow,
    #                                      'relative_course': relative_courseshow, "time": timeshow, "total": totalshow,
    #                                      "email": emailshow}
    #
    #             else:
    #
    #                 for z in self.widgets_objx:
    #                     self.widgets_objx[z].config(text='')
    #                 self.widgets_objx['matricshow'].config(text=num)
    #
    #                 for i, x in zip(self.widgets_objx, range(len(self.widgets_objx))):
    #                     if i != 'matricshow':
    #                         self.widgets_objx[i].config(text=student[num][x - 1])
    #
    #                     if x == 16:
    #                         dict_xx = {'Art': '17. Literature', 'Science': '17. Biology', 'Commerce': '17. Commerce'}
    #                         self.relative_course.config(text=dict_xx[student[num][4]])
    #                         dict_x = {'17. Literature': student[num][17], '17. Biology': student[num][16],
    #                                   '17. Commerce': student[num][15]}
    #                         self.widgets_objx[i].config(text=dict_x[self.relative_course.cget('text')])
    #                         if 'updatee' in self.widgets_obj:
    #
    #                             if self.new_update == '17':
    #                                 self.widgets_obj['updatee'].configure(
    #                                     text=f"New {''.join(self.relative_course.cget('text').split(' ')[1]).lower()} score")
    #                     if x > 16:
    #                         data = '' if str(student[num][(x - 1) + 2]) == 'None' else student[num][(x - 1) + 2]
    #                         self.widgets_objx[i].config(text=data)
    #
    #             #                THIS IS WHERE THE UPDATE CODE IS
    #
    #             def verifyupdate():
    #                 global updatee, update_entry
    #
    #                 # code to edit the student details
    #                 ans = ask_entry.get().strip()
    #                 if self.err_label:
    #                     self.err_label.config(text='')
    #                 self.option_dicts = {'1': 'matric no', '2': 'first name', '3': 'last name', '4': 'password', '5'
    #                 : 'phone number', '6': 'course', '7': 'address', '8': 'country', '9': 'state of origin', '10'
    #                                      : 'state', '11': 'city', '12': 'gender', '13': 'date of birth',
    #                                      '14': 'session', '15': 'math score', '16': 'english score',
    #                                      '17': ''.join(
    #                                          self.relative_course.cget('text').split(' ')[1]).lower() + ' score',
    #                                      "18": "time", '19': "total score", '20': "email"}
    #                 option_dict = self.option_dicts
    #                 if ans and ans in option_dict:
    #                     self.new_update = ans
    #                     if self.flag:
    #                         update_entry.delete(0, END)
    #                         updatee.configure(text=f"New {option_dict[ans]}")
    #
    #                     else:
    #                         updatee = Label(self, text=f"New {option_dict[ans]}", font='Bookman-Old-Style 12 normal')
    #                         updatee.place(x=700, y=290)
    #                         updatee.configure(foreground='white', background='#989492')
    #                         update_entry = Entry(self, width=30, bd=0)
    #                         update_entry.place(x=900, y=290)
    #
    #                         # code add widgets to dictionary
    #                         self.widgets_obj['updatee'] = updatee
    #                         self.widgets_obj['update_entry'] = update_entry
    #
    #                     def update(data):
    #                         response = {}
    #                         if 'done' in data:
    #                             with open("server_response.json", 'r') as file:
    #                                 response = json.load(file)
    #                         else:
    #                             response = data
    #                         print(response)
    #                         try:
    #                             if response and 'updated' in response.keys():
    #                                 wid = Tk.winfo_x(self.parent) + 500
    #                                 hei = Tk.winfo_y(self.parent) + 200
    #                                 animation_function(self, self.photo9, "Information successfully changed ",
    #                                                    controller.show_frame, 'Editstudent', f'320x300+{wid}+{hei}',
    #                                                    font=('Bookman-Old-Style 10 bold'), )
    #
    #                             else:
    #                                 for i in response:
    #                                     self.destroy_animate()
    #                                     messagebox.showinfo(i, f"{response[i]}")
    #
    #                             update_entry.delete(0, END)
    #                             anss_btn.unbind("<Return>")
    #                         except:
    #                             pass
    #
    #                     label = updatee.cget('text').split(' ')[1]
    #                     info_to_edit = label.replace(' ', '_') if ' ' in label else label
    #
    #                     if info_to_edit in ['last_name', 'first_name', 'matric_no']:
    #                         info_to_edit = info_to_edit.replace('_', '')
    #
    #                     info_to_edit = {1: info_to_edit + ',', 2: '', 3: num}
    #                     if not self.flag:
    #                         anss_btn = Button(self, text="Enter", bd=0, fg='white', bg='#696564',
    #                                           font='Bookman-Old-Style 12 normal', cursor='hand2',
    #                                           command=lambda: self.submit_call(info_to_edit, 'update'))
    #                         anss_btn.bind("<Return>", lambda event: self.submit_call(info_to_edit, 'update'))
    #                         anss_btn.bind("<Enter>", lambda event: on_enter(rec='activate3', variable=anss_btn))
    #                         anss_btn.bind("<Leave>", lambda event: on_leave(rec="deactivate3", variable=anss_btn))
    #                         anss_btn.place(x=720, y=340)
    #                         self.flag = True
    #                         self.widgets_obj['anss_btn'] = anss_btn
    #                     update_entry.bind("<Return>", lambda event: self.submit_call(info_to_edit, 'update'))
    #
    #                     EditStudent.verify_update = update
    #
    #                 def on_enter1(rec):
    #                     if rec == "activate":
    #                         ans_btn.configure(cursor='hand2', bg='#695348')
    #
    #                 def on_leave1(rec):
    #                     if rec == "deactivate":
    #                         ans_btn.configure(cursor='hand2', bg='#696564')
    #
    #                 ans_btn.bind("<Enter>", lambda event: on_enter1(rec='activate'))
    #                 ans_btn.bind("<Leave>", lambda event: on_leave1(rec="deactivate"))
    #
    #             if not self.widget_flag:
    #                 ans_btn = Button(self, text="Enter", bd=0, fg="white", bg='#696564',
    #                                  font='Bookman-Old-Style 12 normal', command=verifyupdate)
    #                 self.widgets_obj['ans_btn'] = ans_btn
    #                 ans_btn.bind("<Return>", lambda event: verifyupdate())
    #                 ans_btn.place(x=720, y=230)
    #                 self.widget_flag = True
    #
    #
    #         elif student and 'info' in student:
    #             if student['info'] == 'Internal error':
    #                 messagebox.showerror('error', f"{student['info']}")
    #
    #         elif student and 'connection error' in student:
    #             self.destroy_animate()
    #             messagebox.showerror('error', f"{student['connection error']}")
    #         elif 'error' in student:
    #             self.destroy_animate()
    #             messagebox.showerror('Application error', f" Check {student['error']} error")
    #         else:
    #             self.destroy_animate()
    #             messagebox.showinfo("Error", "Student does not exist")
    #
    #     EditStudent.s_process = check
    #     Frame.bind(self, "<Enter>", lambda event: entry())
    #     Frame.bind(self, "<Leave>", lambda event: entry1())
    #
    #     # # self.check_btn = Button(self, text="Check", bd=0, fg='white', bg='#696564',
    #     # #                         font='Bookman-Old-Style 12 normal',
    #     # #                         command=lambda: self.submit_call(user_entry.get().strip(), 'check'))
    #     # self.check_btn.place(x=320, y=130)
    #     # self.check_btn.bind("<Enter>", lambda event: on_enter(rec='activate'))
    #     # self.check_btn.bind("<Leave>", lambda event: on_leave(rec="deactivate"))
    #     #
    #     # self.back_btn = Button(self, text="BACK", bd=0, bg='#696564', font='Bookman-Old-Style 12 normal',
    #     #                        command=lambda: self.back(controller))
    #     # self.back_btn.bind("<Enter>", lambda event: on_enter(rec="activate2"))
    #     # self.back_btn.bind("<Leave>", lambda event: on_leave(rec="deactivate2"))
    #     # self.back_btn.place(x=200, y=620)
    #     # self.back_btn.configure(foreground='white', bg='#696564')
    #     # deny_focus(self.children)
    #
        self.configure(background=win_bg)
    #
    # # this code bind the widgets on t_layer_frame
    # def bind_widgets(self):
    #     try:
    #         self.binding[0].bind_all("<MouseWheel>", lambda event: self.binding[2](event, self.binding[1]))
    #     except Exception as e:
    #         pass
    #
    # def submit_call(self, info, type):
    #     global update_entry, flag
    #
    #     if self.err_label:
    #         label = self.err_label
    #         try:
    #             label.config(text='')
    #         except:
    #             pass
    #     statis = {'Nigeria': ['Lagos', 'Kaduna', 'Abuja', 'Osun', 'Delta', 'Oyo', 'Ondo', 'River', 'Anambra',
    #                           'Enugu', 'Kwara', 'Ogun', 'Imo', 'Cross River', 'Kogi', 'Plateau', 'Kano', 'Gombe'],
    #               'Ghana': ['Accra']}
    #     citis = {'Lagos': ['Victoria island', 'Ogba', 'Aguda', 'Ikeja', 'Ikoyi'], 'Kaduna': ['kaduna'],
    #              'Abuja': ['Iyanyan'],
    #              'Osun': ['Osogbo'], "Ondo": ['Akure'], 'Delta': ['Asaba'], 'Oyo': ['Ibadan'],
    #              'River': ['Port harcourt'],
    #              'Anambra': ['Awka'], 'Enugu': ['Enugu'], 'Kwara': ['Ilorin'], 'Plateau': ['Jos']}
    #
    #     if update_entry and isinstance(info, dict):
    #         label1 = ''
    #         if updatee.cget('text').split(' ')[1] in \
    #                 ['math', 'english', ''.join(self.relative_course.cget('text').split(' ')[1]).lower()]:
    #             label1 = updatee.cget('text').split(' ')[1]
    #         else:
    #             label1 = ' '.join(updatee.cget('text').split(' ')[1:])
    #         info_to_edit = label1.replace(' ', '_') if ' ' in label1 else label1
    #         info[1] = info_to_edit + ','
    #
    #         if info_to_edit in ['last_name', 'first_name', 'matric_no']:
    #             info[1] = info_to_edit.replace('_', '') + ','
    #         info[2] = update_entry.get().strip().title().replace(',', '~') + ','
    #         info[3] = self.widgets_obj['user_entry'].get().strip()
    #
    #     # function to call after streaming
    #     class_variable = ''
    #     if type == 'update':
    #         class_variable = EditStudent.verify_update
    #     elif type == 'check':
    #         class_variable = EditStudent.s_process
    #     dict_it = {'Nigeria': ['080', '081', '070', '090'], 'Ghana': []}
    #     matricno = ''.join(self.student.keys()) if self.student else ''
    #     details = self.student[matricno] if self.student else ''
    #     if not info[2].strip(','):
    #         flag = False
    #     else:
    #
    #         if info[1].strip(',') == 'phone_number':
    #             if len(info[2].strip(',')) == 11:
    #                 if not self.student[matricno][6]:
    #                     label.config(text='*Update country before phone number')
    #                     flag = False
    #                 elif info[2][:3] in dict_it[details[6]]:
    #                     flag = True
    #                 else:
    #                     label.config(text='*Invalid Number')
    #                     flag = False
    #             else:
    #                 label.config(text='*Phone number  is not complete')
    #                 flag = False
    #
    #         elif info[1].strip(',') == 'matricno':
    #             if info[2].strip(',')[0] != '6':
    #                 label.config(text='*Invalid matric number')
    #                 flag = False
    #
    #
    #         elif info[1].strip(',') == 'course':
    #             if info[2].strip(',') not in ['Art', 'Commerce', 'Science']:
    #                 label.config(text='*Updated course is not available')
    #                 flag = False
    #         elif info[1].strip(',') == 'country':
    #             if info[2].strip(',') not in ['Nigeria', 'Ghana']:
    #                 label.config(text='*Updated country not allowed')
    #                 flag = False
    #         elif info[1].strip(',') == 'state_of_origin' or info[1].strip(',') == 'state':
    #             cnb = self.student[matricno][6]
    #             if not self.student[matricno][6]:
    #                 label.config(text='*Update country before state')
    #                 flag = False
    #             else:
    #                 if info[2].strip(',') not in statis[cnb]:
    #                     label.config(text='*Updated state not in list')
    #                     flag = False
    #         elif info[1].strip(',') == 'firstname' or info[1].strip(',') == 'lastname':
    #             if not info[2].strip(',').isalpha():
    #                 label.config(text='*Name must be alphabet')
    #                 flag = False
    #
    #         elif info[1].strip(',') == 'gender':
    #             if info[2].strip(',') not in ['Male', 'Female']:
    #                 label.config(text='*Gender must male or female')
    #                 flag = False
    #
    #         elif info[1].strip(',') == 'city':
    #
    #             if not self.student[matricno][6]:
    #                 label.config(text='*Update country and state before city')
    #                 flag = False
    #             elif not self.student[matricno][8]:
    #                 label.config(text='*Update country and state before city')
    #                 flag = False
    #             else:
    #                 if info[2].strip(',').title() not in citis[self.student[matricno][8]]:
    #                     label.config(text='*Updated city not in list')
    #                     flag = False
    #
    #         elif info[1].strip(',') == 'session':
    #             if info[2].strip(',').lower() not in ['true', 'false']:
    #                 label.config(text='*Student session must be boolean value.')
    #                 flag = False
    #
    #         elif info[1].strip(',') == 'date_of_birth':
    #             zii = ['', '-', '', '-', '']
    #             year = [str(i) for i in range(1970, 2010)]
    #             month = {str(i): [str(x) for x in range(1, 32)] for i in range(1, 13)}
    #             month['2'] = [str(i) for i in range(1, 30)]
    #             for z in ['9', '11', '4', '6']:
    #                 month[z] = [str(i) for i in range(1, 31)]
    #             if '-' in info[2].strip(','):
    #                 xii = info[2].strip(',').split('-')
    #                 zii[0], zii[2], zii[4] = xii[0], xii[1], xii[2]
    #
    #                 if ''.join(zii) != info[2].strip(','):
    #                     label.config(text="*date of birth format: eg '1-2-2023'")
    #                     flag = False
    #                 elif zii[4] not in year:
    #                     label.config(text="*Age is not allowed")
    #                     flag = False
    #                 elif zii[2] not in month:
    #                     label.config(text="*Month should be between 1-13 ")
    #                     flag = False
    #                 elif zii[0] not in month[zii[2]]:
    #                     label.config(text="*Date is invalid")
    #                     flag = False
    #             else:
    #                 label.config(text="*Date of birth  format: eg '0-2-2023'")
    #                 flag = False
    #
    #         elif info[1].strip(',') == 'time':
    #             if ':' not in info[2].strip(','):
    #                 label.config(text="*Time example: 0:02")
    #                 flag = False
    #             elif ':' in info[2].strip(','):
    #                 auth_time = info[2].strip(',').split(':')
    #
    #                 if len(auth_time) != 2:
    #                     label.config(text="*Time example: 0:02")
    #                     flag = False
    #                 elif int(auth_time[0]) > 60:
    #                     label.config(text="*Maximum time allowed is 60 mins")
    #                     flag = False
    #                 elif int(auth_time[1]) > 60:
    #                     label.config(text="*60 should be the maximum seconds applied")
    #                     flag = False
    #                 elif len(auth_time[1]) != 2:
    #                     label.config(text="*Time example: 0:02")
    #                     flag = False
    #
    #                 elif len(auth_time[0]) == 2 and int(auth_time[0]) < 10:
    #                     label.config(text="*Time example: 0:02")
    #                     flag = False
    #
    #         elif info[1].strip(',') == 'total_score':
    #             if info[2].strip(',') != '0':
    #                 label.config(text="*Total score should be 0")
    #                 flag = False
    #
    #         elif info[1].strip(',') == 'email':
    #             if info[2].strip(',').lower().endswith('.com'):
    #                 email = info[2].strip(',').lower()
    #                 x = email.split('@') if '@' in email else ''
    #                 y = email.split('.') if '.' in email else ''
    #                 z = x + y
    #                 if len(z) != 4:
    #                     label.config(text="*Email must be this example: Jhondoe@email.com")
    #                     flag = False
    #             elif not info[2].strip(',').lower().endswith('.com'):
    #                 print(info[2].strip(',').lower())
    #                 label.config(text="*Email must be this example: Jhondoe@email.com")
    #                 flag = False
    #
    #         elif type == 'update':
    #             if info[1].strip(',') in ['math', 'english',
    #                                       ''.join(self.relative_course.cget('text').split(' ')[1]).lower()]:
    #                 if info[2].strip(',') != '0':
    #                     label.config(text='*Student score must be zero')
    #                     flag = False
    #
    #     if flag:
    #         if update_entry and isinstance(info, dict):
    #             info[1] = info[1].split("_")[0] + ',' if info[1].strip(',') == 'total_score' else info[1]
    #             info[2] = info[2].lower() if info[1] == 'email,' else info[2]
    #             info = info[1] + info[2] + info[3]
    #         self.animate = Toplevel(self.parent, screen='')
    #         self.animate_canvas = Canvas(self.animate, width=WIDTH, height=HEIGHT, bg="white",
    #                                      highlightbackground='white', bd=0)
    #         wid = Tk.winfo_x(self.parent) + 500
    #         hei = Tk.winfo_y(self.parent) + 200
    #         display_animation(self.animate, self.animate_canvas, f'400x250+{wid}+{hei}')
    #         async_thread = async_Thread(tcp_echo_client(self, '{}#u/894#{}'.format('edit student', info),
    #                                                     class_variable))
    #         async_thread.daemon = True
    #         async_thread.start()
    #
    #         flag = True
    #     else:
    #         messagebox.showerror('Error', 'Check update details for errors')
    #         flag = True
    #
    # def logout(self, controller):
    #
    #     if self.widgets_obj:
    #         for i in self.widgets_obj:
    #             if i == 'user_entry':
    #                 self.widgets_obj[i].delete(0, END)
    #             else:
    #                 self.widgets_obj[i].destroy()
    #
    #         self.flag = False
    #         self.widget_flag = False
    #         if self.err_label:
    #             self.err_label.destroy()

    def back(self, controller):
        controller.show_frame(Adminpickpage, 'backward')
        deny_focus(self.children)

    def destroy_animate(self):
        try:
            self.animate.destroy()
        except:
            pass





