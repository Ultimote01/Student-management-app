import os,sys,time
from PIL import  ImageDraw,Image,ImageFont

# fucntion deny widgets focus
def deny_focus(frame):
    value = frame
    for i in value:
        value[i].configure(takefocus=False)
        def traverse(page):
            for i in page:
                page[i].configure(takefocus=False)
                if page[i].children:
                    traverse(page[i].children)

        traverse(value[i].children)

# function set widgets focus
def set_innerfocus(frame):
    value =frame
    for z ,i in enumerate(value):

        if 'label' in str(i) or 'canvas' in str(i) :
            pass
        else:
            value[i].configure(takefocus=True)
            if z == 0:
                value[i].focus()
        def traverse(page):
            for i in page:
                if 'label'  in str(i) or 'canvas' in str(i):
                    pass
                else:
                    page[i].configure(takefocus=True)

                if page[i].children:
                    traverse(page[i].children)

        traverse(value[i].children)


# function performs logout operation
def class_objects(segments):
    l=[Createstudent,EditStudent,ShowAllStudents,DeleteStudent]
    if object_dict:
        if segments == Adminlandpage:
            for i in l:
                object_dict[i].logout('')




def net_hander(response):
    if processing_flag:
        return 'running'
    else:
        response.close()
        return 'running'

