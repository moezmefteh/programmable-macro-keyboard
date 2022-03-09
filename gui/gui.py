import tkinter as tk
from tkinter import *
from tkinter import ttk
key = tk.Tk()  # key window name
key.title('Macro_Keyboard configuration software')  # title Name


    # entry box
    
T = Text(key, height = 1, width = 30)
T.grid(rowspan= 1 , columnspan = 100, ipadx = 999 , ipady = 20)
T1 = Text(key, height = 1, width = 30)
T1.grid(rowspan= 3 , columnspan = 50, ipadx = 55 , ipady = 10)

 





# Size window size
key.geometry('1010x550')         # normal size
key.maxsize(width=1010, height=250)      # maximum size
key.minsize(width= 1010 , height = 250)     # minimum size
# end window size

key.configure(bg = 'orange')    #  add background color

# entry box

# end entry box

# add all button line wise 
def onKeyDown(e):
    # The obvious information
    c = e.keysym
    T.delete('1.0', END)
    s = e.state

    # Manual way to get the modifiers
    ctrl  = (s & 0x4) != 0
    alt   = (s & 0x8) != 0 or (s & 0x80) != 0
    shift = (s & 0x1) != 0

    # Merge it into an output
    # if alt:
    #     c = 'alt+' + c
    if shift:
        c = 'shift+' + c
    if ctrl:
        c = 'ctrl+' + c
    T.insert(tk.END, c)

    # return(T.get("1.0",END))
def WriteConfiguration(notparsed,i,token,curseur):
    import os
    path=os.path.join(os.path.expanduser('~'),'Documents','Arduino','libraries','UNO-HIDKeyboard-Library-master','HIDKeyboard.h')
    f = open(path, 'r')
    list_of_lines =f.readlines()
    if token==0:
        list_of_lines[i+curseur+161]='#define first_'+str(i)+' '+notparsed+'\n'
        list_of_lines[i+curseur+162]='#define second_'+str(i)+' NULL'+'\n'
        list_of_lines[i+curseur+163]='#define third_'+str(i)+' NULL'+'\n'
        list_of_lines[i+curseur+164]='#define token_'+str(i)+' '+str(token)+'\n'

    elif token==1:
        parsed=notparsed.split('+')
        list_of_lines[i+curseur+161]='#define first_'+str(i)+' '+parsed[0]+'\n'
        list_of_lines[i+curseur+162]='#define second_'+str(i)+' '+parsed[1]+'\n'
        list_of_lines[i+curseur+163]='#define third_'+str(i)+' NULL'+'\n'
        list_of_lines[i+curseur+164]='#define token_'+str(i)+' '+str(token)+'\n'

    elif token==2:
        parsed=notparsed.split('+')
        list_of_lines[i+curseur+161]='#define first_'+str(i)+' '+parsed[0]+'\n'
        list_of_lines[i+curseur+162]='#define second_'+str(i)+' '+parsed[1]+'\n'
        list_of_lines[i+curseur+163]='#define third_'+str(i)+' '+parsed[2]+'\n'
        list_of_lines[i+curseur+164]='#define token_'+str(i)+' '+str(token)+'\n'
    f = open(path , 'w')
    f.writelines(list_of_lines)
    f.close()



# x=onKeyDown
def buclick(i):
    notparsed =T.get("1.0",END+'-1c')
    token=notparsed.count("+")
    curseur=0
    if i==1:
        WriteConfiguration(notparsed,i,token,curseur)
    if i==2:
        curseur=3
        WriteConfiguration(notparsed,i,token,curseur) 
    if i==3:
        curseur=6
        WriteConfiguration(notparsed,i,token,curseur)  

        

    # list_of_lines[i+2]='#define first_'+i+"
     
    # print(notparsed.count("+"))

    
    

    # First Line Button
