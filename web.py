# Menu program to configure Apache web server

from os import system
import subprocess as sp
from time import sleep

while True :
    system("clear")
    system("tput setaf 4")
    print("------Web Server configuration------\n")
    system("tput setaf 6")
    print("1. Press 1 to install Apache Web Server Software")
    print("2. Press 2 to create web pages")
    print("3. Press 3 to start services")
    print("4. Press 4 to stop services")
    print("5. Press 5 to Exit")

    system("tput setaf 3")
    ch = int(input("\nEnter your choice : "))

    if ch==1 : 
        x = sp.getstatusoutput("rpm -q httpd")
        if x[0] != 0 :
            system("yum install httpd")
            sleep(2)
        else : 
            system("tput setaf 2")
            print("\nAlready installed ")
            sleep(2)

    elif ch==2 :
        system("tput setaf 3")
        page = input("\nEnter name of html page (with.html extension) : ")
        system(f"vim /var/www/html/{page}")
        system("tput setaf 2")
        print("\nWeb Page created successfully")
        sleep(2)

    elif ch==3 :
        system("tput setaf 2")
        system("systemctl start httpd")
        print("\nYour service has been started")
        sleep(2)

    elif ch==4 :
        system("tput setaf 2")
        system("systemctl stop httpd")
        print("\nYour service has been stopped")
        sleep(2)

    elif ch==5 :
        system("tput setaf 3")
        print("Bye...")
        system("tput setaf 7")
        exit()

    else :
        system("tput setaf 1")
        print("\nWrong Choice\nTry again")
        sleep(2)
