# class Circule:
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 *(self.radius ** 2)

#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# c1 = Circule(5)
# print(c1.area())
# print(c1.perimeter())

# class Employee:
#     def __init__(self,role,dipartment,salary):
#         self.role = role
#         self.dipartment = dipartment
#         self.salary = salary    

#     def show_details(self):
#         print(f"Role: {self.role}")
#         print(f"Dipartment: {self.dipartment}")
#         print(f"Salary: {self.salary}")

# class Engineer(Employee):
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer","IT",50000)

# eng1 = Engineer("John", 30)
# eng1.show_details()
# print(f"Name: {eng1.name}")

# class Order:
#     def __init__(self,item,price):
#         self.item = item
#         self.price = price

#     def __gt__(self,other):
#         if self.price > other.price:
#             return True
#         else:
#             return False

# ord1 = Order("Laptop", 1000)
# ord2 = Order("Phone", 2000)

# print(ord1 < ord2)  