import mysql.connector

#Log ind på database serveren
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="testdb"
)

#Mycursor er "nøglen" til at kunne "komme ind" og interagere med databasen
mycursor = mydb.cursor()

#Viser alle tabeller i databasen "testdb", kolonnerne i tabellen "customers", samt rækker i tabellen "customers"
mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)
   
mycursor.execute("SHOW COLUMNS FROM customers")

for col in mycursor:
    print(col)

mycursor.execute("SELECT * FROM customers")

for row in mycursor:
    print(row)

mycursor.close() #Lukker forbindelsen til databasen