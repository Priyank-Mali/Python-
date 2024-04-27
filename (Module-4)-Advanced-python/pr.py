n = int(input("Enter nu of line you want to read: "))
file = open("pr.txt",'r')
for i in range(n):
    print(file.readline())