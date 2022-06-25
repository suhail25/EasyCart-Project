import mysql.connector as mysql
from mysql.connector import *
from BuyProduct import *
from Customer import *
from Customerlogin import *
from Seller import *
from Sellerlogin import *
from PrintTableData import *
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

def Print_Seller_Table():

	cursor=db.cursor()
	query="SELECT * FROM Seller"

	try:
		cursor.execute(query)
		result=cursor.fetchall()
		Print_Table(result,"Seller")
	except Error as error:
		print("Failed to print the Seller Table {}".format(error))


def Print_Customer_Table():

	cursor=db.cursor()
	query="SELECT * FROM Customer"

	try:
		cursor.execute(query)
		result=cursor.fetchall()
		Print_Table(result,"Customer")
	except Error as error:
		print("Failed to print the Customer Table {}".format(error))


def Delete_Seller_Table():


	Print_Seller_Table()

	print("Please enter the Seller ID you want to Delete")
	Seller_ID=str(input())

	cursor=db.cursor()
	values=(Seller_ID)
	query="DELETE FROM Seller WHERE seller_id = %s"

	try:
		cursor.execute(query,(values, ))
		db.commit()

	except Error as error:
		print("Failed to Delete from Seller Table {}".format(error))

def Delete_Customer_Table():


	Print_Customer_Table()

	print("Please enter the Customer ID you want to Delete")
	Customer_ID=str(input())

	cursor=db.cursor()
	values=(Customer_ID)

	query="DELETE FROM Customer WHERE customer_id = %s"

	try:
		cursor.execute(query,(values, ))
		db.commit()

	except Error as error:
		print("Failed to Delete from Customer Table {}".format(error))


def Print_Product_Table():

	cursor=db.cursor()
	query="SELECT * FROM Product"

	try:
		cursor.execute(query)
		result=cursor.fetchall()
		Print_Table(result,"Product")
	except Error as error:
		print("Failed to print the Product Table {}".format(error))


def Delete_Product_Table():


	Print_Product_Table()

	print("Please enter the Product ID you want to Delete")
	Product_ID=str(input())

	cursor=db.cursor()
	values=(Product_ID)

	query="DELETE FROM Product WHERE product_id = %s"

	try:
		cursor.execute(query,(values, ))
		db.commit()

	except Error as error:
		print("Failed to Delete from Product Table {}".format(error))

def Print_Order_Table():

	cursor=db.cursor()
	query="SELECT * FROM Orders"

	try:
		cursor.execute(query)
		result=cursor.fetchall()
		Print_Table(result,"Orders")
	except Error as error:
		print("Failed to print the Order Table {}".format(error))


def Delete_Product_Table():

	Print_Order_Table()

	print("Please enter the Order ID you want to Delete")
	Order_ID=str(input())

	cursor=db.cursor()
	values=(Order_ID)

	query="DELETE FROM Orders WHERE order_id = %s"

	try:
		cursor.execute(query,(values, ))
		db.commit()

	except Error as error:
		print("Failed to Delete from Orders Table {}".format(error))

def Admin_Main():

	choice=-1
	while(choice!=9):
		print("Please select one of the operations:")
		print(" ")
		print("1. View Sellers Table")
		print("2. View Customer Table")
		print("3. Delete Seller")
		print("4. Delete Customer")
		print("5. View Products")
		print("6. Delete Products")
		print("7. View Orders")
		print("8. Delete from Orders")
		print("9. Exit")

		print(" ")

		choice=int(input())

		clear_screen()

		if(choice==1):
			Print_Seller_Table()

		elif(choice==2):
			Print_Customer_Table()

		elif(choice==3):
			Delete_Seller_Table()

		elif(choice==4):
			Delete_Customer_Table()

		elif(choice==5):
			Print_Product_Table()

		elif(choice==6):
			Delete_Product_Table()

		elif(choice==7):
			Print_Order_Table()

		elif(choice==8):
			Delete_Order_Table()

		else:
			break




