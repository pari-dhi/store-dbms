import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rootcode",
    database="opticalproject")

print(db)
myc=db.cursor()



#dictionaries to call back to for lens and brands
brands={}
brand_a={'B001':3000, 'B002':3500, 'B003':2500, 'B004':4000}
brand_b={'B005':4000, 'B006':4500, 'B007':3500, 'B008':5000}
brand_c={'B009':5000, 'B010':5500, 'B011':4500, 'B012':6000}
brands.update(brand_a)
brands.update(brand_b)
brands.update(brand_c)

lenses={'L001':700, 'L002':800, 'L003':900,'L004':800, 'L005':700}

brandnames={}
brand_i={'B001':'Christian Dior', 'B002':'Prada', 'B003':'Hugo'}
brand_ii={'B004':'Jilly Stuart', 'B005':'Ray Ban', 'B006':'Emozioni'} 
brand_iii={'B007':'Saint Laurent', 'B008':'Silhouette', 'B009':'Oakley'}
brand_iv={'B010':'Gucci', 'B011':'Michael Kors', 'B012':'Izumi'}

brandnames.update(brand_i)
brandnames.update(brand_ii)
brandnames.update(brand_iii)
brandnames.update(brand_iv)

lenscon={'L001':'Progressive'}
lens1={'L002':'Concave', 'L003':'Bifocal'}
lens2={'L004':'Convex', 'L005':'Cylindrical'}
lenscon.update(lens1)
lenscon.update(lens2)



#price functions
#submodules for set price function

#1
def choose_brand():
    print("\nHere are the available brands of frames:")
    print("--------------------------------------------------")
    print("\n \t \t \t BRANDS")
    print("\n--------------------------------------------------")
    print("  Brand ID | Brand Name")
    print("--------------------------------------------------")
    query="Select * from BRANDS"
    myc.execute(query)
    display=myc.fetchall()
    for i in display:
        print(i)
    db.commit()
    print("-------------------------------------------")
    print("")
    br_id=input("What is the Brand ID of your purchase?\nPlease enter here:")
    req_br=brands[br_id]
    oid=int(input("Please re-enter your Order ID:"))
    query="UPDATE PRICEDETAILS SET BRANDPRICE='%s' WHERE ORDER_ID='%s'"
    values=(req_br, oid)
    myc.execute(query,values)
    db.commit()
    return(req_br)



#2
def choose_lens():
    print("\nHere are the available lens types available:")
    print("--------------------------------------------------")
    print("\n \t \t LENS TYPES")
    print("\n--------------------------------------------------")
    print("  Lens ID | Type | Suitable Eye Condition")
    print("--------------------------------------------------")
    query="Select * from LENSES"
    myc.execute(query)
    display=myc.fetchall()
    for i in display:
        print(i)
    db.commit()
    print("-------------------------------------------------")
    print("")
    lns_id=input("What is the Lens ID of your purchase?\nPlease enter here:")
    req_lns=lenses[lns_id]
    oid=int(input("Please re-enter your Order ID:"))
    query="UPDATE PRICEDETAILS SET LENSPRICE='%s' WHERE ORDER_ID='%s'"
    values=(req_lns, oid)
    myc.execute(query,values)
    db.commit()
    return(req_lns)




#function to set the total price
#submodule for add new 
def price_setting():
    oid=int(input("Please re-enter your assigned Order ID:"))
    query=("INSERT INTO PRICEDETAILS(ORDER_ID, BRANDPRICE, LENSPRICE, F_PRICE)"
           "VALUES(%s, %s, %s, %s)")
    values=(oid, None, None, None)
    myc.execute(query,values)
    db.commit()
    x=choose_lens()
    y=choose_brand()
    pri_ce=x+y
    query="UPDATE PRICEDETAILS SET F_PRICE='%s' WHERE ORDER_ID='%s'"
    values=(pri_ce, oid)
    myc.execute(query, values)
    db.commit()
    return(pri_ce)




#fucntion to set up order id chronologically
#submodule for add new function
y=[]
def set_order_id():
    query="Select ORDER_ID from BASE"
    myc.execute(query)
    result=myc.fetchall()
    db.commit()
    for x in result:
        y.append(x)
    for i in y:    
        y.sort(reverse=True)
        z=y.pop(0)
        w=z[0]+1
        return(w)
    



