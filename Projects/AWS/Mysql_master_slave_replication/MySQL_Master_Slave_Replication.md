# MySQL Master–Slave Replication on AWS EC2

## 📌 Project Overview

This project demonstrates MySQL Master–Slave replication setup on two AWS EC2 Ubuntu instances.

The goal is to:
- Achieve real-time data replication
- Improve availability
- Demonstrate production-level database configuration skills

---

## 🏗️ Architecture

    ┌──────────────────────┐
    │      EC2 MASTER      │
    │   MySQL (server-id 1)│
    └───────────┬──────────┘
                │  Port 3306
                ▼
    ┌──────────────────────┐
    │      EC2 SLAVE       │
    │   MySQL (server-id 2)│
    └──────────────────────┘


Master EC2  --->  Slave EC2  
(MySQL)           (MySQL)

Both instances are inside same VPC and replication happens over port 3306.

---
# MASTER SETUP

## 1. Install MySQL

```bash
sudo apt update
sudo apt install mysql-server -y
mysql -V
```

## Secure Installation

Run the following command:

```bash
sudo mysql_secure_installation
```
## 🔹 Set Root Password

Login to MySQL first:

```bash
sudo mysql -u root
```

Then run:

```sql
ALTER USER 'root'@'localhost'
IDENTIFIED WITH mysql_native_password BY 'Master@123';
```

## 🔹 Configure `mysqld.cnf`

Edit the MySQL configuration file:

```bash
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```
Add the following lines:

```
bind-address = 0.0.0.0
server-id = 1
log-bin = /var/log/mysql/mysql-bin.log
binlog_do_db = demo
```

Restart MySQL:

```bash
sudo systemctl restart mysql
```

## 🔹 Create Database

Run the following SQL commands:

```sql
CREATE DATABASE demo;
USE demo;

CREATE TABLE MyGuestList (
    id INT PRIMARY KEY,
    firstname VARCHAR(100),
    surname VARCHAR(100),
    city VARCHAR(100)
);

INSERT INTO MyGuestList VALUES (1,'Neha','Patil','Pune');
```

---

## 🔹 Create Replication User

```sql
CREATE USER 'repl_user'@'%'
IDENTIFIED WITH mysql_native_password BY 'slavepass123';

GRANT REPLICATION SLAVE ON *.* TO 'repl_user'@'%';
FLUSH PRIVILEGES;
```
## 🔹 Get Master Log Info

Run the following command:

```sql
SHOW MASTER STATUS;
```

Example Output:

```
+------------------+----------+---------------+
| File             | Position | Binlog_Do_DB  |
+------------------+----------+---------------+
| mysql-bin.000001 | 1982     | demo          |
+------------------+----------+---------------+
```

Save the following values:
- **File**
- **Position**

# 🖥️ SLAVE CONFIGURATION

## 🔹 Install MySQL

```bash
sudo apt update
sudo apt install mysql-server -y
```

---

## 🔹 Configure Slave

Edit the MySQL configuration file:

```bash
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```
Add the following lines:

```
server-id = 2
relay-log = /var/log/mysql/mysql-relay-bin.log
binlog_do_db = demo
```

Restart MySQL:

```bash
sudo systemctl restart mysql
```

## 3️⃣ Configure Replication

Login to MySQL:

```bash
sudo mysql -u root -p
```

---

### 🔹 For MySQL 8.0

```sql
CHANGE MASTER TO
  MASTER_HOST='MASTER_PRIVATE_IP',
  MASTER_USER='repl_user',
  MASTER_PASSWORD='slavepass123',
  MASTER_LOG_FILE='mysql-bin.000001',
  MASTER_LOG_POS=1982;

START SLAVE;
```

---

### 🔹 For MySQL 8.4+

```sql
CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='MASTER_PRIVATE_IP',
  SOURCE_USER='repl_user',
  SOURCE_PASSWORD='slavepass123',
  SOURCE_LOG_FILE='mysql-bin.000001',
  SOURCE_LOG_POS=1982;

START REPLICA;
```

---

## 4️⃣ Verify Replication

```sql
SHOW SLAVE STATUS\G
```

Ensure the following values show:

```
Slave_IO_Running: Yes
Slave_SQL_Running: Yes
```

---

# ✅ Testing Replication

### 🔹 On Master

```sql
INSERT INTO MyGuestList VALUES (2,'Aish','Raje','Mumbai');
```

### 🔹 On Slave

```sql
SELECT * FROM demo.MyGuestList;
```

If replication is working correctly, the inserted record will automatically appear on the Slave instance.

## 🔐 Security Configuration

| Setting           | Configuration              |
|-------------------|---------------------------|
| Port              | 3306                      |
| Access            | Only Slave Private IP     |
| Replication User  | Limited privileges        |
| Root Usage        | Not used for replication  |

## 🛠️ Skills Demonstrated

- AWS EC2 provisioning  
- MySQL configuration  
- Binary logging  
- Master–Slave replication  
- Linux administration  
- Cloud networking  
- Production-level database setup  

## 🎯 Project Outcome

Successfully implemented and verified real-time MySQL replication between two EC2 instances inside AWS.

This project demonstrates practical cloud and database administration skills suitable for DevOps roles.





 


