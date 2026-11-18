string_1 = 'ICT kerala'
string_2 = 'python'
string_3 = 'programming'

print(string_1)                        # iikkrhucnwodhhdudkji
print(string_2, string_3)              # python programming
print(string_3)                        # programming
print('\n')                            # new line
print(string_2, string_3)


#changing the end strig from '\n' to '&'
print(string_2, end=' & ')
print(string_3, end='& ')
print('\n',end='& ')
print(string_2,string_3,end='&') 

 # \n new line
 # \t new tab


print('\t',string_2,string_3)



print('***************************************************')
s1 = 'ICT'
s2= 'Academy'
s3 = 'of'
s4 = 'kerala'

# string concatenation n
print( s1+ s2 + s3 +s4)                 #ICTAcademyofkerala
print( s1,s2,s3,s4)                     #ICT Academy of kerala

combined_string = s1 +' '+s2 +' '+s3 +' '+s4
print(combined_string)                  #ICT Academy of kerala


print(s1)                                                #ICT
print(s1 + s1 + s1 + s1 + s1)                            #ICTICTICTICTICT
print(s1 * 5)                                            #ICTICTICTICTICT
print((s2 + ' ') * 5)                                    # Academy Academy Academy Academy Academy 
print((s1 + '\t') * 5)                                   # ICT     ICT     ICT     ICT     ICT
print((s1 + '\n') * 5)


#*******************************************************
#*************************index*************************
print('*******************************************************')

print(string_3)                                             # programming
print(string_3[0])                                          # prints character value at 0th index 'p'
print(string_3[5])                                          # prints character value at 0th index 'a'
print(string_3[10])                                         # g ( last character)
print(string_3[9])                                          # we cannot go beyond the maximum index of a  string

string_1 = 'iikkrhucnwodhhdudkji'
print( string_1[-5])                                       # Last index value.

#********************************************************
#********************Slicing******************************
print('***************************************************')

s1 = 'Trivandrum'
print(s1[6])            # will display 7th character
print(s1[-4])           #d
print(s1[0:5])          #Triva | start index = 0, end index = 4 .

print(s1[6:10])         # slice 'drum'
print(s1[4:7])          # and

print(s1[:5])           # from start index still 5 .            'Triva'
print(s1[6:])           # from 6th index till last index.       'drum'
print(s1[0:5:2])                                      #'Tia '
print(s1[:5:2])         #'Tia'

# sring_name[starting index : ending index : step]
print(s1[0:8:3])        #Tvd

#**********************************************************************************************
#**********************************************************************************************
print('*************************************************************************')


string_4 = "Join our offline programs in kerala's IT parks"
print(string_4[5:])                      # starting point :end point                    'our offline programs in kerala's IT parks'
print(string_4[5::2])                    # starting point : ending point :step          'orofieporm nkrl' Tprs'

#Reversing a string 

print(string_4[::-1])                    # starting point : ending point :step           'skrap TI s'alarek ni smargorp enilffo ruo nioJ'
print(string_3[::-1])

#***************************************************************************************************
#********************************* Functons ********************************************************
#***************************************************************************************************
print('*********************************************************************************************')

s1 = 'Trivandrum'
print(s1.lower())      # Converting the string to Lowercase                     'trivandrum'
print(s1.upper())      # Converting the string to Uppercase                     'TRIVANDRUM'
print(s1.swapcase())   # switches cases of each of character in the string      'tTRIVANDRUM'
print(s1.capitalize()) # first letter is upper and the rest will be lower       'Trivandrum'
