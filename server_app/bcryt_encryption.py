import bcrypt



def generate_salt(value):
    # Generate a random salt
    salt = bcrypt.gensalt()

    # Hash the password using the salt
    hashed_password = bcrypt.hashpw(value.encode('utf-8'), salt).decode('utf-8')
    val = list(value)
    # val[3] = hashed_password.decode()
    # val = val + list(ex_data) + [salt.decode()]
    return hashed_password,salt.decode('utf-8')

# print(generate_salt('july4th1989'))



def generate_string(password):

    stored_salt='$2b$12$05JeooMdmdUe4MyG3AP2pe'.encode()

    # Hash the entered password using the stored salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), stored_salt)