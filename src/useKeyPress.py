from .globalVariables import g_route
from .adminlandpage import Adminlandpage
from .globalVariables import getGlobalVariable


def handle_key_press(event):
    if g_route[-1] == Adminlandpage:
        # getGlobalVariable("object_dict")[Adminlandpage].form.key_handler(event)
        k=90


