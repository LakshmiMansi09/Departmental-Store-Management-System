#--------------DEPARTMENTAL STORE MANAGER---------------"
#---------------Designed & Maintained By:---------------"
#------------------AKSHAT BOKDIA------------------------"

import mysql.connector

#GLOBAL VARAIBLES DECLARATION

my_connection = ""
cursor = ""
user_name = ""
password = ""

#MODULE TO CHECK MYSQL CONNECTIVITY

def MySQLconnectivityCheck():
    global my_connection
    global user_name
    global password
    
    user_name = input("Enter MySQL Server's Username:")
    password = input("Enter MySQL Server's Password:")

    my_connection = mysql.connector.connect(host = "127.0.0.1", user = user_name, 
                                            passwd = password, auth_plugin = "mysql_native_password")
    if my_connection.is_connected(): 
        print("Congratulations! Successfully established your MySQL connection! :)")         
        cursor = my_connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS DSMS")
        cursor.execute("COMMIT")
        cursor.close()
        return my_connection
    else:
        print("ERROR 404!! KINDLY CHECK THE USERNAME AND PASSWORD ONCE AGAIN! :(")

#MODULE TO ESTABILISH MYSQL CONNECTIVITY

def MySQLconnectivity():
    global user_name
    global password
    global my_connection

    my_connection = mysql.connector.connect(host = "localhost", user = user_name, passwd = password, 
                                            database = "DSMS", auth_plugin = "mysql_native_password")
    if my_connection.is_connected():
        return my_connection
    else:
        print("ERROR-ESTABILISHING-MYSQL-CONNECTION")
        my_connection.close()

#MODULE FOR EMPLOYEE RECORD

def NewEmployee():
    if my_connection:
        while True:
           cursor = my_connection.cursor()
           Table1 = """CREATE TABLE IF NOT EXISTS EMPLOYEE(ADMISSION_ID INT,NAME VARCHAR(30),GENDER CHAR(1),
                      MARITAL_STATUS CHAR(1),SALARY INT,DOB DATE,
                      HIRED_DATE DATE,PROFESSION VARCHAR(20), PRIMARY KEY(ADMISSION_ID))"""
           cursor.execute(Table1)

           adm_id = int(input("Enter Employee's Admission Id:"))
           name = input("Enter Employee's Name:")
           gender = input("Enter Employee's Gender(M/F):")
           m_status = input("Enter Employee's Marital Status(M/S):")
           salary = int(input("Enter Employee's Earnings:"))
           dob = input("Enter Employee's DOB(YYYY-MM-DD):")
           hiredate = input("Enter Emloyee's HireDate(YYYY-MM-DD):")
           prof = input("Enter Employee's Profession:")

           st1 = """INSERT INTO EMPLOYEE(ADMISSION_ID,NAME,GENDER,MARITAL_STATUS,SALARY,DOB,HIRED_DATE,PROFESSION)
                 VALUES({},'{}','{}','{}',{},'{}','{}','{}')""".format(adm_id,name,gender,m_status,salary,dob,hiredate,prof)
           cursor.execute(st1)
           cursor.execute("COMMIT")
           st2 = "INSERT INTO ATTENDANCE(NAME) VALUES('{}')".format(name)
           cursor.execute(st2)
           cursor.execute("COMMIT")
           cursor.close()
           print("ENTRY ADDED SUCCESSFULLY!")
           ch = input("Would You Like To Add More(Y/N)?")
           if ch.upper() != 'Y':
               break
    else:
        print("ERROR-ESTABILISHING-MYSQL-CONNECTION")

def displayEmployee():
    if my_connection:
        cursor = my_connection.cursor()
        cursor.execute("SELECT * FROM EMPLOYEE")
        data = cursor.fetchall()
        for row in data:
            print(row)
        cursor.close()
    else:
        print("##Something went wrong!Please Try Again!##")

#MODULE FOR WHOLESALERS RECORD

