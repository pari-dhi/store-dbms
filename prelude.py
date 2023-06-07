import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rootcode",
    database="project")

print(db)


mycursor=db.cursor()


mycursor.execute("CREATE TABLE BASE(ORDER_ID integer primary key,"
                 "CUST_NAME varchar(20), PHONE_NO VARCHAR(12),"
                 "LEFTLENS VARCHAR(15), RIGHTLENS VARCHAR(15), PRICE INTEGER")
                

db.commit()



#table pricedetails was created in sql
#columns in price are:
#order_id
#brandprice: to store price of brand
#lensprice: to store price of lens
# f_price for final price



#tables for display


mycursor.execute("CREATE TABLE BRANDS(BRAND_ID VARCHAR(5),"
                 "BRAND_NAME VARCHAR(30))")
db.commit()


mycursor.execute("INSERT INTO BRANDS VALUES"
                 "('B001', 'Christian Dior'),('B002', 'Prada'),"
                 "('B003', 'Hugo'), ('B004', 'Jilly Stuart'),"
                 "('B005', 'Ray Ban'), ('B006','Emozioni'),"
                 "('B007', 'Saint Laurent'), ('B008', 'Silhouette'),"
                 "('B009', 'Oakley'), ('B010', 'Gucci'),"
                 "('B011','Michael Kors'), ('B012', 'Izumi')")

db.commit()


mycursor.execute("CREATE TALBLE LENS_TYPES(LENS_SLNO VARCHAR(10),"
                 "LENS_TYPE VARCHAR(15), CONDITION VARCHAR(15))")
db.commit()


mycursor.execute("INSERT INTO LENS_TYPES VALUES"
                 "('L001', 'Progressive', 'Presbyopia'),"
                 "('L002', 'Concave', 'Myopia'),"
                 "('L005', 'Bifocal', 'Presbyopia'),"
                 "('L006', 'Convex', 'Hypermetropia'),"
                 "('L007', 'Cylindrical', 'Astigmatism')")
db.commit()
