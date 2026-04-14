#!/usr/bin/python3

# INET4031
# Alieu Sarr
# 04-13-2026
# 04-13-2026


import os # import for running os operations and commands. Lets you work directly with files and system directories.
import re # Import for access to regular expression functions, lets me search and match strings
import sys # Import to get command line arguments (user arguments and IO Streams)

def main():
    for line in sys.stdin:

        # match variable is a bool which checks whether the '#' character is present or not
        match = re.match("^#",line) # outputs either a true or false

        # split up the line input to create a new user after every ':'
        fields = line.strip().split(':')

        # This is a data validation This is a data validation check. If a line is a match, that means it's just a comment, or if it doesnt have 5 peices of data the script skips it using the continue command.  
        if match or len(fields) != 5:
            continue

        # These three lines map specific columns from the file to program variables. gecos specifically formats the "General Electric Comprehensive Operating System" field, which stores user metadata like full names and room numbers.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # This splits the 5th field by commas to add users to multiple groups at once
        groups = fields[4].split(',')

        # Provides feedback to the admin so they know which account is currently being processed, basically a debugging tool
        print("==> Creating account for %s..." % (username))
        
        #  initializing the cmd variable which contains the full Linux shell command to create a user without a password
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # It uses echo to pipe the password twice into the passwd command. 
        # This automates the password set process, which would usually require manual typing
        # 
        os.system(cmd)

        #  Allows you to see the user is about to receive a password
        print("==> Setting the password for %s..." % (username))
    
        # this ensures the right password is associated with the right user in the actual password file
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        print(cmd)
        # print out the current command being run and then tell the system to run that command
        os.system(cmd)
        for group in groups:
            # This checks if the group field contains a hyphen. In this script's logic, a hyphen means no groups assigned.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
