import mysql.connector 
con=mysql.connector.connect(host="localhost",user="root",passwd="Akhilesh1327$l",database="bank_data")
cursor=con.cursor()

#Function which performs the activity of removing specific amount from one account and adding
#the same into the account of another customer after making sure that both the accounts
#exist and the credentials of the customer making the transfer match successfully
def transfer():
    print("---WELCOME TO TRANSFER PAGE---")
    Account_number_1=int(input("ENTER ACCOUNT NUMBER OF YOUR ACCOUNT:"))
    Phone_number=int(input("ENTER YOUR PHONE NUMBER:"))
    Account_number_2=int(input("ENTER ACCOUNT NUMBER OF THE OTHER ACCOUNT:"))
    sql_select_query="select phone_number,account_number,balance from new_customer"
    cursor.execute(sql_select_query)
    data=cursor.fetchall()
    amount=float(input("ENTER AMOUNT TO BE TRANSFERRED"))
    for row in data:
        existing=False
        if row[1]==Account_number_2:
            print("OTHER ACCOUNT NUMBER EXISTS")
            existing=True
            break
        else:
            continue
    else:
        print("THE OTHER ACCOUNT NUMBER DOESNT EXIST")
    
    for row in data:
        deduct=False
        if row[0]==Phone_number and row[1]==Account_number_1 and float(row[2])>=amount and existing==True:
            print("YOUR ACCOUNT NUMBER AND PHONE NUMBER MATCHED")
            final_amount_1=float(row[2])-amount
            sql_update_query_1="update new_customer set balance={} where account_number={}".format(final_amount_1,Account_number_1)
            cursor.execute(sql_update_query_1)
            con.commit()
            deduct=True
            break
        else:
            continue
    else:
        print("YOUR ACCOUNT NUMBER OR PHONE NUMBER IS INVALID")
    for row in data:
        added=False
        if row[1]==Account_number_2 and deduct==True:
            final_amount_2=float(row[2])+amount
            sql_update_query_2="update new_customer set balance={} where account_number={}".format(final_amount_2,Account_number_2)
            cursor.execute(sql_update_query_2)
            con.commit()
            added=True
            break
        else:
            continue
    if added==True:
        print("Rs/-",amount,"","SUCCESSFULLY TRANSFERRED FROM YOUR ACCOUNT TO ACCOUNT NUMBER",Account_number_2)
    else:
        print("TRANSFER UNSUCCESSFUL")
    
    
