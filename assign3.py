
##############
#q1 assig3
##############
print('\nQ1\n\n')
user_input=input('type a word or sentence here: ')
words_list=[]

occurence_count={}

if ' ' in user_input:
#######_now i have tried to remove the few commonly used symbols_#######
    sentence = user_input.replace('.',' ')
    
    sentence_new = sentence.replace('?',' ')
    
    words_list = sentence_new.split(' ')
    
    words_list.pop()
##########_now the world_list contains only the words_########
    
else:
    for letter in user_input:

        words_list.append(letter)
    
    print(words_list)
    
set1=set(words_list)

for value in set1:
    occurence_count[value]=words_list.count(value)

print(f'\nfollowing dictionary shows the occurence count\n{occurence_count}')

####q2 assign3
print('\nQ2\n\n')
#days31=['01','03','05','07','08','10','12']
#days30=['04','06','09','11']

error_msg='incorrect date entered'

day=int(input('Day(in DD format): '))
month=input('Month(in MM format): ')
year=int(input('Year(in YYYY format): '))

if year in range(1800,2026):
    ######_checking those months which have 31 Days_########
    if month in ['01','03','05','07','08','10','12']:
        
        if month=='12':
            if day==31:
                op_day=1
                op_month=1
                op_year=year+1
            
            elif day in range(1,31):
                op_day=day+1
                op_month=int(month)
                op_year=year
            else:
                print(error_msg)
        else:
            if day==31:
                op_day=1
                op_month=int(month)+1
                op_year=year
            
            elif day in range(1,31):
                op_day=day+1
                op_month=int(month)
                op_year=year
            else:
                print(error_msg)
    
    ######_checking those months which have 30 Days_########
    elif month in ['04','06','09','11']:
        if day==30:
            op_day=1
            op_month=int(month)+1
            op_year=year
        
        elif day in range(1,30):
            op_day=day+1
            op_month=int(month)
            op_year=year
        else:
            print(error_msg)
    
    ######_checking for February month_########
    elif month=='02':
        if year%4==0:
            if day==29:
                op_day=1
                op_month=3
                op_year=year
            
            elif day in range(1,29):
                op_day=day+1
                op_month=int(month)
                op_year=year

            else:
                print(error_msg)
        
        else:
            if day==28:
                op_day=1
                op_month=3
                op_year=year
            
            elif day in range(1,28):
                op_day=day+1
                op_month=int(month)
                op_year=year

            else:
                print(error_msg)

    print(f'\nNext date is:{op_day}/{op_month}/{op_year}  [Date/Month/Year]')
else:
    print('enter the correct year. (MUST LIE B/W 1800 and 2025)')
################
# Q3 assignment 3
################
print('\nQ3\n\n')
print('called the squared function')
def squared(*args):
    output_list=[]
    for num in args:
        output_list.append((num,num**2))
    return output_list
squared(2,5,14,6,32,19,8,10)

####q4 assign3                                                                          
print('\nQ4\n\n')
gpa=int(input('enter your GPA: '))

if gpa in range(4,11):
    mydict={10:["'A+'",'Outstanding'],9:["'A'",'Excellent'],8:["'B+'",'Very Good'],7:["'B'",'Good'],6:["'C+'",'Average'],5:["'C'",'Below Average'],4:["'D'",'Poor']}

    print(f'Your grade is {mydict[gpa][0]} and {mydict[gpa][1]} Performance')
else:
    print('entered GPA is out of the specified range(your entery must lie b/w 4 and 10)')

#####
#Q5 assig3
#####
print('\nQ5\n\n')
print('ABCDEFGHIJK\n ABCDEFGHI \n  ABCDEFG  \n   ABCDE   \n    ABC    \n     A')

########
#Q5 assig3
########
print('\nQ5"another method"\n\n')
all_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
how_many=int(input('how many letters you want in 1st row? (must lie b/w 1 and 26) '))
m=how_many
no_of_spaces=0
while m>0:
    space=' '
    no_of_spaces+=1
    print(f'{space*no_of_spaces}{all_letters[0:m]}{space*no_of_spaces}')
    m=m-2
############
#q6 assig3
############
print('\nQ6\n\n')
all_names=[]
all_sids=[]
while True:
###########taking user input
    consent=input('want to enter data? (type Y/N)')
    if consent.upper()=='Y':

        name=input('enter name of the student: ')
        sid=int(input('enter the SID: '))

        all_names.append(name)
        all_sids.append(sid)
        continue
    
    elif consent.upper()=='N':
###############creating the dictionary of the data entered        
        i=-1
        mydata={}
        while i<len(all_names)-1:
            i+=1
            
            mydata[all_sids[i]]=all_names[i]
            
        print(mydata)
#############_now mydata stores whole data that has been entered_##################

##############
##############sorting on the basis of the SIDs
##############        
        mylist1=list(mydata.items())
        mylist1.sort()
        
        sorted_sid=dict(mylist1)
        
        print('\ndictionary sorted on the basis of the SIDs:-')
        print(sorted_sid)
################  
################sorting on the basis of the names
################
        list_names=list(mydata.values())
        list_names.sort()

        list_sids=list(mydata.keys())

        sorted_names={}

        for name in list_names:
            for the_sid in list_sids:
                if mydata[the_sid]==name:
                    sorted_names[the_sid]=name
########_else: continue used just to improve readability,otherwise,it can be skipped as well_##########
                else:
                    continue
            else:
                continue
        print('\ndictionary sorted on the basis of the names:-')
        print(sorted_names)
##################
#printing a specific student name using SID
##################
        
    else:
        print('give appropriate consent')
    
    break
given_sid=int(input('type down any SID,to extract the name: '))
print(f'\nthe sid entered belongs to:-{mydata[given_sid]}')
##############
#Q7 assignment 3
##############
print('\nQ7\n\n')
fib_seq=[0,1]
how_long=int(input('how many terms of the Fibonacci seq. you want to print :'))
while len(fib_seq)<how_long:
    
    each_term=fib_seq[-1]+fib_seq[-2]
    
    fib_seq.append(each_term)

print(fib_seq)

total=0

for num in fib_seq:
    total=total+num
print(f'average of the above sequence is: {total/(len(fib_seq))}')               

######q8 assign3
print('\nQ8\n\n')
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

Set_a=Set1^Set2
print(f'ans for part(a) is: Set_a={Set_a}')

Set_b=Set1^Set2^Set3
print(f'\nans for part(b) is: Set_b={Set_b}')

Set_c = (Set1&Set2 | Set2&Set3 | Set3&Set1) - (Set1&Set2&Set3)
print(f'\nans of part(c) is: Set_c={Set_c}')

Set_d= {1,2,3,4,5,6,7,8,9,10}-Set1
print(f'\nans of part(d) is: Set_d={Set_d}')

Set_e={1,2,3,4,5,6,7,8,9,10} - (Set1|Set2|Set3)
print(f'\nans of part(e) is: Set_e={Set_e}')                                     
