#calculator
import tkinter as tk
from tkinter import ttk
import os
import math
import sys

value_list=[]

def button_press(num):
    global equation_text

    equation_text=equation_text+str(num)
    equation_label.set(equation_text)

def equals():

    try:
        global equation_text

        total= str(eval(equation_text))
        equation_label.set(total)
        equation_text=total
        value_list.append(equation_text)
    except ZeroDivisionError:

        equation_label.set("error")

def clear():
    global equation_text

    equation_text=""
    equation_label.set(equation_text)

def Sinusfunctie():
    global equation_text

    try:
        result1 = round(math.sin(eval(equation_text)), 2)
        equation_label.set(result1)
        equation_text = str(result1)
    except:
        equation_label.set("Error")
        equation_text = ""

def Cosinusfunctie():
    global equation_text

    try:
        result2= round(math.cos(eval(equation_text)), 2)
        equation_label.set(result2)
        equation_text=str(result2)
    except:
        equation_label.set("Error")
        equation_text= ''

def Tangensfunctie():
    global equation_text

    try:
        result3= round(math.tan(eval(equation_text)), 2)
        equation_label.set(result3)
        equation_text=str(result3)
    except:
        equation_label.set("Error")
        equation_text= ''

def aSinusfunctie():
    global equation_text
    try:     
         ii3=round(math.asin(eval(equation_text)),2)
         equation_label.set(ii3)
         equation_text=str(ii3)
    except:
         equation_label.set('Error')
         equation_text=''

def aCosinusfunctie():
    global equation_text
    try:     
         ii2=round(math.acos(eval(equation_text)),2)
         equation_label.set(ii2)
         equation_text=str(ii2)
    except:
         equation_label.set('Error')
         equation_text=''

def aTangensfunctie():
    global equation_text
    try:     
         ii1=round(math.atan(eval(equation_text)),2)
         equation_label.set(ii1)
         equation_text=str(ii1)
    except:
         equation_label.set('Error')
         equation_text=''

def rootfunctie():
    global equation_text
    try:    
        root1=round(math.sqrt(eval(equation_text)),2)
        equation_label.set(root1)
        equation_text=str(root1)
    except:
        equation_label.set('Error')
        equation_text=''

def deleteonefunctie():
    global equation_text
    
    if len(equation_text) > 0:
        equation_text = equation_text[:-1]
        equation_label.set(equation_text)
  
def ansfunctie():
    
    if len(value_list) == 1:
        equation_label.set(value_list)
    elif len(value_list)>1:
        equation_label.set(equation_label+value_list[-1])
    else:
        equation_label.set("Error")




def updatelogwindow():
    newlogwindow=tk.Toplevel(window)
    newlogwindow.title('UpdateLog and Future Updates')
    newlogwindow.geometry('400x400')
    newlogwindow.config(bg='#28b54d')
    text_widget1=tk.Text(newlogwindow, font=20)
    filepath1=os.path.join(os.path.dirname(__file__),'UpdateLog.txt')
    with open(filepath1,'r') as file1:
        UpdateLog=file1.read()
    text_widget1.insert(tk.END,UpdateLog)
    text_widget1.pack(padx=10,pady=10)
    text_widget1.configure(state='disabled')
pi="3.14159265"
#degrees= 1
#radians=degrees*(pi/180.0)
#degrees = radians * ( 180.0 / pi )

window = tk.Tk()
window.geometry("600x600")
window.title("Calculator, version 1.0")
window.config(bg="#28b54d")
script_dir = os.path.dirname(sys.argv[0])
icon_path = os.path.join(script_dir, "171352_calculator_icon.ico")

window.iconbitmap(default=icon_path)
equation_text = ""

equation_label = tk.StringVar()

label = tk.Label(window, textvariable=equation_label, 
                 font=("Arial", 30),
                 width=22,
                 height=1,
                 bg="#28b54d")
label.pack()

frame = tk.Frame(window)
frame.config(bg='#28b54d')
frame.pack()


button1= tk.Button(frame, bg='white', text=1, height=2, width=9, font=35,
                   command= lambda: button_press(1))
button1.grid(row=1, column=0)

button2= tk.Button(frame, bg='white', text=2, height=2, width=9, font=35, 
                   command= lambda: button_press(2))
button2.grid(row=1, column=1)

button3= tk.Button(frame, bg='white', text=3, height=2, width=9, font=35, 
                   command= lambda: button_press(3))
button3.grid(row=1, column=2)

button4= tk.Button(frame, bg='white', text=4, height=2, width=9, font=35, 
                   command= lambda: button_press(4))
button4.grid(row=2, column=0)

button5= tk.Button(frame, bg='white', text=5, height=2, width=9, font=35, 
                   command= lambda: button_press(5))
