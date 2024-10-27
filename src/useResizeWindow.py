from .landingpage import Landingpage,Adminlandpage
from .adminpickpage import Adminpickpage
from .globalVariables import  getGlobalVariable

MAX_WIDTH=1366
MAX_HEIGHT=745

MIN_WIDTH=370
MIN_HEIGHT=340

window_position=()

def get_resize_window(event):

    # if event is equal to the first frame
    if (str(event.widget) == ".!frame"):
        # print(event)
        if (event.width > MIN_WIDTH  or event.height > MIN_HEIGHT):
            object_dict = getGlobalVariable("object_dict")
            object_dict[Landingpage].resize_widgets(event.width,event.height)
            object_dict['master'].minsize(MIN_WIDTH,MIN_HEIGHT)
            object_dict[Adminlandpage].resize_widgets(event)

        object_dict[Adminpickpage].sidebar.render_sidebar(event)

    elif (str(event.widget) == '.'):

        global window_position
        window_position=(event.x,event.y)

