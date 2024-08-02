import mysql.connector

def store_data_to_db(df):
    db = mysql.connector.connect(
        host="your-db-endpoint",
        user="your-db-username",
        password="your-db-password",
        database="flight_data"
    )
    cursor = db.cursor()
    for index, row in df.iterrows():
        query = "INSERT INTO flights (flight_number, departure, arrival, status) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (row['flight_number'], row['departure'], row['arrival'], row['status']))
    db.commit()
    cursor.close()
    db.close()
