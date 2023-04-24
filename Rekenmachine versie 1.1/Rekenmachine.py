#calculator
import tkinter as tk #importeren van de Tkinter library die helpt met GUI's maken
import os #importeren van os, operating system, voor extensies in de computer
import math#importeren van math, een wiskunde library die helpt met wiskundige functies
import sys # importeren van de library system, die help net als OS om files and andere dingen met het host systeem te doen

value_list=[] #variabele gebruikt voor de ans functie
#bg='#28b54d'

def button_press(num): #gebruikt voor het indrukken van een button
    global equation_text #globaal de equation text, zodat het dezelfde variabele is.

    equation_text=equation_text+str(num) #voegt de parameter in de functie van de buton toe aan de equation_text
    equation_label.set(equation_text) # zet de equation_label hetzelfde als de equation_text

def equals(): # gebruikt voor het uitrekenen van een rekensom, functie van de =button

    try: #het proberen van een rekensom heeft het voordeel dat het programma niet crashed
        global equation_text # globaal varaibel equation_text gebruiken

        total= str(eval(equation_text)) #het totaal van de rekensom berekenen 
        equation_label.set(total) # update het equation_label naar het totaal
        equation_text=total # om te zorgen dat de equation_text ook hetzelfde als het totaal is
        value_list.append(equation_text) # zorgt voor dat er een lijst gemaakt word, voor de Ans functie, zodat hij de laatste value kan opslaan en weergeven
    except ZeroDivisionError: #voor een niet door nul delen error, maar er moeten er nog meer komen

        equation_label.set("error") # geeft aan dat er een error is gebeurt en de rekensom niet uitgevoerd kan worden

def clear(): # cleared de equation_text en de equation_label voor een nieuwe rekensom
    global equation_text, equation_label, lastans

    lastans=equation_text
    equation_text=""
    equation_label.set(equation_text)
    

#de goniometrische functies zijn bijna allemaal hetzelfde
def Sinusfunctie(): # gebruikt om de sinus uit te rekenen van een in getyped getal
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
#einde goniometrische functies

def rootfunctie(): #gebruikt om de wortel van een getal te trekken
    global equation_text 
    try:    #proberen zodat geen min getallen er door heen komen
        root1=round(math.sqrt(eval(equation_text)),2) # eval gebruiken om de wortel te evaluaten
        equation_label.set(root1)
        equation_text=str(root1)
    except: #error als er een min getal is
        equation_label.set('Error')
        equation_text=''

def deleteonefunctie(): # om een letter van een string af te halen per 1 keer
    global equation_text
    
    if len(equation_text) > 0: #als de lengte groter is dan nul
        equation_text = equation_text[:-1] # dan trekt hij een charachter van de equation text af
        equation_label.set(equation_text) # Updaten van de equation_label

def updatelogwindow(): #window waar de update log in staat
    global newlogwindow

    newlogwindow=tk.Toplevel(window) # maken van een nieuwe window die boven de Main window komt
    newlogwindow.title('UpdateLog and Future Updates') # titel van de nieuwe window
    newlogwindow.geometry('400x400') # Zorgt voor hoe groot de window wordt
    newlogwindow.config(bg='#28b54d') # achtergrond kleur als standaard
    text_widget1=tk.Text(newlogwindow, font=20) #text widget voor de updateLog.txt
    filepath1=os.path.join(os.path.dirname(__file__),'UpdateLog.txt') # het pad naar het txt bestand
    with open(filepath1,'r') as file1: # het openen met filepath word opgeslagen als file1
        UpdateLog=file1.read() #het lezen van het bestand via het pad
    text_widget1.insert(tk.END,UpdateLog) # inserts de text file in de newlogwindow
    text_widget1.pack(padx=10,pady=10)  #padx en pady gebruikt voor afstand tussen de muur en andere widgets
    text_widget1.configure(state='disabled')# zodat de text niet geedit kan worden door de user van de rekenmachine

