#!/usr/bin/python3

# INET4031
# Alieu Sarr
# 04-13-2026
# 04-13-2026


import os # import for running os operations and commands. Lets you work directly with files and system directories.
import re # Import for access to regular expression functions, lets me search and match strings
import sys # Import to get comand line arguments (user arguments and IO Streams)

def main():
    for line in sys.stdin:

        # match variable is a bool which checks whether the '#' char is present or not
        match = re.match("^#",line) # outputs either a true or false

        # split up the line input to create a new user after every ':'
        fields = line.strip().split(':')

        # This is a data validation This is a data validation check. If a line is a match that means its just a comment or if it doesnt have 5 peices of data the script skips it using the continue command.  
        if match or len(fields) != 5:
            continue

        # These three lines map specific columns from the file to program variables. gecos specifically formats the "General Electric Comprehensive Operating System" field, which stores user metadata like full names and room numbers.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # This splits the 5th field by commas to addd users to multiple groups at once
        groups = fields[4].split(',')

        # 
        print("==> Creating account for %s..." % (username))
        
        #  
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # 
        # 
        os.system(cmd)

        #  
        print("==> Setting the password for %s..." % (username))
    
        # 
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #

        # 
        os.system(cmd)
        for group in groups:
            # 
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
