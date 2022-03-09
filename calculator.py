from tkinter import *
from turtle import width
win=Tk()
win.title('calculator')
win.minsize(height=400,width=400)

the_expression=''
entry_made=str

##### creating an entry box to intake the expression #####
entry1=Entry(win,textvariable=entry_made)
entry1.place(x=140,y=250)

##### showing the result in the label placed below it #####
label_result=Label(win,text='You will get the result printed here')
label_result.place(x=140,y=300)

## defining a function that will enter the values/symbols to entry box , depending upon what button we press ###
def edit(n):
    global the_expression
    the_expression=the_expression + str(n)
    entry_made.set(the_expression)

### defined a functin that will calc. and show the result ####
def give_result():

    result=eval(entry1.get()) ## result=eval(entry_made) ----> this won't work(yaad rkho yaar), look the last part for the reasoning ##
    label_result.configure(text=f'{result}')
    
    ### the following code is also valid if you want see the result in the entry box itself ####
    #entry_made.set(result)

######### 2nd Row ##########
bt7=Button(win,text='7',height=2,width=3,command=lambda:edit('7'))
bt7.grid(row=2,column=1)

bt8=Button(win,text='8',height=2,width=3,command=lambda:edit('8'))
bt8.grid(row=2,column=2)

bt9=Button(win,text='9',height=2,width=3,command=lambda:edit('9'))
bt9.grid(row=2,column=3)

bt0=Button(win,text='0',height=2,width=3,command=lambda:edit('0'))
bt0.grid(row=2,column=4)

bt_equal=Button(win,text="=",height=2,width=3,command=give_result)
bt_equal.grid(row=2,column=5)
######################

########## 3rd Row ############
bt4=Button(win,text='4',height=2,width=3,command=lambda:edit('4'))
bt4.grid(row=3,column=1)

bt5=Button(win,text='5',height=2,width=3,command=lambda:edit('5'))
bt5.grid(row=3,column=2)

bt6=Button(win,text='6',height=2,width=3,command=lambda:edit('6'))
bt6.grid(row=3,column=3)

bt_add=Button(win,text='+',height=2,width=3,command=lambda:edit('+'))
bt_add.grid(row=3,column=4)

bt_sub=Button(win,text='-',height=2,width=3,command=lambda:edit('-'))
bt_sub.grid(row=3,column=5)
###########################

########## 4th Row ###########

bt1=Button(win,text='1',height=2,width=3,command=lambda:edit('1'))
bt1.grid(row=4,column=1)

bt2=Button(win,text='2',height=2,width=3,command=lambda:edit('2'))
bt2.grid(row=4,column=2)

bt3=Button(win,text='3',height=2,width=3,command=lambda:edit('3'))
bt3.grid(row=4,column=3)

bt_prod=Button(win,text='*',height=2,width=3,command=lambda:edit('*'))
bt_prod.grid(row=4,column=4)

bt_div=Button(win,text='/',height=2,width=3,command=lambda:edit('/'))
bt_div.grid(row=4,column=5)

##############################

def all_clear():
    global the_expression
    the_expression=''
    entry_made.set('')

def clear_last_entry():
    global the_expression
    the_expression=the_expression[:-1]
    entry_made.set(the_expression)
    
########## 5th Row ############
btc=Button(win,text='clear',height=2,command=lambda:clear_last_entry())
btc.grid(row=5,column=2,columnspan=2,ipadx=10)

bt_float=Button(win,text='.',height=2,command=lambda:edit('.'))
bt_float.grid(row=5,column=1,ipadx=8)

bt_open_bracket=Button(win,text='(',height=2,width=3,command=lambda:edit('('))
bt_open_bracket.grid(row=5,column=4)

bt_close_bracket=Button(win,text=')',height=2,width=3,command=lambda:edit(')'))
bt_close_bracket.grid(row=5,column=5)
###########################

########## 6th Row ###########
bt_clr_all=Button(win,text='clear all',command=lambda:all_clear())
bt_clr_all.grid(row=6,column=1,columnspan=5,ipadx=40)
###########################

win.mainloop()

########################################################################################################
### since entry_made is Stringvar type object ###
# thus eval function can't be applied to it # , #eval function can be applied to str,byte,code object # 
########################################################################################################