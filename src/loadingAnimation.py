import math
from tkinter import *



num_circles = 10
colors=['red','lightblue','blue','purple','brown','lightgrey','darkgrey','pink','grey','yellow']
animation_speed = 2 # Lower values make the animation faster
class Animation():

    def __init__(self,toplevel,canvas,geometry):
        self.toplevel=toplevel

        self.toplevel.geometry(geometry)
        self.toplevel.overrideredirect(True)

        self.toplevel.focus()

        # Constants
        self.canvas = canvas
        self.canvas.pack()
        self.canvas.config(bg='black',highlightbackground='black')
        self.rounded_button()
        self.toplevel.grab_set()
        self.items=[]
        self.update_circles()

    def update_circles(self):
        try:

            global circle_positions, frame
            self.canvas.delete('all')

            self.items=[]
            for i in range(num_circles):
                x, y = circle_positions[i]
                id=self.canvas.create_oval(x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius,
                                   fill=colors[i], outline=colors[i])
                self.items.append(id)
                # Update circle positions to create animation effect
                angle = (i / num_circles) * 360  # Vary the angle for each circle
                circle_positions[i] = (center_x + radius * math.cos(math.radians(angle + frame)),
                                       center_y + radius * math.sin(math.radians(angle + frame)))

            frame = (frame + 1) % 360
            self.toplevel.after(animation_speed, self.update_circles)  # Update every 10 milliseconds
        except:
            pass


    def rounded_button(self):
        x1,y1,x2,y2=0,0,400,250
        radius = 30
        points = [x1 + radius, y1, x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1, x2, y1, x2,
                  y1 + radius,
                  x2, y1 + radius, x2, y1 + radius, x2, y2 - radius, x2, y2 - radius, x2, y2, x2 - radius, y2,
                  x2 - radius, y2,
                  x2 - radius, y2, x1 + radius, y2, x1 + radius, y2, x1, y2, x1, y2 - radius, x1, y2 - radius, x1,
                  y2 - radius, x1,
                  y1 + radius, x1, y1 + radius, x1, y1]

        item = self.canvas.create_polygon(points, fill='black', outline='#d0c5c1', smooth=True,
                                          tags=f"tag{0}",width='3')

center_x, center_y = 190, 120
radius = 60
circle_radius = 15
frame = 0

# Initialize circle positions
circle_positions = [(center_x, center_y - radius) for _ in range(num_circles)]