#function to add details of new purchase
#5
def add_new():
    oid=set_order_id()
    print("Your Order ID is:", oid)
    cname=input("Please enter your name:")
    phno=input("Please enter your phone number:")
    print("Please enter your eye power.")
    print("(Must be as prescribed by a qualified optician.)")
    leye=input("Of left eye:")
    reye=input("Of right eye:")
    prce=price_setting()
    query=("INSERT INTO BASE(ORDER_ID, CUST_NAME, PHONE_NO, LEFTLENS, RIGHTLENS,"
           "PRICE) VALUES (%s,%s,%s,%s,%s,%s)")
    value=(oid, cname, phno, leye, reye, prce)
    myc.execute(query, value)
    db.commit()

    

#function to display details of old purchase
def display_record():
    print("")
    o_id=int(input("Please enter your Order ID:"))
    name=input("Please enter your name:")
    print("")
    print("The order details associated with the given Order ID are:")
    print("\n-------------------------------------------------------------------------")
    print("  Order ID | Name | Phone No. | Left Eye Power | Right Eye Power | Price")
    print("-------------------------------------------------------------------------")
    query="select * from base where order_id='%s' and cust_name=%s"
    value=(o_id, name)
    myc.execute(query,value)
    display=myc.fetchall()
    for x in display:
        print(x)
    db.commit()
    print("-------------------------------------------------------------------------")
    



#functions to edit brand and lenses
#to add as sub-module in edit price function
def edit_brand():
    or_id=int(input("Please enter your Order ID:"))
    print("")
    print("--------------------------------------------------")
    print("\n \t \t \t BRANDS")
    print("\n--------------------------------------------------")
    print("  Brand ID | Brand Name")
    print("--------------------------------------------------")
    query="Select * from BRANDS"
    myc.execute(query)
    display=myc.fetchall()
    for i in display:
        print(i)
    db.commit()
    print("--------------------------------------------------")
    print("")
    new_br=input("Enter the new Brand ID:")
    new_brprice=brands[new_br]
    query1="update pricedetails set brandprice='%s' where order_id='%s'"
    value1=(new_brprice, or_id)
    myc.execute(query1, value1)
    db.commit()
    return(new_brprice)

def edit_lens():
    or_id=int(input("Please enter your Order ID:"))
    print("")
    print("Here are the available lens types available:")
    print("--------------------------------------------------")
    print("\n \t \t LENS TYPES")
    print("\n--------------------------------------------------")
    print("  Lens ID | Type | Suitable Eye Condition")
    print("--------------------------------------------------")
    query="Select * from LENSES"
    myc.execute(query)
    display=myc.fetchall()
    for i in display:
        print(i)
    db.commit()
    print("--------------------------------------------------")
    print("")
    new_lens=input("Enter the new Lens ID:")
    new_lensprice=lenses[new_lens]
    query2="update pricedetails set brandprice='%s' where order_id='%s'"
    value2=(new_lensprice, or_id)
    myc.execute(query2, value2)
    db.commit()
    return(new_lensprice)



#function to edit the price
#To be added as sub-module in edit record
def edit_price():
    print("\tEnter A to edit the Brand of the purchased item.")
    print("")
    print("\tEnter B to edit the type of Lens. ")
    print("")
    print("\tEnter C to edit both.")
    print("")
    n=input("Enter your choice:")
    if (n.upper() =='A'):
        edited_brandprice=edit_brand()
        lensss=input("Please enter your Lens ID:")
        lensprice=lenses[lensss]
        o_id=int(input("Please re-enter your Order ID:"))
        new_price=edited_brandprice + lensprice
        query="update pricedetails set f_price='%s' where order_id='%s'"
        values=(new_price, o_id)
        myc.execute(query, values)
        db.commit()
        print("Your data has been modified.") 
    elif (n.upper()=='B'):
        edited_lensprice=edit_lens()
        brandsss=input("Please enter your Brand ID:")
        brandprice=brands[brandsss]
        o_id=int(input("Please re-enter your Order ID:"))
        new_price=edited_brandprice + edited_lensprice
        query="update pricedetails set f_price='%s' where order_id='%s'"
        values=(new_price, o_id)
        myc.execute(query, values)
        db.commit()
        print("Your data has been modified.")
    elif (n.upper()=='C'):
        edited_brandprice=edit_brand()
        edited_lensprice=edit_lens()
        lensss=input("Please enter your Lens ID:")
        lensprice=lenses[lensss]
        brandsss=input("Please enter your Brand ID:")
        brandprice=brands[brandsss]
        o_id=int(input("Please re-enter your Order ID:"))
        new_price=edited_brandprice + edited_lensprice
        query="update pricedetails set f_price='%s' where order_id='%s'"
        values=(new_price, o_id)
        myc.execute(query, values)
        db.commit()
    else:
        print("Invalid input.")
        


