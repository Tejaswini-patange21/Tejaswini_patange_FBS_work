import random
userid=input("Enter the userid:")
pass1 = input("Enter the password:")

if(userid=="tejupatange"and pass1=="teju2104"):
    captcha= random.randint(1000,9999)
    print("captcha:",captcha)
    input=int(input("Enter the captcha:"))

    if(input==captcha):
        print("login successful")
    else:
        print("wrong captcha")    
else:
    print("Incorrect userid and password")        