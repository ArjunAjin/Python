# # function adding 2 numbers

# def display_sum(num1,num2):
#     sum = num1+num2
#     print('The Sum of',num1,'and',num2,'is : ',sum)

# # display_sum(22,10)

# # a function will have,
# # 1. function name : mandatory
# # 2. inputs()
# # 3. Body of the function :mandatory
# # 4. Output

# # while we define input variable in the function definition
# # we. are creation new variables with scope within the function

# def display_num():
#     num1 = float(input('Enter a first value:'))
#     num2 = float(input('Enter the second value :'))
#     sum = num1 + num2
#     print('the sum of ',num1 ,'and',num2 ,'is',sum)

# display_num()

# student1 = 'arjun'ex
# student1_age = 22
# student2 = 'arhu'
# student2_age =45

# print(student1,student1_age,'\n',student2,student2_age)
# print("**************************************************************")

# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# student1 = Student('arjun',34)
# student2 = Student('athul',98)      
# print(student1.name,student2.age)


# class Book():
#     def __init__(self,Name, Author,Page_no,year):
#         self.Name = Name
#         self.author= Author
# #         self.page_no = Page_no
# #         self.year = year

# # Book1 = Book('githanjali','rabndhranathaa',345,1999)
# # Book2 = Book('sind','jopal',234,1989)

# # print(Book1.Name,Book1.author,Book1.page_no,Book1.year)
# # print(Book2.Name,Book2.author,Book2.page_no,Book2.year)



# # class Emplooye():
# #     def __init__(self,name,salary,id_no,job_role,joining_date):
# #         self.name = name
# #         self.salary = salary
# #         self.id_no = id_no
# #         self.job_role = job_role
# #         self.joining_date = joining_date

# #     def display_details(self):
# #         print(self.name,self.salary,self.id_no,self.job_role,self.joining_date)


# # Emplooye1 = Emplooye('arjun',23000,34,'manager',2024)
# # Emplooye2 = Emplooye('athul',34000,45,'assistant',2022)
# # Emplooye1.display_details()
# # Emplooye2.display_details()

# # # print(Emplooye1.name,Emplooye1.salary,Emplooye1.id_no,Emplooye1.job_role,Emplooye1.joining_date)
# # # print(Emplooye2.name,Emplooye2.salary,Emplooye2.id_no,Emplooye2.job_role,Emplooye2.joining_date)

# # 

# # class Animal():
# #     def __init__(self,eat,sleep):
# #         self.eat = eat
# #         self.sleep = sleep
    

# # class Dog(Animal):
# #     def __init__(self,eat,sleep):
# #         super().__init__(eat,sleep)

# #     def bark(self):
# #        return"woof"

# # class Cat(Animal):
# #     def __init__(self, eat, sleep):
# #         super().__init__(eat, sleep)
# #     def meow(self):
# #         self.speak = 'meaow'

# # dog= Dog(eat='yes',sleep='yes')
# # cat= Cat(eat='yes',sleep='yes')

# # print(Dog.sleep, Dog.eat)
# # print(Cat.eat,Cat.sleep,Cat.speak())


# # #create a parent class called person
# # #add the following attributes :name,age
# # #create a constructor (__int__) to initialise these attribute
# # #create a method called display() that prints the name and age
# # # create a child class called student that inherits from person
# # # add one additional; attribute to the student class: course
# # #create a method called show_course() that prints the students course

# # class person():
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
        

# # class Emplyee:
# #     def __init__(self,employee_name,department,salary):
# #         self.employee_name = employee_name
# #         self._department = department
# #         self.__salary = salary

# #     @property
# #     def salary (self):
# #         return self.__salary


# #     @salary.setter
# #     def salary (self.salary):


# # from abc import ABC, abstractmethod
# # class BankAccount:
# #     def __init__(self,account_holder,account_type,balance):
# #         self.account_holder = account_holder
# #         self._account_type = account_type
# #         self.__balance = balance

