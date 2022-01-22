#Ques 1
print('\nQues 1')
mystring='Python is a case sensitive language'

print (f'Answer of part (a) {len(mystring)}')

print (f'answer of part (b) {(mystring[::-1])}')

sliced=mystring[10:26]

print (f'answer of part (c) sliced= {(sliced)}')

mylist=mystring.split(' ')

mylist.remove('a')
mylist.remove('case')
mylist.remove('sensitive')

mylist.insert(2,'object oriented')

m=' '.join(mylist)

print(f'answer of part (d) {m}')
#for the part (d) the other code that can be written is

#new_string=mystring.replace('a case sensitive','object oriented')
#print(new_string)

a_ka_index=mystring.index('a')

print(f'answer of part (e) "index of a" {a_ka_index}')

list2=mystring.split()

part_f=''.join(list2)
print(f'answer of part (f) is {part_f}')


#Ques 2
print('\nQues 2')
name=input('write your name: ')

SID=int(input('wrtie your SID: '))

dept_name=input('wrtie your department name: ')

CGPA=float(input('write your CGPA here: '))

print(f'\nHey,{name} Here!\nMy SID is {SID}\nI am from {dept_name} department and my CGPA is {CGPA}')

#Ques 3
print('\nQues 3')
a=56
b=10
print(f'a is {a} and b is {b}')

print(f'a&b is equal to {a&b}')
print(f'a|b is equal to {a|b}')
print(f'a^b is equal to {a^b}')

print(f'left shifting a and b, a is now {a<<2} and b is now {b<<2}')

print(f'shifting a 2bits right, a is now {a>>2}\nshifting b 4bits right, b is now {b>>4}')

#Ques 4
print('\nQues 4')
number1=float(input('enter a number: '))
number2=float(input('type another number: '))
number3=float(input('enter the third number: '))

if number1>number2 and number1>number3:
    
    print(f'\nthe largest number is {number1}')

elif number2>number3 and number2>number1:
    
    print(f'\nthe largest number is {number2}')
else:
    print(f'\nthe largest number is {number3}')

#Ques 5
print('\nQues 5')
entered_string=input('type any string to check presence of "name": ')

if 'name' in entered_string:
    print("Yes")
else:
    print("No")

#Ques 6
print('\nQues 6')

len1=int(input('length of side one: '))
len2=int(input('length of side two: '))
len3=int(input('length of side three: '))

if len1>len2+len3 or len2>len1+len3 or len3>len1+len2:
    print('\nNo')
else:
    print('\nYes')
