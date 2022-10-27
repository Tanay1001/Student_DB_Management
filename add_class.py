#add_class
import base64
from PIL import Image
from connect import *
from tkinter import *
from tkinter import messagebox
import gotohome as g2h
from tkcalendar import *
import re
gender=""
filename=""
id_no=1
date=""
def dateSplit(dat):
    global date
    date=dat.split("/",3)
def changeId(r):
    global id_no
    id_no=r
def RadioEvent(r):
    global gender
    if r==1:
        gender="Male"
    elif r==2:
        gender="Female"
    elif r==3:
        gender="Others"
def openimage(top3):
    global filename
    filename=filedialog.askopenfilename(initialdir="/",title="Select A File",filetype=((".gif","*gif"),("All Files","*.*")))
    image_file_name=Label(top3,text=filename,font='Bodoni 11',width=30)
    image_file_name.place(x=502,y=550)
def add2database(top3,first,last,father_first,father_last,mother_first,mother_last,dob,gender,address,phone_gurdian_1,phone_gurdian_2,email_1,email_2,image,stream):
    obj=student(first,last,father_first,father_last,mother_first,mother_last,dob,gender,address,phone_gurdian_1,phone_gurdian_2,email_1,email_2,image,stream)
    if obj.editDataToDatabase():
        if obj.dataUpdate():
            messagebox.showinfo("Data updated!","Data is sucessfully updated")
            top3.destroy()
            g2h.gogo()
