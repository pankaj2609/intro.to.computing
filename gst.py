##### Ques1 #######

from tkinter import *
win=Tk()
win.title('ques.1')
win.minsize(width=300,height=400)

label1=Label(win,text='original cost')
label1.grid(row=0,column=0)

label2=Label(win,text='net price')
label2.grid(row=1,column=0)

orig_cost=str
net_price=str

entry1=Entry(win,textvariable=orig_cost)### can't do operation on orig_cost object but we can set its value equal to something that will be visible to us in the entry box ####
entry1.grid(row=0,column=1)

entry2=Entry(win,textvariable=net_price)
entry2.grid(row=1,column=1)

result=Label(win,text='')
result.place(x=25,y=75)

def show_result():
    #result.configure(text=f'GST rate is {((int(net_price)-int(orig_cost))*100)/int(orig_cost)}%')
    result.configure(text=f'GST rate is {((int(entry2.get())-int(entry1.get()))*100)/int(entry1.get())}%')
button1=Button(win,text='calculate GST',command=show_result)
button1.place(x=30,y=100)

win.mainloop()


