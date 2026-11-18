# student1_name = 'Arjun_k_ajin'
# student1_Age = 24

# student2_name = 'ajin'
# student2_Age = 14

# student3_name = 'Ajith'
# student3_Age = 27

# student4_name = 'Amal'
# student4_Age = 24

# student5_name = 'Athul'
# student5_Age = 24

# print(student1_name,student1_Age,'\n',student2_name,student2_Age,'\n',student3_name,student3_Age,'\n',student4_name,student4_Age,'\n',student5_name,student5_Age)


# print('************************************************************************************************************')


# class Student:         # class
#     def __init__(self, name, Age):
#         self.name = name
#         self.Age = Age

# student1 = Student("John",12)             # object
# student2 = Student("Arjun",22)            # object
# student3 = Student("Ajith",32)            # object
# student4 = Student("Abhinav",24)          # object
# student5 = Student("jerin",32)
# print(student1.name, student1.Age,'\n',student2.name, student2.Age,'\n',student3.name, student3.Age,'\n',student4.name, student4.Age,'\n',student5.name, student5.Age,)

# print('************************************************************************************************************')

# class Book:         # class
#     def __init__(self, Name, Author,Page_no,year):
#         self.Name = Name
#         self.Author = Author
#         self.Page_no = Page_no
#         self.year = year

# Book1 = Book('Aadhu jivitham','beshir',101,1999)
# Book2 = Book('Hero','jacob',345,2004)
# Book3 = Book('War and Peace','Leo Tolstoy',111,1987)
# Book4 = Book('The Guide ','R.K. Narayan',85,2013)
# Book5 = Book('Gitanjali','Rabindranath Tagore',859,1997)

# print(Book1.Name, Book1.Author, Book1.Page_no, Book1.year)
# print(Book2.Name, Book2.Author, Book2.Page_no, Book2.year)
# print(Book3.Name, Book3.Author, Book3.Page_no, Book3.year)
# print(Book4.Name, Book4.Author, Book4.Page_no, Book4.year)
# print(Book5.Name, Book5.Author, Book5.Page_no, Book5.year)


# print('************************************************************************************************************')

# class Employee:         # class
#     age = 10                                                                 # class attribute
#     def __init__(self, name,salary, id_no,job_role,joining_date):
#         self.Name = name                                                    # Attribute are two type 1.( instent attribute ).  2. class attribute
#         self.salary = salary
#         self.id_no = id_no
#         self.job_role = job_role
#         self.joining_date = joining_date

#     def display_details(self):
#         print(self.Name,self.salary,self.id_no,self.job_role,self.joining_date)


# # using function call

# Employee1 = Employee('Arjun',170000,22,'manager','12-1-2010')
# Employee2 = Employee('Athul',11000,232,'hr','1-2-2019')
# Employee3 = Employee('Amal',1500,256,'assistant','11-10-2025')
# Employee4 = Employee('Abhinav',13000,22,'engineer','12-2-2025')
# Employee5 = Employee('Ajith',34000,2345,'junior assistant','16-9-2026')
# Employee1.display_details()
# Employee2.display_details()
# Employee3.display_details()
# Employee4.display_details()
# Employee5.display_details()

# print("************************************************************************************************************")

# # Accesing the class attribute ( class attribute value doesn't change     ///     store commonly used values  )
# print(Employee.age)


# print('************************************************************************************************************')


# Employee1 = Employee('Arjun',170000,22,'manager','12-1-2010')
# Employee2 = Employee('Athul',11000,232,'hr','1-2-2019')
# Employee3 = Employee('Amal',1500,256,'assistant','11-10-2025')
# Employee4 = Employee('Abhinav',13000,22,'engineer','12-2-2025')
# Employee5 = Employee('Ajith',34000,2345,'junior assistant','16-9-2026')

