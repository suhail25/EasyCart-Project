import mysql.connector as mysql
from mysql.connector import *
from prettytable import PrettyTable
import time
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "PPathak@2106",
    database = "easycart"
)

def clear_screen():
	tmp=sp.call('cls',shell=True)


def Print_Table(data, TableName):

	x=PrettyTable()

	if(TableName=="Users" or TableName=="Seller" or TableName=="Customer"):
		x.field_names=["User_ID", "User Name", "Password", "Email", "Phone No."]

		for i in range(len(data)):
			arr=[]
			for j in data[i]:
				arr.append(j)
			x.add_row(arr)

		print(x)

	elif(TableName=="Product"):

		x.field_names=["Product_ID", "Product Name", "Description", "Seller_ID", "Category", "Cost", "Quantity", "Rating", "Totalreviews"]

		for i in range(len(data)):
			arr=[]
			for j in data[i]:
				arr.append(j)
			x.add_row(arr)

		print(x)

	elif(TableName=="Cart"):

		x.field_names=["Cart_ID", "Product Name", "Product_ID", "Customer_ID", "Cost", "Date Added", "Expected Delivery"]

		for i in range(len(data)):
			arr=[]
			for j in data[i]:
				arr.append(j)
			x.add_row(arr)

		print(x)

	elif(TableName=="Orders"):

		x.field_names=["Order_ID", "Customer_ID", "Product_ID", "Order Date", "Cost", "Payment Mode","Status"]

		for i in range(len(data)):
			arr=[]
			for j in data[i]:
				arr.append(j)
			x.add_row(arr)

		print(x)

	elif(TableName=="Category"):

		x.field_names=["Category_ID", "Category Name"]

		for i in range(len(data)):
			arr=[]
			for j in data[i]:
				arr.append(j)
			x.add_row(arr)

		print(x)





