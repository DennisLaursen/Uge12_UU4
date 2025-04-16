#Denne kode viser alle databaser på serveren
import mysql.connector

#Log ind på database serveren
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
)

#Mycursor er "nøglen" til at kunne "komme ind" og interagere med databasen
mycursor = mydb.cursor()

#Viser alle databaser på serveren
mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)