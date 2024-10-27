from tkinter import NW
def createRoundedRec(canvas, x1, y1, x2, y2, radius, tag, active_rectangle, nonactive_rectangle,text="",
bind_widget=True, fill="white",outline="black",font="Bookman-Old-Style 12 normal",image="",text_color="white",
         width=0 , image_coords=(0,0)):

    points = [x1 + radius, y1, x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1, x2, y1, x2,
              y1 + radius,
              x2, y1 + radius, x2, y1 + radius, x2, y2 - radius, x2, y2 - radius, x2, y2, x2 - radius, y2,
              x2 - radius, y2,
              x2 - radius, y2, x1 + radius, y2, x1 + radius, y2, x1, y2, x1, y2 - radius, x1, y2 - radius, x1,
              y2 - radius, x1,
              y1 + radius, x1, y1 + radius, x1, y1]


    item = canvas.create_polygon(points, fill=fill, outline=outline, smooth=True, tags=f"tag{tag}",width=width)
    text = canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, fill=text_color,
                              font=font,
                              tags=f"tags{tag}")
    if bind_widget:
        canvas.tag_bind(item, "<Enter>", lambda event: active_rectangle(event, 'enter'))
        canvas.tag_bind(item, "<Leave>", lambda event: nonactive_rectangle(event, 'leave'))
        canvas.tag_bind(text, "<Enter>", lambda event: active_rectangle(event, 'enter'))
        canvas.tag_bind(text, "<Leave>", lambda event: nonactive_rectangle(event, 'leave'))
        canvas.tag_bind(item, "<Button-1>", lambda event: active_rectangle(event, 'clicked'))
        canvas.tag_bind(text, "<Button-1>", lambda event:active_rectangle(event, 'clicked'))
        canvas.tag_bind(item, "<ButtonRelease-1>", lambda event:nonactive_rectangle(event, 'buttonrelease'))
        canvas.tag_bind(text, "<ButtonRelease-1>", lambda event: nonactive_rectangle(event, 'buttonrelease'))




    if image:
        image=canvas.create_image(x1+image_coords[0],y1+image_coords[0],
                                  image=image, anchor=NW, tags=f"tagi{tag}")
        if bind_widget:
            canvas.tag_bind(image, "<ButtonRelease-1>", lambda event: nonactive_rectangle(event, 'buttonrelease'))
            canvas.tag_bind(image, "<Enter>", lambda event: active_rectangle(event, 'enter'))
            canvas.tag_bind(image, "<Button-1>", lambda event: active_rectangle(event, 'clicked'))
            canvas.tag_bind(image, "<Leave>", lambda event: nonactive_rectangle(event, 'leave'))

