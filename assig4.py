###___q1___###
print('q1')
def hanoi(disks,source='p1',helper='p2',final='p3'):
    if disks==0:
        return
    else:
        #           _s_for_this_case,   h_for_this_case,   f_for_this_case ##########
        hanoi(disks-1,      source,     final,          helper)
        
        print(f'MOVING DISK {disks} FROM {source} TO {final}')

        #           _s_for_this_case,   h_for_this_case,   f_for_this_case       ###
        hanoi(disks-1,      helper,     source,         final)

hanoi(3)

#### q2 (by iteration) ######
#### using for-while loop ####
print('q2 (by iteration)')
mylist1=[(0,1,0)]
#### this list will store all the rows of PASCAL'S TRIANGLE as tuple ####

rows=int(input('how many rows of pascal triangle to print?  '))

while len(mylist1)<rows:
### using the last element of mylist1 , we will be creating the next element ###
    old_element=mylist1[-1]

    new_element=['0','0']

    for a in range(len(old_element)):

        if a+1<len(old_element):
        
            new_element.insert(-1,int(old_element[a])+int(old_element[a+1]))
#### now the new_element is complete and shall be added to the mylist1 ####
    mylist1.append(tuple(new_element))

#### now printing the each row of the pascal's triangle #####
for a in mylist1:
    print(a[1:len(a)-1])

#### another iteration method q2 #####
#### using for loop only ######
print('another iteration method q2')
from math import factorial

#### defining the mathematical function nCr ####
def c(n,r):
    return factorial(n)/((factorial(n-r))*(factorial(r)))

kitni_row=int(input('how many rows of pascal triangle? '))

for row_no in range(1,kitni_row+1):
    elements_of_a_row=[]
##### this inner for loop is to print a specific row #####
    for r in range(row_no):
        m=int(c(row_no-1,r))

        elements_of_a_row.append(m)

    print(elements_of_a_row)

##########################
### q2 (by recursion) ####
print('q2 (by recursion)')
from math import factorial

def c(n,r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))

def print_the_current_row(n):
    each_row=[]
    for r in range(0,n):
        each_row.append(c(n-1,r))
    print(each_row)

def pascal_triangle(n):
    if n==0:
        return
    else:
        pascal_triangle(n-1)
        print_the_current_row(n)
pascal_triangle(8)

###########
### q3 #####
print('q3')
print('in the following code we will get the result for a/b ')
a=int(input('type the value of a: '))
b=int(input('type the value of b: '))
print(f'value of a is {a} \n         b is {b}')

ans=divmod(a,b)
print(f'ans is{ans}')
## q3(a)
print('\nq3(a)')
print(callable(ans))
## q3(b)
print('\nq3(b)')
print(ans[0]==ans[1]==0)
## q3(c)
print('\nq3(c)')
tuple1=tuple([ans[0],ans[1],4,5,6])
print(f'greater than 4:-{tuple(filter(lambda m:m>4,tuple1))}')

## q3(d)
print('\nq3(d)')
print(f'the result obtained in last part was{tuple1}')
set1=set(tuple1)
print(set1)
## q3(e)
print('\nq3(e)')
frozenset(set1)
print('the set has been made immutable')
## q3(f)
print('\nq3(f)')
print(f'the max value present in the set is: {max(set1)}')
print(f'\nhash value of this number is:{hash(max(set1))}')

##########
######  q4   #######
print('q4')
class Student:
	def __init__(self,roll_number,name):
		self.name=name
		self.roll_number=roll_number

	def __del__(self):
		print(f'the object has been deleted')

stu1=Student(roll_number=19,name='paras')
stu1.name
del(stu1)


##############
##### q5 #####
print('q5')
class EmpDetails:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def update_salary(self,new_salary):
        print('salary updated')
        self.salary=new_salary
    def __str__(self):
        return f'\nName={self.name} Salary={self.salary}'
    
    def __del__(self):
        print('\n\nobject has been deleted successfully')

emp1=EmpDetails(name='Mehak',salary=40000)
emp2=EmpDetails(salary=50000,name='Ashok')
emp3=EmpDetails(salary=60000,name='Viren')

print(emp1)
print(emp2)
print(emp3)

emp1.update_salary(70000)
print(emp1)

del(emp3)

#############
#### q6 #####
print('\nq6')
def anagrams(s):
    if s=='':
        return[s]
    else:
        ans=[]
        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans


george_said=input('word spoken by george: ')

barbie_made=anagrams(george_said)
print(f'barbie rearranged letters to get:{barbie_made}')
if george_said in barbie_made:
    print('True friends')
else:
    print('fake friendship')

input('\n hit enter')