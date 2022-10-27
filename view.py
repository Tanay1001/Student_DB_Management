#view student data page
#view.py
from tkinter import *
import base64
from PIL import Image
from connect import *
from tkinter import messagebox
import gotohome as g2h
def ShowTheImage(r):
    mycursor=mysql.cursor()
    mycursor.execute("select * from students")
    data=mycursor.fetchall()
    for i in data:
        if i[0]==int(r):
            cursor=mysql.cursor()
            query="select image from students where id='"+r+"'"
            cursor.execute(query)
            data=cursor.fetchall()
            image=data[0][0]
            binary_data=base64.b64decode(image)
            image=Image.open(io.BytesIO(binary_data))
            image.show()
def showdet(r):
    mycursor=mysql.cursor()
    mycursor.execute("select * from students")
    data2=mycursor.fetchall()
    
    newwindow=Tk()
    newwindow.geometry("1000x500")
    newwindow.title('Student details')
    for i in data2:
        if r==i[0]:
            
            #det_label=Label(newwindow,text="Students Full Name:",font='Bodoni 16')
            #det_label.pack()
            name="Student: "+str(i[1])+" "+str(i[2])+" "
            det_label=Label(newwindow,text=name,font='Bodoni 16')
            det_label.pack()

            #det_label=Label(newwindow,text="Fathers Full Name:",font='Bodoni 16')
            #det_label.pack()
            name="Father: "+str(i[3])+" "+str(i[4])+" "
            det_label=Label(newwindow,text=name,font='Bodoni 16')
            det_label.pack()

            #det_label=Label(newwindow,text="Mothers Full Name:",font='Bodoni 16')
            #det_label.pack()
            name="Mother: "+str(i[5])+" "+str(i[6])+" "
            det_label=Label(newwindow,text=name,font='Bodoni 16')
            det_label.pack()

            #det_label=Label(newwindow,text="Date of Birth:",font='Bodoni 16')
            #det_label.pack()
            name="DOB: "+str(i[7])+" "
            det_label=Label(newwindow,text=name,font='Bodoni 16')
            det_label.pack()

            #det_label=Label(newwindow,text="Gender:",font='Bodoni 16')
            #det_label.pack()
            name="Gender: "+str(i[8])+" "
            det_label=Label(newwindow,text=name,font='Bodoni 16')
            det_label.pack()

            name="Contact: "+str(i[10])+" "+str(i[11])+" "
            det_label=Label(newwindow,text=name,font='Bodoni 16')
            det_label.pack()

            #det_label=Label(newwindow,text="Email Id:",font='Bodoni 16')
            #det_label.pack()
            name="Email: "+str(i[12])+" "+str(i[13])+" "
            det_label=Label(newwindow,text=name,font='Bodoni 16')
            det_label.pack()

            #det_label=Label(newwindow,text="Stream:",font='Bodoni 16')
            #det_label.pack()
            name="Stream: "+str(i[15])+" "
            det_label=Label(newwindow,text=name,font='Bodoni 16')
            det_label.pack()

            det_label=Label(newwindow,text="Address:",font='Bodoni 16')
            det_label.pack()
            name=" "+str(i[9])+" "
            det_label=Label(newwindow,text=name,font='Bodoni 16')
            det_label.pack()

            #det_label=Label(newwindow,text="Phone Numbers:",font='Bodoni 16')
            #det_label.pack()
            
            
            det_button=Button(newwindow,text="View Image",font='Bodoni 16',command=lambda i=i:ShowTheImage(str(i[0])))
            det_button.pack()

            

    newwindow.mainloop()
def showdata():
    
    window=Tk()
    window.attributes("-fullscreen", True)
    
    homebutton=Button(window,text="Home",bg='gray',font='Bodoni 36',command=lambda:[window.destroy(),g2h.gogo()])
    homebutton.pack(fill=X)

    heading_label=Label(window,text="Id",font='Bodoni 16')
    heading_label.place(x=360,y=110)

    heading_label=Label(window,text="Name",font='Bodoni 16')
    heading_label.place(x=530,y=110)

    heading_label=Label(window,text="Surname",font='Bodoni 16')
    heading_label.place(x=700,y=110)

    heading_label=Label(window,text="More details",font='Bodoni 16')
    heading_label.place(x=870,y=110)

    mycursor=mysql.cursor()
    mycursor.execute("select * from students")
    data=mycursor.fetchall()
    
    y1=160

    
    
    for i in data:
        student_id=Label(window,text=str(i[0]),font='Bodoni 16')
        student_id.place(x=360,y=y1)

        student_name=Label(window,text=str(i[1]),font='Bodoni 16')
        student_name.place(x=530,y=y1)

        student_surname=Label(window,text=str(i[2]),font='Bodoni 16')
        student_surname.place(x=700,y=y1)

        student_moredet=Button(window,text="More details",font='Bodoni 16',command=lambda i=i:showdet(i[0]))
        student_moredet.place(x=870,y=y1)

        y1=y1+50
    window.mainloop()
