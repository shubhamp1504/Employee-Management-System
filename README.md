# Employee Management System using Python, MySQL & Docker

## 📌 Project Overview

The **Employee Management System** is a simple command-line application developed using **Python** and **MySQL**. The application allows users to add employee details and view all employee records stored in the database.

The project is containerized using **Docker**, making it easy to deploy and run on any system without installing Python or MySQL locally.

---

## 🚀 Features

* Add new employees
* View all employees
* Store employee data in MySQL database
* Automatically creates the employee table if it does not exist
* Dockerized application for easy deployment

---

## 🛠️ Technologies Used

* Python 3
* MySQL
* PyMySQL
* Docker
* Docker Compose

---

## 📂 Project Structure

```
Employee_Management/
│── app.py
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── README.md
```

---

## ⚙️ How It Works

1. The application connects to the MySQL database.
2. It checks whether the `employees` table exists.
3. If the table does not exist, it creates it automatically.
4. The user is shown a simple menu:

   * Add Employee
   * View Employees
   * Exit
5. Employee information is stored permanently in the MySQL database.

---

## 🐳 Run the Project Using Docker

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Employee_Management.git

cd Employee_Management
```

---

### Step 2: Build and Start Containers

```bash
docker compose up --build
```

---

### Step 3: Run the Application

If your application container is already running:

```bash
docker compose run mypythonapp
```

or

```bash
docker exec -it <container_name> python app.py
```

---

## 📋 Sample Output

```
1. Add Employee
2. View Employees
3. Exit

Enter Choice: 1

Enter Name: Shubham
Enter Department: DevOps

Employee Added Successfully
```

View Employees:

```
1. Shubham | DevOps
2. Rahul   | Python Developer
3. Priya   | Cloud Engineer
```

---

## 🗄️ Database Schema

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);
```

---

## 📚 Future Improvements

* Update employee details
* Delete employee records
* Search employees by ID or name
* Login authentication
* Employee salary management
* Email notifications
* Web interface using Flask or Django
* REST API integration
* Docker volume for persistent database storage
* Deploy on AWS using Docker

---

## 💡 Learning Outcomes

Through this project, I learned:

* Python database connectivity using PyMySQL
* CRUD operations in MySQL
* SQL table creation
* Docker containerization
* Docker Compose for multi-container applications
* Container networking
* Basic DevOps concepts

---

## 👨‍💻 Author

**Shubham Patil**

Aspiring DevOps Engineer

### Skills

* Linux
* Shell Scripting
* Git & GitHub
* Python
* MySQL
* Docker
* Jenkins
* AWS

---

## ⭐ If you like this project

Please give this repository a **Star ⭐** on GitHub.