def settingswindow(): # om de settings aan te passen van alle windows
    global scale, scale2, scale3, settingwindow, buttonconfirmwindow,buttonconfirmbuttons

    settingwindow=tk.Toplevel(window) # Nieuwe window voor settings die boven de Main window komt
    settingwindow.title('Settings') # titel van de window
    settingwindow.geometry('400x400') # grote van de window
    scale=tk.Scale(settingwindow, from_=0, to=255, bg='red', command=set_bgcolor) # een slider met 255 values voor de rode value van de som van rgb naar hexadecimale variabele
    scale.grid(row=0,column=0) #positie van de slider op een window met behulp van een grid
    scale2=tk.Scale(settingwindow, from_=0, to=255,bg='green', command=set_bgcolor)# zie de rode slider, maar dan voor groen
    scale2.grid(row=0,column=1)#positie van de slider op een window met behulp van een grid
    scale3=tk.Scale(settingwindow, from_=0, to=255,bg='blue', command=set_bgcolor)# precies hetzelfde als de rode slider maar dan voor de kleur blauw
    scale3.grid(row=0,column=2)#positie van de slider op een window met behulp van een grid
    buttonconfirmwindow=tk.Button(settingwindow, bg='white', text='windowcolor', height=2, width=9, font=35, 
                   command=windowcolorconfirmfunction )
    buttonconfirmwindow.grid(row=0, column=3)
    buttonconfirmbuttons=tk.Button(settingwindow, text='buttoncolor', height=2, width=9, font=35,
                                   command=buttoncolorconfirmfunction)
    buttonconfirmbuttons.grid(row=0, column=4)
   
def windowcolorconfirmfunction():
    # zorgt ervoor dat de achtergronden overeenkomen met de gekozen kleur
    window.config(bg=bg) 
    label.config(bg=bg)
    frame.config(bg=bg)
    settingwindow.config(bg=bg)
    newlogwindow.config(bg=bg)
    creditswindow.config(bg=bg)
    instructieswindow.config(bg=bg)

def buttoncolorconfirmfunction():
    global bg
    buttonconfirmbuttons.config(bg=bg)
    buttonconfirmwindow.config(bg=bg)
    button0.config(bg=bg)
    button1.config(bg=bg)
    button2.config(bg=bg)
    button3.config(bg=bg)
    button4.config(bg=bg)
    button5.config(bg=bg)
    button6.config(bg=bg)
    button7.config(bg=bg)
    button8.config(bg=bg)
    button9.config(bg=bg)
    plusbutton.config(bg=bg)
    minusbutton.config(bg=bg)
    dividebutton.config(bg=bg)
    timesbutton.config(bg=bg)
    equalsbutton.config(bg=bg)
    sinusbutton.config(bg=bg)
    asinusbutton.config(bg=bg)
    cosinusbutton.config(bg=bg)
    acosinusbutton.config(bg=bg)
    Tangensbutton.config(bg=bg)
    aTangensbutton.config(bg=bg)
    clearbutton.config(bg=bg)
    kommabutton.config(bg=bg)
    pibutton.config(bg=bg)
    rootbutton.config(bg=bg)
    powerbutton.config(bg=bg)
    ansbutton.config(bg=bg)
    haakjeLButton.config(bg=bg)
    haakjeRButton.config(bg=bg)
    deletebutton.config(bg=bg)
    updatelogbutton.config(bg=bg)
    Settingsbutton.config(bg=bg)
    creditsbutton.config(bg=bg)
    instructiesbutton.config(bg=bg)

def set_bgcolor(scale_value): # zorgt voor dat de achtergrond aangepast kan worden met behulp van de sliders in de settingswindow
    global settingwindow, newlogwindow, bg
    #Set the background color of the window based on the scale's value;  wat informatie van chatgpt
    bg = '#%02x%02x%02x' % (scale.get(), scale2.get(), scale3.get()) # zorgt ervoor dat het informatie verzameld van de sliders en combineerd het tot een hexadecimaal getal dat opgeslagen wordt in een variable en het wordt gebruikt voor de kleur van achtergronden.

def creditswindowfunction():
    global creditswindow
    creditswindow=tk.Toplevel(window)
    creditswindow.title('Credits')
    creditswindow.geometry('400x400')
    text_widget2=tk.Text(creditswindow, font=20)
    filepath2=os.path.join(os.path.dirname(__file__),'credits.txt')
    with open(filepath2,'r') as file2:
        creditsfile=file2.read()
    text_widget2.insert(tk.END,creditsfile)
    text_widget2.pack(padx=10, pady=10)
    text_widget2.configure(state='disabled')

def ansfunctie():
    global equation_label, equation_text, lastans
    equation_text=lastans
    equation_label.set(equation_text)

def instructieswindowfunction():
    global instructieswindow
    
    instructieswindow=tk.Toplevel(window)
    instructieswindow.title('instructies')
    instructieswindow.geometry('400x400')
    text_widget3=tk.Text(instructieswindow, font=20)
    filepath3=os.path.join(os.path.dirname(__file__),'instructies.txt')
    with open(filepath3,'r') as file3:
        instructiesfile=file3.read()
    text_widget3.insert(tk.END,instructiesfile)
    text_widget3.pack(padx=10, pady=10)
    text_widget3.configure(state='disabled')

pi="3.14159265" #Waarde van pi

