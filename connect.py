import mysql.connector as my
from tkinter import messagebox
import io
try:
    mysql=my.connect(host='localhost',
                     user='root',
                     passwd='',
                     database='student_info')
except:
    messagebox.showwarning("Database connectivity error!","Unable to connect to the database")
