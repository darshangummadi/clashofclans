import cx_Oracle

def connect_to_oracle():
    try:
        # Use the TNS alias defined in tnsnames.ora
        connection = cx_Oracle.connect(user='ADMIN', password='Oracleclash2024', dsn='gf63e059c3dfcbd_ax9cd7nk6hac0um4_high')
        print("Connection successful")
        return connection
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print(f"Database error: {error.message}")
        return None

def main():
    connection = connect_to_oracle()
    if connection:
        connection.close()
        print("Connection closed")

if __name__ == "__main__":
    main()