def create_directory(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
        return directory_path
    except Exception as e:
        return "An error occurred while creating the directory:"+str(e)






def time_keeper():
    timer, rest = time.strftime("%H:%M:%S").split(':'), 'AM'
    timer[0] = (int(timer[0])) - 12 if int(timer[0]) > 12 else timer[0]
    rest = 'AM' if int(timer[0]) < 12 else 'PM'
    return  f"{ timer[0]}:{timer[1]}:{timer[2]} {rest}"


def on_enter(method):
    for i in method:
        if i == 'usertlproceed':
            method[i].config(bg='#695348', fg='white')
        elif i == 'usertlback_btn':
            method[i].config(bg='#b08454', fg='white')
        elif i == 'math_btn':
            method[i].config(bg='#b08454', fg='white')
        elif i == 'english_btn':
            method[i].config(bg='#b08454', fg='white')
        elif i == 'biology_btn':
            method[i].config(bg='#b08454', fg='white')
        elif i == 'lit_btn':
            method[i].config(bg='#b08454', fg='white')
        elif i == 'busstudy_btn':
            method[i].config(bg='#b08454', fg='white')
        elif i == 'back_btn':
            method[i].config(bg='#b08454', fg='white')
        elif i == 'next':
            method[i].config(bg='#b08454', fg='white')
        elif i == 'previous':
            method[i].config(bg='#b08454', fg='white')


def on_leave(method):
    for i in method:
        if i == 'usertlproceed':
            method[i].config(bg='white', fg='black')
        elif i == 'usertlback_btn':
            method[i].config(bg='white', fg='black')
        elif i == 'math_btn':
            method[i].config(bg='white', fg='black')
        elif i == 'english_btn':
            method[i].config(bg='white', fg='black')
        elif i == 'biology_btn':
            method[i].config(bg='white', fg='black')
        elif i == 'lit_btn':
            method[i].config(bg='white', fg='black')
        elif i == 'busstudy_btn':
            method[i].config(bg='white', fg='black')
        elif i == 'back_btn':
            method[i].config(bg='white', fg='black')
        elif i == 'next':
            method[i].config(bg='lightgrey', fg='black')
        elif i == 'previous':
            method[i].config(bg='lightgrey', fg='black')




def hexToDecimal(value):
    hex=''

    if value.startswith('#'):
        hex=value.lstrip('#')

    r=int(hex[0:2],16)
    g=int(hex[2:4],16)
    b=int(hex[4:6],16)

    return r,g,b


def draw_image_masked_iamge_in_text(text, font_path, image, mask_image, image_size, text_cord):
    # Load font
    font = ImageFont.truetype(font_path, 100)

    background_image = image.resize(image_size)
    # Create a blank image
    image = Image.new('RGBA', background_image.size, (255, 255, 255, 0))  # RGBA for alpha channel

    # Draw text on the image (text acts as a mask)
    draw = ImageDraw.Draw(image)
    draw.text(text_cord, text, font=font, fill=(255, 255, 255, 255))  # RGB color, A = 255 for fully opaque



    # Load image to be drawn inside the text and convert to RGBA
    img_to_draw = Image.open(mask_image).convert("RGBA")

    # Ensure that both images have the same size
    img_to_draw = img_to_draw.resize(image.size)

    # Paste the image using the alpha channel of the text
    image.paste(img_to_draw, (0, 0), mask=image)

    result_image = Image.alpha_composite(background_image, image)
    result_image.save("..\\Student_management_app\\_images\\college_image_v.png")

    return result_image


def draw_image_in_text(text, font_path,font_size,image, text_cord,image_size,background_color_rgba=(255,255,255,0),
                       foreground_color=(0,0,0,255)):
    # Load font
    font = ImageFont.truetype(font_path, font_size)
    background_image=''

    if image:
        background_image = Image.open(image).convert("RGBA").resize(image_size)
    else :
       background_image = Image.new('RGBA', image_size, background_color_rgba)  # RGBA for alpha channel

    # Create a blank image
    image = Image.new('RGBA', background_image.size, (255, 255, 255, 0))  # RGBA for alpha channel

    # Draw text on the image (text acts as a mask)
    draw = ImageDraw.Draw(image)
    draw.text(text_cord, text, font=font, fill=(255, 255, 255, 255))  # RGB color, A = 255 for fully opaque

    image_to_mask = Image.new('RGBA', background_image.size, foreground_color)  # RGBA for alpha channel


    # Paste the image using the alpha channel of the text
    image.paste(image_to_mask, (0, 0), mask=image)

    result_image = Image.alpha_composite(background_image, image)
    # Save the result
    # result_image.save("_images\\sch_logo.jpg")
    return result_image

def get_points(x1,y1,x2,y2,radius):
    points = [x1 + radius, y1, x1 + radius, y1, x1 + radius, y1, x2 - radius, y1, x2 - radius, y1, x2, y1, x2,
              y1 + radius,
              x2, y1 + radius, x2, y1 + radius, x2, y2 - radius, x2, y2 - radius, x2, y2, x2 - radius, y2,
              x2 - radius, y2,
              x2 - radius, y2, x1 + radius, y2, x1 + radius, y2, x1, y2, x1, y2 - radius, x1, y2 - radius, x1,
              y2 - radius, x1,
              y1 + radius, x1, y1 + radius, x1, y1]

    return points


def resource_path(relative_path):
    """Get the absolaute path to resource"""

    try:
        #pyinstaller  creates a temp folder and stores path in _MEIPASS
        base_path=sys._MEIPASS

    except Exception:
        base_path=os.path.abspath(".")

    return  os.path.join(base_path,relative_path)


def rounded_image_with_mask(width, height, radius, image_path, outline_width=0):
    # Create a new RGBA image with a white background
    image = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Draw a rounded rectangle
    draw.rounded_rectangle(
        [(0, 0), (width, height)],
        fill=(255, 255, 255, 255),  # You can change the fill color
        outline='black',  # No outline
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
        outline='black',
        radius=radius,
        width=outline_width
    )


    # Resize the image to match the size of the mask
    paste_image = paste_image.resize((width, height))

    # Paste the image onto the rounded rectangle using the mask
    image.paste(paste_image, (0, 0), mask)
    # image.show()


    return image

def rounded_image(width, height, radius,outline_width,foreground=(255, 255, 255, 255)):
    # Create a new RGBA image with a white background
    image = Image.new("RGBA", (width, height),(255, 255, 255, 0))
    draw = ImageDraw.Draw(image)


    # Draw a rounded rectangle
    draw.rounded_rectangle(
        [(0, 0), (width, height)],
        fill=foreground,  # You can change the fill color
        outline='black',  # No outline
        radius=radius,
        width=outline_width
    )

    return  image