def Wholesalers():
    if my_connection:
        while True:
           cursor = my_connection.cursor()
           Table2 = """CREATE TABLE IF NOT EXISTS WHOLESALERS(NAME VARCHAR(20),ADDRESS VARCHAR(80),
                     CONTACT_NO CHAR(10),MAIL_ID VARCHAR(30),SUPPLY VARCHAR(20))"""
           cursor.execute(Table2)

           Wname = input("Enter Wholesaler's Name:")
           Waddr = input("Enter Wholesaler's Store Address:")
           Wphone = input("Enter Wholesaler's ContactNumber:")          
           Wemail = input("Enter Wholesaler's Email-Id:")         
           Wsupply = input("Enter Wholesaler's Supply of Goods:")

           Wst = """INSERT INTO WHOLESALERS(NAME,ADDRESS,CONTACT_NO,MAIL_ID,SUPPLY) 
                  VALUES('{}','{}','{}','{}','{}')""".format(Wname,Waddr,Wphone,Wemail,Wsupply)
           cursor.execute(Wst)
           cursor.execute("COMMIT")
           cursor.close()
           print("ENTRY ADDED SUCCESSFULLY!")
           ch2 = input("Would You Like To Add More(Y/N)?")
           if ch2.upper() != 'Y':
               break
    else:
        print("ERROR-ESTABILISHING-MYSQL-CONNECTION")

def displayWholesalers():
    if my_connection:
        cursor=my_connection.cursor()
        cursor.execute("SELECT * FROM WHOLESALERS")
        data=cursor.fetchall()
        for row in data:
            print(row)
        cursor.close()
    else:
        print("##Something went wrong!Please Try Again!##")

#MODULE TO TRACK THE ATTENDANCE OF EMPLOYEES
    
def AttendanceTracker():
    print("Hello There. Good To See You!")
    from datetime import datetime,date                # datetime object containing current date and time
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")       # dd/mm/YY H:M:S
    print("It is:",time)
    today = date.today()
    str_today = str(today)
    if my_connection:
            while True:
                cursor = my_connection.cursor()
                Table3 = """CREATE TABLE IF NOT EXISTS ATTENDANCE(NAME VARCHAR(30),DAYS_WORKING INT,
                          DAYS_PRESENT INT,DAYS_ABSENT INT)"""
                cursor.execute(Table3)
                
                if '01-01' in str_today:
                    Wdays = int(input("Enter the NO. of Working Days for this Year:"))
                    Pdays = Adays = 0
                    Aname = input("Enter Employee's name:")
                    sql0 = "SELECT NAME FROM ATTENDANCE WHERE NAME='{}'".format(Aname)
                    cursor.execute(sql0)
                    data = cursor.fetchall()
                    if not data:
                        print("^^Record Not Found!Please Try Again!^^")
                        break
                    A_Pdays = input("Was the Employee Present Today (Y/N)?")
                    if A_Pdays.upper() == 'Y':
                        Pdays += 1
                    else:
                        Adays += 1
                    cursor = my_connection.cursor()    
                    Ast = """UPDATE ATTENDANCE 
                           SET DAYS_WORKING={},DAYS_PRESENT={},DAYS_ABSENT={}
                           WHERE NAME='{}'""".format(Wdays,Pdays,Adays,Aname)
                    cursor.execute(Ast)
                    cursor.execute("COMMIT")
                    cursor.close()
                    print("Attendance of "+Aname+" Taken Successfully!")
                    ch3 = input("Would You Like To Record More(Y/N)?")
                    if ch3.upper() != 'Y':
                        break
                
                else:              
                    Aname = input("Enter Employee's name:")
                    sql0 = "SELECT NAME FROM ATTENDANCE WHERE NAME='{}'".format(Aname)
                    sql1 = "SELECT DAYS_PRESENT FROM ATTENDANCE WHERE NAME='{}'".format(Aname)
                    sql2 = "SELECT DAYS_ABSENT FROM ATTENDANCE WHERE NAME='{}'".format(Aname)
                    sql3 = "SELECT DAYS_WORKING FROM ATTENDANCE WHERE NAME='{}'".format(Aname)
                    cursor.execute(sql0)
                    data = cursor.fetchall()
                    if not data:
                        print("^^Record Not Found!Please Try Again!^^")
                        break
                    else:
                        cursor.execute(sql1)
                        data = cursor.fetchall()                                                   
                        Pdays = data[0][0]
                        if Pdays is not None:
                            Pdays = int(Pdays)
                        else:
                            Pdays=0
                        cursor.execute(sql2)
                        data = cursor.fetchall()
                        Adays = data[0][0]
                        if Adays is not None:
                            Adays = int(Adays)
                        else:
                            Adays = 0
                        cursor.execute(sql3)
                        data = cursor.fetchall()
                        Wdays = data[0][0]
                        if Wdays is not None:
                            Wdays = int(Wdays)
                        else:
                            Wdays = int(input("Enter the NO. of Working Days for New Employee:"))
                                           
                        A_Pdays = input("Was the Employee Present Today (Y/N)?")
                        if A_Pdays.upper() == 'Y':
                            Pdays += 1
                        else:
                            Adays += 1
                        cursor = my_connection.cursor()    
                        Ast = """UPDATE ATTENDANCE 
                               SET DAYS_WORKING={},DAYS_PRESENT={},DAYS_ABSENT={}
                               WHERE NAME='{}'""".format(Wdays,Pdays,Adays,Aname)
                        cursor.execute(Ast)
                        cursor.execute("COMMIT")
                        cursor.close()
                        print("Attendance of",Aname,"Taken Successfully!")
                        ch3 = input("Would You Like To Record More(Y/N)?")
                        if ch3.upper() != 'Y':
                            break
    else:
        print("ERROR-ESTABILISHING-MYSQL-CONNECTION")

