import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="Akhilesh1327$l",database="bank_data")
cursor=con.cursor()

#Function which performs the activity of adding amount to the savings
#account of the customer after making sure that their credentials are correct
def withdraw():
    print("---WELCOME TO WITHDRAWL PAGE---")
    Account_number=int(input("ENTER YOUR ACCOUNT NUMBER"))
    Phone_number=int(input("ENTER YOUR PHONE NUMBER"))
    amount=float(input("ENTER AMOUNT TO BE WITHDRAWED"))
    sql_select_query="select phone_number,account_number,balance from new_customer"
    cursor.execute(sql_select_query)
    data=cursor.fetchall()
    for row in data:
        if row[0]==Phone_number and row[1]==Account_number and float(row[2])>amount:
            print("PHONE NUMBER AND ACCOUNT NUMBER MATCHED")
            final_amount=float(row[2])-amount
            sql_update_query="update new_customer set balance={} where account_number={}".format(final_amount,Account_number)
            cursor.execute(sql_update_query)
            con.commit()
            print("AMOUNT SUCCESSFULLY WITHDRAWED")
            break
        else:
            continue
    else:
        print("INVALID ACCOUNT NUMBER OR MOBILE NUMBER OR INSUFFICIENT AMOUNT")
    
    
