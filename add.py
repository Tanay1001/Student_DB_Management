#add
from tkinter import *
from tkinter import filedialog
from tkcalendar import *
from add_class import *
import gotohome as g2h
gender=""
filename=""

def RadioEvent(r):
    global gender
    if r==1:
        gender="Male"
    elif r==2:
        gender="Female"
    elif r==3:
        gender="Others"
def openimage(top2):
    global filename
    filename=filedialog.askopenfilename(initialdir="/",title="Select A File",filetype=((".gif","*gif"),("All Files","*.*")))
    image_file_name=Label(top2,text=filename,font='Bodoni 11',width=30)
    image_file_name.place(x=502,y=550)
def add2database(top2,first,last,father_first,father_last,mother_first,mother_last,dob,gender,address,phone_gurdian_1,phone_gurdian_2,email_1,email_2,image,stream):
    obj=student(first,last,father_first,father_last,mother_first,mother_last,dob,gender,address,phone_gurdian_1,phone_gurdian_2,email_1,email_2,image,stream)
    if obj.addDataToDatabase():
        if obj.dataAdded():
            messagebox.showinfo("Data added!","Data is sucessfully added")
            top2.destroy()
            g2h.gogo()
def adddata():
    top2=Tk()
    top2.attributes("-fullscreen", True)
    
    top2.title('Add Student Data')
    
    homebutton=Button(top2,text="Home",bg='gray',font='Bodoni 36',command=lambda:[top2.destroy(),g2h.gogo()])
    homebutton.pack(fill=X)

    clearbutton=Button(top2,text="Clear",bg='gray',font='Bodoni 36',command=lambda:[top2.destroy(),adddata()])
    clearbutton.pack(fill=X)
    
    student_name=Label(top2,text="Students Name:",font='Bodoni 16')
    student_name.place(x=150,y=200)
    student_first_name=Entry(top2,font='Bodoni 16',width=15)
    student_first_name.place(x=302,y=200)
    student_last_name=Entry(top2,font='Bodoni 16',width=15)
    student_last_name.place(x=502,y=200)
    
    mother_name=Label(top2,text="Mothers Name:",font='Bodoni 16')
    mother_name.place(x=150,y=245)
    mother_first_name=Entry(top2,font='Bodoni 16',width=15)
    mother_first_name.place(x=302,y=245)
    mother_last_name=Entry(top2,font='Bodoni 16',width=15)
    mother_last_name.place(x=502,y=245)

    duplicate_button_1=Button(top2,text="Duplicate surname",font='Bodoni 10',command=lambda:[mother_last_name.delete(0,END)
                                                                                             ,mother_last_name.insert(0,str(student_last_name.get()))])
    duplicate_button_1.place(x=700,y=245)

    father_name=Label(top2,text="Fathers Name:",font='Bodoni 16')
    father_name.place(x=150,y=290)
    father_first_name=Entry(top2,font='Bodoni 16',width=15)
    father_first_name.place(x=302,y=290)
    father_last_name=Entry(top2,font='Bodoni 16',width=15)
    father_last_name.place(x=502,y=290)

    duplicate_button_1=Button(top2,text="Duplicate surname",font='Bodoni 10',command=lambda:[father_last_name.delete(0,END)
                                                                                             ,father_last_name.insert(0,str(student_last_name.get()))])
    duplicate_button_1.place(x=700,y=290)
    
    father_name=Label(top2,text="Gender:",font='Bodoni 16')
    father_name.place(x=702,y=200)
    r=IntVar()
    Radiobutton(top2,text="Male",variable=r,value=1,font='Bodoni 16',height=1,width=8,indicatoron=0,command=lambda:RadioEvent(r.get())).place(x=842,y=200)
    Radiobutton(top2,text="Female",variable=r,value=2,font='Bodoni 16',height=1,width=8,indicatoron=0,command=lambda:RadioEvent(r.get())).place(x=992,y=200)
    Radiobutton(top2,text="Others",variable=r,value=3,font='Bodoni 16',height=1,width=8,indicatoron=0,command=lambda:RadioEvent(r.get())).place(x=1142,y=200)

    contact_no=Label(top2,text="Contact:",font='Bodoni 16')
    contact_no.place(x=150,y=335)
    contact_no_1=Entry(top2,font='Bodoni 16',width=15)
    contact_no_1.place(x=302,y=335)
    contact_no_2=Entry(top2,font='Bodoni 16',width=15)
    contact_no_2.place(x=502,y=335)

    email_id=Label(top2,text="Email:",font='Bodoni 16')
    email_id.place(x=702,y=335)
    email_id_1=Entry(top2,font='Bodoni 16',width=20)
    email_id_1.place(x=775,y=335)
    #email_id_1.place(x=823,y=335)
    email_id_2=Entry(top2,font='Bodoni 16',width=20)
    email_id_2.place(x=1032,y=335)
    #email_id_2.place(x=1032,y=335)

    address_label=Label(top2,text="Address:",font='Bodoni 16')
    address_label.place(x=150,y=390)
    address=Text(top2,font='Bodoni 16',width=32,height=4)
    address.place(x=302,y=390)

    stream_label=Label(top2,text="Stream:",font='Bodoni 16')
    stream_label.place(x=150,y=510)
    streams_list=['SELECT','COMPUTER','CIVIL','ELECTRONICS','MECHANICAL']
    c=StringVar()
    droplist=OptionMenu(top2,c,*streams_list)
    droplist.config(width=15)
    c.set(streams_list[0])
    droplist.place(x=302,y=510)

    image_label=Label(top2,text="Passport size image:",font='Bodoni 16')
    image_label.place(x=150,y=550)
    image_button=Button(top2,text="Select Image",font='Bodoni 16',command=lambda:openimage(top2))
    image_button.place(x=360,y=550)
    
    dob_label=Label(top2,text="Date of birth:",font='Bodoni 16')
    dob_label.place(x=702,y=390)
    
    cal=Calendar(top2,selectmode="day",year=2003,month=1,day=1)
    cal.place(x=850,y=390)
    
    submit=Button(top2,text="Submit",bg='gray',font='Bodoni 36',command=lambda:add2database(top2,student_first_name.get(),
                                                                                            student_last_name.get(),
                                                                                            father_first_name.get(),
                                                                                            father_last_name.get(),
                                                                                            mother_first_name.get(),
                                                                                            mother_last_name.get(),
                                                                                            cal.get_date(),
                                                                                            gender,
                                                                                            address.get(1.0,END),
                                                                                            contact_no_1.get(),
                                                                                            contact_no_2.get(),
                                                                                            email_id_1.get(),
                                                                                            email_id_2.get(),
                                                                                            filename,c.get()))
    submit.place(x=590,y=625)

    top2.mainloop()
