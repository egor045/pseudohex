# pseudohex
Traveller/Cepheus System pseudohex module

This Python module implements "pseudohex" as used in the Traveller role-playing games and the Open Game License Cepheus System. 

Pseudohex data is an extension of classic hexdecimal notation and was originally used as a compact way to represent numerical values in the original 1977 Traveller RPG. It has remained in use through all Traveller versions since then.

Pseudohex represents numbers greater than 9 as A-Z, omitting I and O for clarity. 

From a Python perspective, pseudohex stores numerical data supplied as either str (single character in the range 0-9A-Z) 
or int in the range 0-33. Attempts to use values outside these ranges will result in a ValueError.

Examples:
```
>>> from pseudohex.pseudohex import Pseudohex
>>> p = Pseudohex(11)
>>> int(p)
11
>>> str(p)
'B'
>>>
p = Pseudohex()
>>> int(p)
0
>>> str(p)
'0'
>>> 
```
Comparisons:
```
>>> p == 11
True
>>> p == 'C'
False
>>> p < 'M'
True
>>> p < 3
False
>>> p > 3
True
```

Invalid data:
```
>>> p = Pseudohex('@')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/pseudohex/pseudohex.py", line 17, in __init__
    raise ValueError('Invalid value {}'.format(value))
ValueError: Invalid value @
>>> 
```
