import mysql.connector

#Log ind på database serveren
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
)

#Mycursor er "nøglen" til at kunne "komme ind" og interagere med databasen
mycursor = mydb.cursor()

#Opretter en database
mycursor.execute("CREATE DATABASE testdb") #Kan kun køres én gang, da navngivningen er statisk. Så koden vil fejle, hvis databasen allerede eksisterer.