#function to edit records
def edit():
    display_record()
    print("Are you sure you want to edit these details?")
    w=input("Enter Y/N:")
    if (w.upper()=='N'):
        print("")
    elif (w.upper()=='Y'):
        order_id=int(input("Please re-enter your Order ID:"))
        print("")
        print("Which parameter would you like to change?")
        print("")
        print("\tEnter A to edit your Name.")
        print("")
        print("\tEnter B to edit your Phone Number.")
        print("")
        print("\tEnter C to edit the Left Lens Power.")
        print("")
        print("\tEnter D to edit the Right Lens Power.")
        print("")
        print("\tEnter E to edit Brand or Lens type.")
        print("")
        print("\tEnter F to edit Price.")
        print("")
        chois=input("Enter choice:")
        if (chois.upper()== 'E'):
            edit_price()
        elif (chois.upper()=='D'):
            rlens=input("Enter the new Right Lens Power:")
            query1="Update base set rightlens=%s where order_id='%s'"
            value1=(rlens, order_id)
            myc.execute(query1,value1)
            db.commit()
            print("The data has been modified.")
        elif (chois.upper()=='C'):
            leflens=input("Enter the new Left Lens Power:")
            query2="Update base set leftlens=%s where order_id='%s'"
            value2=(leflens,order_id)
            myc.execute(query2,value2)
            db.commit()
            print("The data has been modified.")
        elif (chois.upper()=='B'):
            phno=input("Enter new Phone Number:")
            query3="Update base set Phone_NO=%s where order_id='%s'"
            value3=(phno,order_id)
            myc.execute(query3, value3)
            db.commit()
            print("The data has been modified.")
        elif (chois.upper()=='A'):
            name=input("Enter new Name:")
            query4="Update base set cust_name=%s where order_id='%s'"
            value4=(name, order_id)
            myc.execute(query4,value4)
            db.commit()
            print("The data has been modified.")
        elif (chois.upper()=='F'):
            print("")
            edit_price()
        else:
            print("Invalid input.")
        print("All the edits have (if any) been stored in the database.")
    else:
        print("Invalid Input.")

def edit_loop():
    edit()
    print("Would you like to edit more details?")
    exchos=input("Enter Y/N:")
    if (exchos.upper()=='Y'):
        edit_loop()
    elif(exchos.upper()=='N'):
        print('')
    else:
        print("Invalid Input.")
    
    


#function to delete a record
#store back up of deleted data in text file
def delete_details():
    o_id=int(input("Please re-enter your Order ID:"))
    na_me=input("Please enter your name:")
    f=open(r'C:\Users\DELL\Desktop\school\python files\projectfiles\sample.txt', 'a')
    print("")
    print("The following data will be deleted:")
    print("\n--------------------------------------------------------------------------")
    print("  Order ID | Name | Phone No. | Left Eye Power | Right Eye Power | Price")
    print("--------------------------------------------------------------------------")
    query="select * from base where order_id='%s' and cust_name=%s"
    value=(o_id, na_me)
    myc.execute(query,value)
    display=myc.fetchall()
    for x in display:
        print(x)
    db.commit()
    print("---------------------------------------------------------------------------")
    print("\nAre you sure you want to delete these details?")
    choicse=input("Enter Y/N:")
    if (choicse.upper()=='Y'):
        queryA="select * from base where order_id='%s' and cust_name=%s"
        valueA=(o_id, na_me)
        myc.execute(queryA,valueA)
        display=myc.fetchall()
        for x in display:
            f.write(str(x))
            f.write('\n')
            f.close()
        db.commit()
        queryB="delete from base where order_id='%s' and cust_name=%s"
        valueB=(o_id, na_me)
        myc.execute(queryB,valueB)
        db.commit()
        queryC="delete from pricedetails where order_id=%s"
        valueC=(o_id)
        #myc.execute(queryC,valueC)
        db.commit()
        print("The data has been deleted.")
        print("A back-up of the deleted data may be viewed by the admin.")
    elif (choicse.upper()=='N'):
        print("")
    else:
        print("Invalid Input.")
        


