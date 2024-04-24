# Write a Python script to sort (ascending and descending) a dictionary by value. 

my_dict = {
    "priyank":99,
    "rahul":90,
    "kalam":81
}

# emp_list = sorted(my_dict.items(),key = lambda x : x[1])

# print(emp_list)

emp_list = sorted(my_dict.values())
print(emp_list)