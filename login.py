#Establishing connection between python and mysql
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Akhilesh1327$l",database="bank_data")
cursor=con.cursor()

#importing all the modules required
import deposit
import withdrawl
import transfer
import update_info
import details

#Function to create serialised account numbers
def acc_num():
    sql="select count(*) from new_customer"
    cursor.execute(sql)
    data=cursor.fetchone()
    global i
    i=1000
    i=data[0]+i
    
#Function to add new customer details into table
def new_customer():
    print("----WELCOME TO NEW CUSTOMER PAGE----")
    First_name=input("ENTER YOUR FIRST NAME:")
    Second_name=input("ENTER YOUR SECOND NAME:")
    Phone_number=int(input("ENTER YOUR PHONE NUMBER:"))
    Username=input("ENTER YOUR USERNAME:")
    Password=input("ENTER YOUR PASSWORD:")
    Email=input("ENTER YOUR EMAIL:")
    Balance=0
    acc_num()
    Account_number=i
    Date_of_birth=input("ENTER DATE OF BIRTH IN YYYY-MM-DD FORMAT")
    sql="insert into new_customer(first_name,second_name,phone_number,username,password,account_number,balance,email,date_of_birth) values('{}','{}',{},'{}','{}',{},{},'{}','{}')".format(First_name,Second_name,Phone_number,Username,Password,Account_number,Balance,Email,Date_of_birth)
    cursor.execute(sql)
    con.commit()
    print("SUCCESSFUL ENTRY FOR A NEW USER")

#Function to check the username and password of the customer and allowing them to login if they are correct   
login=False
def existing_customer():
    print("----WELCOME----")
    print("ENTER USERNAME AND PASSWORD TO PROCEED")
    Username=input("ENTER USERNAME:")
    Password=input("ENTER PASSWORD:")
    sql="select username,password from new_customer"
    cursor.execute(sql)
    data=cursor.fetchall()
    for row in data:
        if row[0]==Username and row[1]==Password:
            print("SUCCESSFULLY LOGGED IN")
            global login
            login=True
            break
        else:
            continue
    else:
        print("INVALID USERNAME OR PASSWORD")
        
 #Function to allow login of admins by checking that their login credentials are correct                    
def adminlogin():
    print("----WELCOME----")
    print("ENTER YOUR NAME AND SECRET KEY TO PROCEED")
    Name=input("ENTER YOUR NAME")
    Secret_key=int(input("ENTER SECRET KEY"))
    sql="select * from admin"
    cursor.execute(sql)
    data=cursor.fetchall()
    for row in data:
        if row[0].lower()==Name.lower() and row[1]==Secret_key:
            print("SUCCESSFUL ADMIN LOGIN")
            print("YOU CAN NOW CHNAGE THE DETAILS OF THE RESPECTIVE CUSTOMER")
            update_info.update_info()
            break
        else:
            continue
    else:
        print("INVALID ADMIN ENTRY")
    
#Function to check whether its a new customer,an existing customer or an admin
#This is the main function as all of the funtions from different modules are called under this function login
def login():
    print("----WELCOME TO LOGIN PAGE----")
    print("1. NEW CUSTOMER")
    print("2. EXISTING USER")
    print("3. ADMIN LOGIN")
    choice=int(input("ENTER YOUR CHOICE"))
    if choice==1:
        print()
        new_customer()
        existing_customer()
    elif choice==2:
        print()
        existing_customer()
    elif choice==3:
        print()
        adminlogin()

#Giving user choices of the activites and performing the respective activity as per their choice
    if login==True:
        print("CHOOSE THE ACTIVITY FROM THE FOLLOWING")
        print("1. Deposit")
        print("2. Withdrawl")
        print("3. Transfer")
        print("4. Details")
        print("5. Exit")
        ch=int(input("ENTER YOUR CHOICE"))
        if ch==1:
            deposit.deposit()
        elif ch==2:
            withdrawl.withdraw()
        elif ch==3:
            transfer.transfer()
        elif ch==4:
            details.details()
        elif ch==5:
            print("THANK YOU VISIT AGAIN")

login()
   
      
        
        
