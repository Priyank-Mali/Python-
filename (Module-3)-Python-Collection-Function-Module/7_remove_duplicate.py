my_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

emp_list = []
for i in range(0,len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[i] not in emp_list:
            emp_list.append(my_list[i])
            if my_list[i]!=my_list[j]:
                if my_list[j] not in emp_list:
                    emp_list.append(my_list[j])
print(emp_list)

