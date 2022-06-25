import mysql.connector as mysql
from mysql.connector import *
from BuyProduct import *
from Customer import *
from Customerlogin import *
from Seller import *
from Sellerlogin import *
from PrintTableData import *
from Admin import *
import subprocess as sp
import time
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "PPathak@2106",
    database = "easycart"
)

def clear_screen():
    tmp=sp.call('cls',shell=True)

if(__name__=="__main__"):

    print("Welcome to EasyCart")
    print(" ")
    print(" ")

    choice=1

    while(choice!=4):

        
        print("Please Select category:")
        print(" ")
        print("1. Admin")
        print("2. Seller")
        print("3. Customer")
        print("4. exit")
        print(" ")

        choice=int(input())

        clear_screen()

        if(choice==1):
        	Admin_Main()

        elif(choice==2):
        	User_ID=Sellerlogin()

        elif(choice==3):
        	User_ID=Customerlogin()

        else:
        	break

        if((choice==2 or choice==3) and User_ID!=-1):
        	break

    if(choice==4):
        print("Thanks for visitng EasyCart. Please come again!!!!")
        exit(0)

    time.sleep(1)
    clear_screen()
    
    if(User_ID[0]=='S'):
        Seller_main(User_ID)

    elif(User_ID[0]=='C'):
        Customer_main(User_ID)

        


