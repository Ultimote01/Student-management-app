import json
import tkinter as tk
from tkinter import messagebox, Frame,Tk
import os,sys



from src.landingpage import  Landingpage
from src.adminlandpage import Adminlandpage
from src.adminpickpage import Adminpickpage
from src.helper import set_innerfocus,deny_focus,resource_path
from src.globalVariables import g_route, setGlobalVariable ,data_dicts ,object_dict
from src.useMousePress import handleMousePress



hm_dir=os.path.expanduser('~')

class App():

    def __init__(self):
        self.root=Tk()
        self.main_frame = Frame(self.root)
        if os.path.exists("app_settings\\window_position.json"):
            with open ("app_settings\\window_position.json",'r') as file:
                window_position=''
                files=file.read()

                if files:
                    window_position=eval(files)

                if window_position:
                    self.root.geometry(f"1200x700+{window_position[0]}+{window_position[1]}")
                else:
                    self.root.geometry("1200x700")

        self.root.aspect()


        platform= sys.platform
        if str(platform) == 'win32':
            self.root.wm_iconbitmap(self, resource_path("_images\\sch_logo1.ico"),)
        # self.root.iconbitmap(self, resource_path("_images\\sch_logo1.ico"))
        self.main_frame.pack(fill="both", expand=True)


        self.frames={}

        for F in (Landingpage, Adminpickpage, Adminlandpage):
            frame = F(self.main_frame, self)
            self.frames[F]=frame


        self.show_frame(Landingpage,route='forward')


        setGlobalVariable("object_dict", self.frames)
        setGlobalVariable("object_dict",self.main_frame , key="window")
        setGlobalVariable("object_dict", self.root, 'master')

        # event handle function
        from src.useResizeWindow import get_resize_window

        self.root.bind("<Configure>", get_resize_window)


        def quitter_function():

            # "-options": must be -default, -detail, -icon, -message, -parent, -title, or -type
            x = messagebox.askquestion('Quit?', "Are you sure")

            if x == "yes":
                if os.path.exists("server_response.json"):
                    os.remove("server_response.json")
                if os.path.exists("server_response1.json"):
                    os.remove("server_response1.json")
                if os.path.exists("server_response3.json"):
                    os.remove('server_response3.json')
                if not os.path.exists("app_settings.json"):
                    from src.useResizeWindow import window_position
                    import json
                    with open("app_settings\\window_position.json",'w') as file :
                        file.write(json.dumps(window_position))


                self.root.destroy()

        self.root.protocol('WM_DELETE_WINDOW', lambda: quitter_function())

        self.last_clkPage = Landingpage

        def filterWidgets(parent, event):
            global removedFocus

            if not removedFocus:
                if 'entry' not in str(event.widget):
                    removedFocus = True
                    for x in parent.children:
                        if 'entry' in str(x):
                            parent.children[x]['insertofftime'] = 100000
                            parent.itemconfigure('tagl', fill='white')

        def Getcurrentpage(event):

            """ x=widget.winfo_rootx()+event.x
            y=widget.winfo_rooty()+event.y
               """
            try:
                if g_route[-1] == self.last_clkPage:
                    self.last_clkPage = g_route[-1]


                elif g_route[-1] != self.last_clkPage:
                    self.last_clkPage = g_route[-1]
                    global removedFocus
                    removedFocus = False
                #
                # #Remove entry focus
                if self.last_clkPage == Adminlandpage:
                    parent = self.frames[Adminlandpage].children['!canvas']
                    filterWidgets(parent, event)
                #
                # if self.last_clkPage == Createstudent:
                #     parent = self.frames[Createstudent].children['!frame'].children['!canvas']
                #     filterWidgets(parent, event)


            except Exception as e:
                print(e)

        self.root.bind('<Button-1>', Getcurrentpage)



    def show_frame(self,page,route=None):

        global func_to_call

        set_innerfocus(self.frames[page].children)
        #
        if page == Adminlandpage:
            deny_focus(self.frames[Landingpage].children)
            if os.path.exists("server_response.json"):
                os.remove("server_response.json")
            if os.path.exists("server_response1.json"):
                os.remove("server_response1.json")
            if os.path.exists("server_response3.json"):
                os.remove('server_response3.json')
        #
        #     self.frames[page].password_entry.config(state='normal')
        #     if shw_temp == 'showall':
        #         self.frames[ShowAllStudents].temp=False
        #     if self.frames[ShowAllStudents].retreat:
        #         self.frames[ShowAllStudents].retreat=False
        #     class_objects(Adminlandpage)
        #
        #
        # elif page == Userlandpage:
        #     object_dict['route']=''
        #     self.frames[page].password_entry.config(state='normal')
        #
        # elif page == Sciencepickpage:
        #     object_dict['route']=Sciencepickpage
        #
        # elif page == Commpickpage:
        #     object_dict['route']=Commpickpage
        #
        # elif page == Artpickpage:
        #     object_dict['route']=Artpickpage
        #
        # elif page == ShowAllStudents:
        #     ShowAllStudents.s_process('')
        #     #self.attributes('-alpha',0.9)
        #
        # elif page == Createstudent:
        #     self.frames[page].bindwidgets()
        #
        # elif page == EditStudent:
        #     self.frames[page].bind_widgets()
        #
        # #we create a variable of each class to call with session time function
        # if page in [Sciencepickpage, Artpickpage,Commpickpage,English,Math,Literature,Biology,Commerce]:
        #     func_to_call=page

        title_x = str(page)
        title_x = title_x.split('.')[1].split("'")[0]
        title_x = 'WCH Student App' if title_x == 'Landingpage' else title_x
        self.tc = Tk.wm_title(self.root, title_x.upper())

        global g_route
        if route == 'forward':
            if g_route:
                deny_focus(self.frames[g_route[-1]].children)
            g_route.append(page)
        elif route == 'backward':
            if g_route:
                g_route = g_route[:-1]
        elif route == 'logout':
            if g_route:
                g_route = g_route[:2]


        frame = self.frames[g_route[-1]]

        for x in self.frames:
            if frame == self.frames[x]:
               self.frames[x].pack(fill="both", expand=True)

            else:
                frame_list=str(x).split('.')

                if  frame_list and len(frame_list) > 1:
                    self.frames[x].pack_forget()






if __name__ == "__main__":
    try:
        app = App()
        app.root.mainloop()
    except KeyboardInterrupt:
        print('Keyboard Interrupt')