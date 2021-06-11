import os
def fscheck(fsname): # organizes contents of /proc/mount in mydict with mountpoint as key, rest as values, if input exists as mountpoint, returns value, else returns false.
    mydict = {}
    fslist = os.popen('cat /proc/mounts')
    for i in fslist.readlines():
        mylist = i.strip().split(' ')
        mydict[mylist[1]] = mylist[:1] + mylist[2:]
    if fsname in mydict:
        return mydict(fsname)
    else:
        return False