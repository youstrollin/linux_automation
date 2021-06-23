#physical server or VM process done previously via playbook, only receives option + LUN IDs/device names
#PENDING: Maybe separate the inq and rescan parts into separate functions, they have multiple "calls" already.
#
import os
import subprocess
import re
import sys

class MyException(Exception):
    pass

def vmcreate(devids):
    commandinq = ['inq', '-no_dots']
    commandls = ['ls', '-1', '/sys/class/scsi_host']
    commandecho = ['echo', '---']
    scsi_list = []
    predevices = []
    postdevices = []
    with open(os.devnull, 'w') as devnull:
        piperead = subprocess.Popen(commandinq, stdout=subprocess.PIPE, stderr=devnull) #devnull because 2.6 compatibility, if not subprocess.DEVNULL
        for i in piperead.stdout.readlines():
            if re.match(r"^\/dev\/sd[a-z]+", i): predevices.append(i.split()[0]) #runs inq -no_dots, output that matches /dev/sdX+ is stored as predevices list
            else: MyException("No valid devices matched on INQ command output.")
        piperead = subprocess.Popen(commandls, stdout=subprocess.PIPE, stderr=devnull)
        for i in piperead.stdout.readlines(): scsi_list.append('/sys/class/scsi_host/{0}/scan'.format(i.strip´())) #runs ls -1 /sys/class/scsi_host, output is opened as file and --- written
        for i in scsi_list:
            with open(i, 'w') as outfile: outfile.write("---\n")
        piperead = subprocess.Popen(commandinq, stdout=subprocess.PIPE, stderr=devnull) #devnull because 2.6 compatibility, if not subprocess.DEVNULL
        for i in piperead.stdout.readlines():                                           # runs inq again after rescan, stores in postdevices list.
            if re.match(r"^\/dev\/sd[a-z]+", i): postdevices.append(i.split()[0])
            else: MyException("No valid devices matched on INQ command output.")
    #HERE COMPARE PREDEVICES AND POSTDEVICES TO SEE WHICH IS NEW, WOULD BE NICE TO ADD THE INQ CAP ROW TO MATCH DISK SIZE WITH USER INPUT

def phycreate(devids):

def main():
    myarguments = sys.argv[1:]
    myopt = myarguments[0]
    devids = myarguments[1:]
    if myopt == "vm":
        vmcreate(devids) #call VM function
    elif myarguments[0] == "physical":
        phycreate(devids) #call physical function
    else:
        MyException("Invalid input/argument on execution")

if __name__ == "__main__":
    main()