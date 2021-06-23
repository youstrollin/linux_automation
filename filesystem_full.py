import os
import subprocess
import re
class MyException(Exception):
    pass
def fscheck(fsname): # organizes contents of /proc/mount in mydict with mountpoint as key, rest as values, if input exists as mountpoint, returns value, else returns false.
    mydict = {}
    if re.match(r"^\/[0-9a-zA-Z_.\/]+", fsname): #REVIEW BETTER SANITIZATION METHOD
        command = ['cat', '/proc/mounts']
        with open(os.devnull, 'w') as devnull:
            fslist = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=devnull) #devnull because 2.6 compatibility
            for i in fslist.stdout.readlines():
              mylist = i.strip().split(' ')
              mydict[mylist[1]] = mylist[:1] + mylist[2:]
             if fsname in mydict:
              return mydict(fsname)
          else:
              return False
    else:
        raise MyException("Provided filesystem path is not valid.")

def inodecheck(fsname):
    command = ['df', '-i']
    if re.match(r"^\/[0-9a-zA-Z_.\/]+", fsname): #REVIEW BETTER SANITIZATION METHOD
        command.append(fsname)
        inodelist = subprocess.Popen(command stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        if re.match("^[0-9]+", inodelist.stdout.readlines()[-1].strip()):
            if inodelist.stdout.readlines()[-1].strip().split()[2] > 0:
                return True
            elif inodelist.stdout.readlines()[-1].strip().split()[2] <= 0:
                return False
            else
                raise MyExeception("inodecheck used valuen err")

