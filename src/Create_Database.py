#Denne kode opretter en database kaldet "testdb" på serveren
import mysql.connector

#Log ind på database serveren
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
)

#Mycursor er "nøglen" til at kunne "komme ind" og interagere med databasen
mycursor = mydb.cursor()

#Tjek om databasen allerede eksisterer
mycursor.execute("SHOW DATABASES")
existing_databases = [db[0] for db in mycursor.fetchall()] #Henter alle eksisterende databaser

if "testdb" in existing_databases: #Tjekker om databasen allerede eksisterer
    print("Database 'testdb' already exists.")
else:
    mycursor.execute("CREATE DATABASE testdb") #Opretter databasen, hvis den ikke allerede eksisterer
    print("Database 'testdb' created successfully.")

mycursor.close() #Lukker forbindelsen til databasen