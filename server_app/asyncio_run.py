import asyncio, sqlite3, json, zipfile, os, time, bcrypt

home_dir=os.path.expanduser("~")
hm_dir = home_dir + "\\pictures\\tempo\\"


async def create_media():
    dirs=[]
    # Create a unique zip file for each client connection
    hm_dirx = os.path.expanduser("~") + "\\Pictures\\"
    zip_filename = f"{hm_dirx}client_{1001}_{190}.zip"
    
    for file in os.listdir(hm_dir):
         dirs.append(hm_dir+file)

    def create_zip_archive(zip_path,files_to_send):
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for file in files_to_send:
                zip_file.write(file,os.path.basename(file))

    # Create and send the zip archive
    create_zip_archive(zip_filename,dirs)

    return zip_filename
    #os.remove( f"client_{addr[0]}_{addr[1]}.zip")


async def handle_echo(reader, writer):
    data=b''
    while True:
        response = await reader.read(1024)
        print(response)
        data+=response
        if response.endswith(b'end'):
            break
    data=data[:len(data)-3]
    con = sqlite3.connect('student.db')
    cursor = con.cursor()
    message = data.decode().split('#u/894#')
    addr = writer.get_extra_info('peername')
    print(f"Received {message[0]!r} from {addr!r},{time.strftime('%I:%M, %A/%B/%Y')}")
    admin = {}
    student = {}

    try:
        if message[0] == 'Showallstudents':
            print(message)
            if message[1] == '0':
                print('connected to database', message[0])
                resultx = cursor.execute(f"SELECT * FROM Student")

                for row in cursor.fetchall():
                    student[row[0]] = row[1:]
                student_json = json.dumps(student)
                writer.write(student_json.encode())

            elif message[1] == 'fetch_data':
                path = await create_media()
                with open(path, 'rb') as file:
                    data = file.read()
                writer.write(data)

        elif message[0] == 'admin login':
            data = message[1]
            print(data)
            print('connected to database', message[0])
            resultx = cursor.execute(f"SELECT * FROM Admin  WHERE username =('{data}')")
            for i in resultx:
                x = [x for x, i in zip(i, range(len(i))) if i > 0]
                admin[i[0]] = x
            if not admin:
                admin['info'] = 'Admin not found'

            admin_json = json.dumps(admin)
            writer.write(admin_json.encode())

        elif message[0] == 'create student':

            data = eval(message[1])
            ex_data = data[len(data) - 1:]
            data = data[:len(data) - 1]
            matricno = data[0]
            if matricno[0] == '6' or matricno[:3] == '527':
                if data[5] == 'Science':
                    if matricno[0] == '6':
                        data = tuple(list(data) + ['True', 0, 0, '', 0, '', '1:60', 0])
                    elif matricno[:3] == '527':
                        data = tuple(list(data) + ['None', 0, 0, '', 0, '', '1:60', 0])

                elif data[5] == 'Commerce':
                    if matricno[0] == '6':
                        data = tuple(list(data) + ['True', 0, 0, 0, '', '', '1:60', 0])
                    elif matricno[:3] == '527':
                        data = tuple(list(data) + ['None', 0, 0, 0, '', '', '1:60', 0])

                elif data[5] == 'Art':
                    if matricno[0] == '6':
                        data = tuple(list(data) + ['True', 0, 0, '', '', 0, '1:60', 0])
                    elif matricno[:3] == '527':
                        data = tuple(list(data) + ['None', 0, 0, '', '', 0, '1:60', 0])

                def generate_salt(value):
                    # Generate a random salt
                    salt = bcrypt.gensalt()

                    # Hash the password using the salt
                    hashed_password = bcrypt.hashpw(value[3].encode('utf-8'), salt)
                    val = list(value)
                    val[3] = hashed_password.decode()
                    val = val + list(ex_data) + [salt.decode()]
                    return tuple(val)

                data = generate_salt(data)

                info = 'matricno,firstname,lastname,password,course,address,phone_number,country,state_of_origin\
                ,state,city,gender,Date_of_Birth'
                try:
                    print(data)
                    cursor.execute("INSERT INTO Student(matricno,firstname,lastname,password,phone_number,course,address,country,\
                    state_of_origin,state,city,gender,Date_of_Birth,session,math,english,commerce,biology,literature,time,\
                    total,email,salt)VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
                    con.commit()

                    for i in cursor.execute(f"SELECT {info} FROM Student WHERE matricno is {matricno} "):
                        x = [x for x, i in zip(i, range(len(i))) if i > 0]
                        student[i[0]] = x

                    def process_image(value):
                        print('started')
                        zip_filename = "received_files.zip"
                        with open(zip_filename, 'wb') as file:
                            file.write(value)

                        with zipfile.ZipFile(zip_filename, 'r') as zipf:
                            zipf.extractall(home_dir+"\\pictures\\Database_media\\")
                        os.remove(zip_filename)
                        return 'done'

                    print(process_image(eval(message[2])))

                except Exception as e:
                    if str(e) == 'UNIQUE constraint failed: Student.matricno':
                        print('error creating student')
                        student[matricno] = "Student With That Matric No. Already Exist"
                    else:
                        student[matricno] = 'error creating student: Try again later. '
                        print(e)

                student_json = json.dumps(student)
                writer.write(student_json.encode())

        elif message[0] == 'edit student':

            student = {}
            try:
                # request for data to verify
                if message[1].isnumeric() and len(message[1]) == 7:
                    print('connected to database')

                    resultx = cursor.execute(f"SELECT * FROM Student WHERE matricno is {message[1]}")
                    for i in resultx:
                        x = [x for x, i in zip(i, range(len(i))) if i > 0]
                        student[i[0]] = x

                        # request for data to verify
                elif message[1].isnumeric() and message[1][:3] == '527':
                    print('connected to database')

                    resultx = cursor.execute(f"SELECT * FROM Student WHERE matricno is {message[1]}")
                    for i in resultx:
                        x = [x for x, i in zip(i, range(len(i))) if i > 0]
                        student[i[0]] = x

                        # modify data and send back response
                elif ',' in message[1]:
                    print(message[1])
                    data = message[1].split(',')
                    data = [i.replace('~', ',') for i in data]

                    cursor.execute(
                        "UPDATE Student SET {} = ('{}') WHERE matricno = ('{}')".format(data[0], data[1], int(data[2])))
                    con.commit()
                    if data[1][0] == '6':
                        res = cursor.execute(f"SELECT * FROM Student WHERE matricno is {data[1]}")
                        for row in cursor.fetchall():

                            if int(data[1]) in row:
                                student['updated'] = data[0]
                            else:
                                student['info'] = 'Internal error'
                    else:
                        resultx = cursor.execute(f"SELECT * FROM Student WHERE matricno is {data[2]}")
                        for row in cursor.fetchall():
                            data[1] = int(data[1]) if len(data[1]) <= 2 else data[1]
                            if data[1] in row:
                                student['updated'] = data[0]
                            else:
                                student['info'] = 'Internal error'

            except Exception as e:
                if str(e) == 'UNIQUE constraint failed: Student.matricno':
                    student['info'] = "Student With That Matric No. Already Exist"
                else:
                    student['info'] = 'Internal error'
                print(e)

            student_json = json.dumps(student)
            writer.write(student_json.encode())

        elif message[0] == 'delete student':
            student = {}
            try:
                # request for data to verify
                if message[1].isnumeric() and len(message[1]) == 7:
                    print('connected to database')
                    resultx = cursor.execute(f"SELECT * FROM Student WHERE matricno is {message[1]}")
                    for i in resultx:
                        x = [x for x, i in zip(i, range(len(i))) if i > 0]
                        student[i[0]] = x

                        # request for data to verify
                elif message[1].isnumeric() and message[1][:3] == '527':
                    print('connected to database')

                    resultx = cursor.execute(f"SELECT * FROM Student WHERE matricno is {message[1]}")
                    for i in resultx:
                        x = [x for x, i in zip(i, range(len(i))) if i > 0]
                        student[i[0]] = x

                        # modify data and send back response
                elif ',' in message[1]:
                    data = message[1].split(',')
                    cursor.execute(f"DELETE FROM Student WHERE matricno =('{data[0]}')")
                    con.commit()
                    print(data[0])
                    if os.path.exists(data[0] + '.jpg'):
                        os.remove(data[0] + '.jpg')
                    student['updated'] = 'Deleted'

            except Exception as e:
                student['info'] = 'Internal error'
                print(e)

            student_json = json.dumps(student)
            writer.write(student_json.encode())

        elif message[0] == 'unverified_student':

            # request for new registration in the database that are not verified
            # send back response
            print('connected to database', message[0])
            try:
                result_tab = cursor.execute(f"SELECT * FROM Student")
                for row in cursor.fetchall():
                    if row:
                        if str(row[0])[:3] == '527':
                            student[row[0]] = row[1:]
                if not student:
                    student['info'] = 'No new Registration'

            except Exception as e:
                print(e)

            student_json = json.dumps(student)
            writer.write(student_json.encode())

        elif message[0] == 'user login':
            student = {}
            data = message[1]
            try:
                print('connected to database')
                resultx = cursor.execute(f"SELECT * FROM Student WHERE matricno= ('{data}')")
                for i in resultx:
                    x = [x for x, i in zip(i, range(len(i))) if i > 0]
                    student[i[0]] = x
                if not student:
                    student['info'] = 'Student not found'
            except:
                student['error'] = 'Internal error'

            student_json = json.dumps(student)
            writer.write(student_json.encode())

        else:
            print(f'Received: {message}')
            writer.write('Hello world'.encode())

    except Exception as e:
        print(e)
        writer.write('Internal error'.encode())
    await writer.drain()

    print("Close the connection")
    writer.close()
    con.close()
    admin = {}
    student = {}
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_echo, '', 8889)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs} {time.strftime('%I:%M %p  %A,%B,%Y')}")

    async with server:
        await server.serve_forever()


try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass