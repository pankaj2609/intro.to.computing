#question 1 code
print('\nQues1')

a=float(input('1st no. '))

b=float(input('2nd no. '))

c=float(input('3rd no. '))
print('average of the three numbers is {}'.format((a+b+c)/3))

#question 2 code
print('\nQues2')

gross_income=float(input('enter you gross income: '))

dependents=int(input('enter no. of dependents: '))

tax_rate=0.2

standard_deduction=10000

dependent_deduction=3000

taxable_income=gross_income-standard_deduction-(dependent_deduction*dependents)

tax=taxable_income*tax_rate
print(f'Your income tax is= {tax}')

#question 3 code
print('\nQues3')

sid=int(input('write your SID: '))

name=input('write your Name: ')

gender=input('mention your Gender [F,M,U] : ')

course=input('name of the course: ')

cgpa=float(input('write your CGPA: '))

mylist=[sid,name,gender,course,cgpa]

print(mylist)

#question 4 code
print('\nQues4')

s1=float(input('enter marks of student 1: '))
s2=float(input('enter marks of student 2: '))
s3=float(input('enter marks of student 3: '))
s4=float(input('enter marks of student 4: '))
s5=float(input('enter marks of student 5: '))
mylist=[s1,s2,s3,s4,s5]
print(f'this is the list without sorting {mylist}')
mylist.sort()
print(f'list after sorting {mylist}')

#question 5 code
#part(a)
print('\nQues5(a)')

colors=['Red','Green','White','Black','Pink','Yellow']
print(colors)
colors.pop(3)

print(colors)

#question 5 code
#part(b)
print('\nQues5(b)')

colors=['Red','Green','White','Black','Pink','Yellow']
print(colors)

colors[3:5]=["Purple"]

print(colors)

