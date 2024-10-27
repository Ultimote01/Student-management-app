class English():
    verify=''
    top_level_object=''
    def __init__(self, parent, controller):

        self.parent = parent
        self.top_level = Toplevel(parent, bg='white')
        self.top_level.geometry("1200x500+100+90")
        self.top_level.wm_title('English')
        self.top_level.withdraw()
        self.label = Label(self.top_level, text='', width=7, bg='white', fg='black', font='Bookman-Old-Style 12 bold')
        self.label.place(x=1100, y=15)
        self.var = IntVar()
        self.var.set(0)

        self.control = controller
        self.label1 = Label(self.top_level, text='QUESTIONS:', bg='white', fg='black', font='Bookman-Old-Style 20 bold')
        self.label1.place(x=40, y=50)

        self.label2 = Label(self.top_level, text='', bg='white', fg='grey', font='Bookman-Old-Style 16 bold')
        self.label2.place(x=40, y=110)

        self.label3 = Label(self.top_level, text='OPTIONS:', bg='white', fg='black', font='Bookman-Old-Style 20 bold')
        self.label3.place(x=40, y=170)

        self.option1 = Radiobutton(self.top_level, text="", variable=self.var, value=1,
                                   font='Bookman-Old-Style 13 bold',
                                   bg='white', fg='grey')
        self.option1.place(x=40, y=230)

        self.option2 = Radiobutton(self.top_level, text="", variable=self.var, value=2, font='Bookman-Old-Style 13 bold'
                                   , bg='white', fg='grey')
        self.option2.place(x=40, y=290)

        self.option3 = Radiobutton(self.top_level, text="", variable=self.var, value=3, font='Bookman-Old-Style 13 bold'
                                   , bg='white', fg='grey')
        self.option3.place(x=40, y=350)

        self.previous = Button(self.top_level, text='Previous', bg='lightgrey', fg='black',
                               cursor='hand2', font='Bookman-Old-Style 14 bold', bd=0, command=self.previous_q)
        self.previous.place(x=40, y=430)

        self.next = Button(self.top_level, text='Next', bg='lightgrey', fg='black',
                           cursor='hand2', font='Bookman-Old-Style 14 bold', bd=0, command=self.next_q)
        self.next.place(x=1000, y=430)

        self.previous.bind("<Enter>", lambda event: on_enter({'previous': self.previous}))
        self.next.bind("<Enter>", lambda event: on_enter({'next': self.next}))
        self.previous.bind("<Leave>", lambda event: on_leave({'previous': self.previous}))
        self.next.bind("<Leave>", lambda event: on_leave({'next': self.next}))
        self.opt_list = [0, 0, 0, 0, 0]
        self.ans = []
        self.score = [0, 0, 0, 0, 0]
        self.list = []
        self.switch = False
        English.top_level_object=self.top_level

        def verify(data):
            if self.switch:
                module2.Animation.toplevel.grab_release()
                info = data
                module2.Animation.toplevel.destroy()
                if info:
                    for j in info:
                        if j == 'updated':
                            messagebox.showinfo('', "you scored {} marks.".format(sum(self.score)))
                            self.top_level.destroy()
                            self.parent.english_btn.config(state='disabled')
                            self.switch = False
                            if 0 not in total_score:
                                result=sum(total_score)
                                messagebox.showinfo('Result','Your total score is {}'.format(result))
                        else:
                            messagebox.showerror('', 'Try again.')
                            self.switch = False

            else:
                self.top_level.destroy()
        English.verify=verify

        def quitter_function():
            English.top_level_object = ''
            self.top_level.destroy()

        self.top_level.protocol('WM_DELETE_WINDOW', lambda: quitter_function())

    def update_widget(self):
        global exam_no1

        for quest, i in zip(exam_json['english_quest'], range(len(exam_json['english_quest']))):
            if i == exam_no1:
                self.label2.config(text="{}: {}".format(quest, exam_json['english_quest'][quest]))

        for questx, x in zip(exam_json['english_opt'], range(len(exam_json['english_opt']))):
            if x == exam_no1:
                self.option1.config(text="{}: {}".format(questx, exam_json['english_opt'][questx][0]))
                self.option2.config(text="{}: {}.".format(questx, exam_json['english_opt'][questx][1]))
                self.option3.config(text="{}: {}".format(questx, exam_json['english_opt'][questx][2]))
                self.list.append(exam_json['english_opt'][questx][0])
                self.list.append(exam_json['english_opt'][questx][1])
                self.list.append(exam_json['english_opt'][questx][2])
        self.ans = [exam_json['english_ans'][i] for i in exam_json['english_ans']]



    def next_q(self):
        global submit_flag,exam_no1

        if exam_no1 <=3:
            exam_no1+=1

            if exam_no1 == 4:
                self.next.config(text='Done')
            for quest, i in zip(exam_json['english_quest'], range(len(exam_json['english_quest']))):
                if i == exam_no1:
                    self.label2.config(text="{}: {}".format(quest, exam_json['english_quest'][quest]))
            if self.var.get() > 0:
                if (self.list[self.var.get() - 1]) == self.ans[exam_no1 - 1]:
                    self.score[exam_no1 - 1] = 10

            self.list = []
            for questx, x in zip(exam_json['english_opt'], range(len(exam_json['english_opt']))):
                if x == exam_no1:
                    self.option1.config(text="{}: {}".format('1', exam_json['english_opt'][questx][0]))
                    self.option2.config(text="{}: {}.".format('2', exam_json['english_opt'][questx][1]))
                    self.option3.config(text="{}: {}".format('3', exam_json['english_opt'][questx][2]))
                    self.list.append(exam_json['english_opt'][questx][0])
                    self.list.append(exam_json['english_opt'][questx][1])
                    self.list.append(exam_json['english_opt'][questx][2])

            self.opt_list[exam_no1 - 1] = self.var.get()

            self.var.set(0)
        elif exam_no1 > 3:
            submit_flag = True
            self.switch = True
            score = sum(self.score) if sum(self.score) >= 10 else 1
            global total_score
            total_score[1]=score
            info = "english,{},{}".format(score, matricno)
            asyncio.run(tcp_echo_client(self.parent, '{}#u/894#{}'.format('edit student', info),
                                        English.verify))


    def previous_q(self):
        global exam_no1

        if  exam_no1 > 0:
            exam_no1 -= 1
        if exam_no1 < 4:
            self.next.config(text='Next')
        self.score[exam_no1] = 0
        for quest, i in zip(exam_json['english_quest'], range(len(exam_json['english_quest']))):
            if i == exam_no1:
                self.label2.config(text="{}: {}".format(quest, exam_json['english_quest'][quest]))
        self.list=[]
        for questx, x in zip(exam_json['english_opt'], range(len(exam_json['english_opt']))):
            if x == exam_no1:
                self.option1.config(text="{}: {}".format(1, exam_json['english_opt'][questx][0]))
                self.option2.config(text="{}: {}.".format(2, exam_json['english_opt'][questx][1]))
                self.option3.config(text="{}: {}".format(3, exam_json['english_opt'][questx][2]))
                self.list.append(exam_json['english_opt'][questx][0])
                self.list.append(exam_json['english_opt'][questx][1])
                self.list.append(exam_json['english_opt'][questx][2])


        self.var.set(self.opt_list[exam_no1])

