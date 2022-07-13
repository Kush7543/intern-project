from getpass import getpass
from ssl import _PasswordType
from time import sleep


print("--WELCOME TO INSTABOT CLI APPLICATION--")
sleep(2)
print("setting up the connection with https://www.instagram.com/",end="")
for i in range(3):
    sleep(1)
    print('.',end="")
    print()
    sleep(2)
    print("connection established!")

#login user

username = input("username:")
Password = getpass(prompt="password:")
my_bot.login(username=username,password=Password)
print(f"--{username}LOGGEDIN SUCCESSFULLY.--")

#operation to perform

while True:
    print("choose suitable options: ")
    print("""1.Follow user\n2.Unfollow user\n3.Send message to user\n4.Exit app""")
    print("Enter option you choose:"",end")
    n=int(input())
    if n == 1:
        user= input("enter username:")
        my_bot.follow(user)
        print(F"--{user}FOLLOWED.--")
    elif n == 2:
        user = input("enter username:")
        my_bot.unfollow(user)
        print(F"--{user} UNFOLLOWED.--")
    elif n == 3:
        user = input("enter username: ")

        message = input("message you want to send: ")
        my_bot.send_message(message, user)
        print(F"--MESSAGE SUCCESSFULLY SENT TO {user}.--")
    elif n == 4:
         
        my_bot.logout()
        print("logging out the user", end="")
        for i in range(3):
         sleep(1)
        print('.', end="")
        print()
        sleep(2)
        print("Connection ended!")
        print("logged out successfully")
        break
    else:
        print("--WRONG INPUT CHOOSE AGAIN")
        remove('./config')

  