#!/usr/bin/python

file=open("/etc/passwd")

file.readlines()

file.seek(0)

list=file.readlines()


for i in range(0,(len(list))):
    print i+1, list[0].split(":",5)
    print "rootuser,passwd,uid,gid,u_info,path"