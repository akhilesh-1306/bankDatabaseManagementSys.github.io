import new_customer
import withdrawl
import deposit
import transfer
import update_info
import details


def fun():
    while True:
        print("1. Withdrawl")
        print("2. Deposit")
        print("3. Transfer")
        print("4. Update_info")
        print("5. Details")
        print("6. Exit")
        ch=int(input("enter choice"))
        if ch==1:
            withdrawl.withdraw()    
        elif ch==2:
             deposit.deposit()  
        elif ch==3:
            transfer.transfer()
        elif ch==4:
            update_info.update_info
        elif ch==5:
            details.details()
        elif ch==6:
            break
            
       
fun()
    
        
        
        
    
    
    
