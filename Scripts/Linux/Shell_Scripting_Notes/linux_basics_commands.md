# Linux File & Directory + Viewing + Searching Commands

------------------------------------------------------------------------

## 📁 File & Directory Commands

### ls

List files and directories. - `ls` -- basic listing\
- `ls -l` -- long format\
- `ls -a` -- show hidden files\
- `ls -lh` -- human-readable sizes

### pwd

Print current working directory.

### cd

Change directory. - `cd /path` -- go to specific directory\
- `cd ..` -- move one level up

### mkdir

Create a new directory. - `mkdir dir_name`\
- `mkdir -p parent/child` (create nested directories)

### rmdir

Remove empty directory.

### cp

Copy files or directories. - `cp file1 file2`\
- `cp -r dir1 dir2` (recursive copy)

### mv

Move or rename files/directories. - `mv oldname newname`\
- `mv file /path/`

### rm

Remove files or directories. - `rm file`\
- `rm -r dir` (remove directory recursively)\
- `rm -f file` (force delete)

### touch

Create empty file or update file timestamp. - `touch filename`

------------------------------------------------------------------------

## 📄 File Viewing Commands

### cat

Display file contents. - `cat file.txt`

### less

View file interactively (recommended for large files). - Use `q` to
quit.

### more

Basic file viewer (older than less).

### head

Show first 10 lines of a file. - `head file.txt`\
- `head -n 20 file.txt`

### tail

Show last 10 lines of a file. - `tail file.txt`\
- `tail -n 20 file.txt`

### tail -f

Monitor file in real-time (used for logs). - `tail -f logfile.log`

------------------------------------------------------------------------

## 🔍 Searching Commands

### grep

Search for patterns inside files. - `grep "text" file.txt`\
- `grep -i "text" file.txt` (case insensitive)\
- `grep -r "text" /directory` (recursive search)

### find

Search for files and directories. - `find /path -name "file.txt"`\
- `find /path -type f` (files only)\
- `find /path -mtime +7` (modified more than 7 days ago)

### which

Locate executable path of a command. - `which python`

### locate

Quickly find files using indexed database. - `locate filename`\
(Note: Database must be updated using `updatedb`.)

-----------------------------------------------------------------------