def displayAttendanceTracker():
    if my_connection:
        cursor = my_connection.cursor()
        cursor.execute("SELECT * FROM ATTENDANCE")
        data = cursor.fetchall()
        for row in data:
            print(row)
        cursor.close()
    else:
        print("##Something went wrong!Please Try Again!##")
    
#MODULE FOR ENTIRE STOCK LIST IN THE STORE
#TABLE 4 - STOCKLIST
        
def displayStockListAll():
    if my_connection:
        cursor = my_connection.cursor()
        cursor.execute("SELECT * FROM STOCKLIST")
        data=cursor.fetchall()
        for row in data:
            print(row)
        cursor.close()
    else:
        print("##Something went wrong!Please Try Again!##")

def displayStockListParticular():
    if my_connection:
        cursor = my_connection.cursor()
        Supply = {1:'Grocery',2:'Dairy/Bakery',3:'Cereals/Spices',4:'Snacks/Beverages',5:'Hygiene/Beauty'}
        print(Supply)
        ch4 = int(input("Which Items Would You Like To Have A Look At(NUMBER)?"))
        Type = Supply.get(ch4)
        cursor.execute("SELECT * FROM STOCKLIST WHERE TYPE='{}'".format(Type))
        data = cursor.fetchall()
        if data:
            for row in data:
                print(row)
        else:
            print("^^Record Not Found!Please Try Again!^^")
        cursor.close()
    else:
        print("##Something went wrong!Please Try Again!##")

#MODULE TO UPDATE STOCKLIST

def StockListVolume():
    if my_connection:
        while True:
            cursor = my_connection.cursor()
            cursor.execute("SELECT ITEM_NAME FROM STOCKLIST_VOLUME")
            data = cursor.fetchall()
            if not data:
                cursor = my_connection.cursor()
                Table5 = """CREATE TABLE IF NOT EXISTS STOCKLIST_VOLUME(SNO CHAR(4) PRIMARY KEY,
                          ITEM_NAME VARCHAR(50),PRICE FLOAT,TYPE VARCHAR(20))"""           
                cursor.execute(Table5)
                cursor.execute("COMMIT")
                cursor.execute("INSERT INTO STOCKLIST_VOLUME SELECT * FROM STOCKLIST")
                cursor.execute("COMMIT")
                cursor.execute("ALTER TABLE STOCKLIST_VOLUME ADD(QUANTITY INT)")
                cursor.execute("COMMIT")
                cursor.close()
            
            update = 'Y'
            while update.upper()=='Y':
                cursor = my_connection.cursor()
                s_no1 = input("Enter The Item's Sno:")
                cursor.execute("SELECT ITEM_NAME FROM STOCKLIST_VOLUME WHERE SNO='{}'".format(s_no1))
                data = cursor.fetchall()
                if data:
                    amount1 = float(input("Enter The Number Of Items Stored:"))
                    cursor.execute("UPDATE STOCKLIST_VOLUME SET QUANTITY={} WHERE SNO='{}'".format(amount1,s_no1))
                    cursor.execute("COMMIT")
                    print("Your StockList Has Been Updated!")
                    cursor.close()
                else:
                    print("\\\Record Not Found!Please Try Again!\\\ ")
                update = input("Would You Like To Add More(Y/N)?")
                if update.upper()!='Y':
                    break
            break
    else:
        print("ERROR-ESTABILISHING-MYSQL-CONNECTION")      

