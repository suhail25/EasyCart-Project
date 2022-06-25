import mysql.connector as mysql
from mysql.connector import *
from BuyProduct import *
from Customer import *
from Customerlogin import *
from Sellerlogin import *
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

def get_productcount():

	cursor=db.cursor()

	query="SELECT * FROM Product"
	cursor.execute(query)


	result=cursor.fetchall()
	ans=0
	for i in result:
		ans=max(ans,int(i[0]))
	return ans


def get_Category():

	cursor=db.cursor()

	query="SELECT * FROM Category"
	cursor.execute(query)

	result=cursor.fetchall()

	print("Select one from the following Category: ")
	Print_Table(result,"Category")

	ans=int(input())

	for i in result:
		if(int(i[0])==ans):
			return i[1]


def add_product(seller_id):

	product_id=get_productcount()+1

	print("Please enter the following information")
	print(" ")

	print("Product Name:")
	product_name=str(input())
	print(" ")

	print("Product Description:")
	product_description=str(input())

	print("Select a Category:")
	Category=get_Category()

	print("Select Cost:")
	cost=float(input())

	print("Select Quantity:")
	quantity=int(input())


	cursor=db.cursor()
	rating=3
	totalreviews=1
	#key=str(key)
	values=(product_id,product_name,product_description,seller_id,Category,cost,quantity,rating,totalreviews)
	#print(values,passwd)
	query="INSERT INTO Product (product_id,product_name,product_description,seller_id,Category,cost,quantity,rating,totalreviews) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

	try:
		cursor.execute(query,values)
		db.commit()

	except Error as error:
		print("Failed to add product into Product table {}".format(error))

def del_prod(prod_id):

	cursor=db.cursor()
	values=(prod_id)
	query="DELETE FROM Product WHERE product_id = %s"

	try:
		cursor.execute(query,(values, ))
		db.commit()

	except Error as error:
		print("Failed to delete product from Product table {}".format(error))


def remove_product(sel_id):

	cursor=db.cursor()
	values=(sel_id)

	query="SELECT * FROM Product WHERE seller_id = %s"

	cursor.execute(query,(values, ))

	result=cursor.fetchall()

	Print_Table(result,"Product")

	print(" ")

	print("From these products enter the product_id of the product you want to delete.")

	prod_id=int(input())

	del_prod(prod_id);

def update_product(sel_id):

	cursor=db.cursor()
	values=(sel_id)
	query="SELECT * FROM Product WHERE Seller_id=%s"

	try:
		cursor.execute(query,(values,))
		result=cursor.fetchall()
		Print_Table(result,"Product")

	except Error as error:
		print("Failed to find Products for given Seller {}".format(error))

	print(" ")

	print("From these products enter the product_id of the product you want to delete.")

	prod_id=int(input())

	dict1={}
	print("Select one of the following attributes:")

	print("1. Product Name")
	print("2. Product Description")
	print("3. Cost")
	print("4. Quantity")

	attribute=int(input())

	cursor=db.cursor()
	print("Enter the updated value: ")
	if(attribute==1 or attribute==2):
		new_value=str(input())
		if(attribute==1):
			query="UPDATE Product SET product_name = %s WHERE product_id = %s"
		else:
			query="UPDATE Product SET product_description = %s WHERE product_id = %s"

	elif(attribute==3):
		new_value=float(input())
		query="UPDATE Product SET Cost = %s WHERE product_id = %s"
	else:
		new_value=int(input())
		query="UPDATE Product SET Quantity = %s WHERE product_id = %s"
	
	values=(new_value,prod_id)
	try:
		cursor.execute(query,values)
		db.commit()
	except Error as error:
		print("Failed to update product from Product table {}".format(error))

def check_income(seller_id):

	income=0
	cursor=db.cursor()

	query="SELECT product_id FROM orders"
	try:
		cursor.execute(query)
		result=cursor.fetchall()
		db.commit()
		for i in result:

			cursor=db.cursor()
			query="SELECT Cost FROM Product WHERE product_id = %s and seller_id=%s"
			values=(i[0],seller_id)
			try:
				cursor.execute(query,values)
				result1=cursor.fetchall()
				if(len(result1)>0):
					income+=result1[0][0]
			except Error as error:
				print("Failed to calculate income {}".format(error))

		print(" ")
		print("Your income till now is:", income)

	except Error as error:
		print("Failed to calculate income {}".format(error))
		

def Seller_main(seller_id):

	choice=-1
	while(choice!=5):

		print("Please select one of the opertion: ")
		print("1. Add Product")
		print("2. Remove Product")
		print("3. Update Product")
		print("4. Check income")
		print("5. Exit")
		print(" ")

		choice=int(input())
		clear_screen()

		if(choice==1):
			add_product(seller_id)

		elif(choice==2):
			remove_product(seller_id)

		elif(choice==3):
			update_product(seller_id)

		elif(choice==4):
			check_income(seller_id)

		elif(choice==5):
			break

		

