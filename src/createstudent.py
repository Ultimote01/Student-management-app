from tkinter import  Frame,Canvas,IntVar,StringVar,Label,Entry,Button,END,Toplevel
from PIL import Image,ImageTk
from .globalVariables import pwd,win_bg
import tkinter as tk
import tkinter as ttk
import re
import zipfile
from .helper import  deny_focus

class Createstudent(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.var = IntVar()
        self.var.set(0)
        self.country_var = StringVar()
        self.state_var = StringVar()
        self.origin_var = StringVar()
        self.course_var = StringVar()
        self.city_var = StringVar()
        self.country_code = StringVar()
        self.month_var = StringVar()
        self.date_var = StringVar()
        self.year_var = StringVar()
        self.photo = ''
        self.extention = ''
        self.imagepath = ''
        self.err_label1 = {}
        self.animate = ''
        self.animate_canvas = ''
        image = Image.open(pwd + "emoji2.jpg")
        resized_image = image.resize((320, 200), Image.BICUBIC)
        self.photo9 = ImageTk.PhotoImage(resized_image)
        self.parent = controller
        from .adminlandpage import Adminlandpage



        # frame to hold the canvas widget
        frame = tk.Frame(self, bg='black')
        frame.place(x=130, y=70, anchor='nw')

        d_layer_canvas = Canvas(frame, width=1060, height=620, bd=0, highlightbackground='#d0c5c1',
                                bg='#d0c5c1', highlightcolor='#d0c5c1')
        d_layer_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        d_L_LFont = ('sans-serif', 25)
        d_L_EFont = ('sans-serif', 13, 'bold')

        self.d_layer_obj = {'canvas': d_layer_canvas}

        vsb = tk.Scrollbar(self, orient="vertical", command=d_layer_canvas.yview)
        vsb.place(x=1180, y=70, anchor='nw', height=625)

        d_layer_canvas.config(yscrollcommand=vsb.set)
        d_layer_canvas.configure(scrollregion=(0, 0, 0, 800))

        heading = Label(self, text="Registration Form", font=('Times New Roman', 30))
        heading.place(x=128, y=4)
        heading.configure(foreground='black', background=win_bg)
        self.item, self.d_value, self.d_id, self.offtime, self.d_time = '', '', '', 600, ''

        def drawline(canvas, value, y=None, id=None, event=None, flag=False, inline_flag=False):
            global removedFocus
            removedFocus = False

            
            obj = {self.firstname_entry: 30, self.lastname_entry: 90, self.matricno_entry: 150,
                   self.address_entry: 210, self.phone_number_entry: 272, self.password_entry: 332,
                   self.cfm_password_entry: 402, self.email_entry: 472}

            if event:
                if event.send_event and event.state == 1 and event.keysym == 'Tab':

                    if id == self.firstname_entry:
                        y = y - 1
                        inline_flag = True
                        canvas.itemconfigure('tagl', fill='white')
                    elif id == self.cfm_password_entry:
                        y = obj[id] - 71
                    elif id == self.email_entry:
                        y = obj[id] - 66
                    elif id == self.phone_number_entry:
                        y = obj[id] - 63
                    else:
                        y = obj[id] - 61
                    for _ in obj:
                        if obj[_] == (y + 1) or obj[_] == (y - 4):
                            id = _
                    flag = True

                elif 'KeyPress' in str(event) and event.keysym == 'Tab':
                    if id == self.password_entry:
                        y = obj[id] + 74
                    elif id == self.email_entry:
                        y = y - 1
                        inline_flag = True
                        canvas.itemconfigure('tagl', fill='white')
                    elif id == self.cfm_password_entry:
                        y = obj[id] + 69
                    elif id == self.address_entry:
                        y = obj[id] + 61
                    elif id == self.phone_number_entry:
                        y = obj[id] + 59
                    else:
                        y = obj[id] + 59
                    for _ in obj:
                        if obj[_] == (y + 1) or obj[_] == (y - 4):
                            id = _
                    flag = True

            # statement place the line if button is clicked
            elif not event:
                if value == 'clickedin':
                    y -= 1
            if flag:
                if not self.item:
                    if value == 'clickedin':
                        self.y = y
                        self.id = id
                        self.item = canvas.create_line(423, y + 22, 618, y + 22, fill='grey', width=3, tags='tagl')
                elif self.item:
                    if value == 'clickedout':
                        if self.offtime != 1000000:
                            self.id['insertofftime'] = 1000000  # we make the active cursor disappear
                            self.offtime = 1000000
                            canvas.itemconfigure('tagl', fill='white')
                    else:
                        self.y = y
                        self.id = id
                        canvas.coords('tagl', 423, y + 22, 618, y + 22)
                        id['insertofftime'] = 600
                        self.offtime = 600
                        if not inline_flag:
                            canvas.itemconfigure('tagl', fill='grey')

        firstname = Label(d_layer_canvas, text="First Name", font=(d_L_LFont[0], d_L_LFont[1]))
        d_layer_canvas.create_window(70, 10, window=firstname, anchor=tk.NW)
        firstname.configure(foreground='black', background='#d0c5c1')
        self.firstname_entry = Entry(d_layer_canvas, bd=0, font=(d_L_EFont[0], d_L_EFont[1], d_L_EFont[2]))
        d_layer_canvas.create_window(430, 29, window=self.firstname_entry, anchor=tk.NW)
        max_length = 10  # input length
        validation = self.register(lambda P: self.validate_input(P, max_length, 'firstname'))
        self.firstname_entry.config(validate="key", validatecommand=(validation, "%P"))
        self.create_rounded_button(d_layer_canvas, 420, 27, 620, 55, 10, 'white', '', '0', '', '', '')
        self.firstname_entry.bind("<Button-1>",
                                  lambda event: drawline(d_layer_canvas, 'clickedin', 30, self.firstname_entry,
                                                         flag=True))
        self.firstname_entry.bind('<KeyPress>',
                                  lambda event: drawline(d_layer_canvas, 'clickedin', 30, self.firstname_entry,
                                                         event=event))
        self.firstname_entry.bind('<Key>', lambda event: drawline(d_layer_canvas, 'clickedin', 30, self.firstname_entry,
                                                                  event=event))
        # d_layer_canvas.bind("<Button-1>", lambda event: drawline(d_layer_canvas,'clickedout',flag=True))

        lastname = Label(d_layer_canvas, text="Lastname", font=(d_L_LFont[0], d_L_LFont[1]))
        d_layer_canvas.create_window(70, 70, window=lastname, anchor=tk.NW)
        lastname.configure(foreground='black', background='#d0c5c1')
        self.lastname_entry = Entry(d_layer_canvas, bd=0, font=(d_L_EFont[0], d_L_EFont[1], d_L_EFont[2]))
        max_length1 = 10  # input length
        validation1 = self.register(lambda P: self.validate_input(P, max_length1, 'lastname'))
        self.lastname_entry.config(validate="key", validatecommand=(validation1, "%P"))
        d_layer_canvas.create_window(430, 89, window=self.lastname_entry, anchor=tk.NW)
        self.create_rounded_button(d_layer_canvas, 420, 87, 620, 115, 10, 'white', '', '1', '', '', '')
        self.lastname_entry.bind("<Button-1>",
                                 lambda event: drawline(d_layer_canvas, 'clickedin', 90, self.lastname_entry,
                                                        flag=True))
        self.lastname_entry.bind('<KeyPress>',
                                 lambda event: drawline(d_layer_canvas, 'clickedin', 90, self.lastname_entry,
                                                        event=event))
        self.lastname_entry.bind('<Key>', lambda event: drawline(d_layer_canvas, 'clickedin', 90, self.lastname_entry,
                                                                 event=event))

        self.matricno = Label(d_layer_canvas, text="Matric No.", bd=0, font=(d_L_LFont[0], d_L_LFont[1]))
        d_layer_canvas.create_window(70, 130, window=self.matricno, anchor=tk.NW)
        self.matricno.configure(foreground='black', background='#d0c5c1')
        self.matricno_entry = Entry(d_layer_canvas, bd=0, font=(d_L_EFont[0], d_L_EFont[1], d_L_EFont[2]))
        if self.matricno.cget('text') == "Matric No.":
            max_length2 = 7  # input length
        else:
            max_length2 = 8
        validation2 = self.register(lambda P: self.validate_input(P, max_length2, 'matricno'))
        self.matricno_entry.config(validate="key", validatecommand=(validation2, "%P"))
        d_layer_canvas.create_window(430, 149, window=self.matricno_entry, anchor=tk.NW)
        self.create_rounded_button(d_layer_canvas, 420, 147, 620, 175, 10, 'white', '', '2', '', '', '')
        self.matricno_entry.bind("<Button-1>",
                                 lambda event: drawline(d_layer_canvas, 'clickedin', 150, self.matricno_entry,
                                                        flag=True))
        self.matricno_entry.bind('<KeyPress>',
                                 lambda event: drawline(d_layer_canvas, 'clickedin', 150, self.matricno_entry,
                                                        event=event))
        self.matricno_entry.bind('<Key>', lambda event: drawline(d_layer_canvas, 'clickedin', 150, self.matricno_entry,
                                                                 event=event))

        address = Label(d_layer_canvas, text="Home Address", bd=0, font=(d_L_LFont[0], d_L_LFont[1]))
        d_layer_canvas.create_window(70, 190, window=address, anchor=tk.NW)
        address.configure(foreground='black', background='#d0c5c1')
        self.address_entry = Entry(d_layer_canvas, bd=0, font=(d_L_EFont[0], d_L_EFont[1], d_L_EFont[2]))
        max_length3 = 150  # input length
        validation3 = self.register(lambda P: self.validate_input(P, max_length3, 'address'))
        self.address_entry.config(validate="key", validatecommand=(validation3, "%P"))
        d_layer_canvas.create_window(430, 209, window=self.address_entry, anchor=tk.NW)
        self.create_rounded_button(d_layer_canvas, 420, 207, 620, 235, 10, 'white', '', '3', '', '', '')
        self.address_entry.bind("<Button-1>",
                                lambda event: drawline(d_layer_canvas, 'clickedin', 210, self.address_entry, flag=True))
        self.address_entry.bind('<KeyPress>',
                                lambda event: drawline(d_layer_canvas, 'clickedin', 210, self.address_entry,
                                                       event=event))
        self.address_entry.bind('<Key>', lambda event: drawline(d_layer_canvas, 'clickedin', 210, self.address_entry,
                                                                event=event))

        phone_number = Label(d_layer_canvas, text="Phone number", font=(d_L_LFont[0], d_L_LFont[1]))
        d_layer_canvas.create_window(70, 250, window=phone_number, anchor=tk.NW)
        phone_number.configure(foreground='black', background='#d0c5c1')
        self.phone_number_entry = Entry(d_layer_canvas, bd=0, font=(d_L_EFont[0], d_L_EFont[1], d_L_EFont[2]))
        max_length4 = 11  # input length
        validation4 = self.register(lambda P: self.validate_input(P, max_length4, 'phone_number'))
        self.phone_number_entry.config(validate="key", validatecommand=(validation4, "%P"))
        d_layer_canvas.create_window(430, 269, window=self.phone_number_entry, anchor=tk.NW, tags='tagw0')
        self.create_rounded_button(d_layer_canvas, 420, 267, 620, 297, 10, 'white', '', '4', '', '', '')
        self.phone_number_entry.bind("<Button-1>",
                                     lambda event: drawline(d_layer_canvas, 'clickedin', 272, self.phone_number_entry,
                                                            flag=True))
        self.phone_number_entry.bind('<KeyPress>',
                                     lambda event: drawline(d_layer_canvas, 'clickedin', 272, self.phone_number_entry,
                                                            event=event))
        self.phone_number_entry.bind('<Key>',
                                     lambda event: drawline(d_layer_canvas, 'clickedin', 272, self.phone_number_entry,
                                                            event=event))

        password = Label(d_layer_canvas, text="Password", font=(d_L_LFont[0], d_L_LFont[1]))
        d_layer_canvas.create_window(70, 310, window=password, anchor=tk.NW)
        password.configure(foreground='black', background='#d0c5c1')
        self.password_entry = Entry(d_layer_canvas, bd=0, font=(d_L_EFont[0], d_L_EFont[1], d_L_EFont[2]), show='*')
        max_length5 = 20  # input length
        validation5 = self.register(lambda P: self.validate_input(P, max_length5, 'password'))
        self.password_entry.config(validate="key", validatecommand=(validation5, "%P"))
        d_layer_canvas.create_window(430, 329, window=self.password_entry, anchor=tk.NW)
        self.create_rounded_button(d_layer_canvas, 420, 327, 620, 357, 10, 'white', '', '5', '', '', '')
        self.password_entry.bind("<Button-1>",
                                 lambda event: drawline(d_layer_canvas, 'clickedin', 332, self.password_entry,
                                                        flag=True))
        self.password_entry.bind('<KeyPress>',
                                 lambda event: drawline(d_layer_canvas, 'clickedin', 332, self.password_entry,
                                                        event=event))
        self.password_entry.bind('<Key>', lambda event: drawline(d_layer_canvas, 'clickedin', 332, self.password_entry,
                                                                 event=event))

        cfm_password = Label(d_layer_canvas, text="Confirm password", font=(d_L_LFont[0], d_L_LFont[1]))
        d_layer_canvas.create_window(70, 385, window=cfm_password, anchor=tk.NW)
        cfm_password.configure(foreground='black', background='#d0c5c1')
        self.cfm_password_entry = Entry(d_layer_canvas, bd=0, font=(d_L_EFont[0], d_L_EFont[1], d_L_EFont[2]), show='*')
        max_length6 = 20  # input length
        validation6 = self.register(lambda P: self.validate_input(P, max_length6, 'cfm_password'))
        self.cfm_password_entry.config(validate="key", validatecommand=(validation6, "%P"))
        d_layer_canvas.create_window(430, 404, window=self.cfm_password_entry, anchor=tk.NW)
        self.create_rounded_button(d_layer_canvas, 420, 402, 620, 432, 10, 'white', '', '6', '', '', '')
        self.cfm_password_entry.bind("<Button-1>",
                                     lambda event: drawline(d_layer_canvas, 'clickedin', 407, self.cfm_password_entry,
                                                            flag=True))
        self.cfm_password_entry.bind('<KeyPress>',
                                     lambda event: drawline(d_layer_canvas, 'clickedin', 407, self.cfm_password_entry,
                                                            event=event))
        self.cfm_password_entry.bind('<Key>',
                                     lambda event: drawline(d_layer_canvas, 'clickedin', 407, self.cfm_password_entry,
                                                            event=event))

        email = Label(d_layer_canvas, text='Email address', font=(d_L_LFont[0], d_L_LFont[1]))
        d_layer_canvas.create_window(70, 450, window=email, anchor=tk.NW)
        email.configure(foreground='black', background='#d0c5c1')
        self.email_entry = Entry(d_layer_canvas, bd=0, font=(d_L_EFont[0], d_L_EFont[1], d_L_EFont[2]))
        max_length7 = 30  # input length
        validation7 = self.register(lambda P: self.validate_input(P, max_length7, 'email'))
        self.email_entry.config(validate="key", validatecommand=(validation7, "%P"))
        d_layer_canvas.create_window(430, 469, window=self.email_entry, anchor=tk.NW)
        self.create_rounded_button(d_layer_canvas, 420, 467, 620, 497, 10, 'white', '', '7', '', '', '')
        self.email_entry.bind("<Button-1>",
                              lambda event: drawline(d_layer_canvas, 'clickedin', 472, self.email_entry, flag=True))
        self.email_entry.bind('<KeyPress>',
                              lambda event: drawline(d_layer_canvas, 'clickedin', 472, self.email_entry,
                                                     event=event))
        self.email_entry.bind('<Key>', lambda event: drawline(d_layer_canvas, 'clickedin', 472, self.email_entry,
                                                              event=event))

        gender = Label(d_layer_canvas, text="Gender", font=(d_L_LFont[0], d_L_LFont[1]))
        d_layer_canvas.create_window(70, 530, window=gender, anchor=tk.NW)
        gender.configure(foreground='black', background='#d0c5c1')
        r_button = ttk.Radiobutton(d_layer_canvas, text="Male", variable=self.var, value=1)
        d_layer_canvas.create_window(420, 555, window=r_button, anchor=tk.NW)
        r_button1 = ttk.Radiobutton(d_layer_canvas, text="Female", variable=self.var, value=2)
        d_layer_canvas.create_window(500, 555, window=r_button1, anchor=tk.NW)

        self.logout_btn = ttk.Button(self, text='Log out',
                                     cursor='hand2',
                                     command=lambda: controller.show_frame(Adminlandpage, route='logout'))

        self.logout_btn.place(x=1200, y=15)

        # here is where we dynamically option the options base on country selected
        def update_states_menu(*args):

            if args[0] == self.country_var.get():
                selected_country = self.country_var.get()
                selected_state = self.state_var.get()
                self.state_menu['menu'].delete(0, 'end')  # Clear previous options
                self.state_origin_menu['menu'].delete(0, 'end')  # clear previous options

                if selected_country in countries:
                    self.state_var.set('Select State')
                    self.origin_var.set('State of Origin')
                    self.city_var.set('Select City')
                    for state in countries[selected_country]:
                        self.state_menu['menu'].add_command(label=state, command=tk._setit(self.state_var, state, ))
                        self.state_origin_menu['menu'].add_command(label=state,
                                                                   command=tk._setit(self.origin_var, state, ))
            elif args[0] == self.month_var.get():
                selected_month = self.month_var.get()
                self.date_menu['menu'].delete(0, 'end')  # Clear previous options

                if selected_month in month_date:
                    self.date_var.set('date')
                    for date in month_date[selected_month]:
                        self.date_menu['menu'].add_command(label=date, command=tk._setit(self.date_var, date, ))

        def update_city_var(event):
            self.city_var.set('Select City')

        def update_cities_menu(event):

            selected_state = self.state_var.get()
            self.city_menu['menu'].delete(0, 'end')  # Clear previous options

            if selected_state in cities:
                for city in cities[selected_state]:
                    self.city_menu['menu'].add_command(label=city, command=tk._setit(self.city_var, city))

        def update_selection(*args):

            if args[0] and args[0] != '   ':
                if len(self.phone_number_entry.get().strip()) == 11:
                    self.d_layer_obj['canvas'].itemconfigure('tags14', text='')
            elif args[0] and args[0] == '   ':
                if len(self.phone_number_entry.get().strip()) == 11:
                    self.d_layer_obj['canvas'].itemconfigure('tags14',
                                                             text='Select a country code for your number.')

        def upload_photo(canvas):
            global photo
            try:
                get_file = ft.askopenfilename(initialdir='c:\\python31\\',
                                              filetypes=[('jpg(*.jpg)', '*.jpg'), ('png(*.png)', '*.png'),
                                                         ('All files', '*')])
                x = get_file.split('.')
                if app_dir and "An error occurred while creating the directory:" in app_dir:
                    canvas.create_text(750, 250, text="An error occurred while creating the directory:",
                                       fill='red', tags='tagg0')
                elif app_dir:
                    self.extention = x[len(x) - 1]
                    canvas.itemconfigure('tagg0', text='')

                def rounded_button_with_image(width, height, radius, image_path):
                    # Create a new RGBA image with a white background
                    image = Image.new("RGBA", (width, height), (255, 255, 255, 255))
                    draw = ImageDraw.Draw(image)

                    # Draw a rounded rectangle
                    draw.rounded_rectangle(
                        [(0, 0), (width, height)],
                        fill=(255, 0, 0, 255),  # You can change the fill color
                        outline='black',  # No outline
                        radius=radius,
                        width=2
                    )

                    # Open the image to be pasted
                    paste_image = Image.open(image_path)

                    # Create a mask in the shape of the rounded rectangle
                    mask = Image.new("L", (width, height), 0)
                    mask_draw = ImageDraw.Draw(mask)
                    mask_draw.rounded_rectangle(
                        [(0, 0), (width, height)],
                        fill=225,
                        outline='black',
                        radius=radius,
                        width=2
                    )

                    # Resize the image to match the size of the mask
                    paste_image = paste_image.resize((width, height))

                    # Paste the image onto the rounded rectangle using the mask
                    result = Image.new("RGBA", (width, height), (255, 255, 255, 0))
                    result.paste(paste_image, (0, 0), mask)

                    return result

                canvas.delete('tagx10')
                resized_image = rounded_button_with_image(218, 218, 10, get_file)
                canvas.itemconfigure('tags10', text='')
                photo = ImageTk.PhotoImage(resized_image)
                self.photo = photo
                item = canvas.create_image(781, 21, image=photo, anchor=NW, tag='tagx10')
                canvas.tag_bind(item, "<ButtonRelease-1>",
                                lambda event: self.nonactive_rectangle(event, 'buttonrelease2',
                                                                       canvas))
                canvas.tag_bind(item, "<Leave>", lambda event: self.nonactive_rectangle(event, 'leave2', canvas))
                canvas.tag_bind(item, "<Enter>", lambda event: self.active_rectangle(event, 'enter2', canvas))
                self.imagepath = get_file


            except Exception as e:
                print(e)
                messagebox.showinfo('error', 'upload valid image')
                canvas.itemconfigure('tags10', text='Upload Photo')

        self.d_layer_obj['upload_photo'] = upload_photo
        # photo frame
        self.create_rounded_button(d_layer_canvas, 780, 20, 1000, 240, 30, 'white', '', '10', 'black', 'Upload Photo',
                                   'frame')
        self.gender_list = ['', 'Male', 'Female']
        N_state = ['Select State', 'Lagos', 'Kaduna', 'Abuja', 'Osun', 'Delta', 'Oyo', 'Ondo', 'River', 'Anambra',
                   'Enugu', 'Kwara',
                   'Ogun', 'Imo', 'Cross River', 'Kogi', 'Plateau', 'Kano', 'Gombe']
        G_state = ['Select State', 'Accra']
        country_codes = ['', '   ', '+234', '+233']
        month_date = {str(i): '' for i in range(0, 13)}
        for i in month_date:
            if i == '2':
                month_date[i] = [str(i) for i in range(1, 30)]
            elif i == '9' or i == '4' or i == '11' or i == '6':
                month_date[i] = [str(i) for i in range(1, 31)]
            else:
                month_date[i] = [str(i) for i in range(1, 32)]
        year = [''] + [str(i) for i in range(1970, 2010)]

        # Hierarchical dictionary mapping countries to states and states to cities
        countries = {'Select Country': 'Select a Country', 'Nigeria': N_state, 'Ghana': G_state}
        course = ['', 'Course', 'Science', 'Commerce', 'Art']
        cities = {'Lagos': ['Ikeja', 'Victoria island', 'Ogba', 'Aguda'], 'Oyo': ['Ibadan', 'Esehen'],
                  'Accra': ['Kumasi', 'Tema']
            , }
        verify_number = {'+234': ['080', '081', '070', '090'], '+233': ['082', '060', '071']}
        # country and state menu
        # d_layer_canvas.create_arc()
        option_canvas = Canvas(d_layer_canvas, width=500, height=30, bg='#d0c5c1', highlightbackground='#d0c5c1',
                               highlightcolor='#d0c5c1')
        d_layer_canvas.create_window(420, 650, window=option_canvas, anchor=tk.NW)
        # canvas for date menu
        option_canvas1 = Canvas(d_layer_canvas, width=100, height=30, bg='#d0c5c1', highlightbackground='#d0c5c1',
                                highlightcolor='#d0c5c1')
        d_layer_canvas.create_window(420, 610, window=option_canvas1, anchor=tk.NW)

        country_menu = ttk.OptionMenu(option_canvas, self.country_var, *countries.keys(),
                                      command=update_states_menu)
        self.country_var.set("Select Country"), country_menu.grid(row=0, column=0, padx=3)
        self.state_menu = ttk.OptionMenu(option_canvas, self.state_var, 'Select State')
        self.state_menu.bind("<ButtonRelease-1>", update_city_var)
        self.state_var.set('Select State'), self.state_menu.grid(row=0, column=1, padx=3)
        self.state_origin_menu = ttk.OptionMenu(option_canvas, self.origin_var, ' State of Origin')
        self.origin_var.set("State of Origin"), self.state_origin_menu.grid(row=0, column=3, padx=3)
        self.city_menu = ttk.OptionMenu(option_canvas, self.city_var, 'Select City')
        self.city_var.set('Select City'), self.city_menu.grid(row=0, column=2, padx=3)
        self.city_menu.bind("<Button-1>", update_cities_menu)
        course_menu = ttk.OptionMenu(option_canvas, self.course_var, *course)
        self.course_var.set("Course"), course_menu.grid(row=0, column=4, padx=3)
        code_menu = ttk.OptionMenu(d_layer_canvas, self.country_code, *country_codes, command=update_selection)
        self.d_layer_obj['code_menu'] = code_menu
        self.country_code.set('   ')
        self.err_label = ttk.Label(d_layer_canvas, )

        dob_label = ttk.Label(d_layer_canvas, text='Date Of Birth', font=(d_L_LFont[0], d_L_LFont[1]),
                              foreground='black', background='#d0c5c1')
        d_layer_canvas.create_window(70, 600, window=dob_label, anchor=tk.NW)

        month_menu = ttk.OptionMenu(option_canvas1, self.month_var, *month_date.keys(), command=update_states_menu)
        month_menu.grid(row=0, column=0, padx=3), self.month_var.set('month')
        self.date_menu = ttk.OptionMenu(option_canvas1, self.date_var, 'date')
        self.date_menu.grid(row=0, column=1, padx=3), self.date_var.set('date')
        year_menu = ttk.OptionMenu(option_canvas1, self.year_var, *year)
        year_menu.grid(row=0, column=2, padx=3), self.year_var.set('year')
        self.image1 = Image.open(pwd + "eye_1.png")
        self.resized_image1 = self.image1.resize((25, 17), Image.BICUBIC)
        self.photo1 = ImageTk.PhotoImage(self.resized_image1)
        self.show_password = Button(d_layer_canvas, bd=0, image=self.photo1, width=25, height=20,
                                    command=lambda: self.show_passwordd())
        d_layer_canvas.create_window(590, 403, window=self.show_password, anchor=tk.NW)
        self.one = 0
        self.verify_code = ''
        self.user_code = ['0', '0', '0', '0', '0', '0']

        def on_mousewheel(event, canvas):
            # Determine the scroll direction (1 for up, -1 for down)

            delta = -1 if event.delta > 0 else 1

            # Perform the scroll
            canvas.yview_scroll(delta, "units")

        self.binding = [d_layer_canvas, d_layer_canvas, on_mousewheel]

        def change_cursor(value):
            if value == 'Enter':
                self.show_password.configure(cursor='hand2')
            elif value == 'Leave':
                self.show_password.configure(cursor='')

        self.show_password.bind("<Enter>", lambda event: change_cursor('Enter'))
        self.show_password.bind("<Leave>", lambda event: change_cursor('Leave'))

        # Adding students to the database
        def submit1():
            global matric__no, voucher_pass

            v_number = False
            if self.country_code.get() in verify_number:
                if self.phone_number_entry.get().strip()[0:3] in verify_number[self.country_code.get()]:
                    v_number = True

            if self.matricno_entry:
                matric__no = self.matricno_entry.get().strip()

            if self.firstname_entry.get().strip() and self.lastname_entry.get().strip() and matric__no \
                    and self.password_entry.get().strip() and self.address_entry.get().strip() and self.city_var.get() \
                    and self.phone_number_entry.get().strip() and self.gender_list[self.var.get()] and \
                    self.cfm_password_entry.get().strip() and self.country_code.get().title() != '   ' \
                    and self.state_var.get().title() != 'State' and self.origin_var.get().title() != "State of origin" \
                    and self.country_var.get().title() != 'Country' and self.course_var.get().title() != 'Course' \
                    and self.date_var.get() != 'date' and self.month_var.get() != 'month' \
                    and self.year_var.get() != 'year' and self.photo and self.email_entry.get().strip():

                for i in ['tags' + str(i) for i in range(11, 18)]:
                    self.d_layer_obj['canvas'].delete(i)

                if not self.phone_number_entry.get().strip().isnumeric() or \
                        (len(self.phone_number_entry.get().strip())) != 11 or not v_number:
                    self.phone_number_entry.delete(0, END)
                    text = 'Error:it is either phone number is not allowed or incorrect'
                    self.d_layer_obj['canvas'].itemconfigure('tags15', text=text)

                elif self.password_entry.get().strip() != self.cfm_password_entry.get().strip():
                    self.cfm_password_entry.delete(0, END)
                    self.d_layer_obj['canvas'].itemconfigure('tags16', text='Error: password doesn\'t match')

                elif not self.firstname_entry.get().strip().isalpha():
                    self.d_layer_obj['canvas'].itemconfigure('tags11', text='Error: Fistname must alphabet')

                elif not self.lastname_entry.get().strip().isalpha():
                    self.d_layer_obj['canvas'].itemconfigure('tags12', text='Error: Lastname must alphabet')



                else:
                    def code_test():
                        self.verify_code = ''
                        while True:
                            l = [str(i) for i in range(1000)]
                            li = "".join(sample(l, 1))
                            if len(li) > 2:
                                self.verify_code += li[1]
                            elif len(li) == 1:
                                self.verify_code += li
                            if len(self.verify_code) > 5:
                                break

                    if self.matricno.cget('text') == 'Matric No.':
                        if matric__no[0] != '6' and not matric__no.isnumeric() or (len(matric__no)) != 7:
                            if self.matricno_entry:
                                text = 'Error:matric number has to be this example; 6123457'
                                self.d_layer_obj['canvas'].itemconfigure('tags13', text=text)
                        else:
                            code_test()
                            print(self.verify_code)
                            self.verify_email()

                    elif self.matricno.cget('text') == 'Voucher No':
                        if self.matricno_entry.get().strip() != voucher_pass.strip():
                            text = 'Error: Are you sure that number is correct?'
                            self.d_layer_obj['canvas'].itemconfigure('tags13', text=text)
                        else:
                            code_test()
                            print(self.verify_code)
                            self.verify_email()

                    elif self.password_entry.get():
                        if re.match(r'(\w+@[a-z]+\.[a-z]+[a-z]$)', self.email_entry.get().strip()) != None:
                            code_test()
                            print(self.verify_code)
                            self.verify_email()
                        else:
                            self.d_layer_obj['canvas'].itemconfigure('tags17', text='Error: Invalid email address')


                    elif ''.join([self.d_layer_obj['canvas'].itemcget('tags' + str(i)) for i in range(11, 18)]):
                        messagebox.showerror('Error', 'please check if your informations are correct.')

                    else:
                        code_test()
                        print(self.verify_code)
                        self.verify_email()


            else:
                messagebox.showinfo("error", "Scroll down and fill  required spaces")

        def submit(res_data):
            self.student = {}
            global processing_flag, voucher_pass
            if 'done' in res_data:
                with open("server_response.json", 'r') as file:
                    self.student = json.load(file)
            else:
                self.student = res_data

            if self.student:
                s = ''
                for i in self.student.values():
                    s = i
                if not isinstance(s, list):
                    self.destroy_animate()
                    messagebox.showinfo(''.join(self.student.keys()), s)


                else:
                    wid = Tk.winfo_x(self.parent) + 500
                    hei = Tk.winfo_y(self.parent) + 200
                    if self.matricno.cget('text') == 'Voucher No':
                        animation_function(self, self.photo9, "Registration Submitted Successfully",
                                           controller.show_frame, '', f'320x300+{wid}+{hei}',
                                           font=('Bookman-Old-Style 13 bold'))
                    else:
                        animation_function(self, self.photo9, "Student Added Succesfully",
                                           controller.show_frame, '', f'320x300+{wid}+{hei}',
                                           font=('Bookman-Old-Style 13 bold'), )

                    if self.matricno_entry:
                        self.matricno_entry.delete(0, END)
                    self.firstname_entry.delete(0, END)
                    self.password_entry.delete(0, END), self.address_entry.delete(0, END), self.city_var.set(
                        'select City')
                    self.date_var.set('date'), self.month_var.set('month'), self.year_var.set('year')
                    self.phone_number_entry.delete(0, END), self.var.set(0), self.state_var.set('select State')
                    self.origin_var.set('State of origin'), self.country_var.set('Select country')
                    self.d_layer_obj['canvas'].delete('tagx10')
                    self.d_layer_obj['canvas'].itemconfigure('tags10', text='Upload Photo')
                    self.lastname_entry.delete(0, END),
                    self.course_var.set('Select Course'),
                    self.email_entry.delete(0, END)
                    self.cfm_password_entry.delete(0, END)
                    voucher_pass = ''
                    self.phone_number_entry.configure(bg='white'), self.cfm_password_entry.config(bg='white')
                    self.matricno_entry.configure(bg='white'), self.country_code.set('   ')

        # variable of the fucntion submit to use in clientThread class

        Createstudent.s_process = submit
        self.d_layer_obj['submit1'] = submit1

        self.create_rounded_button(d_layer_canvas, 420, 710, 490, 740, 10, '#696564', '', '8', 'white', 'Submit',
                                   'submit')

        b_canvas = Canvas(self, width=80, height=50, highlightcolor=win_bg, highlightbackground=win_bg, bg=win_bg)
        b_canvas.place(x=40, y=600)
        self.create_rounded_button(b_canvas, 2, 2, 60, 34, 10, '#696564', '', '9', 'white', '<-',
                                   'back')
        self.configure(background=win_bg)
        deny_focus(self.children)

    def active_rectangle(self, event, value, canvas):

        clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)  # Get all tags associated with the item
            if value == 'enter':
                if 's' not in tags[0]:
                    canvas.config(cursor='hand2')
                    canvas.itemconfigure(tags[0], fill='#695348')
                elif 's' in tags[0]:
                    canvas.itemconfigure(tags[0].replace('s', ''), fill='#695348')
                    canvas.config(cursor='hand2')

            elif value == 'clicked':
                if 's' not in tags[0]:
                    canvas.itemconfigure(tags[0], fill='#b8b589')
                elif 's' in tags[0]:
                    canvas.itemconfigure(tags[0].replace('s', ''), fill='#b8b589')
            elif value == 'enter1':
                if 's' not in tags[0]:
                    canvas.itemconfigure(tags[0], fill='#695348')
                    canvas.config(cursor='hand2')
                elif 's' in tags[0]:
                    canvas.config(cursor='hand2')
                    canvas.itemconfigure(tags[0].replace('s', ''), fill='#695348')

            elif value == 'clicked1':
                if 's' not in tags[0]:
                    canvas.itemconfigure(tags[0], fill='#b8b589')
                elif 's' in tags[0]:
                    canvas.itemconfigure(tags[0].replace('s', ''), fill='#b8b589')

            elif value == 'enter2':
                canvas.config(cursor='hand2')

    def nonactive_rectangle(self, event, value, canvas):

        clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)  # Get all tags associated with the item
            if value == 'leave':
                if 's' not in tags[0]:
                    canvas.config(cursor='')
                    canvas.itemconfigure(tags[0], fill='#696564')

            elif value == 'buttonrelease':
                if 's' not in tags[0]:
                    canvas.itemconfigure(tags[0], fill='#696564')
                    self.d_layer_obj['submit1']()
                elif 's' in tags[0]:
                    canvas.itemconfigure(tags[0].replace('s', ''), fill='#696564')
                    self.d_layer_obj['submit1']()

            elif value == 'leave1':
                if 's' not in tags[0]:
                    canvas.config(cursor='')
                    canvas.itemconfigure(tags[0], fill='#696564')

            elif value == 'leave2':
                if 's' in tags[0]:
                    canvas.config(cursor='hand2')
                else:
                    canvas.config(cursor='')

            elif value == 'buttonrelease1':
                if 's' not in tags[0]:
                    canvas.itemconfigure(tags[0], fill='#696564')
                    self.back(self.parent)
                elif 's' in tags[0]:
                    canvas.itemconfigure(tags[0].replace('s', ''), fill='#696564')
                    self.back(self.parent)

            elif value == 'buttonrelease2':
                self.d_layer_obj['upload_photo'](canvas)

    def create_rounded_button(self, canvas, x1, y1, x2, y2, radius, background_color, active_fill, tag,
                              text_color, text, type):

        points = [x1 + radius, y1, x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1, x2, y1, x2,
                  y1 + radius,
                  x2, y1 + radius, x2, y1 + radius, x2, y2 - radius, x2, y2 - radius, x2, y2, x2 - radius, y2,
                  x2 - radius, y2, x2 - radius, y2, x1 + radius, y2, x1 + radius, y2, x1, y2, x1, y2 - radius, x1,
                  y2 - radius, x1,
                  y2 - radius, x1, y1 + radius, x1, y1 + radius, x1, y1]

        button = canvas.create_polygon(points, fill=background_color, outline="grey", smooth=True,
                                       tags=f"tag{tag}", activefill=active_fill, width=2)

        if type == 'submit':
            item = canvas.create_polygon(points, fill=background_color, outline="", smooth=True,
                                         tags=f"tag{tag}", activefill=active_fill)
            text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill=text_color, tags=f"tag{tag}s",
                                      font=('Bookman-Old-Style 12 bold'))

            canvas.tag_bind(item, "<Enter>", lambda event: self.active_rectangle(event, 'enter', canvas))
            canvas.tag_bind(item, "<Leave>", lambda event: self.nonactive_rectangle(event, 'leave', canvas))
            canvas.tag_bind(text, "<Enter>", lambda event: self.active_rectangle(event, 'enter', canvas))
            canvas.tag_bind(text, "<Leave>", lambda event: self.nonactive_rectangle(event, 'leave', canvas))
            canvas.tag_bind(item, "<Button-1>", lambda event: self.active_rectangle(event, 'clicked', canvas))
            canvas.tag_bind(text, "<Button-1>", lambda event: self.active_rectangle(event, 'clicked', canvas))
            canvas.tag_bind(item, "<ButtonRelease-1>",
                            lambda event: self.nonactive_rectangle(event, 'buttonrelease', canvas))
            canvas.tag_bind(text, "<ButtonRelease-1>",
                            lambda event: self.nonactive_rectangle(event, 'buttonrelease', canvas))

        if type == 'back':
            item = canvas.create_polygon(points, fill='#696564', outline="", smooth=True, tags=f"tag{tag}")
            text = canvas.create_text(((x1 + x2) / 2) - 5, (y1 + y2) / 2, text=text, fill='white',
                                      font='Bookman-Old-Style 35 normal', tags=f"tags{tag}")
            canvas.tag_bind(item, "<Enter>", lambda event: self.active_rectangle(event, 'enter1', canvas))
            canvas.tag_bind(item, "<Leave>", lambda event: self.nonactive_rectangle(event, 'leave1', canvas))
            canvas.tag_bind(text, "<Enter>", lambda event: self.active_rectangle(event, 'enter1', canvas))
            canvas.tag_bind(text, "<Leave>", lambda event: self.nonactive_rectangle(event, 'leave1', canvas))
            canvas.tag_bind(item, "<Button-1>", lambda event: self.active_rectangle(event, 'clicked1', canvas))
            canvas.tag_bind(text, "<Button-1>", lambda event: self.active_rectangle(event, 'clicked1', canvas))
            canvas.tag_bind(item, "<ButtonRelease-1>", lambda event: self.nonactive_rectangle(event, 'buttonrelease1',
                                                                                              canvas))
            canvas.tag_bind(text, "<ButtonRelease-1>", lambda event: self.nonactive_rectangle(event, 'buttonrelease1',
                                                                                              canvas))

        if type == 'frame':
            item = canvas.create_polygon(points, fill=background_color, outline="grey", smooth=True, tags=f"tag{tag}",
                                         width=5)
            text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill=text_color,
                                      font='Bookman-Old-Style 20 normal', tags=f"tags{tag}")
            canvas.tag_bind(item, "<Enter>", lambda event: self.active_rectangle(event, 'enter2', canvas))
            canvas.tag_bind(item, "<Leave>", lambda event: self.nonactive_rectangle(event, 'leave2', canvas))
            canvas.tag_bind(text, "<Enter>", lambda event: self.active_rectangle(event, 'enter2', canvas))
            canvas.tag_bind(text, "<Leave>", lambda event: self.nonactive_rectangle(event, 'leave2', canvas))
            canvas.tag_bind(item, "<ButtonRelease-1>", lambda event: self.nonactive_rectangle(event, 'buttonrelease2',
                                                                                              canvas))
            canvas.tag_bind(text, "<ButtonRelease-1>", lambda event: self.nonactive_rectangle(event, 'buttonrelease2',
                                                                                              canvas))

    def bindwidgets(self):
        if self.binding:
            self.binding[0].bind_all("<MouseWheel>", lambda event: self.binding[2](event, self.binding[1]))

    def verify_email(self):
        global s_time

        entry_list = []
        s_time = time.strftime("%H:%M:%S").split(":")
        print(s_time)
        top_level = tk.Toplevel(self, bg='black')
        top_level.title('Verify Email')
        top_level.geometry("500x400+200+150")
        top_level.focus()
        top_level.grab_set()
        label = tk.Label(top_level, bg='black', font=('Bookman-Old-Style bold', 30))
        label.place(x=100, y=80)
        label1 = tk.Label(top_level, text='Enter six digits code sent to  your email.', bg='black',
                          font=('Bookman-Old-Style bold', 15), fg='white')
        label1.place(x=100, y=30)

        x = 20
        y = 150

        for i in range(6):
            entry = tk.Entry(top_level, width=2, font=('Bookman-Old-Style bold', 20))
            entry.place(x=x, y=y)
            if i > 0:
                entry.config(state='disabled')
            entry_list.append(entry)
            x += 80
        try:
            entry_list[0].bind("<Key>", lambda event: get_value(event, entry_list[0]))
            entry_list[1].bind("<Key>", lambda event: get_value(event, entry_list[1]))
            entry_list[2].bind("<Key>", lambda event: get_value(event, entry_list[2]))
            entry_list[3].bind("<Key>", lambda event: get_value(event, entry_list[3]))
            entry_list[4].bind("<Key>", lambda event: get_value(event, entry_list[4]))
            entry_list[5].bind("<Key>", lambda event: get_value(event, entry_list[5]))
        except:
            pass

        def get_value(event, widget):
            global s_time

            if event.keysym.isnumeric():
                widget.delete(0, tk.END)

                if str(widget) == str(entry_list[0]):
                    self.user_code[0] = event.keysym
                    entry_list[1].config(state='normal')
                    entry_list[1].focus()
                elif str(widget) == str(entry_list[1]):
                    self.user_code[1] = event.keysym
                    entry_list[2].config(state='normal')
                    entry_list[2].focus()
                elif str(widget) == str(entry_list[2]):
                    self.user_code[2] = event.keysym
                    entry_list[3].config(state='normal')
                    entry_list[3].focus()
                elif str(widget) == str(entry_list[3]):
                    self.user_code[3] = event.keysym
                    entry_list[4].config(state='normal')
                    entry_list[4].focus()
                elif str(widget) == str(entry_list[4]):
                    self.user_code[4] = event.keysym
                    entry_list[5].config(state='normal')
                    entry_list[5].focus()
                elif str(widget) == str(entry_list[5]):
                    self.user_code[5] = event.keysym
                    if ''.join(self.user_code) == self.verify_code:
                        e_time = time.strftime("%H:%M:%S").split(":")

                        if int((e_time)[1]) > int((s_time)[1]) + 2:
                            label.config(text='!!Timed out , Resend code.', fg='red',
                                         font=('Bookman-Old-Style bold', 20))

                        elif int((e_time)[1]) <= int((s_time)[1]) + 2:
                            label.config(text='', bg='black')
                            self.submit_call_caller()
                            self.verify_code = ['0', '0', '0', '0', '0', '0']
                            s_time = ''
                            top_level.destroy()

                    else:
                        label.config(text='!!Wrong Code', fg='red')

            elif event.keysym == 'BackSpace':
                for i in range(2, 7):
                    if str(widget).endswith(str(i)):
                        entry_list[i - 2].focus()

                wii = str(widget)
                index = 1 if wii[len(wii) - 1] == 'y' else int(wii[len(wii) - 1])
                self.user_code[index - 1] = '0'
                if sum([int(i) for i in self.verify_code]) == 0:
                    label.config(text='', bg='black')

        def resend_code():
            global s_time

            self.verify_code = ''
            while True:
                l = [str(i) for i in range(1000)]
                li = "".join(sample(l, 1))
                if len(li) > 2:
                    self.verify_code += li[1]
                elif len(li) == 1:
                    self.verify_code += li
                if len(self.verify_code) > 5:
                    break
            s_time = time.strftime("%H:%M:%S").split(":")
            print(s_time, self.verify_code)

        def change_email():
            global s_time
            s_time = ''
            top_level.destroy()

        button = tk.Button(top_level, text='Resend code', bd=0, bg='purple', fg='white',
                           font=('Bookman-Old-Style bold', 12), command=resend_code)
        button.place(x=50, y=320)
        button1 = tk.Button(top_level, text='Change Email', bd=0, bg='brown', fg='white',
                            font=('Bookman-Old-Style bold', 12),
                            command=change_email)
        button1.place(x=350, y=320)

    def validate_input(self, P, max_length, widget):

        if widget == 'firstname':
            if len(str(P)) == 0 or str(P).isalpha():
                self.d_layer_obj['canvas'].itemconfigure('tag0', outline='grey', width=2)
                self.d_layer_obj['canvas'].itemconfigure('tags11', text='')

            elif not str(P).isalpha():
                self.d_layer_obj['canvas'].itemconfigure('tag0', outline='red', width=3)
                self.d_layer_obj['canvas'].create_text(430, 60, text='Alphabet only', fill='red', tag='tags11',
                                                       font=('Bookman-Old-Style 10 bold', 10), anchor=tk.NW)

        elif widget == 'lastname':
            if len(str(P)) == 0 or str(P).isalpha():
                self.d_layer_obj['canvas'].itemconfigure('tag1', outline='grey', width=2)
                self.d_layer_obj['canvas'].itemconfigure('tags12', text='')

            elif not str(P).isalpha():
                self.d_layer_obj['canvas'].itemconfigure('tag1', outline='red', width=3)
                self.d_layer_obj['canvas'].create_text(430, 120, text='Alphabet only', fill='red', tag='tags12',
                                                       font=('Bookman-Old-Style 10 bold', 10), anchor=tk.NW)

        elif widget == 'matricno':
            if len(str(P)) == 0 or str(P).isnumeric():
                if len(str(P)) > 0:

                    if self.matricno.cget('text') == "Matric No." and str(P)[0] != '6':
                        text = 'Matricno must be index of 6 and 7 digits.'
                        self.d_layer_obj['canvas'].itemconfigure('tag2', outline='red', width=3)
                        self.d_layer_obj['canvas'].create_text(430, 180, text=text, fill='red', tag='tags13',
                                                               font=('Bookman-Old-Style 10 bold', 10), anchor=tk.NW)
                    elif self.matricno.cget('text') == 'Voucher No':
                        if str(P)[:3] != '527':
                            self.d_layer_obj['canvas'].itemconfigure('tag2', outline='red', width=3)
                            text = 'Please enter 8 digits voucher number'
                            self.d_layer_obj['canvas'].create_text(430, 180, text=text, fill='red', tag='tags13',
                                                                   font=('Bookman-Old-Style 10 bold', 10), anchor=tk.NW)

                        elif str(P)[:3] == '527':
                            self.d_layer_obj['canvas'].itemconfigure('tag2', outline='grey', width=2)
                            self.d_layer_obj['canvas'].itemconfigure('tags13', text='')

                elif len(str(P)) == 0:
                    self.d_layer_obj['canvas'].itemconfigure('tag2', outline='grey', width=2)
                    self.d_layer_obj['canvas'].itemconfigure('tags13', text='')


            elif not str(P).isnumeric():
                self.d_layer_obj['canvas'].itemconfigure('tag2', outline='red', width=3)
                if self.matricno.cget('text') == "Matric No.":
                    text = 'Matricno should consist of 7 unique numbers.'
                    self.d_layer_obj['canvas'].itemconfigure('tag2', outline='red', width=3)
                    self.d_layer_obj['canvas'].create_text(430, 180, text=text, fill='red', tag='tags13',
                                                           font=('Bookman-Old-Style 10 bold', 10), anchor=tk.NW)

                elif self.matricno.cget('text') == 'Voucher No':
                    text = 'Please enter 8 digits voucher number'
                    self.d_layer_obj['canvas'].itemconfigure('tag2', outline='red', width=3)
                    self.d_layer_obj['canvas'].create_text(430, 180, text=text, fill='red', tag='tags13',
                                                           font=('Bookman-Old-Style 10 bold', 10), anchor=tk.NW)

        elif widget == 'phone_number':

            if len(str(P)) == 0 or str(P).isnumeric():
                if len(str(P)) == max_length or len(str(P)) == 0:
                    self.d_layer_obj['canvas'].itemconfigure('tag4', outline='grey', width=2)
                    self.d_layer_obj['canvas'].itemconfigure('tags14', text='')
                    self.d_layer_obj['canvas'].create_window(-100, 270, window=self.d_layer_obj['code_menu'],
                                                             anchor=tk.NW)
                    self.d_layer_obj['canvas'].coords('tagw0', 440, 269)

                    if not self.country_code.get().strip() and len(str(P)) == 11:
                        text = 'Select a country code for your number'
                        self.d_layer_obj['canvas'].itemconfigure('tags14', text=text)
                    elif self.country_code.get().strip():
                        self.d_layer_obj['canvas'].itemconfigure('tags14', text='')



                elif len(str(P)) > 0 and len(str(P)) < max_length:
                    self.d_layer_obj['canvas'].itemconfigure('tags14', text='')
                    self.phone_number_entry.config(width=14)
                    self.d_layer_obj['canvas'].coords('tagw0', 475, 269)
                    self.d_layer_obj['canvas'].create_window(425, 270, window=self.d_layer_obj['code_menu'],
                                                             anchor=tk.NW)
                    text = 'Mobile number should be 11 numerical digits'
                    self.d_layer_obj['canvas'].itemconfigure('tag4', outline='red', width=3)
                    self.d_layer_obj['canvas'].create_text(430, 300, text=text, fill='red', tag='tags14',
                                                           font=('Bookman-Old-Style 10 bold', 10), anchor=tk.NW)


            elif not str(P).isnumeric() or len(str(P)) != max_length:
                self.d_layer_obj['canvas'].itemconfigure('tags14', text='')
                text = 'Mobile number should be 11 numerical digits'
                self.d_layer_obj['canvas'].itemconfigure('tag4', outline='red', width=0)
                self.d_layer_obj['canvas'].create_text(430, 300, text=text, fill='red', tag='tags14',
                                                       font=('Bookman-Old-Style 10 bold', 10), anchor=tk.NW)

            if len(str(P)) == max_length:
                self.d_layer_obj['canvas'].coords('tagw0', 475, 269)
                self.d_layer_obj['canvas'].create_window(425, 270, window=self.d_layer_obj['code_menu'], anchor=tk.NW)


        elif widget == 'password':

            res = re.findall(r'[^a-z0-9]+', str(P))
            if len(str(P)) == 0 or len(str(P)) >= 8:
                if not res:
                    self.d_layer_obj['canvas'].itemconfigure('tag5', outline='grey', width=2)
                    self.d_layer_obj['canvas'].itemconfigure('tags15', text='')
                elif res:
                    text = '*Password must be 8 characters long.\n*Numbers and alphabets.'
                    self.d_layer_obj['canvas'].itemconfigure('tag5', outline='red', width=3)
                    self.d_layer_obj['canvas'].create_text(420, 360, text=text, fill='red', tag='tags15',
                                                           font=('Bookman-Old-Style 10 bold', 10), anchor=tk.NW)

            elif res or len(str(P)) < 8:
                text = '*Password must be 8 characters long.\n*Numbers and alphabets.'
                self.d_layer_obj['canvas'].itemconfigure('tag5', outline='red', width=3)
                self.d_layer_obj['canvas'].create_text(420, 360, text=text, fill='red', tag='tags15',
                                                       font=('Bookman-Old-Style 10 bold', 10), anchor=tk.NW)


        elif widget == 'cfm_password':

            if len(str(P)) == 0:
                self.d_layer_obj['canvas'].itemconfigure('tag6', outline='grey', width=2)
                self.d_layer_obj['canvas'].itemconfigure('tags16', text='')

            elif len(self.password_entry.get().strip()) == len(str(P)):
                if self.password_entry.get().strip() == str(P):
                    self.d_layer_obj['canvas'].itemconfigure('tag6', outline='grey', width=2)
                    self.d_layer_obj['canvas'].itemconfigure('tags16', text='')
                else:
                    self.d_layer_obj['canvas'].itemconfigure('tag6', outline='red', width=3)
                    self.d_layer_obj['canvas'].create_text(420, 440, text='*Password does not match', fill='red',
                                                           tag='tags16',
                                                           font=('Bookman-Old-Style 10 bold', 10), anchor=tk.NW)


            elif len(self.password_entry.get().strip()) != len(str(P)):
                self.d_layer_obj['canvas'].itemconfigure('tag6', outline='red', width=3)
                self.d_layer_obj['canvas'].create_text(420, 440, text='*Password does not match', fill='red',
                                                       tag='tags16', font=('Bookman-Old-Style 10 bold', 10),
                                                       anchor=tk.NW)

        elif widget == 'email':
            res = re.match(r'(\w+@[a-z]+\.[a-z]+[a-z]$)', str(P))

            if len(P) == 0:
                self.d_layer_obj['canvas'].itemconfigure('tag7', outline='grey', width=2)
                self.d_layer_obj['canvas'].itemconfigure('tags17', text='')

            elif res == None:
                text = '*email must look like this (amanda@gmail.com)'
                self.d_layer_obj['canvas'].itemconfigure('tag7', outline='red', width=3)
                self.d_layer_obj['canvas'].create_text(420, 500, text=text, fill='red',
                                                       tag='tags17', font=('Bookman-Old-Style 10 bold', 12),
                                                       anchor=tk.NW)
            elif res != None:
                self.d_layer_obj['canvas'].itemconfigure('tag7', outline='grey', width=2)
                self.d_layer_obj['canvas'].itemconfigure('tags17', text='')

        return len(P) <= max_length  # code set the max length

    def submit_call_caller(self):
        print('running')
        char_list = ['/', '!', '{', '}', ']', '[', '=', '(', ')', "%", '#', '!', '^', '*', '~', '`', '|', '/', ";"]
        x, xi, xii, xiii = matric__no, self.firstname_entry.get().title().strip(), \
            self.lastname_entry.get().title().strip(), self.password_entry.get().strip()
        y, yi, yii, yiii = re.sub(r"[^\w\,\s]|\_", '', self.address_entry.get().strip()), self.city_var.get(), \
            self.phone_number_entry.get(), self.gender_list[self.var.get()]
        z, zi, zii, ziii, z4 = self.state_var.get(), self.origin_var.get(), \
            self.country_var.get(), self.course_var.get(), self.email_entry.get().strip()
        zxx = self.date_var.get() + "-" + self.month_var.get() + "-" + self.year_var.get()
        for _ in char_list:
            y = y.replace(_, '')

        info = f"'{x}','{xi}','{xii}','{xiii}','{yii}','{ziii}','{y}','{zii}','{zi}','{z}','{yi}','{yiii}','{zxx}','{z4}'"
        self.submit_call(info)

    def submit_call(self, info):
        global matric_no
        if self.matricno_entry:
            matric_no = self.matricno_entry.get().strip()

        zip_filename = f"client_{1009}_{901}.zip"
        self.create_zip_archive(zip_filename, [self.imagepath])

        with open(zip_filename, 'rb') as file:
            image = file.read()

        self.animate = Toplevel(self.parent, screen='')
        self.animate_canvas = Canvas(self.animate, width=WIDTH, height=HEIGHT, bg="white",
                                     highlightbackground='white', bd=0)
        wid = Tk.winfo_x(self.parent) + 500
        hei = Tk.winfo_y(self.parent) + 200
        display_animation(self.animate, self.animate_canvas, f'400x250+{wid}+{hei}')
        async_thread = async_Thread(tcp_echo_client(self, '{}#u/894#{}#u/894#{}'.format('create student', info, image),
                                                    Createstudent.s_process))
        async_thread.daemon = True
        async_thread.start()
        os.remove(zip_filename)

    # create a temporary zipfile for media file transfer
    def create_zip_archive(self, zip_filename, files_to_compress):
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_to_compress in files_to_compress:
                zipf.write(file_to_compress, os.path.basename('{}.{}'.format(matric_no, self.extention)))

    def show_passwordd(self):

        if self.one == 0:
            self.password_entry.configure(show="")
            self.cfm_password_entry.configure(show="")
            self.one += 1
        elif self.one == 1:
            self.password_entry.configure(show="*")
            self.cfm_password_entry.configure(show="*")
            self.one -= 1

    def logout(self, controller):
        global voucher_pass
        if self.matricno_entry:
            self.matricno_entry.delete(0, END)
        self.date_var.set('date'), self.month_var.set('month'), self.year_var.set('year')
        self.firstname_entry.delete(0, END), self.lastname_entry.delete(0, END)
        self.password_entry.delete(0, END), self.address_entry.delete(0, END), self.city_var.set('Select City')
        self.phone_number_entry.delete(0, END), self.var.set(0), self.state_var.set('select State')
        self.origin_var.set('State of origin'), self.country_var.set('select Country')
        self.course_var.set('Select Course'), self.cfm_password_entry.delete(0, END)
        self.email_entry.delete(0, END), self.d_layer_obj['canvas'].delete('tagx10')
        self.phone_number_entry.configure(bg='white'), self.cfm_password_entry.config(bg='white')
        self.matricno_entry.configure(bg='white'), self.country_code.set('   ')
        voucher_pass = ''
        self.d_layer_obj['canvas'].itemconfigure('tags10', text='Upload Photo')
        if self.err_label.focus_get():
            self.err_label.destroy()
        self.password_entry.unbind("<Return>"),

    def back(self, controller):
        from .adminpickpagev1 import Adminpickpage
        controller.show_frame(Adminpickpage, route='backward')
        deny_focus(self.children)

    def destroy_animate(self):
        try:
            self.animate.destroy()
        except:
            pass

