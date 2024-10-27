def logout_timer(controller,arg):
    global current_minute, current_seconds,session_time_flag,permit

    session_time_flag=False
    permit=True
    info="time,{}:{},{}".format(current_minute,current_seconds,matricno)

    async_thread = async_Thread(
        tcp_echo_client(controller, '{}#u/894#{}'.format('edit student', info),arg))
    async_thread.daemon = True
    async_thread.start()
