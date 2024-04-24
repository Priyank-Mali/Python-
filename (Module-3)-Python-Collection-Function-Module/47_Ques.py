# Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string. 
# Sample string: 'w3resource' Expected output: 
# {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} 

my_str = 'w3resource'

emp_dict = {}

for i in my_str:
    if i in emp_dict:
        emp_dict[i] = emp_dict[i] + 1
    else:
        emp_dict[i] = 1

print(emp_dict)