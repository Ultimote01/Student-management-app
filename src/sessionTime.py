


def session_time():
    global current_seconds,current_minute,state,session_time_flag,current_frame,func_to_call

    l = [Artpickpage,Sciencepickpage,Commpickpage]
    current_seconds-=1
    if current_minute == 0 and current_seconds == 0:
        session_time_flag=False

    elif current_seconds == 0 and session_time_flag == True:
        current_minute-=1
        current_seconds=59

    for i in l:
        object_dict[i].label.config(text="{}:{}".format(current_minute,current_seconds),bg='white')

    if session_time_flag:
        object_dict[Userlandpage].after(1000,session_time)

    else:
        for i in l:
            object_dict[i].label.config(text="",bg='#989492')
        if not permit:
            logout_timer(object_dict['master'],func_to_call.verify)


