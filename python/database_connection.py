import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",   # Leave empty
        database="personal_finance_analytics"
    )

    if connection.is_connected():
        print("Connected Successfully!")

except Exception as e:
    print(e)
finally:

    if connection.is_connected():
        connection.close()
        print("Connection Closed")