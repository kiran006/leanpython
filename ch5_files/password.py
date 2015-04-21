#!/usr/bin/python

pfile = open("/etc/passwd")
print pfile
plist = pfile.readlines()
print plist
for i in range(0,len(plist)):
    print i+1,plist[i].strip()
    