import mysql.connector as mysql
from mysql.connector import *
from datetime import date
from PrintTableData import *
import subprocess as sp
import time
today=date.today()
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "PPathak@2106",
    database = "easycart"
)

def clear_screen():
	tmp=sp.call('cls',shell=True)


def get_Price(Prod_id):

	cursor=db.cursor()
	values=(Prod_id)
	query="SELECT cost FROM Product WHERE product_id = %s"

	try:
		cursor.execute(query,(values, ))
		result=cursor.fetchall()
		return result[0][0]

	except Error as error:
		print("Failed to find products {}".format(error))
		return -1

def get_Product_Name(prod_id):

	cursor=db.cursor()
	values=(prod_id)
	query="SELECT product_name FROM Product WHERE product_id = %s"

	try:
		cursor.execute(query,(values, ))
		result=cursor.fetchall()
		return result[0][0]

	except Error as error:
		print("Failed to find products {}".format(error))
		return -1

def get_CartCount():

	cursor=db.cursor()
	query="SELECT * FROM Cart"

	try:
		cursor.execute(query)
		result=cursor.fetchall()
		ans=0
		for i in result:
			ans=max(ans,int(i[0]))
		return ans

	except Error as error:
		print("Failed to find products {}".format(error))
		return -1


def Add_to_Cart(Customer_id,Prod_id):

	cursor=db.cursor()
	cart_id=get_CartCount()+1
	price=get_Price(Prod_id)
	if(price==-1):
		print("Product with given Product ID is not available.")
		return 

	d1=today.strftime("%Y-%m-%d")
	product_name=get_Product_Name(Prod_id)
	values=(cart_id,product_name,Prod_id,Customer_id,price,d1,"2020-05-15")
	query="INSERT INTO Cart (cart_id, product_name, product_id, customer_id, billamount, dateadded, expectdelivery) VALUES (%s,%s,%s,%s,%s,%s,%s)"

	try:
		cursor.execute(query,values)
		db.commit()

	except Error as error:
	    print("Failed to insert into Cart table {}".format(error))

	
	

def Show_Product(Prod_name, startprice, endprice):

	cursor=db.cursor()

	values=(Prod_name,startprice,endprice)
	query="SELECT * FROM Product WHERE Product_name=%s AND Cost >= %s AND Cost <= %s ORDER BY Rating DESC"

	try:
		cursor.execute(query,values)
		record=cursor.fetchall()
		Print_Table(record,"Product")


	except Error as error:
		print("Failed to find products {}".format(error))

	


def buyproduct(Customer_id):

	print("Please enter Product name: ")
	prod_name=str(input())
	prod_name=prod_name.lower()

	print("Enter Price Range")
	print(" ")

	print("Start value: ")
	start=int(input())
	print(" ")

	print("End Value: ")
	end=int(input())

	print("The available products are: ")
	flag=Show_Product(prod_name,start,end)
	print(" ")

	if(flag==-1):
		return

	print("Select one of the following options: ")
	print("1. Buy a available Product")
	print("2. Exit")

	choice=int(input())
	print(" ")
	if(choice==1):
		print("Enter Product ID of product available that you want to buy:")
		prod_id=str(input())
		print(prod_id)
		Add_to_Cart(Customer_id,prod_id)

	else:
		return








