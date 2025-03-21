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

file=open('C:/Users/spac-46/Documents/GitHub/Uge12_UU4/data/customers.csv') #Åbner filen, som jeg vil indsætte i databasen
csv_data = csv.reader(file)

next(csv_data) #Springer den første række med kolonnenavnene over

for row in csv_data:
    print(row) 
    mycursor.execute('INSERT INTO customers(id, name, email) VALUES(%s, %s, %s)', row) #%s er mine "placeholders", som jeg kan indsætte mine værdier i fra min csv-fil

mydb.commit() #Gemmer mine ændringer til databasen
mycursor.close() #Lukker forbindelsen til databasen
print("Done")