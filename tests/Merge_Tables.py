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

#Opret tabellerne
create_customers = """" \" \
"CREATE TABLE customers (id INTEGER(5), name VARCHAR(255), email VARCHAR(255))" \" \
    """
create_orders = """" \" \
    "CREATE TABLE orders (id INTEGER(5), order_date DATE, customer_id INTEGER(5))" \" \
    """ 
create_products = """" \" \
    "CREATE TABLE products (id INTEGER(5), name VARCHAR(255), price INTEGER(5))" \" \
    """
db.execute_query(create_customers)
db.execute_query(create_orders)
db.execute_query(create_products)