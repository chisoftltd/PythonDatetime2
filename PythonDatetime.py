# Python Datetime
import os
import datetime

os.system("cls")
a = datetime.datetime.now()
print(a)
print()
print(a.year)
print()
print(a.strftime("%A"))
print()
print(a.day)
print()
print(a.weekday())
print()

print(a.strftime("%B"))
print()
print(a.strftime("%Y"))
print()
print(a.strftime("%M"))
print()
print(a.strftime("%G"))
print()
print(a.strftime("%X"))

b = datetime.datetime(2021, 2, 23)
print(b)
print()
print(b.strftime("%B"))
print()
print(b.strftime("%Y"))
print()
print(b.strftime("%M"))
print()
print(b.strftime("%G"))
print()
print(b.strftime("%X"))