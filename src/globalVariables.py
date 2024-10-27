import os
from .helper import  create_directory



num=0


hm_dir= os.path.expanduser("~")
app_dir=create_directory(hm_dir+'\ \ App folder')




current_minute,current_seconds,matricno=0,0,''
session_time_flag,permit=False,False
func_to_call=''


server_response_asx=False
processing_flag=False

#global colors
win_bg='#fefefc'
font_color="black"
border_color="#989492"


pwd=os.getcwd()+"\_images\\"

#remove input focus
removedFocus=False

exam_json={}
submit_flag=False #
g_route=[]


#create student time
s_time=''

WIDTH, HEIGHT = 400, 250
object_dict={}
object_dict1={}
data_dicts={}


counter1 = 0
counter = 0
meter=True
update,update_entry='',''
flag = True
exam_no=0 #This is for questions and answers widgets for math
exam_no1=0 #This is for questions and answers widgets for english
total_score=[0,0,0] #  Global score
voucher_pass=''
x_value=0

variableDict={"num":num,"app_dir":app_dir,"current_minute":current_minute,"current_seconds":current_seconds,
"matricno":matricno,"x_value":x_value,"voucher_pass":voucher_pass,"total_score":total_score,
"exam_no1":exam_no1,"exam_no":exam_no,"flag ":flag,"update":update ,"update_entry":update_entry,
"counter":counter,"counter1":counter1,"meter":meter,"object_dict":object_dict,"object_dict1":object_dict1,
"data_dicts":data_dicts,"g_route":g_route,"removedFocus":removedFocus}


def setGlobalVariable(variable,value,key=''):
    if key :
        variableDict[variable][key]=value
    else:
        variableDict[variable]= value
#
#
#
def getGlobalVariable(value):
     return variableDict[value]