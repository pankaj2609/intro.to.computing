from tkinter import *
import calendar

win=Tk()
win.minsize(height=700,width=700)

win.title('calendar')

frame1=Frame(win)
frame1.grid(row=0,column=0)

label_a=Label(frame1,text='type the year here')
label_a.pack(side=TOP)

entry1=Entry(frame1)
entry1.pack()



def whole_year_calendar():
    yr=int(entry1.get())
    #total_weeks_4=f'{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}'
    #total_weeks_5=f'{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}'
    #total_weeks_6=f'{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}'
    
    
    def jan(month_no):
        weeks=len(calendar.monthcalendar(yr,month_no))
        if weeks==4:
            label1.configure(text=f'JANUARY\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}')
        elif weeks==5:
            label1.configure(text=f'JANUARY\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}')
        elif weeks==6:
            label1.configure(text=f'JANUARY\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}')
    jan(1)
    
    def feb(month_no):
        weeks=len(calendar.monthcalendar(yr,month_no))
        if weeks==4:
            label2.configure(text=f'FEBRUARY\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}')
        elif weeks==5:
            label2.configure(text=f'FEBRUARY\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}')
        elif weeks==6:
            label2.configure(text=f'FEBRUARY\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}')
    feb(2)

    def mar(month_no):
        weeks=len(calendar.monthcalendar(yr,month_no))
        if weeks==4:
            label3.configure(text=f'MARCH\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}')
        elif weeks==5:
            label3.configure(text=f'MARCH\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}')
        elif weeks==6:
            label3.configure(text=f'MARCH\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}')
    mar(3)    

    def apr(month_no):
        weeks=len(calendar.monthcalendar(yr,month_no))
        if weeks==4:
            label4.configure(text=f'APRIL\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}')
        elif weeks==5:
            label4.configure(text=f'APRIL\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}')
        elif weeks==6:
            label4.configure(text=f'APRIL\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}')
    apr(4)

    def may(month_no):
        weeks=len(calendar.monthcalendar(yr,month_no))
        if weeks==4:
            label5.configure(text=f'MAY\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}')
        elif weeks==5:
            label5.configure(text=f'MAY\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}')
        elif weeks==6:
            label5.configure(text=f'MAY\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}')
    may(5)

    def jun(month_no):
        weeks=len(calendar.monthcalendar(yr,month_no))
        if weeks==4:
            label6.configure(text=f'JUNE\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}')
        elif weeks==5:
            label6.configure(text=f'JUNE\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}')
        elif weeks==6:
            label6.configure(text=f'JUNE\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}')
    jun(6)

    def jul(month_no):
        weeks=len(calendar.monthcalendar(yr,month_no))
        if weeks==4:
            label7.configure(text=f'JULY\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}')
        elif weeks==5:
            label7.configure(text=f'JULY\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}')
        elif weeks==6:
            label7.configure(text=f'JULY\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}')
    jul(7)

    def aug(month_no):
        weeks=len(calendar.monthcalendar(yr,month_no))
        if weeks==4:
            label8.configure(text=f'AUGUST\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}')
        elif weeks==5:
            label8.configure(text=f'AUGUST\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}')
        elif weeks==6:
            label8.configure(text=f'AUGUST\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}')
    aug(8)

    def sep(month_no):
        weeks=len(calendar.monthcalendar(yr,month_no))
        if weeks==4:
            label9.configure(text=f'SEPTEMBER\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}')
        elif weeks==5:
            label9.configure(text=f'SEPTEMBER\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}')
        elif weeks==6:
            label9.configure(text=f'SEPTEMBER\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}')
    sep(9)

    def oct(month_no):
        weeks=len(calendar.monthcalendar(yr,month_no))
        if weeks==4:
            label10.configure(text=f'OCTOBER\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}')
        elif weeks==5:
            label10.configure(text=f'OCTOBER\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}')
        elif weeks==6:
            label10.configure(text=f'OCTOBER\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}')
    oct(10)

    def nov(month_no):
        weeks=len(calendar.monthcalendar(yr,month_no))
        if weeks==4:
            label11.configure(text=f'NOVEMBER\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}')
        elif weeks==5:
            label11.configure(text=f'NOVEMBER\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}')
        elif weeks==6:
            label11.configure(text=f'NOVEMBER\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}')
    nov(11)

    def dec(month_no):
        weeks=len(calendar.monthcalendar(yr,month_no))
        if weeks==4:
            label12.configure(text=f'DECEMBER\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}')
        elif weeks==5:
            label12.configure(text=f'DECEMBER\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}')
        elif weeks==6:
            label12.configure(text=f'DECEMBER\n\n{calendar.monthcalendar(yr,month_no)[0]}\n{calendar.monthcalendar(yr,month_no)[1]}\n{calendar.monthcalendar(yr,month_no)[2]}\n{calendar.monthcalendar(yr,month_no)[3]}\n{calendar.monthcalendar(yr,month_no)[4]}\n{calendar.monthcalendar(yr,month_no)[5]}')
    dec(12)

bt1=Button(frame1,text='print Calendar',command=lambda:whole_year_calendar(),bg='green',foreground='white')
bt1.pack()

label0=Label(win,text='kindly read this:-\nEach week is represented by the list of dates.\nEach weeks starts from MONDAY and goes upto SUNDAY.',background='white',foreground='blue',height=5,width=30)
label0.grid(row=0,column=1,columnspan=3,ipadx=300)

label1=Label(win,text='JANUARY',height=8,width=25,background='yellow',font='10')
label1.grid(row=1,column=0,ipadx=10,ipady=10)

label2=Label(win,text='FEBRUARY',height=8,width=25,background='orange',font='10')
label2.grid(row=1,column=1,ipadx=10,ipady=10)

label3=Label(win,text='MARCH',height=8,width=25,background='red',foreground='white',font='10')
label3.grid(row=1,column=2,ipadx=10,ipady=10)

label4=Label(win,text='APRIL',height=8,width=25,background='light green',font='10')
label4.grid(row=1,column=3,ipadx=10,ipady=10)

label5=Label(win,text='MAY',height=8,width=25,background='cyan',font='10')
label5.grid(row=2,column=0,ipadx=10,ipady=10)

label6=Label(win,text='JUNE',height=8,width=25,background='purple',foreground='white',font='10')
label6.grid(row=2,column=1,ipadx=10,ipady=10)

label7=Label(win,text='JULY',height=8,width=25,background='purple',foreground='white',font='10')
label7.grid(row=2,column=2,ipadx=10,ipady=10)

label8=Label(win,text='AUGUST',height=8,width=25,background='cyan',font='10')
label8.grid(row=2,column=3,ipadx=10,ipady=10)

label9=Label(win,text='SEPTEMBER',height=8,width=25,background='light green',font='10')
label9.grid(row=3,column=0,ipadx=10,ipady=10)

label10=Label(win,text='OCTOBER',height=8,width=25,background='red',foreground='white',font='10')
label10.grid(row=3,column=1,ipadx=10,ipady=10)

label11=Label(win,text='NOVEMBER',height=8,width=25,background='orange',font='10')
label11.grid(row=3,column=2,ipadx=10,ipady=10)

label12=Label(win,text='DECEMBER',height=8,width=25,background='yellow',font='10')
label12.grid(row=3,column=3,ipadx=10,ipady=10)


win.mainloop()