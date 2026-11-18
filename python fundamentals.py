std_name='abhinav'
age=25
height=123.45
currently_enrolled=True
subjects_enrolled=['python','c']
date_of_birth=(2,'jan',2003)
skillsknown={'python','java'}
students_detail={'nam':'abi','age':25,'course':'python'}
print(std_name,type(std_name))
print(age,type(age))
print(height,type(height))
print(currently_enrolled,type(currently_enrolled))
print(subjects_enrolled,type(subjects_enrolled))
print(date_of_birth,type(date_of_birth))
print(skillsknown,type(skillsknown))
print(students_detail,type(students_detail))

#2
python=55
mathematics=30
science=50
total = (python+mathematics+science)
print('total marks:',total)
avgmark =total/3
print('avarage marks:',avgmark)
mark=('python','mathematics','science')
minmark=min(mark)
maxmark=max(mark)
print('higest mark:',maxmark)
print('minimum mark:',minmark)
print('python:',python>40)
print('mathematics:',mathematics>40)
print('science:',science>40)

#3
if (avgmark>=90):
    grade='A'
elif(avgmark>=75):
    grade='B'
elif(avgmark>=60):
    grade='C'
elif(avgmark>=40):
    grade='D'
else:
    grade='fail'
    print(grade)

if(avgmark>=60 and python>40 and mathematics>40 and science>40):

    print('eligible to certicate')
    certificate=True

else:
    print('not eligeble')
    certificate=False
#4
mark1=[34,55,67,32]
num=mark1
print('marks obtained in 5 subjects:',mark1)
totalmark=sum(mark1)       
print('total:',totalmark)
count1=0
count=0
i=0
for i in range(len(mark1)):
    if (mark1[i]>=40):
        count=count+1
    else :
        count1=count1+1

print('student scored 40 above:',count)
print('student scored below 40:',count1)

#5

i=1
while i<=50:
    print(i)
    i=i+1
print('even number:')
even_num=0
even_sum=0
while even_num<=50:
    if even_num%2==0:
        print(even_num)
        even_sum=even_sum+even_num
        even_num=even_num+1
    else:
        even_num=even_num+1

print('odd number')   
odd_num=0
odd_sum=0
while odd_num<=50:
    if odd_num%2!=0:
        print(odd_num)
        odd_sum=odd_sum+odd_num
        odd_num=odd_num+1
    else:
        odd_num=odd_num+1

print('even sum:',even_sum)  
print('odd sum:',odd_sum)      

#6
skills={'python','java','sql'}
skills.add('ML')
skills.remove('java')
print(skills)
print('students knows python:','python' in skills)
print(skills)

#7
print('student name:',std_name)
print('age:',age)
print('course details:',subjects_enrolled)
print('total mark:',totalmark)
average_mark=45
print('avgmark:',average_mark)
print('grade:',grade)
print('certificate eligibility:',certificate)
student={'student name':std_name,'age':age,'course details':subjects_enrolled,'total marks':totalmark,'avarge mark':average_mark,'grade':grade,'certificate':certificate}
print('student dictionary:',student)



    


  



