import os
import subprocess
import re
class MyException(Exception):
    pass
def fscheck(fsname): # organizes contents of /proc/mount in mydict with mountpoint as key, rest as values, if input exists as mountpoint, returns value, else returns false.
    mydict = {}
    if re.match(r"^\/[0-9a-zA-Z_.\/]+", fsname): #REVIEW BETTER SANITIZATION METHOD
        command = {'cat', '/proc/mounts'}
        fslist = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        for i in fslist.communicate():
            mylist = i.strip().split(' ')
            mydict[mylist[1]] = mylist[:1] + mylist[2:]
        if fsname in mydict:
            return mydict(fsname)
        else:
            return False
    else:
        raise MyException("Provided filesystem path is not valid.")

def inodecheck(fsname):
    inodecheck_command = ['df', '-i']
    inodecheck_command.append(fsname)
