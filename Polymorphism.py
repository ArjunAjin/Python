class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
            print(f"hi my :name:{self.name}," 
                f"age:{self.age} ")

class Employee(Person):
    def __init__(self, name, age,employe_id,salary,joining_date):
        super().__init__(name,age)
        self.employe_id = employe_id
        self.salary = salary
        self.joining_date = joining_date

    def display(self):
            print(f"hi i am employee:name:{self.name}," f"age:{self.age} my id:{self.employe_id} my salary is {self.salary}")

class Father(Person):
    def __init__(self, name, age,no_of_child):
        super().__init__(name, age)
        self.no_of_child = no_of_child

    def display(self):
        print(f"hi my :name:{self.name}," 
        f"age:{self.age} no of child{self.no_of_child} ")

class Son(Person):
    def __init__(self, name, age,father_name):
        super().__init__(name, age)
        self.father_name = father_name

    def display(self):
        print(f"hi my :name:{self.name}," 
        f"age:{self.age} my father name id{self.father_name} ")


class Husband(Person):
    def __init__(self, name, age,wife_name,date_of_marrage):
        super().__init__(name, age)
        self.wife_name = wife_name
        self.date_of_marrage = date_of_marrage

    def display(self):
            print(f"hi my :name:{self.name}," 
            f"age:{self.age} my name is{self.wife_name} our wedding date is {self.date_of_marrage}")
              




# person = Person("arjun",22)
# # emp = Employee("arjun",22,132,56000,'12/01/2025')
# # father = Father("arjun",22,1)
# # son = Son("arjun",22,"Ajin")
# # hus = Husband("arjun",22,'achu',"12/12/2012")
# person.display_Employee(Person)


print("*************************************************************************")


# create a parent class employee
# create a method called calculate_salary
# print calulate employe salary 
#calculate 3 child classes:
class Employee:
    def calculate_salary(self):
        salary = 25000
        print("Employee Salary:", salary)

emp = Employee()
emp.calculate_salary()


#FulltimeEmploye
# inherit from employee
#override calcilate_salary()
#print"full time employee recives a fixed monthly salary


# Child class
class FulltimeEmployee(Employee):
    def calculate_salary(self):
        print("Full time employee receives a fixed monthly salary")


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("Part time employee salary is based on workin hours")


class Freelancer(Employee):
     def calculate_salary(self):
          print("Part time employee salary is based completing projects")

emp = PartTimeEmployee()
full = FulltimeEmployee()
part = PartTimeEmployee()

emp.calculate_salary()
full.calculate_salary()
part.calculate_salary()




print("***********************************************************************************")


from abc import ABC, abstractmethod

class BankAccount():
    @abstractmethod
    def calculate_intreast(self):
        pass

    def __init__(self,account_holder,account_type,__balance):
        self.account_holder = account_holder
        self._account_type = account_type
        self.__balance = __balance
    @property
    def balance (self):
         return self.__balance
    
    @property
    def account_type (self):
        return self.account_type

    @balance.setter
    def balance(self,increment):
         if increment >= 0:
            self.__balance= increment
         else:
            print("Balance amount cannot be zero")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, "Savings", balance)
       
    def calculate_interest(self):
        return self.balance * 0.05  

class CurrentAcount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, "Current", balance)

    def calculate_interest(self):
        return self.balance * 0.02 


    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposit successful: Rs.{amount}")
        else:
            print("Invalid deposit amount")

    @property
    def balance(self):
         return self.__balance
    
    def withdraw(self, amount):
            if 0 < amount <= self.balance:
                self.balance = self.balance - amount
                print(f"Withdrawal successful: Rs.{amount}")
            else:
                print("Insufficient balance")

    def display_details(self):
            print("\n" "Account Holder:", self.account_holder)
            print("Account Type:", self._account_type)
            print("Balance: Rs.", self.balance, sep="")



     
    
            









































from abc import ABC, abstractmethod

# Task 1: Abstract Parent Class
class BankAccount(ABC):

    def __init__(self, account_holder, account_type, balance):
        self.account_holder = account_holder
        self._account_type = account_type
        self.__balance = 0
        self.balance = balance

    
    @property
    def balance(self):
        return self.__balance

    
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

    
    @abstractmethod
    def calculate_interest(self):
        pass

    
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposit successful: Rs.{amount}")
        else:
            print("Invalid deposit amount")

    # Withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Withdrawal successful: Rs.{amount}")
        else:
            print("Insufficient balance")

    # Display Details
    def display_details(self):
        print("\nAccount Holder:", self.account_holder)
        print("Account Type:", self._account_type)
        print("Balance: Rs.", self.balance, sep="")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, "Savings", balance)
       
    def calculate_interest(self):
        return self.balance * 0.05  

