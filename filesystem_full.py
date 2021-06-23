#
# Pending: better fsname sanitization REGEX, maybe change exceptions to return false and end script in MAIN with return message of one failed.
#
import os
import subprocess
import re
import sys
class MyException(Exception):
    pass
def fscheck(fsname): # organizes contents of /proc/mount in mydict with mountpoint as key, rest as values, if input exists as mountpoint, returns value, else returns false.
    mydict = {}
    if re.match(r"^\/[0-9a-zA-Z_.\/]+", fsname): #REVIEW BETTER SANITIZATION METHOD
        command = ['cat', '/proc/mounts']
        with open(os.devnull, 'w') as devnull:
            fslist = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=devnull) #devnull because 2.6 compatibility, if not subprocess.DEVNULL
            for i in fslist.stdout.readlines():
              mylist = i.strip().split(' ')
              mydict[mylist[1]] = mylist[:1] + mylist[2:]
        if fsname in mydict:
            return mydict[fsname]
        else:
          return False
    else:
        raise MyException("Provided filesystem path is not valid.") #fscheck function tested 23/6 OK py2.6

def inodecheck(fsname): # runs df -i against input fs, parses free inode value and returns true if > 0 or false if <= 0
    command = ['df', '-i']
    if re.match(r"^\/[0-9a-zA-Z_.\/]+", fsname): #REVIEW BETTER SANITIZATION METHOD
        command.append(fsname)
        with open(os.devnull, 'w') as devnull:
            piperead = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=devnull)
            inodelist = piperead.stdout.readlines()[-1].strip().split()
            if re.match("^[0-9]+", inodelist[2]):
                if int(inodelist[2]) > 0:
                    return True
                elif int(inodelist[2]) <= 0:
                    return False
            else:
                raise MyExeception("inodecheck free inodes value error.") #inodecheck function tested 23/6 OK py2.6
    else:
        raise MyException("Filesystem name failed additional REGEX.")

def usagecheck(fsname): # Verifies whether fs usage is over threshold value or not.
    if re.match(r"^\/[0-9a-zA-Z_.\/]+", fsname): #REVIEW BETTER SANITIZATION METHOD
        command = ['df', '-h', fsname]
        threshold = 85
        with open(os.devnull, 'w') as devnull:
            piperead = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=devnull)
            dflist = piperead.stdout.readlines()[-1].strip().split()
        usageper = "".join([item for item in dflist if "%" in item]).replace("%","")
        if int(usageper) >= threshold:
            return True
        elif int(usageper) < threshold:
            return False
        else:
            raise MyException("Filesystem usage percentage math error.")
    else:
        raise MyException("Filesystem name failed additional REGEX.") #usagecheck function tested 23/6 OK py2.6

def main():
    myarguments = "".join(sys.argv[1]) #limited to first argument "fsname" for now.
    if fscheck(myarguments) and inodecheck(myarguments) and usagecheck(myarguments):
        # FILE REMOVAL or LISTING FUNCTION CALL DEPENDING ON EXECUTION ARGUMENT
    else:
         # Maybe remove custom exceptions from functions and handle here with FALSE returned?
if __name__ == "__main__":
    main()