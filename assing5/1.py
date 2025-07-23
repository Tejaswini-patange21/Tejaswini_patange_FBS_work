correct_user_id = "teju"
correct_password = "teju21"

max_attempts = 3
attempts = 0

while(attempts < max_attempts):
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")

    if(user_id == correct_user_id and password == correct_password):
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Incorrect credentials attempts left:",max_attempts)
        
        if(attempts == max_attempts):
            print("To many failed attempts")