window = tk.Tk() #Main window
window.geometry("600x600") # grote van de window
window.title("Rekenmachine versie 1.1") # naam van de window
script_dir = os.path.dirname(sys.argv[0]) # maken van een variabele die directories automatisch kan openen naar een file.
icon_path = os.path.join(script_dir, "171352_calculator_icon.ico") #pad naar de icon van de window
window.iconbitmap(default=icon_path) # het icon op de window zetten

#28b54d, standaard kleur, laten staan

equation_text = "" #rekensom standaard leeg
equation_label = tk.StringVar()#rekensom op label

label = tk.Label(window, textvariable=equation_label, #label waar de equation_label op wordt weergegeven
                 font=("Arial", 30),
                 width=22,
                 height=1)
label.pack() #label op de window zetten

frame = tk.Frame(window) # een frame maken voor alle widgets
frame.pack() #frame widget op de window zetten

button1= tk.Button(frame, bg='white', text=1, height=2, width=9, font=35, # button om 1 in te clicken
                   command= lambda: button_press(1))
button1.grid(row=1, column=0) #button op de window zetten via grid een vaste plek

button2= tk.Button(frame, bg='white', text=2, height=2, width=9, font=35, #button  om 2 te clicken
                   command= lambda: button_press(2))
button2.grid(row=1, column=1) #button op de window zetten via grid een vaste plek

button3= tk.Button(frame, bg='white', text=3, height=2, width=9, font=35, #button om 3 in te clicken
                   command= lambda: button_press(3))
button3.grid(row=1, column=2) #button op de window zetten via grid een vaste plek

button4= tk.Button(frame, bg='white', text=4, height=2, width=9, font=35, #button om 4 in te clicken
                   command= lambda: button_press(4))
button4.grid(row=2, column=0) #button op de window zetten via grid een vaste plek

button5= tk.Button(frame, bg='white', text=5, height=2, width=9, font=35, #button om 5 in te clicken
                   command= lambda: button_press(5))
button5.grid(row=2, column=1) #button op de window zetten via grid een vaste plek

button6= tk.Button(frame, bg='white', text=6, height=2, width=9, font=35, #button om 6 in te clicken
                   command= lambda: button_press(6))
button6.grid(row=2, column=2) #button op de window zetten via grid een vaste plek

button7= tk.Button(frame, bg='white', text=7, height=2, width=9, font=35, #button om 7 in te clicken
                   command= lambda: button_press(7))
button7.grid(row=3, column=0) #button op de window zetten via grid een vaste plek

button8= tk.Button(frame, bg='white', text=8, height=2, width=9, font=35, #Button om 8 in te clicken
                   command= lambda: button_press(8))
button8.grid(row=3, column=1) #button op de window zetten via grid een vaste plek

button9= tk.Button(frame, bg='white', text=9, height=2, width=9, font=35, #button om 9 in te clicken
                   command= lambda: button_press(9)) 
button9.grid(row=3, column=2) #button op de window zetten via grid een vaste plek

button0= tk.Button(frame, bg='white', text=0, height=2, width=9, font=35, #button om 0 in te clicken
                   command= lambda: button_press(0))
button0.grid(row=4, column=0) #button op de window zetten via grid een vaste plek

plusbutton=tk.Button(frame, bg='white', text='+', height=2, width=9, font=35,#button om + in te clicken
               command= lambda: button_press("+"))
plusbutton.grid(row=4, column=1) #button op de window zetten via grid een vaste plek

minusbutton=tk.Button(frame,bg='white', text='-', height=2, width=9, font=35,# button om - in te clicken
               command= lambda: button_press("-")) 
minusbutton.grid(row=4, column=2) #button op de window zetten via grid een vaste plek

dividebutton=tk.Button(frame, bg='white',text="/", height=2, width=9, font=35,# button om / in te clicken
                      command=lambda: button_press("/"))
dividebutton.grid(row=1, column=4) #button op de window zetten via grid een vaste plek

timesbutton=tk.Button(frame, bg='white',text="*", height=2, width=9, font=35, #button om * in te clicken
                      command=lambda: button_press("*"))
timesbutton.grid(row=1, column=3) #button op de window zetten via grid een vaste plek

equalsbutton=tk.Button(frame, bg='white', text='=', height=2, width=9, font=35, #button om oplossing van rekensom te krijgen door behulp van functie: equals
               command= equals)
equalsbutton.grid(row=4, column=4) #button op de window zetten via grid een vaste plek

sinusbutton=tk.Button(frame, bg='white', text='Sin', height=2, width=9, font=35, #button voor sinus
                      command= Sinusfunctie )
sinusbutton.grid(row=5, column=0) #button op de window zetten via grid een vaste plek