class student():
    def __init__(self,first,last,father_first,father_last,mother_first,mother_last,dob,gender,address,phone_gurdian_1,phone_gurdian_2,email_1,email_2,image,stream):
        self.first=first.upper()
        self.last=last.upper()
        self.father_first=father_first.upper()
        self.father_last=father_last.upper()
        self.mother_first=mother_first.upper()
        self.mother_last=mother_last.upper()
        self.dob=dob
        self.gender=gender
        self.address=address
        self.phone_gurdian_1=phone_gurdian_1
        self.phone_gurdian_2=phone_gurdian_2
        self.email_1=email_1
        self.email_2=email_2
        self.image=image
        self.stream=stream     
    def validateEmail(self,email):
        return re.match(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$',email)
    def validatePhoneNo(self,phone):
        return re.match(r'(0|91)?[7-9][0-9]{9}',phone)
    def dataUpdate(self):
        try:
            mycu=mysql.cursor()
            file=open(self.image,'rb').read()
            file=base64.b64encode(file)
            sql="UPDATE `students` SET `first_name`='"+self.first+"',`last_name`='"+self.last+"',`father_first_name`='"+self.father_first+"',`father_last_name`='"+self.father_last+"',`mother_first_name`='"+self.mother_first+"',`mother_last_name`='"+self.mother_last+"',`dob`='"+self.dob+"',`gender`='"+self.gender+"',`address`='"+self.address+"',`phone_gurdian_1`='"+self.phone_gurdian_1+"',`phone_gurdian_2`='"+self.phone_gurdian_2+"',`email_address_1`='"+self.email_1+"',`email_address_2`='"+self.email_2+"',`stream`='"+self.stream+"' WHERE `id`="+str(id_no)+""
            mycu.execute(sql)
            mysql.commit()
            return True
        except Exception:
            messagebox.showwarning("Database connectivity error!","Unable to add data to the database")
            return False
    def dataAdded(self):
        try:
            mycu=mysql.cursor()
            file=open(self.image,'rb').read()
            file=base64.b64encode(file)
            args=(self.first,self.last,self.father_first,self.father_last,self.mother_first,self.mother_last,self.dob,self.gender,self.address,self.phone_gurdian_1,self.phone_gurdian_2,self.email_1,self.email_2,file,self.stream)
            sql="insert into `students`(`first_name`, `last_name`, `father_first_name`, `father_last_name`, `mother_first_name`, `mother_last_name`, `dob`, `gender`, `address`, `phone_gurdian_1`, `phone_gurdian_2`, `email_address_1`, `email_address_2`, `image`, `stream`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycu.execute(sql,args)
            mysql.commit()
            return True
        except Exception:
            messagebox.showwarning("Database connectivity error!","Unable to add data to the database")
            return False
    def editDataToDatabase(self):
        if self.first=="":
            messagebox.showinfo("Data missing!","Please enter the first name of the student")
            return False
        elif self.last=="":
            messagebox.showinfo("Data missing!","Please enter the last name of the student")
            return False
        elif self.mother_first=="":
            messagebox.showinfo("Data missing!","Please enter the first name of the student's mother or guradian")
            return False
        elif self.mother_last=="":
            messagebox.showinfo("Data missing!","Please enter the last name of the student's mother or guradian")
            return False
        elif self.father_first=="":
            messagebox.showinfo("Data missing!","Please enter the first name of the student's father or guradian")
            return False
        elif self.father_last=="":
            messagebox.showinfo("Data missing!","Please enter the last name of the student's father or guradian")
            return False
            
        elif self.gender=="":
            messagebox.showinfo("Data missing!","Please select gender")
            return False
            
        elif self.phone_gurdian_1=="" and self.phone_gurdian_2=="":
            messagebox.showinfo("Data missing!","At least one phone number is required")
            return False
        
        elif self.phone_gurdian_1!="" and not(self.validatePhoneNo(self.phone_gurdian_1)):
            messagebox.showinfo("Data invalid!","Please enter valid phone number")
            return False
        elif self.phone_gurdian_2!="" and not(self.validatePhoneNo(self.phone_gurdian_2)):
            messagebox.showinfo("Data invalid!","Please enter valid phone number")
            return False
            
        elif self.email_1=="" and self.email_2=="":
            messagebox.showinfo("Data missing!","At least one email is required")
            return False

        elif self.email_1!="" and not(self.validateEmail(self.email_1)):
            messagebox.showinfo("Data invalid!","Please enter valid email")
            return False
        elif self.email_2!="" and not(self.validateEmail(self.email_2)):
            messagebox.showinfo("Data invalid!","Please enter valid email")
            return False
            
        elif self.stream=="SELECT":
            messagebox.showinfo("Data missing!","Please select stream")
            return False
        elif self.image=="":
            self.image='Temp.gif'
            return True
        else:
            return True
    def addDataToDatabase(self):
        if self.first=="":
            messagebox.showinfo("Data missing!","Please enter the first name of the student")
            return False
        elif self.last=="":
            messagebox.showinfo("Data missing!","Please enter the last name of the student")
            return False
        elif self.mother_first=="":
            messagebox.showinfo("Data missing!","Please enter the first name of the student's mother or guradian")
            return False
        elif self.mother_last=="":
            messagebox.showinfo("Data missing!","Please enter the last name of the student's mother or guradian")
            return False
        elif self.father_first=="":
            messagebox.showinfo("Data missing!","Please enter the first name of the student's father or guradian")
            return False
        elif self.father_last=="":
            messagebox.showinfo("Data missing!","Please enter the last name of the student's father or guradian")
            return False
            
        elif self.gender=="":
            messagebox.showinfo("Data missing!","Please select gender")
            return False
            
        elif self.phone_gurdian_1=="" and self.phone_gurdian_2=="":
            messagebox.showinfo("Data missing!","At least one phone number is required")
            return False
        
        elif self.phone_gurdian_1!="" and not(self.validatePhoneNo(self.phone_gurdian_1)):
            messagebox.showinfo("Data invalid!","Please enter valid phone number")
            return False
        elif self.phone_gurdian_2!="" and not(self.validatePhoneNo(self.phone_gurdian_2)):
            messagebox.showinfo("Data invalid!","Please enter valid phone number")
            return False
            
        elif self.email_1=="" and self.email_2=="":
            messagebox.showinfo("Data missing!","At least one email is required")
            return False

        elif self.email_1!="" and not(self.validateEmail(self.email_1)):
            messagebox.showinfo("Data invalid!","Please enter valid email")
            return False
        elif self.email_2!="" and not(self.validateEmail(self.email_2)):
            messagebox.showinfo("Data invalid!","Please enter valid email")
            return False
            
        elif self.dob=="1/1/03":
            messagebox.showinfo("Data missing!","Please select the date of birth")
            return False
            
        elif self.stream=="SELECT":
            messagebox.showinfo("Data missing!","Please select stream")
            return False
        elif self.image=="":
            messagebox.showinfo("Data missing!","Please select image")
            return False
        else:
            return True
def dataExistence(first,last,father_first,father_last):
    mycursor=mysql.cursor()
    mycursor.execute("select * from students")
    data=mycursor.fetchall()
    for i in data:
        if i[1]==first and i[2]==last and i[3]==father_first and i[4]==father_last:
            return True
    return False
'''
print(i[1])
cursor=mysql.cursor()
query="select image from students where first_name='"+i[1]+"'"
cursor.execute(query)
data=cursor.fetchall()
image=data[0][0]
binary_data=base64.b64decode(image)
image=Image.open(io.BytesIO(binary_data))
image.show()
'''
def deleteRecord(first,last,father_first,father_last):
    mycu=mysql.cursor()
    sql="DELETE FROM `students` WHERE first_name='"+first+"' AND last_name='"+last+"' AND father_first_name='"+father_first+"' AND father_last_name='"+father_last+"'"
    mycu.execute(sql)
    mysql.commit()
    return True
def getEditDataFromDatabase(top2,first,last,father_first,father_last):
    if dataExistence(first,last,father_first,father_last):
        top2.destroy()
        mycursor=mysql.cursor()
        mycursor.execute("select * from students")
        data=mycursor.fetchall()
        for i in data:
            if i[1]==first and i[2]==last and i[3]==father_first and i[4]==father_last:
                top3=Tk()
                top3.attributes("-fullscreen", True)
                top3.title('Edit Student Data')
                changeId(i[0])

                homebutton=Button(top3,text="Home",bg='gray',font='Bodoni 36',command=lambda:[top3.destroy(),g2h.gogo()])
                homebutton.pack(fill=X)

                clearbutton=Button(top3,text="Delete Record",bg='gray',font='Bodoni 36',command=lambda:[top3.destroy(),deleteRecord(first,last,father_first,father_last),g2h.gogo()])
                clearbutton.pack(fill=X)

                student_name=Label(top3,text="Students Name:",font='Bodoni 16')
                student_name.place(x=150,y=200)
                student_first_name=Entry(top3,font='Bodoni 16',width=15)
                student_first_name.place(x=302,y=200)
                student_last_name=Entry(top3,font='Bodoni 16',width=15)
                student_last_name.place(x=502,y=200)
                student_first_name.insert(0,str(i[1]))
                student_last_name.insert(0,str(i[2]))

                mother_name=Label(top3,text="Mothers Name:",font='Bodoni 16')
                mother_name.place(x=150,y=245)
                mother_first_name=Entry(top3,font='Bodoni 16',width=15)
                mother_first_name.place(x=302,y=245)
                mother_last_name=Entry(top3,font='Bodoni 16',width=15)
                mother_last_name.place(x=502,y=245)
                mother_first_name.insert(0,str(i[5]))
                mother_last_name.insert(0,str(i[6]))

                father_name=Label(top3,text="Fathers Name:",font='Bodoni 16')
                father_name.place(x=150,y=290)
                father_first_name=Entry(top3,font='Bodoni 16',width=15)
                father_first_name.place(x=302,y=290)
                father_last_name=Entry(top3,font='Bodoni 16',width=15)
                father_last_name.place(x=502,y=290)
                father_first_name.insert(0,str(i[3]))
                father_last_name.insert(0,str(i[4]))
                
                gender_name=Label(top3,text="Gender:",font='Bodoni 16')
                gender_name.place(x=702,y=200)
                r=IntVar()
                if str(i[8])=="Male":
                    RadioEvent(1)
                elif str(i[8])=="Female":
                    RadioEvent(2)
                else:
                    RadioEvent(3)
                Radiobutton(top3,text="Male",variable=r,value=1,font='Bodoni 16',height=1,width=8,indicatoron=0,command=lambda:RadioEvent(r.get())).place(x=842,y=200)
                Radiobutton(top3,text="Female",variable=r,value=2,font='Bodoni 16',height=1,width=8,indicatoron=0,command=lambda:RadioEvent(r.get())).place(x=992,y=200)
                Radiobutton(top3,text="Others",variable=r,value=3,font='Bodoni 16',height=1,width=8,indicatoron=0,command=lambda:RadioEvent(r.get())).place(x=1142,y=200)

                contact_no=Label(top3,text=gender,font='Bodoni 16')
                contact_no.place(x=850,y=250)
                
                contact_no=Label(top3,text="Contact:",font='Bodoni 16')
                contact_no.place(x=150,y=335)
                contact_no_1=Entry(top3,font='Bodoni 16',width=15)
                contact_no_1.place(x=302,y=335)
                contact_no_2=Entry(top3,font='Bodoni 16',width=15)
                contact_no_2.place(x=502,y=335)
                contact_no_1.insert(0,str(i[10]))
                contact_no_2.insert(0,str(i[11]))

                email_id=Label(top3,text="Email:",font='Bodoni 16')
                email_id.place(x=702,y=335)
                email_id_1=Entry(top3,font='Bodoni 16',width=15)
                email_id_1.place(x=823,y=335)
                email_id_2=Entry(top3,font='Bodoni 16',width=15)
                email_id_2.place(x=1032,y=335)
                email_id_1.insert(0,str(i[12]))
                email_id_2.insert(0,str(i[13]))

                address_label=Label(top3,text="Address:",font='Bodoni 16')
                address_label.place(x=150,y=390)
                address=Text(top3,font='Bodoni 16',width=32,height=4)
                address.place(x=302,y=390)
                address.insert(INSERT,str(i[9]))
                
                stream_label=Label(top3,text="Stream:",font='Bodoni 16')
                stream_label.place(x=150,y=510)
                streams_list=['SELECT','COMPUTER','CIVIL','ELECTRONICS','MECHANICAL']
                c=StringVar()
                droplist=OptionMenu(top3,c,*streams_list)
                droplist.config(width=15)
                if i[15]=='COMPUTER':
                    c.set(streams_list[1])
                if i[15]=='CIVIL':
                    c.set(streams_list[2])
                if i[15]=='ELECTRONICS':
                    c.set(streams_list[3])
                if i[15]=='MECHANICAL':
                    c.set(streams_list[4])
                droplist.place(x=302,y=510)

                image_label=Label(top3,text="Passport size image:",font='Bodoni 16')
                image_label.place(x=150,y=550)
                image_button=Button(top3,text="Select Image",font='Bodoni 16',command=lambda:openimage(top3))
                image_button.place(x=360,y=550)

                dob_label=Label(top3,text="Date of birth:",font='Bodoni 16')
                dob_label.place(x=702,y=390)

                dateSplit(str(i[7]))
                
                cal=Calendar(top3,selectmode="day",year=int(date[2]),month=int(date[0]),day=int(date[1]))
                cal.place(x=850,y=390)

                submit=Button(top3,text="Update",bg='gray',font='Bodoni 36',command=lambda:add2database(top3,student_first_name.get(),
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

                top3.mainloop()
                
    else:
        messagebox.showinfo("Data not found!","Data does not exist")
        
