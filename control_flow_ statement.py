#**********************Conditional statement*************************
#************Checking whether a number is bigger than 50************* 
#********************************************************************
 
# number = input('Please enter a number :' )  # get user input
# number_int = int(number)          # convert the input as a number

# if(number_int > 50):
#     print('The number is bigger than 50')


# if(number_int < 50):
#     print('The number is smaller than 50')

# print('end program')

#number > 50           # the number entered in bigger than 50
#number <= 50                #  the number entered in not bigger than 50

#********************************************
#****************if else statement***********
#********************************************
print('****************************************************')


# number = input('Please enter a number :' )  # get user input
# number_int = int(number)

# if(number_int > 50):
#     print('The number is bigger than 50') 
# else:
#     print('The number is smaller than 50')

# print('End programming')


#****************************************************
# print odd or even value using user value
# print('*******************************************************')
# number = input('enter a number')
# number = int(number)

# if('number % 2 == 0'):
#     print('even number')
# else:
#     print('odd number')

print('********************************************************')
#***************************************************************

# temperature = input('please enter the temperature in celsius')
# temperature = float(temperature)

# >= 35 : verry hot
# 25 - 35 : warm
# 15 - 25 : cold
# <= : freezzing

# if(temperature>=35):
#     print('very hot day')
# else:
#      if(temperature >= 25):
#          print('warm day')
#      else:
#         if(temperature >= 15):
#             print('cold day')
#         else:
#             print('freezing day')


#*************************************************************
#*************************Nested if else loop*****************
# if(temperature>=35):
#     print('very hot day')
# elif(temperature >= 25): 
#     print('warm day')
# elif(temperature >= 15):
#     print('cold day')
# else:
#     print('freezing day')


#****************************************************************
#*********************ITERATIVE STATEMENT************************
#****************************************************************

# iteration statement are used when certain task are to be executed multiple tasks


# for loop : used when no of conditions are know
# while loop : used when no of iteration are unknown. but, stopping condition is know

#print your name 10 times
# for i in range(10):     # we are  giving no of iterations.
#     print(i, 'Arjun')   # iterative) task

print('***********************************************************************')

# for i in range (3,10,3):                      # 3,6,9.
#     print(i, ' : Arjun')

# Giving a step as positive  value
# for i in range (1,10,3):                     
#     print(i, ' : Arjun')

# # Giving a step as negative value
# for i in range (10,3,-1):                   # 10 , 9 , 8 , 7 , 6 , 5 , 4 
#     print(i, ' : Arjun')

#print all odd number <50
# print('odd number between 1 & 50')
# for i in range (1,50,2):                 
#     print(i,)

# print('***********************************************************')

# # print all odd number between 20 & 50
# print('odd number between 20 & 50')
# for i in range (21,50,2):                 
#     print(i,)


print('***********************************************************')
#********************************************************************
#************************While loop**********************************
#********************************************************************

num = 1 
while(num < 10):
    print(num) 
    num = num + 3
print('End of while loop')

print('***********************************************************')

#**********************************************************************

#print all odd number <50
# print('odd number odd number <50')
# num = 1 
# while(num < 50):
#     print(num , end=',') 
#     num = num + 2



# # print all odd number between 20 & 50
# print('\n', 'odd number between 20 & 50')
# num = 21 
# while(num < 50):
#     print(num , end=',') 
#     num = num + 2


num = int(input('Enter a number:'))
