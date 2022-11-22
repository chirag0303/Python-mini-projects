import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="1234")

if mydb.is_connected():
    print("Successfully connected to MySQL database")

c= mydb.cursor()
c.execute("drop database if exists Temple_Management ")
c.execute("create database Temple_Management")
c.execute("Use Temple_Management")

c.execute("create table user (username varchar(30), passwd varchar(30))")
c.execute("insert into user values('VPS','secret@123')")
mydb.commit()

c.execute("Create table Temple_details(Sr_No tinyint(2) primary key,Temple_name varchar(100),Open_Time Time,Closing_Time Time,Open_Days varchar(100),Address varchar(100))")

c.execute("Insert into Temple_details Values(1,'Danghati Temple','070000','170000','Working Days','Goverdhan')")

c.execute("Insert into Temple_details Values(2, 'LaxmiNarayan Temple', '080000' , '180000' ,'all week','Goverdhan')")

c.execute("Insert into Temple_details Values(3, 'MukharBind Temple' , '070000' , '183000', 'Wednesday' ,'Goverdhan')")

c.execute("Insert into Temple_details Values(4,'JanmBhumi', '070000', '180000', 'Working Days','Mathura')")

c.execute("Insert into Temple_details Values(5,'Prem Mandir','080000' , '170000', 'Working Days except Thrusday','Chhatikrah Road, Mathura')")

c.execute("Insert into Temple_details Values(6,'Chakleshwar Mahadev','060000','180000','Weekends','Goverdhan')")

c.execute("Insert into Temple_details Values(7,'Hanuman Temple','070000','190000','Tuesday','Mathura')")

c.execute("Insert into Temple_details Values(8,'Satya Narayan Temple','080000','180000','All week','Jatipura Road,Goverdhan')")

c.execute("Insert into Temple_details Values(9,'Srinathji Temple','073000','183000','all week','Mathura')")

c.execute("Insert into Temple_details Values(10,'Shri Radha Rani Temple' ,'080000' ,'180000','Working Days','Vrindavan')")

mydb.commit()

sno=10
def login():
    print("-" * 100)
    print("\t LOGIN")
    un = input("Enter User Name : ")
    pw = input("Enter Password : ")
    q = "select * from user where username = %s and passwd = %s"
    val = (un,pw)
    c1 = mydb.cursor()
    c1.execute(q,val)
    res = c1.fetchall()
    print("-" * 100)
    if len(res) == 0:
        print("Invalid User Name or Password ")
        print("-" * 100)
        return False
    else:
        print("Access Granted !!!")
        print("-" * 100)
        return True

def updatetemple():
    c=mydb.cursor()
    tn=input("Enter Temple Name which you want to update :")
    while True:
        print("-"*30)
        print("A - Opening Time")
        print("B - Closing Time")
        print("C - Opening Days")
        print("D - Exit for Updating")
        print("-"*30,'\n')
        choice=input("Enter your choice:")
        if choice=="A":
            new=input("\tEnter opening time:")
            q="update Temple_details set open_time=%s where temple_name=%s"
            val=(new,tn)
            c.execute(q,val)
            mydb.commit()
            print("Successfully Updated\n")
        elif choice=="B":
            new=input("\tEnter closing time:")
            q="update Temple_details set closing_time=%s where temple_name=%s"
            val=(new,tn)
            c.execute(q,val)
            mydb.commit()
            print("Successfully Updated\n")
        elif choice=="C":
            new=input("\tEnter opening days:")
            q="update Temple_details set open_days=%s where temple_name=%s"
            val=(new,tn)
            c.execute(q,val)
            mydb.commit()
            print("Successfully Updated\n")
        elif choice=="D":
            break
        else:
            print("Invalid Input\n")

def addtemple():
    print("You need to verify again to add a new temple in the list")
    c=mydb.cursor()
    if login():
        global sno
        sno+=1
        tn=input("Enter Temple name:")
        ot=input("Enter Opening Time in format HHMMSS:")
        ct=input("Enter Closing Time HHMMSS:")
        od=input("Enter Opening Days:")
        add=input("Enter Address:")
        q="insert into temple_details values(%s,%s,%s,%s,%s,%s)"
        val = (sno,tn,ot,ct,od,add)
        c.execute(q,val)
        mydb.commit()
        print("Temple details added successfully")

def showalltemples():
    c = mydb.cursor()
    c.execute("select * from temple_details")
    res = c.fetchall()
    
    print("List of Temples")
    for val in res:
        print("Sr no. : "+str(val[0]) + "   Temple Name :" + val[1])

def countTemples():
    c=mydb.cursor()
    c.execute("select count(*) from temple_details")
    res=c.fetchall()
    print("Number of Temples in the list are ",res[0][0])
    
def showtemple():
    c=mydb.cursor()
    tn=input("Enter Temple name whose details you want to see:")
    q="select * from temple_details where temple_name=%s"
    
    val=(tn,)
    c.execute(q,val)
    res=c.fetchall()
    print("-"*100)
    print("Sr no.\tTemple Name\tOpening Time \tClosing Time\tOpening Days\tAddress")
    print("-"*100)
    for val in res:
       print(val[0], "\t",val[1],"\t ",val[2],"\t ",val[3],"\t",val[4],"\t",val[5])    


def deletetemple():
    print("You need to verify again to delete temple in the list")
    if login():
        global sno
        c=mydb.cursor()
        sno-=1
        sn=input("Enter serial number of temple:")
        q="delete from temple_details where sr_no=%s"
        val=(sn,)
        c.execute(q,val)
        mydb.commit()
        print("Temple Deleted Successfully")


if login():
    while True:
        print("-" * 100)
        print("\t MENU")
        print("-" * 100)
        print("Press 1 - To see a Temple details")
        print("Press 2 - Add a new Temple")
        print("Press 3 - Show all Temples")
        print("Press 4 - Show number of Temples")
        print("Press 5 - Delete a Temple")
        print("Press 6 - Updating Temple Details")
        print("Press 7 - Quit")
        ch = int(input("Enter Your Choice : "))

        if ch==1:
            showtemple()

        elif ch==2:
            addtemple()

        elif ch==3:
            showalltemples()

        elif ch==4:
            countTemples()

        elif ch==5:
            deletetemple()

        elif ch==6:
            updatetemple()
            
        elif ch==7:
            break
        else:
            print("Invalid Input")
    

    


