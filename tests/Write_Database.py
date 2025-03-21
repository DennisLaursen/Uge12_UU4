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

#Opretter en tabel med kolonnerne id, name og email
mycursor.execute("CREATE TABLE customers (id INTEGER(5), name VARCHAR(255), email VARCHAR(255))") #Kan kun køres én gang, og vil efterfølgende fejle, hvis tabellen allerede eksisterer

print("Table created successfully!") #Skal printes, hvis tabellen er oprettet korrekt