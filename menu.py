# Menu program for automation using python

from os import system 
from time import sleep

while True :    
    system("clear")
    system("tput setaf 3")
    print("----------------------".center(170))
    print("!!Welcome to My Menu!!".center(170))
    print("----------------------".center(170))

# Menu options

    system("tput setaf 6")
    print("1. Press 1 to work locally")
    print("2. Press 2 to work remotely")
    print("3. Press 3 to exit")
    system("tput setaf 5")
    ch = int(input("\nEnter your choice : "))
    system("tput setaf 6")

    if ch==2 :
        system("tput setaf 5")
        ip = input("Enter IP address of remote system : ")
        system("tput setaf 7")
        system(f"ssh {ip}")
        
    elif ch==1 :
        while True :
            system("clear")
            system("tput setaf 3")
            print("------Hadoop Menu------")
            system("tput setaf 6")
            print("\n1. Press 1 to setup NameNode")
            print("2. Press 2 to setup DataNode")
            print("3. Press 3 to return to main menu")
            print("4. Press 4 to Exit the program")
            system("tput setaf 5")
            hdp = int(input("\nEnter your choice : "))
            system("tput setaf 6")

            if hdp==1 : 
                while True :
                    system("clear")
                    system("tput setaf 3")
                    print("------NameNode Menu------\n")
                    system("tput setaf 6")
                    print("1.  Press 1 to open hdfs-site.xml file")
                    print("2.  Press 2 to open core-site.xml file")
                    print("3.  Press 3 to start services of NameNode")
                    print("4.  Press 4 to stop NameNode")
                    print("5.  Press 5 to check report")
                    print("6.  Press 6 to upload an empty file")
                    print("7.  Press 7 to create and upload a file")
                    print("8.  Press 8 to remove a file")
                    print("9.  Press 9 to read a file")
                    print("10. Press 10 to see all files")
                    print("11. Press 11 to save file to local system")
                    print("12. Press 12 to start safemode")
                    print("13. Press 13 to stop safemode")
                    print("14. Press 14 to go back to Main menu")
                    print("15. Press 15 to Exit the program")
                    system("tput setaf 5")
                    ch = int(input("\nEnter your choice : "))
                    if ch==1 : 
                        system("tput setaf 4")
                        dirNN = input("Create folder for NameNode : ")
                        system(f"mkdir {dirNN}")
                        system("tput setaf 3")
                        print("Opening hdfs-site.xml file...")
                        sleep(1)
                        system("vim /etc/hadoop/hdfs-site.xml")
                        system("tput setaf 2")
                        print("hdfs-site.xml file successfully modified")
                        system("hadoop namenode -format")
                        sleep(2)
                    elif ch==2 :
                        system("vim /etc/hadoop/core-site.xml")
                        system("tput setaf 2")
                        print("core-site.xml file successfully modified")
                        sleep(2)
                    elif ch==3 :
                        system("tput setaf 3")
                        system("hadoop-daemon.sh start namenode")
                        system("tput setaf 2")
                        system("jps")
                        print("Namenode started successfully :-)")
                        sleep(2)
                    elif ch == 4 :
                        system("tput setaf 2")
                        system("hadoop-daemon.sh stop namenode")
                        sleep(2)
                    elif ch==5 :
                        system("tput setaf 2")
                        system("hadoop dfsadmin -report")
                        input("...")
                    elif ch==6 :
                        system("tput setaf 5")
                        fname = input("File name : ")
                        system(f"hadoop fs -touchz /{fname}")
                        system("tput setaf 2")
                        print("File ceated successfully")
                        input("...")
                    elif ch==7 :
                        system("tput setaf 5")
                        fname = input("File name : ")
                        print("Write in file :")
                        system("tput setaf 7")
                        system(f"cat > {fname}")
                        system(f"hadoop fs -put {fname} /")
                        system("tput setaf 2")
                        print("File uploaded successfully")
                        input("...")
                    elif ch==8 :
                        system("tput setaf 5")
                        fname = input("File name : ")
                        system("tput setaf 1")
                        system(f"hadoop fs -rm /{fname}")
                        input("...")
                    elif ch==9 : 
                        system("tput setaf 5")
                        fname = input("File name : ")
                        system("tput setaf 7")
                        system(f"hadoop fs -cat /{fname}")
                        input("...")
                    elif ch==10 :
                        system("tput setaf 4")
                        system("hadoop fs -ls /")
                        input("...")
                    elif ch==11 :
                        system("tput setaf 4")
                        src = input("Enter the name of file you want to copy : ")
                        dest = input("Enter location where you want to save the file : ")
                        system(f"hadoop fs -copyToLocal /{src} {dest}")
                        system("tput setaf 2")
                        print("File copied successfully")
                        sleep(2)
                    elif ch==12 :
                        system("tput setaf 2")
                        system("hadoop dfsadmin -safemode get")
                    elif ch==13 :
                        system("tput setaf 2")
                        system("hadoop dfsadmin -safemode leave")
                    elif ch==14 :
                        break
                    elif ch==15 :
                        system("tput setaf 3")
                        print("Bye...")
                        system("tput setaf 7")
                        exit()
                    else :
                        system("tput setaf 1")
                        print("Wrong choice/n")
                        #input("...")
                        sleep(2)

            elif hdp==2 : 
                while True :
                    system("clear")
                    system("tput setaf 3")
                    print("------DataNode Menu------\n")
                    system("tput setaf 6")
                    print("1.  Press 1 to open hdfs-site.xml file")
                    print("2.  Press 2 to open core-site.xml file")
                    print("3.  Press 3 to start services of DataNode")
                    print("4.  Press 4 to stop DataNode")
                    print("5.  Press 5 to check report")
                    print("6.  Press 6 to upload an empty file")
                    print("7.  Press 7 to create and upload a file")
                    print("8.  Press 8 to remove a file")
                    print("9.  Press 9 to read a file")
                    print("10. Press 10 to see all files")
                    print("11. Press 11 to go back to Main menu")
                    print("12. Press 12 to Exit the program\n")
                    system("tput setaf 5")
                    ch = int(input("Enter your choice : "))
                    if ch==1 : 
                        system("tput setaf 5")
                        dirDN = input("Create folder for DataNode : ")
                        system(f"mkdir {dirDN}")
                        system("tput setaf 3")
                        print("Opening hdfs-site.xml file...")
                        sleep(1)
                        system("vim /etc/hadoop/hdfs-site.xml")
                        system("tput setaf 2")
                        print("hdfs-site.xml file successfully modified")
                        sleep(2)
                    elif ch==2 :
                        system("vim /etc/hadoop/core-site.xml")
                        system("tput setaf 2")
                        print("core-site.xml file successfully modified")
                        sleep(2)
                    elif ch==3 :
                        system("tput setaf 3")
                        system("hadoop-daemon.sh start datanode")
                        system("tput setaf 2")
                        system("jps")
                        print("DataNode started successfully :-)")
                        sleep(2)
                    elif ch == 4 :
                        system("tput setaf 2")
                        system("hadoop-daemon.sh stop datanode")
                        sleep(2)
                    elif ch==5 :
                        system("tput setaf 2")
                        system("hadoop dfsadmin -report")
                        input("...")
                    elif ch==6 :
                        system("tput setaf 5")
                        fname = input("File name : ")
                        system(f"hadoop fs -touchz /{fname}")
                        system("tput setaf 2")
                        print("File ceated successfully")
                        input("...")
                    elif ch==7 :
                        system("tput setaf 5")
                        fname = input("File name : ")
                        print("Write in file :")
                        system("tput setaf 7")
                        system(f"cat > {fname}")
                        system(f"hadoop fs -put {fname} /")
                        system("tput setaf 2")
                        print("File uploaded successfully")
                        input("...")
                    elif ch==8 :
                        system("tput setaf 5")
                        fname = input("File name : ")
                        system("tput setaf 1")
                        system(f"hadoop fs -rm /{fname}")
                        input("...")
                    elif ch==9 : 
                        system("tput setaf 5")
                        fname = input("File name : ")
                        system("tput setaf 4")
                        system(f"hadoop fs -cat /{fname}")
                        input("...")
                    elif ch==10 :
                        system("tput setaf 4")
                        system("hadoop fs -ls /")
                        input("...")
                    elif ch==11 :
                        break
                    elif ch==12 :
                        system("tput setaf 3")
                        print("Bye...")
                        system("tput setaf 7")
                        exit()
                    else :
                        system("tput setaf 1")
                        print("!!Wrong choice!!\nTry again")
                        sleep(2)
            elif hdp==3 :
                break
            elif hdp==4 :
                system("tput setaf 3")
                print("Bye...")
                system("tput setaf 7")
                exit()
            else :
                system("tput setaf 1")
                print("!!Wrong choice!!\nTry again")
                sleep(2)
    elif ch == 3:
        system("tput setaf 3")
        print("Bye...")
        system("tput setaf 7")
        exit()
    
    else :
        system("tput setaf 1")
        print("!!!! Wrong Choice !!!!\n Try again :-)")
        system("tput setaf 6")
        input("...")
