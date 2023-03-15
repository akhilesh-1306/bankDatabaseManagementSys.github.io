import mysql.connector 
con=mysql.connector.connect(host="localhost",user="root",passwd="Akhilesh1327$l",database="bank_data")
cursor=con.cursor()

#Function which diplays the details of a particular customer
def details():
    print("---WELCOME TO DETAILS PAGE---")
    print("FOR VERIFICATION ENTER THE DETAILS BELOW")
    Account_number=int(input("ENTER YOUR ACCOUNT NUMBER"))
    Phone_number=int(input("ENTER YOUR PHONE NUMBER"))
    sql_select_query_1="select * from new_customer"
    cursor.execute(sql_select_query_1)
    data=cursor.fetchall()
    for row in data:
        validity=False
        if row[5]==Account_number and row[2]==Phone_number:
            validity=True
            break
        else:
            continue
    else:
        print("INVALID ACCOUNT NUMBER OR PHONE NUMBER")
    if validity==True:
        sql_select_query_2="select * from new_customer where account_number={}".format(Account_number)
        cursor.execute(sql_select_query_2)
        data=cursor.fetchone()
        for i in range(8):            
            print("FIRST NAME:",data[0])
            print("SECOND NAME:",data[1])
            print("PHONE NUMBER:",data[2])
            print("USERNAME:",data[3])
            print("EMAIL:",data[7])
            print("BALANCE:",data[6])
            break
    elif validity==False:
        print("INVALID ACCOUNT NUMBER OR PHONE NUMBER")
    if validity==True:
        sql_select_query_3="select date_of_birth from new_customer where account_number={}".format(Account_number)
        cursor.execute(sql_select_query_3)
        data=cursor.fetchone()
        for i in data:
            print("DATE OF BIRTH IS:",end='')
            print(i,end=' ')
        
        
        
        
    
