# class BankAccount:
#     def __init__(self,owner_name,bank_balance,account_type):
#         self.owner_name = owner_name
#         self.__bank_balance = bank_balance  #private
#         self._account_type = account_type


# # to get the private attribute

#     @property
#     def bank_balance(self):
#         return self.__bank_balance

#     @property
#     def account_type(self):
#         return self._account_type
    

# # To update the private attribute
#     @bank_balance.setter
#     def bank_balance(self,deposite_amt):
#         if deposite_amt <= 0:
#             raise "Deposite amount cannot be Zero ot a negative value"
#         self.__bank_balance = self.__bank_balance + deposite_amt

#     @account_type.setter
#     def account_type(self,account_type): 
#            if account_type == "" :
#                raise ValueError("Account type cannot be empty")
#            self.account_type = account_type

    
# bank = BankAccount("Arjun",100,"savings")


# print(bank.bank_balance)


# # syntax : class.setter function = new function
# bank.bank_balance = 123
# print(bank.bank_balance)
# print(bank.account_type)





print("********************************************************")


class Employee:
    def __init__(self,employee_name,department,salary):  
        self.employee_name = employee_name
        self._department = department
        self.__salary = salary

    @property
    def salary (self):
        return self.__salary

    @salary.setter
    def salary (self,value):
        if value <= 0:
            print("salary cannot be negative")
        self.__salary = value

class Manager(Employee):
    def display_detailse(self):
        print("emplooyee_name:",self.employee_name)
        print("Department:",self._department)

m = Manager("arjun","bcs",2334)

m.salary= 4000
m.display_detailse()

print("Current salary",m.salary)

m.salary = 123
 
print("updated salary",m.salary)

print("***************************************************************************")

class Vehicle():
    def __init__(self,vechile_name,rental_type,rental_price):
        self.vechile_name = vechile_name
        self._rental_type = rental_type
        self.__rental_price = rental_price

    @property
    def rental_price(self,):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self,value):
        if value <= 0:
            raise ValueError("Rental price cannot be negative")

        self.__rental_price = value 

    def display_details(self):
        print("vehile name:",self.vehile_name)
        print("rental type:",self.rental_price)



class Car(Vehicle):
    def calculate_rent(self,days):
        return self.rental_price * days
    
    def display_details(self):
            super().display_details()
            print("Rental Price:",self.rental_price)

    def display_details(self):
        print("vehicle name:",self.vechile_name)
        print("Rental Type:",self.rental_type)
        print("Rental Price:",self.rental_price)

    

class Bike(Vehicle):
    def calculate_rent(self,days):
        return self.rental_price * days

    def display_details(self):
        print(" bike details ")
        print("vehicle name",self.vechile_name)
        print("rental type",self.rental_type)
        print("Rental Price",self.rental_price)



car = Car("toyato","4wheel",2000)
bike = Bike("kawasaki","two",800)

print("car rent for 3 days:",car.calculate_rent (3))
print("bike rent for 3 days:",bike.calculate_rent (3))
# Car.display_details()
# print("car rental price:",Car)

# print("car rental price:",car.rental_price)
Car.rental_price = 2500
print("updated car rental price:",car.rental_price)


# Car.display_details()