def addStockListVolume():
    if my_connection:
        while True:
            cursor = my_connection.cursor()
            s_no2=input("Enter The Item's Sno:")
            cursor.execute("SELECT ITEM_NAME FROM STOCKLIST_VOLUME WHERE SNO='{}'".format(s_no2))
            data = cursor.fetchall()
            if data:            
                amount2 = float(input("Enter The Number Of Items Unloaded:"))
                cursor.execute("UPDATE STOCKLIST_VOLUME SET QUANTITY=QUANTITY+{} WHERE SNO='{}'".format(amount2,s_no2))
                cursor.execute("COMMIT")
                print("Your StockList Has Been Updated!")
                cursor.close()      
            else:
                print("\\\Record Not Found!Please Try Again!\\\ ")
            ch5 = input("Would You Like To Add More(Y/N)?")
            if ch5.upper()!='Y':
                break   
    else:
        print("ERROR-ESTABILISHING-MYSQL-CONNECTION")

def displayStockListVolume():
    if my_connection:
        cursor = my_connection.cursor()
        cursor.execute("SELECT * FROM STOCKLIST_VOLUME")
        data = cursor.fetchall()
        for row in data:
            print(row)
    
        cursor.close()
    else:
        print("##Something went wrong!Please Try Again!##")

#MODULE TO CREATE A BILL

def CreateBill():
    if my_connection:
        print("Now That You Have Decided About The Items You Want To Buy, Let's Create The Bill.")
        global TList
        TList = List = []
        while True:
            cursor = my_connection.cursor()
            s_no3 = input("Enter The Item's Sno:")
            cursor.execute("SELECT QUANTITY FROM STOCKLIST_VOLUME WHERE SNO='{}'".format(s_no3))
            data = cursor.fetchall()
            if not data:
                print("\\\Record Not Found!Please Try Again!\\\ ")                
            else:
                n = data[0][0]
                n = float(n)
                cursor.execute("COMMIT")
                cursor.close()           
                amount3 = float(input("Enter The Number Of Items You Wish To Purchase:"))
                if n>amount3:
                    List = [s_no3,amount3]
                    TList.extend(List)
                    cursor = my_connection.cursor()
                    cursor.execute("UPDATE STOCKLIST_VOLUME SET QUANTITY=QUANTITY-{} WHERE SNO='{}'".format(amount3,s_no3))
                    cursor.execute("COMMIT")
                    cursor.close()
                else:
                    print("""Stock Of Item Needed Is Greater Than Available!
                             Kindly Change The Amount Needed Or Wait Until Further Notice!""")
                
            ch6=input("Would You Like To Add More(Y/N)?")
            if ch6.upper()!='Y':
                 print("Thank You!Kindly Enter The Customer Details Next!")
                 break         
    else:
        print("ERROR-ESTABILISHING-MYSQL-CONNECTION")

#MODULE TO ENTER CUSTOMER DETAILS

def CustomerDetails():
    global Name
    global Phone
    global Address
    global Mode_Payment
    
    print("Customer Details:")
    Name = input("Enter Your Name:")
    Phone = input("Enter Your Contact Number:")
    Address = input("Enter Your Address Where The Items Have To Be Delivered:")
    while True:
        Mode_Payment = input("Enter Your Mode Of Payment(Card/COD/Paytm):")
        if Mode_Payment.upper()=='COD':
            print("Kindly Render Exact Amount To The Delivery Person.")
            break
        elif Mode_Payment.upper()=='CARD':
            print("Kindly Keep The Card Ready During Delivery and Ensure That There is Sufficient Balance.")
            break
        elif Mode_Payment.upper()=='PAYTM':
            print("Kindly Send The Required Amount Through Paytm To 'S.H DEPARTMENTAL STORES'")
            break
        else:
            print("Invalid Input!")
    print("Thank You For Your Cooperation!Creating Bill...")
    return

