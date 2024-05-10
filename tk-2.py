import tkinter
import tkinter.messagebox
win1=tkinter.Tk()
win1.geometry('700x500')

def def1():
    x=float(en1.get())
    y=float(en2.get())
    tkinter.messagebox.showinfo(f'x+y={x+y}')

def def2():
    x=float(en1.get())
    y=float(en2.get())    
    tkinter.messagebox.showinfo(f'x-y={x-y}')

def def3():
    x=float(en1.get())
    y=float(en2.get())
    tkinter.messagebox.showinfo(f'x*y={x*y}')

def def4():
    x=float(en1.get())
    y=float(en2.get())
    if y==0:
        tkinter.messagebox.showerror('heyy! y=0 !')

    tkinter.messagebox.showinfo(f'x/y={x/y}')

lable1=tkinter.Label(text='num1:',fg='red')
lable1.pack(padx=10,pady=10)
en1=tkinter.Entry(win1)
en1.pack(padx=10,pady=10)
lable2=tkinter.Label(text='num2',fg='red')
lable2.pack(padx=10,pady=10)
en2=tkinter.Entry(win1)
en2.pack(padx=10,pady=10)

btn1=tkinter.Button(text='+',padx=20,pady=15,command=def1,fg='blue')
btn1.pack(padx=10,pady=10)
btn2=tkinter.Button(text='-',padx=20,pady=15,command=def2,fg='blue')
btn2.pack(padx=10,pady=10)
btn3=tkinter.Button(text='*',padx=20,pady=15,command=def3,fg='blue')
btn3.pack(padx=10,pady=10)
btn4=tkinter.Button(text='/',padx=20,pady=15,command=def4,fg='blue')
btn4.pack(padx=10,pady=10)


win1.mainloop()
