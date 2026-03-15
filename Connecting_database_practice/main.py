from config import get_db_connection

connection = get_db_connection()

if connection is None:
    print("Error: Could not connect to DB")
else:
    try:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_python (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50)
        )
        """)
        connection.commit()
        print("Table created successfully!")
        cursor.execute("SELECT current_database();")
        print(cursor.fetchone())
    except Exception as e:
        print("Error executing SQL:", e)
    finally:
        cursor.close()
        connection.close()