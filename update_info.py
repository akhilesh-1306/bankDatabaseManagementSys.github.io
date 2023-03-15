import mysql.connector 
con=mysql.connector.connect(host="localhost",user="root",passwd="Akhilesh1327$l",database="bank_data")
cursor=con.cursor()

#Function which gives the admin options of which part of customer's details is to be updated
def update_info():
    print("---WELCOME TO UPDATE INFO PAGE---")
    print("CHOOSE WHICH DATA TO BE MODIFIED")
    print("1. First Name")
    print("2. Second Name")
    print("3. Phone Number")
    print("4. Username")
    print("5. Password")
    ch=int(input("***ENTER YOUR CHOICE***"))
    print("FOR VERIFICATION ENTER THE DETAILS BELOW")
    Account_number=int(input("ENTER CUSTOMER ACCOUNT NUMBER"))
    Phone_number=int(input("ENTER CUSTOMER PHONE NUMBER"))
    sql_select_query="select account_number,phone_number from new_customer"
    cursor.execute(sql_select_query)
    data=cursor.fetchall()
    for row in data:
        validity=False
        if row[0]==Account_number and row[1]==Phone_number:
            validity=True
            break
        else:
            continue
    else:
        print("INVALID ACCOUNT NUMBER OR PHONE NUMBER")
    if ch==1 and validity==True:
        First_name=input("ENTER NEW FIRST NAME")
        sql_update_query_1="update new_customer set first_name='{}' where account_number={}".format(First_name,Account_number)
        cursor.execute(sql_update_query_1)
        con.commit()
        print("FIRST NAME SUCCESSFULLY CHANGED")
    elif ch==2 and validity==True:
        Second_name=input("ENTER NEW SECOND NAME")
        sql_update_query_2="update new_customer set second_name='{}' where account_number={}".format(Second_name,Account_number)
        cursor.execute(sql_update_query_2)
        con.commit()
        print("SECOND NAME SUCCESSFULLY CHANGED")
    elif ch==3 and validity==True:
        Phone_number=int(input("ENTER NEW PHONE NUMBER"))
        sql_update_query_3="update new_customer set phone_number={} where account_number={}".format(Phone_number,Account_number)
        cursor.execute(sql_update_query_3)
        con.commit()
        print("PHONE NUMBER SUCCESSFULLY CHANGED")
    elif ch==4 and validity==True:
        Username=input("ENTER NEW USERNAME")
        sql_update_query_4="update new_customer set username='{}' where account_number={}".format(Username,Account_number)
        cursor.execute(sql_update_query_4)
        con.commit()
        print("USERNAME SUCCESSFULLY CHANGED")
    elif ch==5 and validity==True:
        Password=input("ENTER NEW PASSWORD")
        sql_update_query_5="update new_customer set password='{}' where account_number={}".format(Password,Account_number)
        cursor.execute(sql_update_query_5)
        con.commit()
        print("PASSWORD SUCCESSFULLY CHANGED")
        
        
        

    
