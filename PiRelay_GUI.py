from tkinter import *
import webbrowser
import PiRelay


# functions
def onoff1():
    if button1.cget("text") == 'ON':
        relay_1.on()
        button1.configure(text='OFF', fg='Red', relief=SUNKEN)
    elif button1.cget("text") == 'OFF':
        relay_1.off()
        button1.configure(text='ON', fg='Green', relief=RAISED)


def onoff2():
    if button2.cget("text") == 'ON':
        relay_2.on()
        button2.configure(text='OFF', fg='Red', relief=SUNKEN)
    elif button2.cget("text") == 'OFF':
        relay_2.off()
        button2.configure(text='ON', fg='Green', relief=RAISED)


def onoff3():
    if button3.cget("text") == 'ON':
        relay_3.on()
        button3.configure(text='OFF', fg='Red', relief=SUNKEN)
    elif button3.cget("text") == 'OFF':
        relay_3.off()
        button3.configure(text='ON', fg='Green', relief=RAISED)


def onoff4():
    if button4.cget("text") == 'ON':
        relay_4.on()
        button4.configure(text='OFF', fg='Red', relief=SUNKEN)
    elif button4.cget("text") == 'OFF':
        relay_4.off()
        button4.configure(text='ON', fg='Green', relief=RAISED)


def onoff5():
    if button5.cget("text") == 'START ALL':
        relay_1.on()
        relay_2.on()
        relay_3.on()
        relay_4.on()
        button5.configure(text='STOP ALL', bg='Red', relief=SUNKEN)
    elif button5.cget("text") == 'STOP ALL':
        relay_1.off()
        relay_2.off()
        relay_3.off()
        relay_4.off()
        button5.configure(text='START ALL', bg='Green', relief=RAISED)
       
                   
relay_1 = PiRelay.Relay("RELAY1")
relay_2 = PiRelay.Relay("RELAY2")
relay_3 = PiRelay.Relay("RELAY3")
relay_4 = PiRelay.Relay("RELAY4")

# Parent Window
root = Tk()
root.geometry('400x320')
root.title('PiRelay')

# label  1
Label(root, text='HOME AUTOMATION', relief=RAISED, anchor=CENTER,
      font='bold', bg='goldenrod').grid(row=0, column=1, columnspan=5, pady=30)

# label 2
Label(root, text='Relay 1', relief=RAISED, anchor=CENTER, width=6, height=4,
      bg='gray30', fg='white').grid(row=1, column=1, pady=10, padx=5)
Label(root, text='Relay 2', relief=RAISED, anchor=CENTER, width=6, height=4,
      bg='gray30', fg='white').grid(row=1, column=2, pady=10, padx=5)
Label(root, text='Relay 3', relief=RAISED, anchor=CENTER, width=6, height=4,
      bg='gray30', fg='white').grid(row=1, column=3, pady=10, padx=5)
Label(root, text='Relay 4', relief=RAISED, anchor=CENTER, width=6, height=4,
      bg='gray30', fg='white').grid(row=1, column=4, pady=10, padx=5)

# label 3/image
img = PhotoImage(file='Images/pirelay1.png')
Label(root, text='PiRelay', bg='white', bd=0, image=img, width=120,
      height=150).grid(row=1, rowspan=3, column=5, padx=(20, 10))

# Buttons to control the relays
button1 = Button(root, text='ON', command=onoff1, fg='Green')
button1.grid(row=3, column=1, pady=5, padx=5)

button2 = Button(root, text='ON', command=onoff2, fg='Green')
button2.grid(row=3, column=2, pady=5, padx=5)

button3 = Button(root, text='ON',  command=onoff3, fg='Green')
button3.grid(row=3, column=3, pady=5, padx=5)

button4 = Button(root, text='ON',  command=onoff4, fg='Green')
button4.grid(row=3, column=4, pady=5, padx=5)


button5 = Button(root, text='START ALL', command=onoff5, bg='green')
button5.grid(row=4, column=2, columnspan=2, pady=10)


def call_back(url):
    webbrowser.open(url)


# Logo
sblogo = PhotoImage(file='Images/sblogo.png')
sbc = PhotoImage(file='Images/sbc.png')
Label(root, text='Developed by-', font=("Helvetica", 10, "bold italic"),
         padx=5).grid(row=4, column=5)
sb_link = Label(root, padx=5, image=sbc)
sb_link.grid(row=5, column=5)
sb_link.bind("<Button-1>", lambda e: call_back('https://sb-components.co.uk'))


# execution of the program halts
root.tk.call('wm', 'iconphoto', root._w, sblogo)
root.resizable(0, 0)
mainloop()
