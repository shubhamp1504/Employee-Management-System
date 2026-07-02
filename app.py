import pymysql

db = pymysql.connect(
    host= "mysqldb",
    user="root",
    password="root",
    database="company"
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
)
""")

db.commit()

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        dept = input("Enter Department: ")

        sql = "INSERT INTO employees (name, department) VALUES (%s, %s)"
        cursor.execute(sql, (name, dept))
        db.commit()

        print("Employee Added Successfully")

    elif choice == "2":
        cursor.execute("SELECT * FROM employees")

        for row in cursor.fetchall():
            print(row)

    elif choice == "3":
        break

db.close()