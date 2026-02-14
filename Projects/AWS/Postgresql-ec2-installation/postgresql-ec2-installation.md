# PostgreSQL 17 Installation on AWS EC2 (Ubuntu 24.04)

This project demonstrates the installation and configuration of PostgreSQL 17 on an Ubuntu 24.04 EC2 instance, and connecting it remotely using DBeaver.

Official Documentation:
https://www.postgresql.org/download/linux/ubuntu/

---

# PART 1 – PostgreSQL Installation on EC2

## 1️⃣ Update System

```bash
sudo apt update
sudo apt upgrade -y
```
---

## 2️⃣ Automated Repository Configuration

```bash
sudo apt install -y postgresql-common
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
```
---
## 3️⃣ Manual Repository Configuration (Alternative Method)

```bash
sudo apt install curl ca-certificates
sudo install -d /usr/share/postgresql-common/pgdg
sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc
cat /etc/os-release
sudo sh -c "echo 'deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $VERSION_CODENAME-pgdg main' > /etc/apt/sources.list.d/pgdg.list"
sudo apt update
```
---

## 4️⃣ Install PostgreSQL

```bash
sudo apt install postgresql-17
(You can install any required version.)
```
---

## 5️⃣ Verify Installation

```bash
sudo systemctl status postgresql
psql --version
```
---

## 6️⃣ Create User and Database

Inside `psql`:
```sql
CREATE USER username WITH ENCRYPTED PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
```
---

## 7️⃣ Restart PostgreSQL:

```bash
sudo systemctl restart postgresql
```
---
## 8️⃣ Login using the created user:

```sql
psql -U username -h localhost -d database_name
```
<img width="338" height="69" alt="image" src="https://github.com/user-attachments/assets/f0f74f89-a959-45cf-b93e-b63eecf3c1e3" />

---

# PART 2 – Connect PostgreSQL to DBeaver

## 1️⃣ Check if Port 5432 is Listening

```bash
sudo ss -tlnp | grep 5432
```
---
### If:

listen_addresses = localhost

---
### Then modify the configuration file:

```bash
sudo vim /etc/postgresql/17/main/postgresql.conf
```
---

### Change:
listen_addresses = '0.0.0.0'

---
### Save and exit.
### Check again:
```bash
sudo ss -tlnp | grep 5432
```
---

# 2️⃣ If You Get an Error:
FATAL: no pg_hba.conf entry for host
This means PostgreSQL received the connection request, but your IP is not allowed.

---

# 3️⃣ Allow Your Public IP in pg_hba.conf

## Find your laptop public IP:
```bash
curl https://checkip.amazonaws.com
```
---

## SSH into EC2 and edit:
```bash
sudo vim /etc/postgresql/17/main/pg_hba.conf
```
---

## Add at bottom (replace with your IP):

host    all    all    YOUR_PUBLIC_IP/32    md5

---

##  Restart PostgreSQL:
```bash
sudo systemctl restart postgresql
```
---

# 4️⃣ Security Group Configuration

## In AWS Security Group:

- Open port 5432
- Allow your system's public IP instead of 0.0.0.0/0

---
✅ Final Step

- Now connect from DBeaver using:
- Host: EC2 Public IP
- Port: 5432
- Username: Created username
- Password: Your password
- Database: database_name
- Connection should be successful

  <img width="588" height="314" alt="image" src="https://github.com/user-attachments/assets/65c28626-3b8d-46a0-ac15-a360fd7f65a7" />
---

## 🛠️ Skills Demonstrated

- PostgreSQL installation on Ubuntu 24.04
- APT repository configuration
- Service management using systemctl
- Remote PostgreSQL connectivity using DBeaver
- AWS Security Group configuration (Port 5432)
- pg_hba.conf and postgresql.conf configuration
- Troubleshooting connection and authentication errors
---

