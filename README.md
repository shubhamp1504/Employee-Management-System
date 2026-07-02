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

