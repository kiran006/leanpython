 _Helper in module site object:

class _Helper(__builtin__.object)
 |  Define the builtin 'help'.
 |  This is a wrapper around pydoc.help (with a twist).
 |  
 |  Methods defined here:
 |  
 |  __call__(self, *args, **kwds)
 |  
 |  __repr__(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
...skipping...
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> help(dir)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/site.py", line 470, in __call__
    return pydoc.help(*args, **kwds)
  File "/usr/lib/python2.7/pydoc.py", line 1781, in __call__
    self.help(request)
  File "/usr/lib/python2.7/pydoc.py", line 1828, in help
    else: doc(request, 'Help on %s:')
  File "/usr/lib/python2.7/pydoc.py", line 1565, in doc
    pager(render_doc(thing, title, forceload))
  File "/usr/lib/python2.7/pydoc.py", line 1370, in pager
    pager(text)
  File "/usr/lib/python2.7/pydoc.py", line 1390, in <lambda>
    return lambda text: pipepager(text, 'less')
  File "/usr/lib/python2.7/pydoc.py", line 1412, in pipepager
    pipe.close()
KeyboardInterrupt
>>> 
