from .loadingAnimation import Animation
from .globalVariables import object_dict
import tkinter as  ttk



#animation function
def animation_function(page,photo,text,func_to_call,current_page,geometry,font='',edit_rep={}):

    if page.animate_canvas:
        page.animate_canvas.destroy()
    page.animate.geometry(geometry)
    canvas=Canvas(page.animate,highlightbackground='lightgrey',bd=0,bg='lightgrey',width=400,height=300,
                  highlightcolor='lightgrey')
    canvas.pack(fill='both',expand=True)
    label=ttk.Label(canvas,text='{}'.format((text).upper()),font=font,
                    background='lightgrey')
    label.place(x=15,y=10)
    canvas.create_image(160,150,image=photo,anchor=CENTER)

    def destroy_toplevel():
        page.animate.destroy()
        if current_page =='Adminlandpage':
            func_to_call(Adminpickpage,route='forward')
            page.backgroud_process()
        elif current_page == 'Editstudent':
            rep = messagebox.askquestion(title='Done?', message='Are you done?')
            if rep == 'yes':
                if page.widgets_obj:
                    for i in page.widgets_obj:
                        if i == 'user_entry':
                            page.widgets_obj[i].delete(0, END)
                        else:
                            page.widgets_obj[i].destroy()
                    page.flag = False
                    page.widget_flag = False
                    page.err_label.destroy()
            else:
                pass

    button=ttk.Button(canvas,text='CLICK ME', command=destroy_toplevel)
    button.place(x=100,y=270)
    page.animate.bind("<Return>",lambda  event:destroy_toplevel())
    try:
        button.bind("<Return>",lambda event: destroy_toplevel())
    except:
        pass




def display_animation(page,animate_canvas,geometry):
    animate_ins = Animation(page,animate_canvas,geometry)
    global object_dict
    object_dict['Animation'] = animate_ins