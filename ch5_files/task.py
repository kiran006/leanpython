#!/usr/bin/python

#open a input file.
open("/etc/passwd")
# stored open file in pfile variable.
pfile = open("/etc/passwd")
#print pfile data.
print pfile
#asssign pfile readlines to plist.
plist = pfile.readlines()
#print plist.
print plist
#create for loop.
for i in range(0,len(plist)):
    print i+1,plist[i].strip()
    
