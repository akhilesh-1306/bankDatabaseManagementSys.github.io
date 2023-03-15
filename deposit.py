#connection
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Akhilesh1327$l",database="bank_data")
cursor=con.cursor()

#Function which performs the activity of removing amount withdrawn from savings
#account of the customer after making sure that their credentials are correct
def deposit():
    print("----WELCOME TO DEPOSIT PAGE----")
    Account_number=int(input("ENTER YOUR ACCOUNT NUMBER"))
    Phone_number=int(input("ENTER YOUR PHONE NUMBER"))  
    sql_select_query="select phone_number,account_number,balance from new_customer"
    cursor.execute(sql_select_query)
    data=cursor.fetchall()
    for row in data:
        if row[0]==Phone_number and row[1]==Account_number:
            print("PHONE NUMBER AND ACCOUNT NUMBER MATCHED")
            amount=float(input("ENTER AMOUNT TO BE DEPOSITED"))
            final_amount=float(row[2])+amount
            sql_update_query="update new_customer set balance={} where account_number={}".format(final_amount,Account_number)
            cursor.execute(sql_update_query)
            con.commit()
            print("AMOUNT SUCCESSFULLY CREDITED")
            break
        else:
            continue
    else:
        print("INVALID ACCOUNT NUMBER OR MOBILE NUMBER")
            
    