button5.grid(row=2, column=1)

button6= tk.Button(frame, bg='white', text=6, height=2, width=9, font=35, 
                   command= lambda: button_press(6))
button6.grid(row=2, column=2)

button7= tk.Button(frame, bg='white', text=7, height=2, width=9, font=35, 
                   command= lambda: button_press(7))
button7.grid(row=3, column=0)

button8= tk.Button(frame, bg='white', text=8, height=2, width=9, font=35, 
                   command= lambda: button_press(8))
button8.grid(row=3, column=1)

button9= tk.Button(frame, bg='white', text=9, height=2, width=9, font=35, 
                   command= lambda: button_press(9))
button9.grid(row=3, column=2)

button0= tk.Button(frame, bg='white', text=0, height=2, width=9, font=35, 
                   command= lambda: button_press(0))
button0.grid(row=4, column=0)

plusbutton=tk.Button(frame, bg="white", text='+', height=2, width=9, font=35,
               command= lambda: button_press("+"))
plusbutton.grid(row=4, column=1)

minusbutton=tk.Button(frame,bg="white", text='-', height=2, width=9, font=35,
               command= lambda: button_press("-")) 
minusbutton.grid(row=4, column=2)

dividebutton=tk.Button(frame, bg='white',text="/", height=2, width=9, font=35,
                      command=lambda: button_press("/"))
dividebutton.grid(row=1, column=4)

timesbutton=tk.Button(frame, bg='white',text="*", height=2, width=9, font=35,
                      command=lambda: button_press("*"))
timesbutton.grid(row=1, column=3)

equalsbutton=tk.Button(frame, bg="white", text='=', height=2, width=9, font=35,
               command= equals)
equalsbutton.grid(row=4, column=4)

sinusbutton=tk.Button(frame, bg='white', text='Sin', height=2, width=9, font=35,
                      command= Sinusfunctie )
sinusbutton.grid(row=5, column=0)

cosinusbutton=tk.Button(frame, bg='white', text='Cos', height=2, width=9, font=35,
                      command= Cosinusfunctie )
cosinusbutton.grid(row=5, column=1)

Tangensbutton=tk.Button(frame, bg='white', text='Tan', height=2, width=9, font=35,
                      command= Tangensfunctie )
Tangensbutton.grid(row=5, column=2)

clearbutton=tk.Button(frame, bg="white", text='clear', height=2, width=9, font=35,
               command= clear)
clearbutton.grid(row=4, column=3)

kommabutton=tk.Button(frame, bg='white', text='.', height=2, width=9, font=35,
                      command=lambda: button_press(".") )
kommabutton.grid(row=2,column=3)

pibutton=tk.Button(frame, bg="white", text="π", height=2, width=9, font=35,
                   command=lambda:button_press(pi))
pibutton.grid(row=2, column=4)

rootbutton=tk.Button(frame, bg='white', text='√', height=2, width=9, font=35,
                      command=rootfunctie )
rootbutton.grid(row=3, column=4)

asinusbutton=tk.Button(frame, bg='white', text='Sin-1', height=2, width=9, font=35,
                      command= aSinusfunctie )
asinusbutton.grid(row=6, column=0)

acosinusbutton=tk.Button(frame, bg='white', text='Cos-1', height=2, width=9, font=35,
                      command= aCosinusfunctie )
acosinusbutton.grid(row=6, column=1)

aTangensbutton=tk.Button(frame, bg='white', text='Tan-1', height=2, width=9, font=35,
                      command= aTangensfunctie )
aTangensbutton.grid(row=6, column=2)

powerbutton=tk.Button(frame, bg='white', text='^', height=2, width=9, font=35,
                      command=lambda:button_press('**') )
powerbutton.grid(row=3, column=3)

haakjeLButton=tk.Button(frame, bg='white', text='(', height=2, width=9, font=35,
                      command=lambda:button_press('(') )
haakjeLButton.grid(row=6,column=3)

haakjeRButton=tk.Button(frame, bg='white', text=')', height=2, width=9, font=35,
                      command=lambda:button_press(')') )
haakjeRButton.grid(row=6,column=4)

ansbutton=tk.Button(frame, bg='white', text='Ans', height=2, width=9, font=35,
                      command=ansfunctie)
ansbutton.grid(row=5,column=4)

deletebutton=tk.Button(frame, bg='white', text='Del', height=2, width=9, font=35,
                      command=deleteonefunctie)
deletebutton.grid(row=5,column=3)

updatelogbutton=tk.Button(frame, bg='white', text='UpdateLog', height=3, width=9, font=35,
                      command=updatelogwindow)
updatelogbutton.grid(padx=0,pady=50)

window.mainloop()