cosinusbutton=tk.Button(frame, bg='white', text='Cos', height=2, width=9, font=35, # button voor cosinus
                      command= Cosinusfunctie )
cosinusbutton.grid(row=5, column=1) #button op de window zetten via grid een vaste plek

Tangensbutton=tk.Button(frame, bg='white', text='Tan', height=2, width=9, font=35, #button voor tangens
                      command= Tangensfunctie )
Tangensbutton.grid(row=5, column=2) #button op de window zetten via grid een vaste plek

clearbutton=tk.Button(frame, bg='white', text='clear', height=2, width=9, font=35, #button voor het leegmaken van een rekensom, zodat je een nieuwe rekensom kan beginnen
               command= clear)
clearbutton.grid(row=4, column=3) #button op de window zetten via grid een vaste plek

kommabutton=tk.Button(frame, bg='white', text='.', height=2, width=9, font=35, #button voor komma
                      command=lambda: button_press(".") )
kommabutton.grid(row=2,column=3) #button op de window zetten via grid een vaste plek

pibutton=tk.Button(frame, bg='white', text="π", height=2, width=9, font=35, # button voor de pi value
                   command=lambda:button_press(pi))
pibutton.grid(row=2, column=4) #button op de window zetten via grid een vaste plek

rootbutton=tk.Button(frame, bg='white', text='√', height=2, width=9, font=35, #button voor de wortel
                      command=rootfunctie )
rootbutton.grid(row=3, column=4) #button op de window zetten via grid een vaste plek

asinusbutton=tk.Button(frame, bg='white', text='Sin-1', height=2, width=9, font=35, #button voor inverse sinus
                      command= aSinusfunctie )
asinusbutton.grid(row=6, column=0) #button op de window zetten via grid een vaste plek

acosinusbutton=tk.Button(frame, bg='white', text='Cos-1', height=2, width=9, font=35, #button voor inverse cosinus
                      command= aCosinusfunctie )
acosinusbutton.grid(row=6, column=1) #button op de window zetten via grid een vaste plek

aTangensbutton=tk.Button(frame, bg='white', text='Tan-1', height=2, width=9, font=35, #button voor inverse tangens
                      command= aTangensfunctie )
aTangensbutton.grid(row=6, column=2) #button op de window zetten via grid een vaste plek

powerbutton=tk.Button(frame, bg='white', text='^', height=2, width=9, font=35, #button voor machten
                      command=lambda:button_press('**') )
powerbutton.grid(row=3, column=3) #button op de window zetten via grid een vaste plek

haakjeLButton=tk.Button(frame, bg='white', text='(', height=2, width=9, font=35, #button voor het linker haakje
                      command=lambda:button_press('(') )
haakjeLButton.grid(row=6,column=3) #button op de window zetten via grid een vaste plek

haakjeRButton=tk.Button(frame, bg='white', text=')', height=2, width=9, font=35, # button voor het rechter haakje
                      command=lambda:button_press(')') )
haakjeRButton.grid(row=6,column=4) #button op de window zetten via grid een vaste plek
#...Soon™
ansbutton=tk.Button(frame, bg='white', text='Ans', height=2, width=9, font=35, #Button voor het laatste antwoord, wordt weggehaald of vernieuwd/gefixed
                      command=ansfunctie)
ansbutton.grid(row=5,column=4) #button op de window zetten via grid een vaste plek

deletebutton=tk.Button(frame, bg='white', text='Del', height=2, width=9, font=35,#button om een letter per keer te deleten
                      command=deleteonefunctie)
deletebutton.grid(row=5,column=3) #button op de window zetten via grid een vaste plek

updatelogbutton=tk.Button(frame, bg='white', text='UpdateLog', height=3, width=9, font=35, #button voor de update window, zodate je de nieuwste updates kan lezen
                      command=updatelogwindow)
updatelogbutton.grid(row=7, column=0,padx=0,pady=20) #button op de window zetten via grid een vaste plek

Settingsbutton=tk.Button(frame, bg='white', text='Settings', height=3, width=9, font=35, # Button voor de settings window, zodat je je settings kan aanpassen
                      command=settingswindow)
Settingsbutton.grid(row=7,column=1,padx=0,pady=0,) #button op de window zetten via grid een vaste plek

creditsbutton=tk.Button(frame, bg='white', text='Credits', height=3, width=9, font=35,
                        command=creditswindowfunction)
creditsbutton.grid(row=7,column=2)

instructiesbutton=tk.Button(frame, bg='white', text='Instructies', height=3, width=9, font=35,
                        command=instructieswindowfunction)
instructiesbutton.grid(row=7,column=3)

window.mainloop()