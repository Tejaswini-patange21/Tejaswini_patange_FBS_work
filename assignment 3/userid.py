correct_userid = "admin"
correct_password = "12345"

# Input from user
userid = input("Enter user ID: ")
password = input("Enter password: ")

#if credentials are correct
if userid == correct_userid and password == correct_password:
    print("Login successful")
else:
    print("Invalid user ID or password")