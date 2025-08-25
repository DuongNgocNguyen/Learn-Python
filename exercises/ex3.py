"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time:
2014-07-05 14:34:14
"""
# datetime
# time

# Cách 1:
import datetime

now = datetime.datetime.now()
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# Cách 2:
from datetime import datetime as dt # as là từ khóa

now = dt.now()
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))