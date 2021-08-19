import mysql.connector
from datetime import datetime 
# pip install mysql
# pip install mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root", # Add username of your workbench here
    passwd="Aditya" ,# Add the password of your workbench here
    database="bank_db"
)

mycursor=db.cursor()

# mycursor.execute("DROP DATABASE bank_bd") -->to delete database 
# mycursor.execute("CREATE TABLE Customer (name varchar(50) NOT NULL,age smallint UNSIGNED NOT NULL, pincode INT(6) UNSIGNED NOT NULL,created datetime NOT NULL)")---> this is how you create a table
# mycursor.execute("INSERT INTO Customer (name,age,pincode,created) VALUES(%s,%s,%s,%s)",("abcd",28,1234526,datetime.now()))-->this is how you assign values to the table
# db.commit()--> commiting the changes on table after adding or removing the value

# mycursor.execute("SELECT * FROM Customer")
# mycursor.execute("ALTER TABLE Customer ADD COLUMN amount BIGINT UNSIGNED DEFAULT 0")
# mycursor.execute("ALTER TABLE Customer ADD COLUMN personid int PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE Customer ADD COLUMN username VARCHAR(12) NOT NULL ")

mycursor.execute("DELETE FROM Customer WHERE personid=6")
db.commit()
def withdraw():
    amount_withdrawl = int(input("ENTER AMOUNT: "))
    if a>=amount_withdrawl:
        newamount=a-amount_withdrawl
        mycursor.execute(f"UPDATE Customer SET amount = {newamount} WHERE personid={pid}")
        db.commit()
        print(f"TAKE YOUR {amount_withdrawl}Rs from the case and have a nice day")
        print(f"\nCURRENT BALANCE => {newamount}  ")
    else:
            print("not a valid amount")      

def deposit():
    deposit_amount = int(input("ENTER AMOUNT TO DEPOSIT: "))
    newamount=a + deposit_amount

    mycursor.execute(f"UPDATE Customer SET amount = {newamount} WHERE personid={pid}")
    db.commit()

    print(f"PUT {deposit_amount}Rs ON THE CASE BELOW  ")                                                
    print(f"{deposit_amount}Rs DEPOSITED TO YOUR ACCOUNT")
    print(f"\nCURRENT BALANCE => {newamount}  ")

def status():
    mycursor.execute(f"SELECT * FROM Customer WHERE username = '{username_input}' AND pincode='{pin}'")
    for i in mycursor:
        name=i[0]
        created=i[3]
        amount=i[4]
        personid=i[5]
            
    print(f"Hello {name}")
    print(f"Account created on : {created}")
    print(f"Your Current Balance is ==> {amount} \nand your ID id is: {person_id}")
        


# for i in mycursor:
#     print(i)
con=True
while con:
    print("WELCOME TO SSAV BANK")
    a = input("ARE YOU A NEW USER? Y for yes and N for no: ")
    if a=="y" or a=="Y":
        name = input("your name ? ==> ")
        age = int(input("your age ? ==> "))
        amount = int(input("your initial deposit ? ==> "))
        username=input("ENTER A UNIQUE USERNAME: ")
        mycursor.execute(f"SELECT * FROM Customer WHERE username='{username}'")
        c=mycursor.fetchall()
        if len(c) ==0:
            pincode = int(input("SELECT A 6 DIGIT CODE AS YOUR PINCODE and first digit CAN NOT be 0: "))
            if len(str(pincode))==6:
                created=datetime.now()
                Q="INSERT INTO Customer (name,age,pincode,created,amount,username) VALUES(%s,%s,%s,%s,%s,%s)"
                mycursor.execute(Q,(name,age,pincode,created,amount,username))
                db.commit()
                print("user created")
                print("thanks for becoming a member")
                break
            else:
                print("Enter a valid 6 digit pincode")  
                break  
        else:
            print("try a different username")    


    elif a=="n" or a=="N":
        print("existing user")
        username_input = input("YOUR USERNAME : ")
        mycursor.execute(f"SELECT * FROM Customer WHERE username='{username_input}'")
        c=mycursor.fetchall()
        if len(c) == 1:
            mycursor.execute(f"SELECT * FROM Customer WHERE username='{username_input}'")

            for i in mycursor:
                pincode=i[2]
            pin = int(input("YOUR PINCODE : "))
            if pincode == pin:    
                mycursor.execute(f"SELECT amount,personid FROM Customer WHERE username = '{username_input}' AND pincode='{pin}'")
            
            else:
                print("incorrect pincode")
                break
        else:
            print("username does not exist")
            break
            

        for i,person_id in mycursor:
            a=i
            pid=person_id


        transaction_type=input("ENTER 'w' to withdraw , 'd' to deposit and 's' for current status: ")
            
        if transaction_type=="w" or transaction_type=="W":
            withdraw()  
            break    
        elif transaction_type=="d" or transaction_type=="D":
            deposit()
            break
        elif transaction_type == "s" or transaction_type == "S":
            status()
            break
        else:
            print("please select a valid keyword")  
            break  
        
    else:
        print("not a valid input")
        break