# #     @property
# #     def balance(self):
# #         return self.__balance

# #     @balance.setter
# #     def balance (self,amount):
# #         if amount < 0:
# #              raise ValueError('negative value cannot be printed')
# #         self.__balance = amount

    
# # class SavingAccount(BankAccount):
# #     def








# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:",self.name)
#         print("Age",self.age)


# class Student(Person):
#     def __init__(self, name, age,course):
#         super().__init__(name, age)
#         self.course = course



#     def show_course(self):
#         print("course :",self.course)

# student = Student("arjun",22,"bca")
# student.display()
# student.show_course()


# print("**************************************************************************")


# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary

#     def display_details(self):
#         print("Name :",self.name)
#         print("salary :",self.salary)

# class Manager(Employee):
#     def __init__(self, name, salary,department):
#         super().__init__(name, salary)
#         self.department = department

#     def display (self):
#         print("name:",self.name)
#         print("salary :",self.salary)
#         print("Department :",self.department)

# manger = Manager("Arjun",23000,"computer")


# manger.display()




# print("**************************************************************************")

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposite(self,amount):
#         self.money = amount
#         print("money is deposited",self.money)

#     def withdraw(self,amount):
#         if amount <=  0:
#             print("withdrwan",self.amount)
#         else:
#             print("insufficent balance",self.amount)
#         self.withdraw = amount


#     def check_balance(self):
#         print("current balance:",self.check_balance)
    

# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, balance,interest_rate):
#         super().__init__(account_number, balance)
#         self.interest_rate = interest_rate

#     def display_details(self):
#         print("Account number",self.account_number)
#         print("Account Balance:",self.balance)
#         print("intrest rate:", self.interest_rate)

# account =  SavingsAccount(34543,2345,25)

# account.display_details()


# account.deposite(2000)
# account.withdraw(500)
# account. check_balance()

print("***************************************************************")


# from abc import ABC, abstractmethod

# class Product:
#    def __init__(self,product_name,category,price):
#        self.product_name = product_name
#        self._caregory = category
#        self.__price = price
       
       
#     @property
#     def price (self):
#        return self.__price

#     @price.setter
#     def price(self,new_price):
#         if new_price >= 0:
#            self.__price = new_price
#         else:
#            print("Price Cannot Be NNegative")


#     @abstractmethod
   

       
    # Develop a simple Employee Salary Management System using Python OOP concepts. 
# 1. Create an abstract class named Employee. 
# ○ Include an abstract method named calculate_salary(). 
# ○ Include a method named display_details(). 
# 2. Encapsulate the employee's basic salary using a private attribute. 
# ○ Provide a method to retrieve the basic salary. 
# 3. Create two child classes: 
# ○ PermanentEmployee 
# ○ ContractEmployee 
# 4. Implement calculate_salary() differently: 
# ○ Permanent Employee: Basic Salary + 20% allowance. 
# ○ Contract Employee: Basic Salary + 5% allowance. 
# 5. Create objects of both employee types and demonstrate: 
# ○ Displaying employee details. 
# ○ Calculating and displaying their salaries


from abc import ABC,abstractmethod

class Emplooye:
    def __init__(self,name,employe_id,salary):
        self.name = name
        self.employee_id = employe_id
        self.__salary = salary


    def get_rental_price(self):
        return self.salary

    @abstractmethod
    def calculate_salary(self):
        pass


    def display_details(self):
        print("Name:",self.name)
        print("employe id:",self.employee_id)
        print("salary:",self.__salary)
        print("")

class PermanentEmployee(Emplooye):
    employee_type = "Permanent"
    def calculate_salary(self):
        return self.get_rental_price() + 0.25

class ContractEmployee(Emplooye):
    employee_type = "Contract"
    def calculate_salary(self):
        return self.calculate_salary() +0.5


emp1 = PermanentEmployee("arjun",234,"45,00")
emp2 = ContractEmployee("athul",345,"33,00")

emp1.display_details()
emp2.display_details()
