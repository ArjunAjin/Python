# function adding 2 numbers

# def display_sum(num1,num2):
#     sum= num1+num2
#     print('The Sum of',num1,'and',num2,'is : ',sum)

# a function will have,
# 1. function name : mandatory
# 2. inputs()
# 3. Body of the function :mandatory
# 4. Output

# while we define input variable in the function definition
# we. are creation new variables with scope within the function

# display_sum(8,7)
# display_sum(210,72)
# display_sum(88,17)
# display_sum('Happy',' diwali')

# def display_sum_custome():
#     print('Type here:')
#     num1= float(input('Enter your 1st Number. :'))
#     num2= float(input('Enter your 2st Number. :'))
#     sum= num1+num2
#     print('The Sum of',num1,'and',num2,'is : ',sum)

# display_sum_custome()

# def greet_user():
#     print('Greeting You ,')
#     name1=input('Enter your Name :')
#     print('Hi,',name1,'\n','good afternoon','\n','Hope you are Fine')

# greet_user()


# num_1=int(input('Enter your Number : '))
# for i in range(1,11):
#     print(i,'x',num_1,'is : ',i*num_1)
#     i+=1
# print('End')


# Function to display multiplication table of any number

# def display_Multiplication_table():
#     print('We will Display your Number and its Multiplication')
#     num1=int(input('Enter your Number : '))
#     print('............................')
#     print('Multiplication Table of',num1)
#     print('............................')
#     print('............................')
#     for i in range(1,11):
#         print(f" {i} x {num1} = {i*num1}")
#         i+=1
#     print('............................')
#     print('............................')

# display_Multiplication_table()



# sub1=int(input('Enter your Maths Score :'))
# sub2=int(input('Enter your Physics Score :'))
# sub3=int(input('Enter your Chemistry Score :'))
# sub4=int(input('Enter your Biology Score :'))
# sub5=int(input('Enter your English Score :'))

# def display_Score():
#     print('............................')
#     print('1. Your Subject Sum')
#     print('............................')
#     sum_1=sub1+sub2+sub3+sub4+sub5
#     print(f"Total Mark is = {sum_1}")

# def display_Average():
#     print('............................')
#     print('2. Your Subject Average')
#     print('............................')
#     Average=(sub1+sub2+sub3+sub4+sub5)/5
#     print(f"Total Average is = {Average}")

# def display_Largest_Mark():
#     print('............................')
#     print('3. Your Highest Mark ')
#     print('............................')
#     if(sub1>sub2 and sub1>sub3 and sub1>sub4 and sub1>sub5):
#         print('largest mark obtained in Maths')
#     elif (sub2>sub1 and sub2>sub3 and sub2>sub4 and sub2>sub5):
#         print('largest mark obtained in Physics')
#     elif (sub3>sub1 and sub3>sub2 and sub3>sub4 and sub3>sub5):
#             print('largest mark obtained in Chemistry')
#     elif (sub4>sub1 and sub4>sub3 and sub4>sub2 and sub4>sub5):
#             print('largest mark obtained in Biology')
#     elif (sub5>sub1 and sub5>sub3 and sub5>sub4 and sub5>sub2):
#             print('largest mark obtained in English')

# def display_Less_Mark():
#     print('............................')
#     print('4. Your lowest Mark ')
#     print('............................')
#     if(sub1<sub2 and sub1<sub3 and sub1<sub4 and sub1<sub5):
#         print('lowest mark obtained in Maths')
#     elif (sub2<sub1 and sub2<sub3 and sub2<sub4 and sub2<sub5):
#         print('lowest mark obtained in Physics')
#     elif (sub3<sub1 and sub3<sub2 and sub3<sub4 and sub3<sub5):
#             print('lowest mark obtained in Chemistry')
#     elif (sub4<sub1 and sub4<sub3 and sub4<sub2 and sub4<sub5):
#             print('lowest mark obtained in Biology')
#     elif (sub5<sub1 and sub5<sub3 and sub5<sub4 and sub5<sub2):
#             print('lowest mark obtained in English')

# display_Score()
# display_Average()
# display_Largest_Mark()
# display_Less_Mark()


# Using Tuple 

# score=(29,41,38,34,27)
# def display_Sum():
#     sum1=0
#     for i in range(len(score)):
#          sum1+=score[i]
#     print(f"Total Mark is: {sum1}")
#     return sum1

