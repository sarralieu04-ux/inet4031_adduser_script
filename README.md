# inet4031_adduser_script

This Python-based automation system  streamlines the process of managing system users in a Linux environment. This repo holds the code for my INET4031 Lab 8. The script reads a formatted input file via stdin to perform bulk user creation (tested with 6 users), automated password assignment, and group management.
Key features include:

* Input Validation: ignores comments and misconfigured data automatically.
* Metadata Management: Properly formats GECOS fields to include user metadata such as full names.
* Automated Security: Utilizes system pipes to set user passwords without manual work.
* Conditional Group Assignment: Dynamically assigns users to multiple secondary groups while skipping assignment if no groups are specified.


Program Operation
The script is designed to be executed from a Linux terminal and requires root or sudo privileges to modify system files like /etc/passwd and /etc/shadow. Check out create-users.input and create-users.py to see the documented code behind the program.


Prerequisites:
- Python 3.x installed.
- Run *chmod +x create-users.py* for the script to have executable permissions.


Execution:
run: sudo ./create-users.py < create-users.input
