from tkinter import *
root=Tk()
root.title('CALCULATOR')
root.geometry('360x450')
root.resizable(0,0)
root.config(bg='black')
f_num=s_num=operator=None

def get_digit(digit):
    current=re_label['text']
    new=current+str(digit)
    re_label.config(text=new)
    
def clear():
    re_label.config(text='')

def get_operator(op):
    global f_num,operator
    f_num=int(re_label['text'])
    operator=op
    re_label.config(text=' ')

def get_result():
    global f_num,s_num,operator
    s_num=int(re_label['text'])
    if operator=='+':
        re_label.config(text=str(f_num+s_num))
    elif operator=='-':
        re_label.config(text=str(f_num-s_num))
    elif operator=='*':
        re_label.config(text=str(f_num*s_num))
    else:
        if s_num==0:
            re_label.config(text='error')
        else:
            re_label.config(text=str(f_num/s_num))
   
re_label=Label(root,text='',bg='black',fg='white')
re_label.grid(row=0,column=0,columnspan=4,pady=(45,25),sticky='w') #pady for spacing fromm top to down
re_label.config(font=('Georgia',25,('bold italic')))

btn7=Button(root,text='7',bg='yellow',fg='black',width=5,height=2,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('Georgia',15,('bold italic')))

btn8=Button(root,text='8',bg='yellow',fg='black',width=5,height=2,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('Georgia',15,('bold italic')))

btn9=Button(root,text='9',bg='yellow',fg='black',width=5,height=2,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('Georgia',15,('bold italic')))

btn_multi=Button(root,text='*',bg='yellow',fg='black',width=5,height=2,command=lambda:get_operator('*'))
btn_multi.grid(row=1,column=3)
btn_multi.config(font=('Georgia',15,('bold italic')))

btn4=Button(root,text='4',bg='yellow',fg='black',width=5,height=2,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('Georgia',15,('bold italic')))

btn5=Button(root,text='5',bg='yellow',fg='black',width=5,height=2,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('Georgia',15,('bold italic')))

btn6=Button(root,text='6',bg='yellow',fg='black',width=5,height=2,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('Georgia',15,('bold italic')))

btn_sub=Button(root,text='-',bg='yellow',fg='black',width=5,height=2,command=lambda:get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('Georgia',15,('bold italic')))

btn1=Button(root,text='1',bg='yellow',fg='black',width=5,height=2,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('Georgia',15,('bold italic')))

btn2=Button(root,text='2',bg='yellow',fg='black',width=5,height=2,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('Georgia',15,('bold italic')))

btn3=Button(root,text='3',bg='yellow',fg='black',width=5,height=2,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('Georgia',15,('bold italic')))

btn_plus=Button(root,text='+',bg='yellow',fg='black',width=5,height=2,command=lambda:get_operator('+'))
btn_plus.grid(row=3,column=3)
btn_plus.config(font=('Georgia',15,('bold italic')))

btn_Ac=Button(root,text='Ac',bg='yellow',fg='black',width=5,height=2,command=lambda:clear())
btn_Ac.grid(row=4,column=0)
btn_Ac.config(font=('Georgia',15,('bold italic')))

btn0=Button(root,text='0',bg='yellow',fg='black',width=5,height=2,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('Georgia',15,('bold italic')))

btn_div=Button(root,text='/',bg='yellow',fg='black',width=5,height=2,command=lambda:get_operator('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('Georgia',15,('bold italic')))

btn_equal=Button(root,text='=',bg='yellow',fg='black',width=5,height=2,command=lambda:get_result())
btn_equal.grid(row=4,column=2)
btn_equal.config(font=('Georgia',15,('bold italic')))

root.mainloop()