# def display_Average():
#      sum1=0
#      avg=0
#      for i in range(len(score)):
#         sum1+=score[i]
#         avg=sum1/5
#      print(f"Average is: {avg}")

# def display_largest():
#     largest_mark=max(score)
#     print(f"Largest mark is = {largest_mark}")

# def display_minimum():
#     minimum_mark=min(score)
#     print(f"minimum mark is = {minimum_mark}")

# # display_Sum()
# # display_Average()
# # display_largest()
# # display_minimum()


# def calculate_sum(score_list):
#     sum=0
#     for score in range(len(score_list)):
#         sum+=score_list[score]
#     return sum
# def calculate_avg(score_list):
#     total=calculate_sum(score_list)
#     print('Sum is =',total)
#     count=len(score_list) 
#     avg= total/count
#     print(f"Average is = {avg}")

# def display_largest(score_list):
#     largest_mark=max(score)
#     print(f"Largest mark is = {largest_mark}")

# def display_minimum(score_list):
#     minimum_mark=min(score)
#     print(f"minimum mark is = {minimum_mark}")

# score=(20,30,40,50,60,70,80,90)
# calculate_sum(score)
# calculate_avg(score)
# display_largest(score)
# display_minimum(score)





#**************************Optional Argument*****************************************************
print('*************************************************************************')

# def calculate_exponent(num,exp = 2): 
#     print(num**exp)

# calculate_exponent(5) # optional in case doesnt givve a value automatically add exp = 2
# calculate_exponent(5,3) #optional variable

# def create_wish(name, wish = 'Good day'):  #here by exp is n optional input . default value is 'Good day'
#     print({name},{wish})

# create_wish ( "Arjun")  
# create_wish ( "Arjun", 'have a nice day')

# create_wish (wish= 'Have a nice day',name='Arjun')



# print('******************************************************')
# # ***************************************************************

# def student_mark():
#     python = 85
#     mathematics = 90
#     science = 75

#     total = python + mathematics +science
#     print("total mark:", total)
# student_mark()
# # Average
# def Average_mark():
#     python = 85
#     mathematics = 90
#     science = 75
    
#     total = python + mathematics +science
#     Average = total/3
#     print("Average Mark:",Average)
# Average_mark()

# # Highest mark
#     highest_mark =  max(python,mathematics,science)
#     print("Highest mark:",highest_mark)

# # Lowest mark
#     lowest_mark =  min(python,mathematics,science)
#     print("lowest mark:",lowest_mark)

# # student has scored more than 40 in each subject.

#     print('python scored morethan 40:',python>40)
#     print('mathematics scored morethan 40:',mathematics>40)
#     print('science scored morethan 40:',science>40)
# student_mark()

print('********************************************************')
# *****************************************************************

# def divide(num, den):
#     result = num/den
#     print(f'the answer is {result}')

# divide(40,5)
#  # TypeError
# divide(123,0)
# ZeroDivisionError



# ******************************************************************************
# *********************************Exception Handling****************************

# we write  specific criteria so that code flow is not Interrupted
# we write potentional runtime error making code inside 'try' block
# And the exception willbe caught by the 'expect' block

def divide_new(num, den):
    try:
        result = num/den
        print(f'the answer is {result}')
    except:
        print('There is no problem')
    print('end of the problem')
# divide_new(40,5)
# divide_new('a','b')       # TypeError
# divide_new(333,0)         # ZeroDivisionError
# divide_new(50,4)


# Newrirting the function with Exception block displaying the error message

# def divide_new1(num, den):
#     try:
#         result = num/den
#         print(f'the answer is, {result}')
#     except Exception as e:
#         print('There is no problem:{e}')
#         print('end')

# # divide_new1(40,5)
# # divide_new1('a','b')       # TypeError
# # divide_new1(333,0)         # ZeroDivisionError
# # divide_new1(50,4)

# ******************************************************************

def divide_new2(num, den):
    try:
        result = num/den
        print(f'the answer is, {result}')
    except TypeError:
        print('please make sure you are entering the number')
    except ZeroDivisionError:
        print('please make sure to give a non zero value as denominator')
    except Exception as e:
        print(f'There is a problem : {e}')
    print('end')

divide_new2(40,5)
divide_new2('a','b')       # TypeError
divide_new2(333,0)         # ZeroDivisionError
divide_new2(50,4)