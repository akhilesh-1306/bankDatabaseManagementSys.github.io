import mysql.connector 
con=mysql.connector.connect(host="localhost",user="root",passwd="gos123",database="bank_data")
if con.is_connected()==True:
    print("successfully connected to my sql")


def newcustomer():
    print("----WELCOME TO NEW CUSTOMER PAGE----")
    First_name=input("ENTER YOUR FIRST NAME")
    Second_name=input("ENTER SECOND NAME")
    Phone_number=int(input("ENTER PHONE NUMBER"))
    Username=input("ENTER USERNAME")
    Password=input("ENTER PASSWORD")
    
    cursor=con.cursor()
    sql="insert into new_customer(first_name,second_name,phone_number,username,password) values('{}','{}',{},'{}','{}')".format(First_name,Second_name,Phone_number,Username,Password)
    cursor.execute(sql)
    con.commit()
    
   

