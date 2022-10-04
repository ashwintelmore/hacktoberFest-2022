"""
class Employee:
    def __init__(self, name, id):
        self.id = id;
        self.name = name;
    
    def display(self):
        return f"The name of empolyee is {self.name} and his/her id is {self.id}";

e1 = Employee("haridas", 2);
print(e1.display(), "\t", getattr(e1, "name", "id"), "\t", hasattr(e1, "name"), "\t", hasattr(e1, "id") , "\t", hasattr(e1, "lol"));

# updating/setting attribute
setattr(e1, "id", 73);
print(getattr(e1, "id"));
print(e1.display());

# Deleting a Attribute
delattr(e1, "name");
print(hasattr(e1, "name"));

"""
"""
    for our convenience in python we have getattr, setattr, hasattr, delattr methods for attributes

    this == self
"""
"""
class Student:
    def __init__(self):
        print("yaah, i m constructer");

class Shop:
    def __init__(self, shopname, shopid, shopPhoneNumber):
        self.shopname = shopname;
        self.shopid = shopid;
        self.shopPhone = shopPhoneNumber

    def display(self):
        print(f"Shop name is {self.shopname} and shop id is {self.shopid}, shop phone number is {self.shopPhone}");

s = Student();
dukan = Shop("Haridas shop", 14, 987654321);
dukan.display();
"""


class Avg:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def calcu(self):
        return int((self.a + self.b + self.c)/3)
    
    @staticmethod
    def evenOrOdd(c, d):
        return (c+d) % 2 == 0;

a = Avg(1, 2, 3);
# print(a.calcu());

if (a.evenOrOdd(4,4)):
    print("Yah, I m even");
else: 
    print("naah, i m odd")