# print(Employee1.Name,Employee1.salary,Employee1.id_no,Employee1.job_role,Employee1.joining_date)
# print(Employee2.Name,Employee2.salary,Employee2.id_no,Employee2.job_role,Employee2.joining_date)
# print(Employee3.Name,Employee3.salary,Employee3.id_no,Employee3.job_role,Employee3.joining_date)
# print(Employee4.Name,Employee4.salary,Employee4.id_no,Employee4.job_role,Employee4.joining_date)
# print(Employee5.Name,Employee5.salary,Employee5.id_no,Employee5.job_role,Employee5.joining_date)


# #**************************************************************************************************

# print("************************************************************************************")

# class Student: 
#     count = 0        # class
#     def __init__(self, Name,age,height):              
#         self.Name = Name
#         self.Age = age
#         self.height = height

#         #Increment count by 1, When the class has intitialized
#         Student.count = Student.count + 1 


#     def display_count(self):
#         print(Student.count)

# Student1 = Student('Arjun',22,'178.7')
# Student2 = Student('Athul',19,'156')
# Student3 = Student('Ayana',21,'173')
# Student3.display_count()

# #***********************************************************************************************
# #*****************************************Inheritance*******************************************
# print('*****************************************************************************************')

# class Animal:
#     def __init__(self,has_leg):
#         self.has_leg = has_leg

# class Dog(Animal):
#     pass
# dog = Dog(has_leg= 'yes')

# print("The dog has 4 legs",dog.has_leg)



# # create a four classes


# class Animal:
#     def __init__(self,sleep,eat):
#         self.sleep = sleep
#         self.eat = eat

# class Dog(Animal):
#     def __init__(self,sleep,eat):
#         super().__init__(sleep,eat)

#     def bark(self):
#         return "wooff"


# class Cat(Animal):
#     def __init__(self, sleep, eat):
#         super().__init__(sleep, eat)
#         self.speak = "Meow"

   
    
# # Dog = Dog(sleep='yes',eat='yes')
# # Cat = Cat(sleep='yes',eat='yes')

# # print(Dog.speak,Dog.sleep,Dog.eat)
# # print(Cat.speak,Cat.sleep,Cat.eat)



# print("*************************************************************************")

# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         pass
#     def Eat(self):
#         print("the animal is eating")

# class Dog(Animal):
#     def bark(self):
#         return"woof"

# class Cat(Animal):
#     def meow(self):
#         return"meow"

# dog = Dog(name="yes",age="yes")

# cat = Cat(name="yes",age="yes")

# print(dog.name,dog.age,dog.bark())
# print(cat.name,cat.age,cat.meow())




# #*******************************************************************************************************
# print("*********************************************************************************************")






# class person():
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age

#     def display (self):
#         print("Name:", self.name)
#         print("Age:",self.age)


# class student(person):
#     def __init__(self,name,age,course):
#         super().__init__(name,age)
#         self.course = course

#     def show_course(self):
#         print("course:",self.course)

# Student = student("arjun",22,"Data Science") 

# Student.display()
# Student.show_course()

# print("*******************************************************************************")
# #************************************************************************************
# #************************************Abstract Class**********************************


# from abc import ABC, abstractmethod

# class Bank(ABC):
#     @abstractmethod
#     def deposite(self):
#         pass
#     @abstractmethod
#     def loan(self):
#         pass

# class SBI(Bank):
#     def deposite(self):
#         print("Deposite is executed")
        
#     def loan(self):
#         print("Loan is applied")

#     def profit(self):
#         print("profit")
# sbi = SBI()
# sbi.deposite()
# sbi.loan()
# sbi.profit()


#create an abstract parent class called shape
#import ABC and abstract method from the abc module
# create a class called shapes that inherites from ABC
#define an abstrct method called area() inside shape.
#create two child classes: rectangle , circle
# both child classes must inherited from shape
#implement the area()method in both chil classes


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth


    def area(self):
        print( self.length * self.breadth)

class Circle(Shape):
    def __init__(self,radius):
         self.radius = radius

    def area(self):
        print( "area of circle is",3.14 * self.radius ** 2)
            
r = rectangle(5,6)
r.area()
c = Circle(3)
c.area()



























