# *******************************************************
# *************Arithmetic Operators**********************
# *******************************************************

# Binary operations : we need  min of 2 operands.

num_1 = 389
num_2 = 5

sum = num_1 + num_2        #Addition 
Difference = num_1 - num_2  #subtraction
product = num_1 * num_2   #multiplication
Division = num_1 / num_2 # division
exponent = num_1 ** num_2
reminder = num_1 % num_2
floor = num_1 // num_2

print(num_1,'+', num_2,'=',sum)
print(num_1,'-', num_2,'=',Difference) 
print(num_1,'*', num_2,'=',product)
print(num_1,'/', num_2,'=',Division)
print(num_1,'to the power', num_2,'=',exponent)
print('reminder of', num_1,'/',num_2,'=',reminder)
print(num_1,'//', num_2,'=',floor)

print('************************************************')


#*****************************************************************
#******************Relational operator***************************
#****************************************************************
print(num_1,'>',num_2, num_1 > num_2) #True
print(num_1,'<',num_2, num_1 < num_2) #False
print(num_1,'>=',num_2, num_1 >= num_2) #True
print(num_1,'<=',num_2, num_1 <= num_2) #False
print(num_1,'==',num_2, num_1 == num_2) #False
print(num_1,'!=',num_2, num_1 != num_2) #True

#*****************************************************************
#***************Logical Operators*********************************
#***************************************************************** 
# AND - All has to be an agreement
# OR - At least 1 must be in aggreement
# NOT -  opposite.

#operand are boolean

statement_1 = True
statement_2 = False
statement_3 = True
statement_4 = False

#AND 
print(statement_1 and statement_2) # True and False = False
print(statement_1 and statement_3) # True and False = True                                           
print(statement_2 and statement_4) # True and False = False

# OR
print(statement_1 or statement_2) # True and False = True
print(statement_1 or statement_3) # True and False = True
print(statement_2 or statement_4) # True and False = False

#NOT
print(not statement_1 ) # True and False = False
print(not statement_2 ) # True and False = True
