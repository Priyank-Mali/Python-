# Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. 
# Sample data: {'1': ['a','b'], '2': ['c','d']} Expected Output: ac ad bc bd 

my_dict = {
    '1':['a','b'],
    '2':['c','d']
}

emp_list = []

for key,value in my_dict.items():
    for i in value:
        for j in range(0,2):
            if i not in emp_list:
                emp_list.append((my_dict['1'][j])+my_dict['2'][j``])
print(emp_list)