class CurrentAcount(BankAccount):
    def __init__(self, account_holder, balance=0):
        super().__init__(account_holder, "Current", balance)

    def calculate_interest(self):
        return self.balance * 0.02 













# from abc import ABC, abstractmethod


# class BankAccount(ABC):
#     """Abstract parent class: every account type must implement calculate_interest()."""

#     def __init__(self, account_holder, account_type, balance=0):
#         self.account_holder = account_holder   # public
#         self._account_type = account_type      # protected
#         self.__balance = 0                     # private
#         self.balance = balance                 # goes through the setter (validates)

#     # ---------- Encapsulation: getter and setter ----------
#     @property
#     def balance(self):
#         return self.__balance

#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("Balance cannot be negative.")
#         self.__balance = value

#     # ---------- Abstraction ----------
#     @abstractmethod
#     def calculate_interest(self):
#         """Return the annual interest. Each child class must implement this."""

#     # ---------- Banking operations ----------
#     def deposit(self, amount):
#         if amount <= 0:
#             print("Deposit amount must be greater than zero.")
#             return
#         self.balance = self.balance + amount
#         print(f"Deposit successful: Rs.{amount}")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be greater than zero.")
#         elif amount > self.balance:
#             print("Insufficient balance.")
#         else:
#             self.balance = self.balance - amount
#             print(f"Withdrawal successful: Rs.{amount}")

#     def display_details(self):
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Account Type: {self._account_type}")
#         print(f"Balance: Rs.{self.balance}")


# # ---------- Inheritance ----------
# class SavingsAccount(BankAccount):
#     def __init__(self, account_holder, balance=0):
#         super().__init__(account_holder, "Savings", balance)

#     def calculate_interest(self):
#         return self.balance * 0.05   # 5% annual interest


# class CurrentAccount(BankAccount):
#     def __init__(self, account_holder, balance=0):
#         super().__init__(account_holder, "Current", balance)

#     def calculate_interest(self):
#         return self.balance * 0.02   # 2% annual interest


# # ---------- Testing ----------
# if __name__ == "__main__":
#     # BankAccount cannot be created directly (abstract class)
#     try:
#         BankAccount("Test", "Test", 100)
#     except TypeError as e:
#         print("Cannot create BankAccount directly:", e, "\n")

#     ashbi = SavingsAccount("Ashbi", 10000)
#     rahul = CurrentAccount("Rahul", 20000)

#     ashbi.deposit(5000)
#     ashbi.withdraw(2000)
#     print()
#     rahul.deposit(3000)
#     rahul.withdraw(5000)

#     print("\n---------- ACCOUNT DETAILS ----------\n")
#     ashbi.display_details()
#     print()
#     rahul.display_details()

#     print("\n---------- ANNUAL INTEREST ----------\n")
#     print(f"{ashbi.account_holder}'s Annual Interest: Rs.{ashbi.calculate_interest()}")
#     print(f"{rahul.account_holder}'s Annual Interest: Rs.{rahul.calculate_interest()}")

#     # Extra checks: negative balance is blocked, overdraft is refused
#     print("\n---------- EXTRA CHECKS ----------\n")
#     try:
#         ashbi.balance = -500
#     except ValueError as e:
#         print("Setter blocked negative balance:", e)
#     ashbi.withdraw(1000000)

















































































# # Savings Account
# class SavingsAccount(BankAccount):

#     def __init__(self, account_holder, balance):
#         super().__init__(account_holder, "Savings", balance)

#     def calculate_interest(self):
#         return self.balance * 5 / 100


# # Current Account
# class CurrentAccount(BankAccount):

#     def __init__(self, account_holder, balance):
#         super().__init__(account_holder, "Current", balance)

#     def calculate_interest(self):
#         return self.balance * 2 / 100


# # Create Objects
# ashbi = SavingsAccount("Ashbi", 10000)
# rahul = CurrentAccount("Rahul", 20000)


# # Banking Operations
# ashbi.deposit(5000)
# ashbi.withdraw(2000)

# print()

# rahul.deposit(3000)
# rahul.withdraw(5000)


# # Display Account Details
# print("\n---------- ACCOUNT DETAILS ----------")

# ashbi.display_details()
# rahul.display_details()


# # Calculate Annual Interest
# print("\n---------- ANNUAL INTEREST ----------")

# print(f"\nAshbi's Annual Interest: Rs.{ashbi.calculate_interest()}")
# print(f"Rahul's Annual Interest: Rs.{rahul.calculate_interest()}")









    

