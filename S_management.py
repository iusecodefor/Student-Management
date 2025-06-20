import mysql.connector

# Connect to MySQL Database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwerty123",  # Change this to your MySQL password
    database="student_db"
)
cursor = conn.cursor()

# Function to Add Student
def add_student(name, age, cgpa, email):
    sql = "INSERT INTO students (name, age, cgpa, email) VALUES (%s, %s, %s, %s)"
    values = (name, age, cgpa, email)
    cursor.execute(sql, values)
    conn.commit()
    print(" Student added successfully!")

# Function to View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\n Student Records:")
    for student in students:
        print(student)

# Function to Update Student
def update_student(student_id, name, age, cgpa, email):
    sql = "UPDATE students SET name=%s, age=%s, cgpa=%s, email=%s WHERE id=%s"
    values = (name, age, cgpa, email, student_id)
    cursor.execute(sql, values)
    conn.commit()
    print(" Student updated successfully!")

# Function to Delete Student
def delete_student(student_id):
    sql = "DELETE FROM students WHERE id=%s"
    cursor.execute(sql, (student_id,))
    conn.commit()
    print(" Student deleted successfully!")

# Menu-Driven Program
while True:
    print("\n---  Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        cgpa = float(input("Enter CGPA: "))
        email = input("Enter Email: ")
        add_student(name, age, cgpa, email)

    elif choice == "2":
        view_students()

    elif choice == "3":
        student_id = int(input("Enter Student ID to Update: "))
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        cgpa = float(input("Enter New CGPA: "))
        email = input("Enter New Email: ")
        update_student(student_id, name, age, cgpa, email)

    elif choice == "4":
        student_id = int(input("Enter Student ID to Delete: "))
        delete_student(student_id)

    elif choice == "5":
        print(" Exiting Program...")
        break

    else:
        print(" Invalid Choice! Please Try Again.")

# Close Connection
cursor.close()
conn.close()