# f.write("define key1 "+str(onKeyDown)
def compile_upload():
    import os
    import subprocess
    path1=os.path.join(os.path.expanduser('~'),'Documents','Arduino','dfu-programmer-win-0.7.2')
    os.chdir(path1)
    # subprocess.call('cd C:\Users\henta\Downloads\Compressed\dfu-programmer-win-0.7.2',shell=True)
    T1.insert(tk.END,"put the keyboard in dfu mode and Press Enter to continue...")
    input()
    subprocess.call('dfu-programmer atmega16u2 erase',shell=True)
    subprocess.call('dfu-programmer atmega16u2 flash Arduino-usbserial-atmega16u2-Uno-Rev3.hex',shell=True)
    subprocess.call('dfu-programmer atmega16u2 reset',shell=True)
    T1.delete('1.0', END)
    T1.insert(tk.END,"plug out then plug in keyboard and press enter to continue...")
    input()
    o=os.popen('arduino-cli board list').read()
    print(o)
    a=o.split()
    print(a)
    port=a[7]
    FQBN=a[14]
    print(FQBN)
    # subprocess.call('cd C:\Users\henta\Downloads\Compressed\dfu-programmer-win-0.7.2',shell=True)
    path2=os.path.join(os.path.expanduser('~'),'Documents','Arduino','code')
    os.chdir(path2)
    command1="arduino-cli compile --fqbn "+FQBN+" macro_keyboard"
    subprocess.call(command1,shell=True)
    command2="arduino-cli upload -p "+port+" --fqbn "+FQBN+" macro_keyboard"
    subprocess.call(command2,shell=True)
    T1.delete('1.0', END)
    T1.insert(tk.END,"put the keyboard in dfu mode and Press Enter to continue...")
    input()
    os.chdir("C:/Users/henta/Downloads/Compressed/dfu-programmer-win-0.7.2")
    subprocess.call('dfu-programmer atmega16u2 erase',shell=True)
    subprocess.call('dfu-programmer atmega16u2 flash Arduino-keyboard-0.3.hex',shell=True)
    subprocess.call('dfu-programmer atmega16u2 reset',shell=True)
    T1.delete('1.0', END)
    T1.insert(tk.END,"plug out then plug in keyboard and enjoy...")
    input()

a = ttk.Button(key,text = '1' , width = 6, )
a.grid(row = 1 , column = 0, ipadx = 6 , ipady = 10)
a.config(command= lambda: buclick(1) )

b = ttk.Button(key,text = '2' , width = 6, command = lambda : buclick(2))
b.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)

c = ttk.Button(key,text = '3' , width = 6, command = lambda : buclick(3))
c.grid(row = 1 , column = 2, ipadx = 6 , ipady = 10)


# Second Line Button



d = ttk.Button(key,text = '4' , width = 6, command = lambda : buclick(4))
d.grid(row = 2 , column = 0, ipadx = 6 , ipady = 10)



e = ttk.Button(key,text = '5' , width = 6, command = lambda : buclick(5))
e.grid(row = 2 , column = 1, ipadx = 6 , ipady = 10)

f = ttk.Button(key,text = '6' , width = 6, command = lambda : buclick(6))
f.grid(row = 2 , column = 2, ipadx = 6 , ipady = 10)



# third line Button

g = ttk.Button(key,text = '7' , width = 6, command = lambda : press('Z'))
g.grid(row = 3 , column = 0, ipadx = 6 , ipady = 10)


h = ttk.Button(key,text = '8' , width = 6, command = lambda : press('X'))
h.grid(row = 3 , column = 1, ipadx = 6 , ipady = 10)


i = ttk.Button(key,text = '9' , width = 6, command = lambda : press('C'))
i.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)







#Fourth Line Button


j = ttk.Button(key,text = '10' , width = 6, command = lambda : press('Ctrl'))
j.grid(row = 4 , column = 0, ipadx = 6 , ipady = 10)


k = ttk.Button(key,text = '11' , width = 6, command = lambda : press('Fn'))
k.grid(row = 4 , column = 1, ipadx = 6 , ipady = 10)


l = ttk.Button(key,text = '12' , width = 6, command = lambda : press('Window'))
l.grid(row = 4 , column = 2 , ipadx = 6 , ipady = 10)



l = ttk.Button(key,text = 'Apply' , width = 6, command = lambda : compile_upload())
l.grid(row = 4 , column = 30 , ipadx = 6 , ipady = 10)







key.bind('<Key>', onKeyDown)


key.mainloop()  # using ending point
