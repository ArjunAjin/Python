
# 1. Ask the user to enter a number. Write a program to check whether the number is positive  or negative
# num = input('enter a number:')
# num = int(num)

# if num>0:
#     print('The number is positive')
# else:
#     if num<0:
#         print('The number is negative')


# 2. Ask the user to enter their age. Check whether they are eligible to vote. Consider 18 as the minimum voting age. 

# age = input('enter your age:')
# age = int(age)

# if age >= 18:
#     print('you are eligible to vote')
# else:
#     print('your are not eligible to vote')

#3 .Ask the user to enter an integer. Check whether the number is even or odd. 
 
# num1=input('enter an integer value')
# num1 = int(num1)

# if num1 % 2 == 0:
#     print('The number is even' )
# else:
#     print('The number is odd')


#4. Create a program with a predefined password stored in a variable. Ask the user to enter a password. Display: 
# ●  "Access Granted" if the password matches. 
# ●  "Access Denied" otherwise. 

# password = 'python1'
# user_password = input("Enter your password: ")

# if user_password == password:
#     print('Access Granted')
# else:
#     print('Access Denied')

# 5.Ask the user to enter two numbers. Display the greater number. If both numbers are equal, display "Both numbers are equal". 

# number1 = int(input('enter the first number:'))
# number2= int(input('enter the second number:'))

# if number1 > number2 :
#     print('The gratest number is' ,number1)
# else:
#     if number2 > number1:
#         print('The greatest number is',number2)
#     else:
#         print('Both are equal')


#6. Ask the user to enter their marks out of 100.
 
# marks = int(input('Enter your marks out of 100:'))

# if marks >= 90 and marks <=100:
#     print('Grade A')
# elif marks >=80:
#     print('Grade B')
# elif marks >=70:
#     print('Grade C')
# elif marks >=60:
#     print('Grade D')
# elif marks >=50:
#     print('Grade E')
# elif marks <=49:
#     print('Grade F')    

7 # Ask the user to enter three numbers. Write a program to identify and display the largest number.

# number1 = int(input('Enter first number:')) 
# number2 = int(input('Enter Second number:'))
# number3 = int(input('Enter third number:'))

# if number1 >= number2 and number1 >= number3:
#     print('The largest number is :',number1)
# elif number2 >= number1 and number2 >= number3:
#     print('The largest number is :',number2)
# else:
#     print('The largest number is :',number3)

#8. Ask the user to enter a traffic light colour. Display the corresponding instruction: 
# colour =(input('Enter a traffic light colour:'))


# if colour == 'red':
#     print('STOP')
# elif colour == 'Yellow':
#     print('READY')
# elif colour == 'Green':
#     print('GO')
# else:
#     print('Invalid traffic light colour ')

# 10. Create a simple ATM withdrawal program. 
# balance = 10000

# amount = int(input('Enter the withdrawal amount: '))

# if amount <= 0:
#     print('Please enter a positive amount')

# elif amount % 100 != 0:
#     print('Withdrawal amount must be a multiple of 100')

# elif amount > balance:
#     print('Insufficient balance')

# else:
#     balance = balance - amount
#     print('Withdrawal successful')
#     print('Remaining balance:', balance)
# units = int(input("Enter the electricity units consumed: "))

# if units <= 100:
#     bill = units * 2

# elif units <= 200:
#     bill = (100 * 2) + (units - 100) * 3

# elif units <= 300:
#     bill = (100 * 2) + (100 * 3) + (units - 200) * 5

# else:
#     bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

# print("Total electricity bill: ₹", bill)

#9.Create a program that accepts the number of electricity units consumed. Calculate the bill using the following rates: 
# Unit = int(input('Enter electricity unit consumed'))

# if Unit <= 100:
#     bill = Unit * 2

# elif Unit <= 200:
#     bill = ( 100*2 ) + (Unit - 100)* 3

# elif Unit <= 300:
#     bill = ( 100 * 2 ) + (100 * 3) + (Unit - 200) * 5
# else:
#      bill = ( 100 * 2 ) + (100 * 3) + (100 * 4) + (Unit - 300) * 7

# print("Total electricity bill:", bill)


print('*************************************************')
#Logical operators in control flow statement

Age = int(input('enter your age : '))
valid_id = int(input('Do you have a valid id (Y/N)'))

if (valid_id == 'y'):
    valid_id == True
else:
   valid_id == False

verify the eligibilty to vote
print('we are checking your eligibility')

if (Age >= 18):
    if(valid_id): 
        print('ou are eligible to vote')
    else:
        print('you are not eligible to vote')
        print('you need a valid_id card to eligible ')
else:
    print('you are not eligible to vote')
