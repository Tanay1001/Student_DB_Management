#Home page home.py
from view import *
from add import *
from edit import *
from tkinter import *

def home():
    win=Tk()
    win.attributes("-fullscreen", True)
    win.title('Home')

    canvas=Canvas(win,height=700,width=800)
    canvas.pack()

    try:
        background_image=PhotoImage(file='backgrd.gif')
        background_label=Label(canvas,image=background_image)
        background_label.pack()
    except:
        pass

    frame=Frame(win,bg='#bff56e',border='3px')
    frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

    welcomeLabel=Label(frame,text="WELCOME",bg='#bff56e',font='Bodoni 36')
    welcomeLabel.pack(fill=X)

    welcomeLabel=Label(frame,text="",bg='#bff56e',font='Bodoni 36')
    welcomeLabel.pack(fill=X)

    viewbutton=Button(frame,text="View Student Data",bg='gray',font='Bodoni 36',command=lambda:[win.destroy(),showdata()])
    viewbutton.pack(fill=X)

    addbutton=Button(frame,text="Add Student Data",bg='gray',font='Bodoni 36',command=lambda:[win.destroy(),adddata()])
    addbutton.pack(fill=X)

    editbutton=Button(frame,text="Edit Existing Data",bg='gray',font='Bodoni 36',command=lambda:[win.destroy(),editdata()])
    editbutton.pack(fill=X)

    closebutton=Button(frame,text="Close",bg='gray',font='Bodoni 36',command=win.destroy)
    closebutton.pack(fill=X)
    win.mainloop()
home()
