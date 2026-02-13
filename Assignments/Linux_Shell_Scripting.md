# Linux & Shell Scripting Complete Assignments

This document contains all Linux and Shell Scripting assignments including implementations and challenges.

---

# 1️⃣ Shell Scripting – Folder Operations

## Question

Create two folders named **abc** and **xyz**  
(Implemented as D_folder1 and D_folder2)

Using shell script:

- Create a file in folder1  
- Create a file in folder2  
- Create sub_folder1 inside folder1  
- Create sub_folder2 inside folder2  
- Implement: `cp`, `mv`, `rm`, `echo`, `pwd`

## Script

```bash
#!/bin/bash

touch abc.txt
echo "abc file is created"

folder1_path="/home/neha_ubuntu/D_folder1"
folder2_path="/home/neha_ubuntu/D_folder2"

if [ -d "$folder1_path" ]; then
    rm -r "$folder1_path"
fi

if [ -d "$folder2_path" ]; then
    rm -r "$folder2_path"
fi

mkdir "$folder1_path"
mkdir "$folder2_path"

touch "$folder1_path/f1.txt"
touch "$folder2_path/f2.txt"

mkdir "$folder1_path/sub_folder1"
mkdir "$folder2_path/sub_folder2"

cp abc.txt "$folder1_path/sub_folder1/"
mv "$folder1_path/f1.txt" "$folder2_path/"

touch removefile.txt
rm removefile.txt

pwd
```

---

# 2️⃣ Introduction to Linux & Basic Commands

## Create Directory Structure

```bash
mkdir -p /home/neha_ubuntu/Assignment_Folder/Day1/linux_basics/day1
```

## Create 3 Files and Move to data Folder

```bash
touch text_file1.txt text_file2.txt text_file3.txt
mkdir data
mv text_file1.txt text_file2.txt text_file3.txt data/
```

## Redirect Output

```bash
ls -l > output.txt
```

---

# 3️⃣ Working with Files & Permissions

```bash
touch report.txt
chmod 600 report.txt
sudo useradd -m -s /bin/bash mneha
sudo chown mneha report.txt
```

---

# 4️⃣ File Searching & Text Processing

```bash
grep -r -i "trees" /home/neha_ubuntu/Log_Files_Folder/
wc -w /home/neha_ubuntu/Log_Files_Folder/*.log
find . -iname "*.log" -exec grep -i "trees" {} \;
```

---

# 5️⃣ Redirection, Pipes & Filters

```bash
ls -l > Output.txt
cat Output.txt | grep ".txt"
sort Output.txt | uniq | wc -l
```

---

# 6️⃣ Environment Variables

```bash
uname -a > system_report.txt
export MYNAME="neha"
echo 'export MYNAME="neha"' >> ~/.bashrc
```

---

# 7️⃣ Shell Scripting Basics

```bash
#!/bin/bash
read -p "Enter your name:- " name
echo "Good morning, $name !"
chmod +x greet.sh
```

---

# 8️⃣ Conditional Statements

```bash
#!/bin/bash
read -p "Enter file name " file_name
file_path="/home/neha_ubuntu/Assignment_Folder/$file_name"

if [ -f "$file_path" ]; then
    echo "File exists"
else
    echo "File not found"
fi
```

---

# 9️⃣ Loops

```bash
#!/bin/bash

for number in {1..10}
do
    echo $number
done
```

---

# 🔟 Functions & Command-Line Arguments

## Factorial Function

```bash
#!/bin/bash

factorial() {
    num=$1
    fact=1
    for ((i=1; i<=num; i++))
    do
        fact=$((fact * i))
    done
    echo $fact
}

factorial 5
```

---

# Summary

This repository demonstrates:

- Linux file system handling  
- File permissions management  
- Text processing  
- Redirection & pipes  
- Environment variables  
- Shell scripting fundamentals  
- Loops & conditionals  
- Functions & argument handling  
- Basic input validation concepts  

These assignments showcase practical Linux & Shell scripting skills relevant for DevOps roles.
