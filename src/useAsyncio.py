async def main(writer,method):
    global server_response_asx

    await asyncio.sleep(10)
    if not server_response_asx:
        writer.close()
        method({'error':'Internal error'})

async def receive_media_files():
    try:
        addr = socket.gethostbyname('DESKTOP-GU9LDSE')
        reader, writer = await asyncio.open_connection(addr, 8889)
        message = 'Showallstudents#u/894#fetch_data'
        writer.write(message.encode()+b'end')
        await writer.drain()

        data = await reader.read()
        zip_filename = "\\users\\gkyle\\pictures\\received_files.zip"
        with open(zip_filename, 'wb') as file:
            file.write(data)
        print(f"Zip file '{zip_filename}' received successfully.")
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            zipf.extractall("\\users\\gkyle\\pictures\\database_media\\")
        writer.close()
        await writer.wait_closed()
        return 'done'
    except Exception as e:
        print(f"An error occurred while receiving the zip file: {str(e)}")
        return e




async def tcp_echo_client(controller,message,function,new_reg=False,sas_flag=False):
    global server_response_asx

    unreg_student=new_reg
    show_all_student=sas_flag
    server_response_asx=False
    def dummmy_function(data):
        k=data
    try:

        print(f"Started at {time.strftime('%X')},{socket.gethostbyname('DESKTOP-GU9LDSE')}")
        addr=socket.gethostbyname('DESKTOP-GU9LDSE')
        print(addr)
        reader, writer = await asyncio.open_connection(addr, 8889)

        print(f'Send: {message!r}')
        writer.write(message.encode()+b'end')
        await writer.drain()

        if message != 'unverified_student#u/894#0':
            asyncio.create_task(main(writer,function))

        data = await reader.read()
        if data:
            server_response_asx=True

            async def data_writer(data,unreg_student):

                func_to_call=function
                print(f'Received: {data!r}')
                data = json.loads(data)
                if not unreg_student and not show_all_student:
                    with open('server_response.json','w') as file:
                        json.dump(data,file)

                #set by boalean value
                elif show_all_student:
                    with open('server_response3.json','w') as file:
                        json.dump(data,file)
                    media_files= await receive_media_files()
                    if media_files:
                        if not object_dict[ShowAllStudents].load_flag:
                            func_to_call=dummmy_function

                        elif object_dict[ShowAllStudents].load_flag:
                            func_to_call = dummmy_function
                            function('')
                            object_dict[ShowAllStudents].load_flag=False
                else:
                    with open('server_response1.json','w') as file:
                        json.dump(data,file)


                return func_to_call
            process= await data_writer(data,unreg_student)
            if process:

                process({'done':'done'})


        print('Close the connection')
        writer.close()
        await writer.wait_closed()

    except Exception as e:
        if str(e) == '[WinError 1225] The remote computer refused the network connection':
            print(f"tcp_echo  {time.strftime('%X')}")
            function({'connection error':'Host not found'})

        else:
            print(e,'......')
            function({'error':'Application errror'})