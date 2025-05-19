import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sha2002',
    database='student_db'
)

cursor = connection.cursor()

# Create table if not exists
def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            phone VARCHAR(15),
            marks INT,
            grade VARCHAR(5)
        )
    """)
    connection.commit()

# Insert student data
def insert_student(name, email, phone, marks, grade):
    cursor.execute("""
        INSERT INTO students (name, email, phone, marks, grade)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, email, phone, marks, grade))
    connection.commit()

# ✅ Fetch all student records
def fetch_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()
