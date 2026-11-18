#List is a data type used to store collection of values.
# sinces its a combintion of other data type(int,float,string,boolean), we call it as a derived datatype
# LIST CAN CONTAIN HETROGENIOUS DATATYPE
#There is no restriction in terms of datatype in a list.
#List can contain various type of datatype - Hetrogenous

#declaration a list
# name = ""
# print(type(name))                # string

# #method 1 
# lst_name1 = []                             #empty list
# print(type(lst_name1))

# #method 2
# lst_name2 = ['akash','vishnu','ajith']          # list
# print(type(lst_name2))

# #method 3 
# lst_name3 = list()       # just a list
# print(type(lst_name3))


# #Fetching values using index from a list.
# lst_name2 = ['vishnu','akash','ajith']         
# print(lst_name2[0])
# print(lst_name2[1])
# print(lst_name2[2])


# #List containing multiple datatypes
# #personal info as a list : Name, Age, Graduation year, University, Height

# Arjun_info = ['Arjun', 22, 2025, 'MG University', 168.5, lst_name2] #List can contain any Datatype
# print(type(Arjun_info))

# print(Arjun_info[0])                       #Display value at index = 0
# print(type((Arjun_info[0])))               # Display datatype of value at inde = 0

# print(Arjun_info[1])
# print(type((Arjun_info[1])))

# print(Arjun_info[2])
# print(type((Arjun_info[2])))

# print(Arjun_info[3])
# print(type((Arjun_info[3])))

# print(Arjun_info[4])
# print(type((Arjun_info[4])))

# print(Arjun_info[5])
# print(type((Arjun_info[5])))


 
# list1 = [1,2,3,4,5]
# list2 = [False,True,False,True,False]
# print(list1 + list2)

# list3 = (list1 + list2)
# print(list3)



#*********************************************************
#**********************list function**********************
#*********************************************************

list1 = [1,7,3]
list2 = [False,True,False]

lst_name2 = ['vishnu','akash','ajith']  

print(list1)           # unsort  [1, 7, 3]
list1.sort()           # sorting is done here (asecnding order)
print(list1)           # sorted  [1, 3, 7]

#reverse=true
print(list1)                      #unsort
list1.sort(reverse=True)          # sorting is done here (Decending order)           
print(list1)                      # sorted


print(lst_name2)                 #unsort
lst_name2.sort()                 # sorting is done here (Decending order)  
print(lst_name2)                  # sorted


print(lst_name2)
lst_name2.sort(reverse=True)      # sorting is done here (Decending order) 
print(lst_name2)                   # sorted


# extend 
#lst_name = ['akaash','vishnu','ajith', 7,3,1]
lst_name2.extend(list1 )
print(lst_name2)
print(lst_name2[3])

#append
list2.append(list1)           # list1 was added as the last value of the list2
print(list2)                  #[False, True, False, [7, 3, 1]] 
print(list2[3])

list1.append('A')
print(list1)                         #[7, 3, 1, 'A']

list1.reverse()
print(list1)                         #['A', 1, 3, 7]

# Check the count of the value.
print(' the no of times False appear in the list = ', list2.count(False))
print('the no of times True appear in the list = ', list2.count(True))
print("the no of times 'X' appear in the list = ", list2.count('X')) 