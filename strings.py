Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> "Hello AkiraChix"
'Hello AkiraChix'
>>> 'Hello'
'Hello'
>>> "I an an learning python"
'I an an learning python'
>>> "I am learning python"
'I am learning python'
>>> School = "AkiraChix"
>>> school = "Akirachix"
>>> school
'Akirachix'
>>> type (school)
<class 'str'>
>>> "I love " + "Akirachix"
'I love Akirachix'
>>> "1"+ "2"
'12'
>>> "1"*"3"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> "1" * "3"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> "ha" *10
'hahahahahahahahahaha'
>>> "1"*3
'111'
>>> "ha" * "ha"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> print("I love Akirachix")
I love Akirachix
>>> print("Akirachix","is","a","good","school")
Akirachix is a good school
>>> print(2**2, "must be 4")
4 must be 4
>>> x =  "cat"
>>> y = "dog"
>>> print(F"{y} is better than{x}")
dog is better thancat
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> name = "Winfrida Kemunto"
>>> balance 10000000
  File "<stdin>", line 1
    balance 10000000
            ^
SyntaxError: invalid syntax
>>> name = "Winfrida Kemunto"
>>> balance = 100000
>>> print(F"Hello{name}, your current balance is {100000}")
HelloWinfrida Kemunto, your current balance is 100000
>>> print("Hello\b Akirachix")
Hell Akirachix
>>> print("Hello \n Akirachix")
Hello 
 Akirachix
>>> print(Hello \r Akirachix)
  File "<stdin>", line 1
    print(Hello \r Akirachix)
                            ^
SyntaxError: unexpected character after line continuation character
>>> print("Hello \r Akirachix")
 Akirachix
>>> print("Hello \t Akirachix")
Hello 	 Akirachix
>>> print("hello \v Akirachix")
hello 
       Akirachix
>>> print("a\ab")
ab
>>> print(a\a b)
  File "<stdin>", line 1
    print(a\a b)
               ^
SyntaxError: unexpected character after line continuation character
>>> print("a\a b")
a b
>>> len("Akirachix")
9
>>> len("Today is Friday")
15
>>> "a" in "Akirachix"
True
>>> "z" in "Akirachix"
False
>>> "a" not in "Akirachix"
False
>>> "z" not in "Akirachix"
True
>>> s = "Akirachix"
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> x = 10
>>> dir(x)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> s.upper()
'AKIRACHIX'
>>> s.lower()
'akirachix'
>>> s.title()
'Akirachix'
>>> x = "I am a student"
>>> x
'I am a student'
>>> x.title()
'I Am A Student'
>>> x.capitalize()
'I am a student'
>>> s.count("a")
1
>>> s.count("b")
0
>>> s.replace("a , b")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: replace expected at least 2 arguments, got 1
>>> s.replace("a,b")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: replace expected at least 2 arguments, got 1
>>> s.replace("a","b")
'Akirbchix'
>>> z = s.replace("a","b")
>>> z=s.replace("a","b")
>>> x = 10
>>> x +=10
>>> x
20
>>> s.endswith("x")
True
>>> s.endswith("z")
False
>>> s.startswith("A")
True
>>> s.startswith("a")
False
>>> s.islower()
False
>>> s.lower()
'akirachix'
>>> "hello".islower()
True
>>> x.lower()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'lower'
>>> s.isupper()
False
>>> x.isupper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'isupper'
>>> "HELLO".isupper
<built-in method isupper of str object at 0x7facfff6d930>
>>> "HELLO".isupper()
True
>>> s.isnumeric()
False
>>> "20".isnumeric
<built-in method isnumeric of str object at 0x7facff3b5930>
>>> "20 yens".isnumeric()
False
>>> "20".isnumeric()
True
>>> s.isalpha()
True
>>> "20".isalpha()
False
>>> "20 yens".isalpha()
False
>>> s.isalnum()
True
>>> "20".isalnum()
True
>>> "20 years".isalnum()
False
>>> s.isdigit()
False
>>> "20".isdigit()
True
>>> "20 years".isdigit()
False
>>> s.index("A")
0
>>> s.index("x")
8
>>> s.index("a")
4
>>> s.index("z")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> s.find("A")
0
>>> s.find("a")
4
>>> s.find("x")
8
>>> s.find("z")
-1
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
>>> 

