import mysql.connector as mysql
from mysql.connector import *
from Customerlogin import *
from Seller import *
from Sellerlogin import *
from BuyProduct import *
import subprocess as sp
from PrintTableData import *
import time

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "PPathak@2106",
    database = "easycart"
)

def clear_screen():
	tmp=sp.call('cls',shell=True)

def generate_Order_ID():

	cursor=db.cursor()
	query="SELECT Order_ID from Orders"
	ans=0
	try:
		cursor.execute(query)
		result=cursor.fetchall()
		for i in result:
			ans=max(ans,int(i[0]))
		return ans
	except Error as error:
		print("Failed to generate_Order_ID {}".format(error))
		return -1

def Add_to_Orders(i):

	cursor=db.cursor()

	Order_ID=generate_Order_ID()+1
	User_ID=i[3]
	Product_ID=i[2]
	Order_Date=i[5]
	Cost=i[4]
	PaymentStatus="Cash on Delivery"
	Status="Not Delivered"

	values=(Order_ID,User_ID,Product_ID,Order_Date,Cost,PaymentStatus,Status)
	query="INSERT INTO Orders (order_id, user_id, product_id, order_date, cost, PaymentMode, status) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	try:
		cursor.execute(query,values)
		db.commit()
	except Error as error:
		print("Failed to add to orders {}".format(error))

def Checkout_Cart(Customer_id):

	cursor=db.cursor()
	values=(Customer_id)
	query="SELECT * FROM Cart WHERE Customer_id=%s"
	try:
		cursor.execute(query,(values, ))
		result=cursor.fetchall()
		Print_Table(result,"Cart")
		for i in result:			
			Add_to_Orders(i)

	except Error as error:
		print("Failed to Checkout {}".format(error))
		

	query="DELETE FROM Cart where Customer_id=%s"
	try:
		cursor.execute(query,(values, ))

	except Error as error:
		print("Failed to Checkout {}".format(error))
		


def CheckOrders(Customer_id):

	cursor=db.cursor()
	values=(Customer_id)
	query="SELECT * FROM Orders WHERE User_id=%s"

	try:
		cursor.execute(query,(values, ))
		result=cursor.fetchall()
		Print_Table(result,"Orders")

	except Error as error:
		print("Failed to Find any orders {}".format(error))

def Update_Rating(Product_ID,review):

	cursor=db.cursor()
	values=(Product_ID)
	query="SELECT * FROM Product WHERE product_id = %s"
	try:
		cursor.execute(query,(values,))
		result=cursor.fetchall()

		Rating=float(result[0][7])
		totalreviews=int(result[0][8])

		Rating=(Rating*totalreviews+review)/(totalreviews+1)
		totalreviews+=1

		#print(Rating,totalreviews)

		cursor=db.cursor()
		values=(Rating,Product_ID)
		query="UPDATE Product SET rating = %s WHERE product_id = %s"

		try:
			cursor.execute(query,values)
			db.commit()
		except Error as error:
			print("Failed to update Ratings {}".format(error))

		cursor=db.cursor()
		values=(totalreviews,Product_ID)
		query="UPDATE Product SET totalreviews = %s WHERE product_id = %s"

		try:
			cursor.execute(query,values)
			db.commit()
		except Error as error:
			print("Failed to update Ratings {}".format(error))


	except Error as error:
		print("Failed to update Ratings {}".format(error))
	

def Feedback(Customer_id):		

	print("Print the Order_ID of the order for which you would like to give your Feedback:")
	CheckOrders(Customer_id)

	Order_ID=str(input())

	cursor=db.cursor()
	values=(Order_ID)
	query="SELECT * FROM Orders WHERE order_id=%s"

	try:
		cursor.execute(query,(values, ))
		result=cursor.fetchall()
		Product_ID=result[0][2]
		User_ID=result[0][1]
		
		fdate="2020-05-30"

		print("Give rating from 1 to 5 with 1 being lowest and 5 being highest:")
		rating=int(input())

		cursor=db.cursor()
		values=(Order_ID,Product_ID,User_ID,fdate,rating)
		query="INSERT INTO Feedback (order_id, product_id, user_id, fdate, ratingpoints) VALUES (%s,%s,%s,%s,%s)"

		try:
			cursor.execute(query,values)
			db.commit()
			Update_Rating(Product_ID,rating)

		except Error as error:
			print("Failed to Inset Feedback {}".format(error))



	except Error as error:
		print("Failed to Find any Feedback {}".format(error))



def Customer_main(customer_id):

	choice=-1
	while(choice!=5):

		print("Please select one of the opertion:")
		print("1. Buy a Product")
		print("2. CheckOut from Cart")
		print("3. Check Your Orders")
		print("4. Give Feedback")
		print("5. Exit")

		choice=int(input())

		if(choice==1):
			buyproduct(customer_id)

		elif(choice==2):
			Checkout_Cart(customer_id)

		elif(choice==3):
			CheckOrders(customer_id)

		elif(choice==4):
			Feedback(customer_id)

		elif(choice==5):
			return

