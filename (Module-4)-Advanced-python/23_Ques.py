# •	How to Define a Class in Python? What Is Self? Give An Example Of A Python Class 

"""
syntax: 

class class_name:
    # class variables
    # class method

class_name()
"""

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def per_info(self):
        return f"Hello {self.name} your age is {self.age}"

per1 = person("priyank",99)
print(per1.per_info())