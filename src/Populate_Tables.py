import mysql.connector
import csv

#Log ind på database serveren
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Velkommen25",
    database="testdb"
)

#Mycursor er "nøglen" til at kunne "komme ind" og interagere med databasen
mycursor = mydb.cursor()

with open('data/customers.csv') as file: #Åbner filen, som jeg vil indsætte i databasen
    csv_data = csv.DictReader(file)

    for row in csv_data:
        print(row)

mydb.commit() #Gemmer mine ændringer til databasen
mycursor.close() #Lukker forbindelsen til databasen
print("Done")