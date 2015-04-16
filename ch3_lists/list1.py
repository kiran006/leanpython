#!/usr/bin/pyithon

# accessing variable, l1,l2....
l1=['ran','kumar','lean']
l2=[9,8,6,4,'hari','sri','bala']
 

# select l1,l2...

 l1
[1, 2, 4, 6, 'kiran', 'kumar', 'lean']
 l2
[9, 8, 6, 4, 'hari', 'sri', 'bala']

#fine length of l1,l2...
 len(l1)
7
 len(l2)
7

#concatenation of l1 and l2.. 
 l1+l2
[1, 2, 4, 6, 'kiran', 'kumar', 'lean', 9, 8, 6, 4, 'hari', 'sri', 'bala']


#sliecing l1...
 l1[0:5]
[1, 2, 4, 6, 'kiran']
 l1[0:-2]
[1, 2, 4, 6, 'kiran']
 l1[0:-1]
[1, 2, 4, 6, 'kiran', 'kumar']
 l1[0:-3]
[1, 2, 4, 6]

#comparision l1, l2 
 cmp(l1,l2)
-1

# finding maximun of l1 and l2
 max(l1)
'lean'
 max(l2)
'sri'
 
# appending hello to l1
l1.append('hello')
 l1
[1, 2, 4, 6, 'kiran', 'kumar', 'lean', 'hello']


