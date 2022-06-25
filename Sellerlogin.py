import mysql.connector as mysql
from mysql.connector import *
from BuyProduct import *
from Customer import *
from Customerlogin import *
from Seller import *
from PrintTableData import *
import time
import subprocess as sp

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "PPathak@2106",
    database = "easycart"
)

def clear_screen():
    tmp=sp.call('cls',shell=True)

def User_Insert(key,name,email,passwd,phone):

    cursor=db.cursor()
    #key=str(key)
    values=(key,name,passwd,email,phone)
    #print(values,passwd)
    query="INSERT INTO users (user_id, user_name, passcode, email, phoneNo) VALUES (%s,%s,%s,%s,%s)"

    try:
        cursor.execute(query,values)
        db.commit()
        return key
    except Error as error:
        print("Failed to insert into MySQL table {}".format(error))
        return -1

def Seller_Insert(key,name,email,passwd,phone):

    cursor=db.cursor()
    #key=str(key)
    values=(key,name,passwd,email,phone)
    #print(values)
    
    query="INSERT INTO Seller (Seller_id, user_name, passcode, email, phoneNo) VALUES (%s,%s,%s,%s,%s)"

    try:
        cursor.execute(query,values)
        db.commit()
        return key

    except Error as error:
        print("Failed to insert into MySQL table {}".format(error))
        return -1


def Seller_getID(email,passwd):

    cursor=db.cursor()

    values=(email,passwd)

    query="SELECT Seller_id from Seller WHERE Email = %s AND passcode = %s"

    try:
        cursor.execute(query,values)
        record=cursor.fetchall()
        if(record!=[]):
            return record[0][0]
        else:
            print("Failed to find Seller with email and password")
            return -1

    except Error as error:
        print("Failed to find Seller with email and password {}".format(error))
        return -1


def Signup():

    cursor=db.cursor()
    query="Select * from users";

    cursor.execute(query)
    
    total_users=0
    result=cursor.fetchall()
    for i in result:
        total_users=max(total_users,int(i[0]))

    print("Enter Name:")
    name=str(input())
    print(" ")

    print("Enter email:")
    email=str(input())
    print(" ")

    print("Enter passwd:")
    passwd=str(input())
    print(" ")


    print("Enter phone:")
    phone=""
    while(type(phone)!=int):
        try:
            phone=int(input())
        except:
            KeyError
            print("Not valid")


    User_ID=User_Insert(total_users+1,name,email,passwd,phone)
    if(User_ID!=-1):
        
        User_ID='S'+str(User_ID)
        User_ID=Seller_Insert(User_ID,name,email,passwd,phone)
        

    return User_ID

def Login():

    print("Enter email:")
    email=str(input())
    print(" ")

    print("Enter passwd:")
    passwd=str(input())
    print(" ")

    User_ID=Seller_getID(email,passwd)
    
    return User_ID




def Sellerlogin():

    option=1
    while(option!=3):

        print("Select Option:")
        print("1. Signup")
        print("2. Login")
        print("3. Exit ")
        print(" ")

        option=int(input())

        clear_screen()

        if(option==1):
            User_ID=Signup()

        elif(option==2):
            User_ID=Login()

        else:
            return -1

        #print(User_ID)

        if(User_ID!=-1):
            print("Successfully Logged In")
            return User_ID

        clear_screen()

    

