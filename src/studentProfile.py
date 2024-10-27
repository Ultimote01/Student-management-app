import tkinter as tk
from PIL import ImageTk, Image, ImageDraw
import os, random

# Constants
ITEM_HEIGHT = 70  # Height of each item (widget) in pixels
VIEWPORT_HEIGHT = 600  # Height of the viewport in pixels


class VirtualScroller:
    def __init__(self, canvas, data_source, scrollbar, data_frame, total_items):
        self.canvas = canvas
        self.data_source = data_source
        self.scrollbar = scrollbar
        self.data_frame = data_frame
        self.total_items = total_items
        self.viewport_items = []  # List to store the widgets in the viewport
        self.viewport_items1 = []
        self.viewport_items2 = []
        self.scrollrec = 0
        self.last_tag = 0
        self.photo = [ImageTk.PhotoImage(self.rounded_image(300, 300, 20,
                                                            "\\Users\\nathan\\Pictures\\Database_media\\" + file))
                      for file in os.listdir("\\Users\\nathan\\Pictures\\Database_media\\")]
        self.photo1 = ImageTk.PhotoImage(
            Image.open("\\users\\nathan\\documents\\exam_p.png").convert('L').resize((100, 100), Image.BICUBIC))
        print(len(self.photo), '........')

        self.l = ["Matric no:", 'Firstname:', 'Lastname:', 'Password:', 'Phone Number:', 'Courses:', 'Address:',
                  'Country:', 'State of origin:', "State:", "City:", "Gender:", "DOB:"]
        add_length = 1 if len(data_source) == 1 else 550
        self.canvas.configure(scrollregion=(0, 0, 0, self.data_frame[-1] + add_length))
        self._on_canvas_configure()

        self.canvas.bind("<MouseWheel>", self._on_mouse_wheel)

    def rounded_image(self, width, height, radius, image_path,outline_width=10):
        # Create a new RGBA image with a white background
        image = Image.new("RGBA", (width, height), (255, 255, 255, 255))
        draw = ImageDraw.Draw(image)

        # Draw a rounded rectangle
        draw.rounded_rectangle(
            [(0, 0), (width, height)],
            fill=(255, 0, 0, 255),  # You can change the fill color
            outline=255, # No outline
            radius=radius,
            width=outline_width
        )

        # Open the image to be pasted
        paste_image = Image.open(image_path)

        # Create a mask in the shape of the rounded rectangle
        mask = Image.new("L", (width, height), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle(
            [(0, 0), (width, height)],
            fill=225,
            outline=0,
            radius=radius,
            width=outline_width
        )

        # Resize the image to match the size of the mask
        paste_image = paste_image.resize((width, height))

        # Paste the image onto the rounded rectangle using the mask
        result = Image.new("RGBA", (width, height), (255, 255, 255, 0))
        result.paste(paste_image, (0, 0), mask)

        return result

    def _on_canvas_configure(self):
        self.canvas.delete("all")
        self._render_viewport()

    def _on_mouse_wheel(self, event):

        # Scroll up
        self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")
        # Scroll up
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")


        # Scroll down
        else:
            self.canvas.yview_scroll(1, "units")

    def _render_viewport(self):
        global x1, y1, x2, y2

        for x, y in enumerate(self.data_frame):
            x1, y1, x2, y2 = 2, y + 5, 1090, y + 540

            radius = 30
            points = [x1 + radius, y1, x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1, x2, y1, x2,
                      y1 + radius,
                      x2, y1 + radius, x2, y1 + radius, x2, y2 - radius, x2, y2 - radius, x2, y2, x2 - radius, y2,
                      x2 - radius, y2,
                      x2 - radius, y2, x1 + radius, y2, x1 + radius, y2, x1, y2, x1, y2 - radius, x1, y2 - radius, x1,
                      y2 - radius, x1,
                      y1 + radius, x1, y1 + radius, x1, y1]

            item = self.canvas.create_polygon(points, fill='white', outline="", smooth=True,
                                              tags=f"tag{y}")

            image0 = self.canvas.create_image((x1 + x2) - 800, y1 + 250,
                                              image=self.photo1, anchor=tk.CENTER, tags=f"tagz{y}")

            self.canvas.tag_bind(image0, "<Enter>", self.active_rectangle)
            self.canvas.tag_bind(image0, "<Leave>", self.nonactive_rectangle)

            self.canvas.tag_bind(item, "<Enter>", self.active_rectangle)
            self.canvas.tag_bind(item, "<Leave>", self.nonactive_rectangle)

            text = self.canvas.create_text((x1 + x2) - 1080, y1 + 2, text=f"{self.l[0]}"
                                                                          f"\n{self.l[1]}\n{self.l[2]}\n{self.l[3]}\n{self.l[4]}\n{self.l[5]}\n{self.l[6]}\n{self.l[7]}"
                                                                          f"\n{self.l[8]}\n{self.l[9]}\n{self.l[10]}\n{self.l[11]}\n{self.l[12]}",
                                           fill='black', tags=f"tags{y}", font=('Bookman-Old-Style normal', 27),
                                           anchor='nw')

            self.canvas.tag_bind(text, "<Enter>", self.active_rectangle)
            self.canvas.tag_bind(text, "<Leave>", self.nonactive_rectangle)

            text1 = self.canvas.create_text((x1 + x2) - 790, y1 + 2, text=f"{self.data_source[x][0]}"
                                                                          f"\n{self.data_source[x][1]}\n{self.data_source[x][2]}\n{self.data_source[x][3]}\n{self.data_source[x][4]}"
                                                                          f"\n{self.data_source[x][5]}\n{self.data_source[x][6]}\n{self.data_source[x][7]}"
                                                                          f"\n{self.data_source[x][8]}\n{self.data_source[x][9]}\n{self.data_source[x][10]}"
                                                                          f"\n{self.data_source[x][11]}\n{self.data_source[x][12]}",
                                            fill='black', tags=f"tagx{y}", font=('Bookman-Old-Style italic', 27),
                                            anchor='nw')

            self.canvas.tag_bind(text1, "<Enter>", self.active_rectangle)
            self.canvas.tag_bind(text1, "<Leave>", self.nonactive_rectangle)

            image = self.canvas.create_image((x1 + x2) - 160, y1 + 155,
                                             image=self.photo[0], anchor=tk.CENTER, tags=f"tagy{y}")

            self.canvas.tag_bind(image, "<Enter>", self.active_rectangle)
            self.canvas.tag_bind(image, "<Leave>", self.nonactive_rectangle)
            random.shuffle(self.photo)

    def active_rectangle(self, event):

        clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)  # Get all tags associated with the item
            if 's' in tags[0]:
                self.canvas.itemconfigure(tags[0].replace('s', ''), outline='darkblue', width=5)
            elif 'x' in tags[0]:
                self.canvas.itemconfigure(tags[0].replace('x', ''), outline='darkblue', width=5)
            elif 'y' in tags[0]:
                self.canvas.itemconfigure(tags[0].replace('y', ''), outline='darkblue', width=5)
            elif 'z' in tags[0]:
                self.canvas.itemconfigure(tags[0].replace('z', ''), outline='darkblue', width=5)
            else:
                self.canvas.itemconfigure(tags[0], outline='darkblue', width=5)

            if tags[0] != self.last_tag:

                if 's' in tags[0]:
                    self.canvas.itemconfigure(tags[0].replace('s', ''), outline='darkblue', width=5)
                elif 'x' in tags[0]:
                    self.canvas.itemconfigure(tags[0].replace('x', ''), outline='darkblue', width=5)
                elif 'y' in tags[0]:
                    self.canvas.itemconfigure(tags[0].replace('y', ''), outline='darkblue', width=5)
                elif 'z' in tags[0]:
                    self.canvas.itemconfigure(tags[0].replace('z', ''), outline='darkblue', width=5)
                else:
                    self.canvas.itemconfigure(tags[0], outline='darkblue', width=5)

    def nonactive_rectangle(self, event):

        clicked_items = event.widget.find_withtag(tk.CURRENT)  # Get item IDs associated with the clicked tag
        for item_id in clicked_items:
            tags = event.widget.gettags(item_id)  # Get all tags associated with the item
            if 's' in tags[0]:
                self.canvas.itemconfigure(tags[0].replace('s', ''), outline='white')
                self.last_tag = tags[0]
            elif 'x' in tags[0]:
                self.canvas.itemconfigure(tags[0].replace('x', ''), outline='white')
                self.last_tag = tags[0]
            elif 'y' in tags[0]:
                self.canvas.itemconfigure(tags[0].replace('y', ''), outline='white')
                self.last_tag = tags[0]
            elif 'z' in tags[0]:
                self.canvas.itemconfigure(tags[0].replace('z', ''), outline='white')
                self.last_tag = tags[0]
            else:
                self.canvas.itemconfigure(tags[0], outline='white')
                self.last_tag = tags[0]


x1, y1, x2, y2 = 0, 0, 0, 0

# Start the main event loop

