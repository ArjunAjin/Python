# *****************************************************************************
#****************************File Handling*************************************
#******************************************************************************

# filepath = 'C:/PGP_Data_science_and_AIML/Python/student.txt'
# ralative_filepath = open('student.txt','r')



# file = open('student.txt','r')
# content = file.read
# print(content)

# def read_file_filepath():
#     file = open(read_file_filepath,'r')
#     content = file.read
#     print(content)
# def read_file_rel_path():
#     file_1 = open(read_file_filepath,'r')
#     content_1 = file_1.read()
#     print(content_1)

# #file.read() will return all the values as a single string 

# #read a sinle line
 
# def read_line_by_line():
#     file = open(ralative_filepath,'r')
#     content = file.readline()
#     print(content)
#     print(type(content))
#     file.close()
# read_line_by_line()


# #reading a single line

# def read_line_by_line():

#     file = open(ralative_filepath,'r')
#     content = file.readline()
#     print(content)
#     print(type(content))
#     for line in content:
#         print(line)



#******************************************************
#********************Write a file**********************
write_path = 'students.txt'

#Open a files in writing mode
#if the file didn't exist earlier , now, it will be created
#opened in wring mode


def write_file():
    file = open(write_path,'w')
    file.close()

def write_into_file():
    file = open(write_path,'w')
    file.write("Gowtham")
    file.close
    


# write_into_file()

def write_into_file2():
    file = open(write_path,'w')
    file.write("Gowtham\n")
    file.write("Akash\n")
    file.write("vishnu\n")
    file.close
    
write_into_file2()

#we take a name as an argument and write the same
def student_name(i_name):
    file = open(write_path,'w')
    file.write(i_name)
    file.close
    
    
# student_name('Akash a')  


#append data into the file
def append_file():
    file = open(write_path,'a')
    file.write('keerthi')
    file.close
append_file()  

#write a genaral function to append the data into file

def append_data(i_filepath,i_name):
    file = open(i_filepath,'a')
    file.write('\n')
    file.write(i_name)
    file.close

append_data('students.txt','BSNL')


#this method of file assignment is preffered more
def append_data1(i_filepath,i_name):
    with open(i_filepath,'a') as file:
        file.write('\n')
        file.write(i_name)


append_data1('students.txt','BSNL')