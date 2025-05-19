import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sha2002",
        database="student_db"
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            grade VARCHAR(10)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_student(name, age, grade):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, grade))
    conn.commit()
    cursor.close()
    conn.close()

def fetch_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
