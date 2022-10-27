#edit
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from add_class import *
import gotohome as g2h
def geteditdata(top2,first,last,father_first,father_last):
    if first=="" or last=="" or father_first=="" or father_last=="":
        messagebox.showinfo("Data missing!","Please enter the entire data")
    else:
        getEditDataFromDatabase(top2,first.upper(),last.upper(),father_first.upper(),father_last.upper())
        
def editdata():
    
    top2=Tk()
    top2.attributes("-fullscreen", True)
    top2.title('Add Student Data')
    
    homebutton=Button(top2,text="Home",bg='gray',font='Bodoni 36',command=lambda:[top2.destroy(),g2h.gogo()])
    homebutton.pack(fill=X)
    
    student_name=Label(top2,text="Students Name:",font='Bodoni 16')
    student_name.place(x=415,y=130)
    student_first_name=Entry(top2,font='Bodoni 16',width=15)
    student_first_name.place(x=566,y=130)
    student_last_name=Entry(top2,font='Bodoni 16',width=15)
    student_last_name.place(x=766,y=130)

    father_name=Label(top2,text="Fathers Name:",font='Bodoni 16')
    father_name.place(x=415,y=170)
    father_first_name=Entry(top2,font='Bodoni 16',width=15)
    father_first_name.place(x=566,y=170)
    father_last_name=Entry(top2,font='Bodoni 16',width=15)
    father_last_name.place(x=766,y=170)

    editbutton=Button(top2,text="Edit",bg='gray',font='Bodoni 36',command=lambda:geteditdata(top2,student_first_name.get(),
                                                                                       student_last_name.get(),
                                                                                       father_first_name.get(),
                                                                                       father_last_name.get()))
    editbutton.place(x=620,y=220)
    top2.mainloop()
