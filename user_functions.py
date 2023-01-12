def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Write down your email: ")
    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email

def get_user_name_from_input():
    """ Not empty string. No spaces. """
    username = input("Write down your user name :")
    if (" " in username) : 
        print ('User name is not valid')
    else : 
        return username


def get_password_from_input():
    import string
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    password = input("Create your password: ")
    if ([i for i in range(10)] not in password or list(string.punctuation) not in password or list(string.ascii_letters) not in password or len(password) < 8) : 
        print("Password is not valid")
    else : 
        return password 
    