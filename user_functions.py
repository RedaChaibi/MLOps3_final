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
    