#MODULE TO PRINT THE BILL

def PrintBill():
    import math,random
    INVOICE_NO = random.randint(100000,999999)
    SUM = c_items = 0
    CList = []
    from datetime import datetime                                                                             
    now = datetime.now()                                                                                             
    time = now.strftime("%d/%m/%Y %H:%M:%S")                                                                    
                                                                                                                   
    print("**************************************************************")                                      
    print("            *S.H*DEPARTMENTAL*STORES*        *****    *    *  ")                                              
    print("                                            *         *    *  ")                                                         
    print("             Save Money. Live Better.       *         *    *  ")                                                 
    print("                                             ***      ******  ")                                               
    print("               MANAGER ASHOK KUMAR              *     *    *  ")                                              
    print("             WHITEFIELD ENTERPRISES             *     *    *  ")                                                  
    print("                1155 S.THAMES ROAD         *****   *  *    *  ")                                                    
    print("             ROYAPETTAH CHENNAI-600 090                       ")
    print("           PHONE NO:24468455/24464123                         ")
    print("             GSTIN: 35AAGGH2932J6FB                           ")
    print("                                                              ")
    print("                                                              ")
    print("                   GST INVOICE                                ")
    print("Reference: 01 35432                                           ")
    print("                                                              ")
    print("             INVOICE NUMBER:",INVOICE_NO,"                    ")
    print("Bill Date & Time:",time,"                                     ")
    print("--------------------------------------------------------------")
    print("Description             ","Qty   ","Rate   ","Value           ")
    print("--------------------------------------------------------------")
    if my_connection:
        for i in range(0,len(TList),2):
            s_no4 = TList[i]
            cursor = my_connection.cursor()
            cursor.execute("SELECT ITEM_NAME,PRICE FROM STOCKLIST_VOLUME WHERE SNO='{}'".format(s_no4))
            data = cursor.fetchall()
            item = data[0][0]
            rate = data[0][1]
            item = str(item)
            c_items += 1
            rate = float(rate)
            cursor.execute("COMMIT")
            cursor.close()
            qty = TList[i+1]
            CList.append(qty)
            c_qty = math.fsum(CList)
            value = qty*rate
            SUM += value
            print(s_no4,"                   ",qty,"  ",rate,"  ",value            )
            print(item)
            
    tax = 0.09*SUM
    fact = math.comb(45,c_items)
    
    print("--------------------------------------------------------------")
    print("ITEMS:",c_items,"                QTY:",c_qty,"       AMOUNT:",SUM-2*tax )  
    print("--------------------------------------------------------------")
    print("                                                              ")
    print("TAX RATE:                TAX TYPE:     TAX AMOUNT:            ")
    print("9%                       CGST         ",round(tax,2)           ) 
    print("9%                       SGST         ",round(tax,2)           )
    print("                                                              ")
    print("TOTAL AMOUNT:",SUM                                             )
    print("MODE OF PAYMENT:",Mode_Payment                                 )
    print("                                                              ")
    print("CUSTOMER'S NAME:",Name                                         )
    print("CUSTOMER'S CONTACT NO:",Phone                                  )
    print("CUSTOMER'S ADDRESS:",Address                                   )
    print("                                                              ")
    print("                                                              ")
    print("FACT: The Total Number Of Possibilities To Choose",c_items,    )
    print("Things From Our 45 Selling Items Is:",fact                     )
    print("                                                              ")
    print("                                                              ")
    print("THANK YOU FOR SHOPPING WITH US!                               ")
    print("PLEASE VISIT US AGAIN! :)                                     ")
    print("**************************************************************")                                                                      
 
#MODULE FOR HELP

def Help():
    print("For Further Details Regarding Your Order Or To Know About The Availability Of Items,")
    print("Kindly Contact Us- 24468455/24464123")
    print("We Would Love To Help You And Resolve All Your Queries And Ensure That You Get Your Order On Time!")

'##########################################################################################################################################################################################################################################'

#MAIN SCREEN OF THE PROGRAM

