"""
Take a number as string input from the user, then convert it to:
Integer
Float
Complex number
Print each converted value with its type.
"""
num=input("Enter a number:")
print("Integer:",int(num),type(int(num)))
print("Float:",float(num),type(float(num)))
print("Complex Number:",complex(num),type(complex(num)))