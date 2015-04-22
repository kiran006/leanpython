#!/usr/bin/python


open("file.txt","r+")
f=open("file.txt","r+")
f.readlines()
list=f.readlines()

for i in range(0,(len(list))):
    print i

