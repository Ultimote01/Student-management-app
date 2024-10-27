import tkinter as tk
from random import *
import time

verify_code=[0,0,0,0,0,0]
s_time=''

def update_animation():
    global s_time
    entry_list = []
    s_time=time.strftime("%H:%M:%S").split(":")
    print(s_time)
    top_level = tk.Toplevel(root,bg='black')
    top_level.title('Verify Email')
    top_level.geometry("500x400+200+150")
    label=tk.Label(top_level,bg='black',font=('Bookman-Old-Style bold',30))
    label.place(x=100,y=80)
    label1 = tk.Label(top_level,text='Enter six digits code sent to  your email.',bg='black',
                      font=('Bookman-Old-Style bold', 15),
                      fg='white')
    label1.place(x=100, y=30)

    x = 20
    y = 150

    for i in range(6):
        entry = tk.Entry(top_level, width=2, font=('Bookman-Old-Style bold',20))
        entry.place(x=x,y=y)
        if i > 0:
            entry.config(state='disabled')
        entry_list.append(entry)
        x+=80


    entry_list[0].bind("<Key>",lambda event:get_value(event,entry_list[0]))
    entry_list[1].bind("<Key>", lambda event: get_value(event, entry_list[1]))
    entry_list[2].bind("<Key>", lambda event: get_value(event, entry_list[2]))
    entry_list[3].bind("<Key>", lambda event: get_value(event, entry_list[3]))
    entry_list[4].bind("<Key>", lambda event: get_value(event, entry_list[4]))
    entry_list[5].bind("<Key>", lambda event: get_value(event, entry_list[5]))

    def get_value(event, widget):
        global verify_code,s_time

        if root.focus_get():
           print('yes')

        if event.keysym.isnumeric():
            widget.delete(0,tk.END)


            if str(widget) == ".!toplevel.!entry":
                verify_code[0]=event.keysym
                entry_list[1].config(state='normal')
                entry_list[1].focus()
            elif str(widget) == ".!toplevel.!entry2":
                verify_code[1] = event.keysym
                entry_list[2].config(state='normal')
                entry_list[2].focus()
            elif str(widget) == ".!toplevel.!entry3":
                verify_code[2] = event.keysym
                entry_list[3].config(state='normal')
                entry_list[3].focus()
            elif str(widget) == ".!toplevel.!entry4":
                verify_code[3] = event.keysym
                entry_list[4].config(state='normal')
                entry_list[4].focus()
            elif str(widget) == ".!toplevel.!entry5":
                verify_code[4] = event.keysym
                entry_list[5].config(state='normal')
                entry_list[5].focus()
            elif str(widget) == ".!toplevel.!entry6":
                verify_code[5] = event.keysym
                if ''.join(verify_code) == num:
                    e_time=time.strftime("%H:%M:%S").split(":")

                    if int((e_time)[1]) > int((s_time)[1])+2:
                        label.config(text='!!Timed out , Resend code.', fg='red',font=('Bookman-Old-Style bold',20))

                    elif int((e_time)[1]) <= int((s_time)[1])+2:
                        label.config(text='',bg='black')
                        verify_code = [0, 0, 0, 0, 0, 0]
                        s_time = ''
                        root.destroy()

                else:
                    label.config(text='!!Wrong Code',fg='red')

        elif event.keysym =='BackSpace':
            for i in range(2,7):
                if str(widget).endswith(str(i)):
                    entry_list[i-2].focus()

            wii=str(widget)
            index=1 if wii[len(wii)-1] == 'y' else int(wii[len(wii)-1])
            verify_code[index-1]=0
            if sum([int(i) for i in verify_code]) == 0:
                label.config(text='', bg='black')


    def resend_code():
        global num,s_time
        num=''
        while True:
            l = [str(i) for i in range(1000)]
            li = "".join(sample(l, 1))
            if len(li) > 2:
                num += li[1]
            elif len(li) == 1:
                num += li
            if len(num) > 5:
                break
        s_time = time.strftime("%H:%M:%S").split(":")
        print(s_time,num)
    def change_email():
        global verify_code,s_time
        verify_code = [0, 0, 0, 0, 0, 0]
        s_time = ''
        root.destroy()

    button = tk.Button(top_level, text='Resend code', bd=0, bg='purple', fg='white',
                           font=('Bookman-Old-Style bold', 12),command=resend_code)
    button.place(x=50, y=320)
    button1 = tk.Button(top_level, text='Change Email', bd=0, bg='brown', fg='white',font=('Bookman-Old-Style bold', 12),
                        command=change_email)
    button1.place(x=350, y=320)

root = tk.Tk()
root.title("Main window")
root.geometry('100x100+20+10')

num = ''
while True:
    l = [str(i) for i in range(1000)]
    li = "".join(sample(l, 1))
    if len(li) > 2:
        num += li[1]
    elif len(li) == 1:
        num += li
    if len(num) > 5:
        break

print(num)
update_animation()
root.mainloop()



