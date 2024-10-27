from tkinter import Canvas,Button,Entry,Label
import tkinter as tk
from .globalVariables import getGlobalVariable,setGlobalVariable



widgets={"canvas":Canvas,"button":Button,"entry":Entry,"label":Label}
class Form():

    def __init__(self,parent,**kwargs):
        self.canvas=Canvas(parent)
        self.childrenDict={}
        self.canvas.config(cnf=kwargs)
        self.id, self.y, self.item, self.offtime = '', '', '', 600
        self.widgets={"canvas":Canvas,"button":Button,"entry":Entry,"label":Label}
        self.entries=[]
        self.children_coords={}
        self.lineDrawn=''
        self.canvas.create_line(0,0,0,0,tags="tagl0")
        self.recent_focus=''



    def formLayout(self,layout,**kwargs):


        if layout == 'pack':
            self.canvas.pack(cnf=kwargs)

        elif layout == 'grid':
            self.canvas.grid(cnf=kwargs)

        elif layout == 'place':
            self.canvas.place(cnf=kwargs)


    def handleChildren(self,children):

        for i in children:
            self.childrenDict[i]=widgets[children[i]['widget']](self.canvas,cnf=children[i]['config'])
            self.childrenLayout(self.childrenDict[i],children[i]["display"])


    def childrenLayout(self,variable_name,layout,**kwargs):

        if layout == 'pack':
            self.childrenDict[variable_name].pack(cnf=kwargs)
        elif layout == 'grid':
            self.childrenDict[variable_name].grid(cnf=kwargs)

        elif layout == 'place':

            self.childrenDict[variable_name].place(cnf=kwargs)
            self.children_coords[ self.childrenDict[variable_name]]=(kwargs['x'],kwargs['y'])



    def getWidget(self,widget):
        widget=self.childrenDict[widget]
        return widget


    def getwidgets(self):
        return self.childrenDict
    

    def configWidget(self,widget,config):
        widget=self.getWidget(widget)
        widget.config(cnf=config)


    def createWidget(self,variable_name,widget,**kwargs):
        self.childrenDict[variable_name]=widgets[widget](self.canvas,cnf=kwargs)

        if widget == "entry":
            self.entries.append(self.childrenDict[variable_name])
            self.childrenDict[variable_name].bind('<KeyPress>',self.drawline)
            self.childrenDict[variable_name].bind('<Button-1>', self.drawline)

        return self.childrenDict[variable_name]


    def getCanvas(self):

        return self.canvas


    def create_rounded_rec(self, x1, y1, x2, y2, radius, tag, type, active_rectangle,nonactive_rectangle, text='',
                           fill='white',outline='black',text_color="white",font='Bookman-Old-Style 12 normal'):

        points = [x1 + radius, y1, x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1, x2, y1, x2,
                  y1 + radius,
                  x2, y1 + radius, x2, y1 + radius, x2, y2 - radius, x2, y2 - radius, x2, y2, x2 - radius, y2,
                  x2 - radius, y2,
                  x2 - radius, y2, x1 + radius, y2, x1 + radius, y2, x1, y2, x1, y2 - radius, x1, y2 - radius, x1,
                  y2 - radius, x1,
                  y1 + radius, x1, y1 + radius, x1, y1]
        if type == 'entry':
            item = self.canvas.create_polygon(points, fill=fill, outline=outline, smooth=True,
                                         tags=f"tag{tag}", width=2)
        elif type == 'submit':
            item = self.canvas.create_polygon(points, fill=fill, outline=outline, smooth=True, tags=f"tag{tag}")
            text = self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill=text_color,
                                      font=font,
                                      tags=f"tags{tag}")
            self.canvas.tag_bind(item, "<Enter>", lambda event: active_rectangle(event, 'enter'))
            self.canvas.tag_bind(item, "<Leave>", lambda event: nonactive_rectangle(event, 'leave'))
            self.canvas.tag_bind(text, "<Enter>", lambda event: active_rectangle(event, 'enter'))
            self.canvas.tag_bind(text, "<Leave>", lambda event: nonactive_rectangle(event, 'leave'))
            self.canvas.tag_bind(item, "<Button-1>", lambda event: active_rectangle(event, 'clicked'))
            self.canvas.tag_bind(text, "<Button-1>", lambda event: active_rectangle(event, 'clicked'))
            self.canvas.tag_bind(item, "<ButtonRelease-1>", lambda event: nonactive_rectangle(event, 'buttonrelease'))
            self.canvas.tag_bind(text, "<ButtonRelease-1>", lambda event: nonactive_rectangle(event, 'buttonrelease'))

        elif type == 'back':
            item = self.canvas.create_polygon(points, fill=fill, outline=outline, smooth=True, tags=f"tag{tag}")
            text = self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill=text_color,
                                      font=font, tags=f"tags{tag}")
            self.canvas.tag_bind(item, "<Enter>", lambda event: active_rectangle(event, 'enter'))
            self.canvas.tag_bind(item, "<Leave>", lambda event: nonactive_rectangle(event, 'leave'))
            self.canvas.tag_bind(text, "<Enter>", lambda event: active_rectangle(event, 'enter'))
            self.canvas.tag_bind(text, "<Leave>", lambda event: nonactive_rectangle(event, 'leave'))
            self.canvas.tag_bind(item, "<Button-1>", lambda event: active_rectangle(event, 'clicked'))
            self.canvas.tag_bind(text, "<Button-1>", lambda event: active_rectangle(event, 'clicked'))
            self.canvas.tag_bind(item, "<ButtonRelease-1>", lambda event: nonactive_rectangle(event, 'buttonrelease'))
            self.canvas.tag_bind(text, "<ButtonRelease-1>", lambda event: nonactive_rectangle(event, 'buttonrelease'))


        elif type == 'rectangle':
            item = self.canvas.create_polygon(points, fill=fill, outline=outline, smooth=True,
                                         tags=f"tagr{tag}", width=3)
            self.canvas.delete("tagl0")
            self.canvas.create_line(0,0,0,0,tags="tagl0")
            self.canvas.tag_bind(item, "<Enter>", lambda event: active_rectangle(event, 'enter'))


    def drawline(self,event):

        for i in self.entries:
            if str(event.widget).split(".")[-1] == str(i).split('.')[-1]:
                coords = self.children_coords[i]

                if not self.lineDrawn:
                    self.lineDrawn = self.canvas.create_line(coords[0], coords[1] + 24, coords[0] + 220, coords[1] + 24,
                                                             width=3, smooth=True, fill='grey', tags="tagm")
                else:
                    self.canvas.coords("tagm", coords[0], coords[1] + 24, coords[0] + 220, coords[1] + 24)
                    self.canvas.itemconfigure("tagm", fill="grey")

                if "Shift" in  str(event) and event.keysym == 'Tab' :
                    self.canvas.itemconfigure("tagm",fill="white")

                elif "Shift" not  in  str(event) and event.keysym == 'Tab':
                    self.canvas.itemconfigure("tagm", fill="white")

   