#function to view all records
#only for admin
def view_all():
    print("\nAll Records:")
    print("")
    print("--------------------------------------------------------------------------")
    print("  Order ID | Name | Phone No. | Left Eye Power | Right Eye Power | Price")
    print("--------------------------------------------------------------------------")
    query="select * from base"
    myc.execute(query)
    results=myc.fetchall()
    for x in results:
        print(x)
    db.commit()
    print("---------------------------------------------------------------------------")
        


#function to view deleted records
#only for admin
def view_del():
    dfile=open(r'C:\Users\DELL\Desktop\school\python files\projectfiles\sample.txt', 'r')
    str1=dfile.read()
    print(str1)
    dfile.close()

    
#main menu functions
def main_menu():
    print("--------------------------------------------------------------------------------")
    print("\n\t\t   OPTICAL STORE - SELF BILLING SYSTEM")
    print("\n--------------------------------------------------------------------------------")
    print("")
    print("\tEnter A to access the Customer Menu.")
    print("\n\tEnter B to access the Admin Menu.")
    ch=input("\n\tEnter here:")
    print("\n--------------------------------------------------------------------------------")
    if (ch.upper()=='A'):
        print("\n\t\t\tCUSTOMER'S MAIN MENU")
        print("\n--------------------------------------------------------------------------------")
        print("")
        print("\tEnter A to Add details of a new purchase.")
        print("")
        print("\tEnter B to Display details of a previous purchase.")
        print("")
        print("\tEnter C to Edit details of a previous purchase.")
        print("")
        print("\tEnter D to Delete details of a purchase.")
        ems=input("\n\tEnter here:")
        print("\n--------------------------------------------------------------------------------")
        print("")
        if (ems.upper()=='A'):
            add_new()
            print("These details have been stored in the database.")
        elif (ems.upper()=='B'):
            display_record()
        elif (ems.upper()=='C'):
            edit_loop()
        elif (ems.upper()=='D'):
            delete_details()
        else:
            print("Invalid Input.")
    elif (ch.upper()=='B'):
        pss=input("\nEnter the Admin password:")
        if (pss=='admin'):
            print("Correct password, proceed.")
            print("\n--------------------------------------------------------------------------------")
            print("\n\t\t   ADMINISTATOR'S MAIN MENU")
            print("\n--------------------------------------------------------------------------------")
            print("")
            print("\tEnter A to Add details of a new purchase.")
            print("")
            print("\tEnter B to Display details of a previous purchase.")
            print("")
            print("\tEnter C to Edit details of a previous purchase.")
            print("")
            print("\tEnter D to Delete details of a purchase.")
            print("")
            print("\tEnter E to View details of all purchases.")
            print("")
            print("\tEnter F to View details of deleted purchases.")
            print("\n--------------------------------------------------------------------------------")
            ems=input("\nEnter your choice:")
            if (ems.upper()=='A'):
                add_new()
                print("These details have been stored in the database.")
            elif (ems.upper()=='B'):
                display_record()
            elif (ems.upper()=='C'):
                edit_loop()
            elif (ems.upper()=='D'):
                delete_details()
            elif (ems.upper()=='E'):
                view_all()
            elif (ems.upper()=='F'):
                view_del()
            else:
                print("Invalid Input.")
        else:
            print("Incorrect Password.")
            
            
def dosl():
    main_menu()
    print("\nWould you like to restart the program?")
    chs=input("Enter Y/N:")
    if (chs.upper()=='Y'):
        dosl()
    elif (chs.upper()=='N'):
        print("")
    else:
        print("Invalid input, Program restarting.")
        dosl()
        
    
dosl()


    
