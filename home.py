import pygame
import os
from tkinter.filedialog import askdirectory
from tkinter import *
from PIL import Image,ImageTk
import random

root=Tk()
root.title("My_mp3")
f=Frame(root,height=500,width=800,bg="orchid")
f.propagate(0)
f.pack()
img=ImageTk.PhotoImage(Image.open('img3.png'))
l=Label(f,image=img)
l.pack()
l.place(x=390,y=30)
songslist=[]
index=0
stop1=0
shuffle=0
vol=0.5
shufflesongs=[]
lb=Listbox(f,font=("Arial 10"), fg="blue", bg="ivory", height=26, width=35, selectmode=SINGLE)
lb.place(x=20,y=30)
p1=0
def add_songs():
    dir=askdirectory()
    os.chdir(dir)
    for file in os.listdir(dir):
        if file.endswith(".mp3"):
            songslist.append(file)
    for i in songslist:
        lb.insert(END,i)
    
    play(0)
 
    
def on_select(event):
    global index
    pos=lb.curselection()
    index=pos[0]
    playselect(index)
    
def queue(): 
    global stop1
    global shuffle
    global index
    global vol
    pos=pygame.mixer.music.get_pos()
    if stop1==0:
        if pos==-1:
            if(shuffle%2==0):
                index+=1
                if(index==len(songslist)):
                    index=0
                pygame.mixer.music.load(songslist[index])
                pygame.mixer.music.set_volume(vol)
                
                m=Message(f,text=songslist[index],width=450,font=('Courier',-20,'bold'),fg='blue')
                m.place(x=310,y=285) 
                pygame.mixer.music.play(0)
            else:
                index=random.randint(0,len(songslist)-1)
                pygame.mixer.music.load(songslist[index])
                pygame.mixer.music.set_volume(vol)
                m=Message(f,text=songslist[index],width=450,font=('Courier',-20,'bold'),fg='blue')
                m.place(x=310,y=285) 
                pygame.mixer.music.play(0)
                
    pygame.mixer.music.set_volume(vol)
    if stop1==0:
        root.after(1000,queue)
 
        

    
lb.bind('<<ListboxSelect>>',on_select)

def playselect(index):
    b4["bg"]="yellow"
    b3["bg"]="yellow"
    global stop1
    global p1
    global shuffle
    global vol
    stop1=0
    p1=0
    
    pygame.mixer.init()
    
    pygame.mixer.music.load(songslist[index])
    pygame.mixer.music.set_volume(vol)
    m=Message(f,text=songslist[index],width=450,font=('Courier',-20,'bold'),fg='blue')
    m.place(x=310,y=285) 
    pygame.mixer.music.play(0)
    queue()
    
    
def play(index):
    b4["bg"]="yellow"
    b3["bg"]="yellow"
    global stop1
    global p1
    global shuffle
    global vol
    stop1=0
    p1=0
    if shuffle%2==0:
        pygame.mixer.init()
        
        pygame.mixer.music.load(songslist[index])
        pygame.mixer.music.set_volume(vol)
        m=Message(f,text=songslist[index],width=450,font=('Courier',-20,'bold'),fg='blue')
        m.place(x=310,y=285) 
    else:
        pygame.mixer.init()
        index=random.randint(0,len(songslist)-1)
        pygame.mixer.music.load(songslist[index])
        pygame.mixer.music.set_volume(vol)
        m=Message(f,text=songslist[index],width=450,font=('Courier',-20,'bold'),fg='blue')
        m.place(x=310,y=285) 
        
    
    pygame.mixer.music.play(0)
    queue()
    
    
def nextsong():

    global index
    if index==len(songslist)-1:
        index=0
    else:
        index+=1
    play(index)

def stop():
    global stop1
    pygame.mixer.music.stop()
    b3["bg"]="red"
    stop1=1
    print("stop")

    
def presong():
    global index
    if index==0:
        index=len(songslist)-1
    else:
        index-=1
    play(index)
def playpause():
    global p1
    p1+=1
    if p1%2==1:
        pygame.mixer.music.pause()
        b4["bg"]="red"
    else:
        pygame.mixer.music.unpause()
        b4["bg"]="yellow"
        
    
def click(num):
    global shuffle
    global vol
    if num==1:
        presong()
    elif num==2:
        nextsong()
    elif num==3:
        stop()
    elif num==4:
        playpause()
    elif num==5:
        lb.delete(0,END)
        add_songs()
    elif num==6:
        shuffle+=1
        if shuffle%2==1:
            b6["bg"]="red"
        else:
            b6["bg"]="yellow"
    elif num==7:
        if vol<1.0:
            vol+=0.1
        if vol>1.0:
            vol=1.0
    elif num==8:
        if vol>0.0:
            vol-=0.1
        if vol<0.0:
            vol=0.0
        
        
b1=Button(f,text='PREVIOUS',width=10,height=1,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:click(1))
b2=Button(f,text='NEXT',width=10,height=1,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:click(2))
b3=Button(f,text='STOP',width=10,height=1,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:click(3))
b4=Button(f,text='PLAY/PAUSE',width=10,height=1,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:click(4))
b5=Button(f,text='ADD SONGS',width=10,height=1,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:click(5))
b6=Button(f,text='SHUFFLE',width=10,height=1,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:click(6))
b7=Button(f,text='Vol +',width=5,height=1,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:click(7))
b8=Button(f,text='Vol -',width=5,height=1,bg='yellow',fg='blue',activebackground='red',activeforeground='black',command=lambda:click(8))


b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
b8.pack()

b3.place(x=390,y=370)
b1.place(x=290,y=370)
b4.place(x=490,y=370)
b2.place(x=590,y=370)
b5.place(x=690,y=370)
b6.place(x=690,y=230)
b8.place(x=690,y=180)
b7.place(x=690,y=120)

root.mainloop()