print('|-------------------------------------------------|')
print('|-------------------------------------------------|')
print('| Welcome to the Website of SH Departmental Store |')
print('|-------------------------------------------------|')
print('|           Designed and Maintained by            |')
print('|-------------------------------------------------|')
print('|                Akshat Bokdia                    |')
print('| ------------------------------------------------|')
print('|*************   STORE MANAGER   *****************|')
print('|-------------------------------------------------|')


#STARTING POINT OF THE SYSYTEM

my_connection = MySQLconnectivityCheck()
if my_connection:
    MySQLconnectivity()
    while True:       
        print('')
        print('Press 1 If you are a Manager:')
        print('Press 2 If you are an Employee:')
        print('Press 3 If you are a Customer:')
        choice = int(input('Enter your choice:'))
          
        if choice == 1:
            n = input('Enter your Password:')
            if n == 'shDS2020':
                print('@@@@ @@ @ @@@@@@@@@ @@@@@@@@')
                a = input()
                if (a == 'This is a protected software'):
                    while True:
                        print('Welcome chief to SH data storage!')
                        print('')
                        print('You can do the following things:')
                        print('')
                        print('|----------------------------------------------------------|')
                        print('|         Press 1 to check Employee Record                 |')
                        print('|         Press 2 to check Wholesalers List                |')
                        print('|         Press 3 to check Attendance Tracker              |')
                        print('|         Press 4 to check Stock List of Items             |')
                        print('|         Press 5 to Update Stock List                     |')
                        print('|         Press 6 to Create a Bill                         |')
                        print('|         Press 7 to Enter Customer Details                |')
                        print('|         Press 8 to print Bill                            |')
                        print('|         Press 0 to exit                                  |')
                        print('|----------------------------------------------------------|')
           
                        choice1=int(input('Enter your choice:'))
                        if (choice1==1):
                            print('Here is the Employee Record')
                            choice1A = input("Enter 'A' To Add A New Employee OR 'B' To Display Employee Record:")
                            if choice1A.upper()=='A':            
                                NewEmployee()
                            elif choice1A.upper()=='B':
                                displayEmployee()
                            else:
                                print('#Wrong Input#')
                        elif (choice1==2):
                            print('Here is the Wholesalers List')
                            choice1B = input("Enter 'A' To Add A New Wholesaler OR 'B' To Display Wholesalers Record:")
                            if choice1B.upper()=='A':            
                                Wholesalers()
                            elif choice1B.upper()=='B':
                                displayWholesalers()
                            else:
                                print('#Wrong Input#')
                        elif (choice1==3):
                            print('Here is the Attendance tracker of the employees')
                            choice1C = input("Enter 'A' To Take Attendance OR 'B' To Display Attendance Record:")
                            if choice1C.upper()=='A':            
                                AttendanceTracker()
                            elif choice1C.upper()=='B':
                                displayAttendanceTracker()
                            else:
                                print('#Wrong Input#')
                        elif (choice1==4):
                            print('Here is the Stock List of the Items')
                            choice1D = input("Enter 'A' To Display Entire StockList OR 'B' To Display StockList By Type:")
                            if choice1D.upper()=='A':            
                                displayStockListAll()
                            elif choice1D.upper()=='B':
                                displayStockListParticular()
                            else:
                                print('#Wrong Input#')
                        elif (choice1==5):
                            print('Here is the Stock List of the Items that you can update')
                            choice1E = input("Enter 'A' To Insert The Amount Of An Item Stored OR 'B' To Add The Amount Of An Item OR C To Display the Updated StockList:")
                            if choice1E.upper()=='A':            
                                StockListVolume()
                            elif choice1E.upper()=='B':
                                addStockListVolume()
                            elif choice1E.upper()=='C':
                                displayStockListVolume()
                            else:
                                print('#Wrong Input#')
                        elif (choice1==6):
                            CreateBill()
                        elif (choice1==7):
                            CustomerDetails()
                        elif (choice1==8):
                            PrintBill()
                        elif (choice1==0):
                            print("Thank you Sir!Don't Forget To Close The Account When Not In Use.")
                            my_connection.close()
                            break
                        else:
                            print('SORRY!!You Entered Wrong Input.Please Try Again!!')
                    break
            else:   
                print('Sorry the password you entered is wrong')
                break
    
        elif (choice==2):
            h=input('Enter your password:')
            if h == 'Bharath':
                while True:
                    print('Welcome employee!')
                    print('')
                    print('You can do following things:')
                    print('')
                    print('|---------------------------------------------------------------|')
                    print('|             Press 1 for Wholesalers List                      |')
                    print('|             Press 2 for Stock List                            |')
                    print('|             Press 3 to Update Stock List                      |')
                    print('|             Press 4 to Create a Bill                          |')
                    print('|             Press 5 to Enter Customer Details                 |')
                    print('|             Press 6 to print Bill                             |')
                    print('|             Press 0 to Exit                                   |')
                    print('|---------------------------------------------------------------|')
                 
                    choice2 = int(input('Enter your Choice:'))
                    if (choice2==1):
                        print('Here is the Wholesalers List')
                        choice2A = input("Enter 'A' To Add A New Wholesaler OR 'B' To Display Wholesalers Record:")
                        if choice2A.upper()=='A':            
                            Wholesalers()
                        elif choice2A.upper()=='B':
                            displayWholesalers()
                        else:
                            print('#Wrong Input#')
                    elif (choice2==2):
                        print('Here is the Stock List')
                        choice2B = input("Enter 'A' To Display Entire StockList OR 'B' To Display StockList By Type:")
                        if choice2B.upper()=='A':            
                            displayStockListAll()
                        elif choice2.upper()=='B':
                            displayStockListParticular()
                        else:
                            print('#Wrong Input#')
                    elif (choice2==3):
                        print('Here you can update the Stock List')
                        choice2C = input("""Enter 'A' To Insert The Amount Of An Item Stored OR 'B'
                                       To Add The Amount Of An Item OR C To Display the Updated StockList:""")
                        if choice2C.upper()=='A':            
                            StockListVolume()
                        elif choice2C.upper()=='B':
                            addStockListVolume()
                        elif choice2C.upper()=='C':
                            displayStockListVolume()
                        else:
                            print('#Wrong Input#')
                    elif (choice2==4):
                        CreateBill()
                    elif (choice2==5):
                        CustomerDetails()
                    elif (choice2==6):
                        PrintBill()                              
                    elif (choice2==0):
                        print("Thank You!Don't Forget To Close The Account When Not In Use.")
                        my_connection.close()
                        break
                    else:
                        print('SORRY!!You Entered Wrong Input.Please Try Again!!')
                break
            else:
                print('Sorry the password you entered is wrong')
                break
        
        elif (choice==3):
            while True:
                print('Welcome to SH departmental store!')
                print('')
                print('Customer Service is our number one priority')
                print('')
                print('You can do the following options:')
                print('')
                print('|-----------------------------------------------------------------|')
                print('|                 Press 1 for Item List                           |')
                print('|                 Press 2 to Create Bill                          |')
                print('|                 Press 3 to Enter Customer Details               |')
                print('|                 Press 4 to print Bill                           |')
                print('|                 Press 5 for Help                                |')           
                print('|                 Press 0 to Exit                                 |')
                print('|-----------------------------------------------------------------|')
                
                choice3 = int(input('Enter your Choice:'))
                if (choice3==1):
                    print('Here is the Item List')
                    choice3A = input("Enter 'A' To Display Entire StockList OR 'B' To Display StockList By Type:")
                    if choice3A.upper()=='A':            
                        displayStockListAll()
                    elif choice3A.upper()=='B':
                        displayStockListParticular()
                    else:
                        print('#Wrong Input#')
                elif (choice3==2):
                    CreateBill()
                elif (choice3==3):
                    CustomerDetails()
                elif (choice3==4):
                    PrintBill()
                elif (choice3==5):
                    Help()
                elif (choice3==0):
                    print("Thank You!!")
                    my_connection.close()
                    break
                else:
                    print('SORRY!!You Entered Wrong Input.Please Try Again!!')
            break    
        else:
            print("SORRY!!You Didn't Choose From 1,2 or 3.Please Try Again!!")

else:
    print('Check Your MySQL Connection First!')

#END OF PROJECT

'##########################################################################################################################################################################################################################################'
