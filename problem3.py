#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks

a = input("Username: ")
if "admin" not in a:
    print("invalid user")

else: 
    b = input("Password: ")
    if "12345password" in b:
        print("Access granted")

    else:
        print("invalid password")