import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Student Record")

connection = sqlite3.connect('management.db')

TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")



appLabel = tk.Label(root, text="Student Record System", fg="white", width=40,bg="black")
appLabel.config(font=("Bebas Neue Pro", 50))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(10, 0))

class Student:
    studentName = ""
    collegeName = ""
    phoneNumber = 0
    address = ""

    def __init__(self, studentName, collegeName, phoneNumber, address):
        self.studentName = studentName
        self.collegeName = collegeName
        self.phoneNumber = phoneNumber
        self.address = address

nameLabel = tk.Label(root, text="Enter  Student  Name  :", width=40, anchor='w',
                     font=("Bebas Neue Pro", 20)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0))
collegeLabel = tk.Label(root, text="Enter  Student  Class  :", width=40, anchor='w',
                        font=("Bebas Neue Pro", 20)).grid(row=2, column=0, padx=(10,0))
phoneLabel = tk.Label(root, text="Enter  Student  Phone  Number  :", width=40, anchor='w',
                      font=("Bebas Neue Pro", 20)).grid(row=3, column=0, padx=(10,0))
addressLabel = tk.Label(root, text="Enter  Student  Address  :", width=40, anchor='w',
                        font=("Bebas Neue Pro", 20)).grid(row=4, column=0, padx=(10,0))

nameEntry = tk.Entry(root, width = 30)
collegeEntry = tk.Entry(root, width = 30)
phoneEntry = tk.Entry(root, width = 30)
addressEntry = tk.Entry(root, width = 30)

nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
collegeEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
phoneEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
addressEntry.grid(row=4, column=1, padx=(0,10), pady = 20)

def takeNameInput():
    global nameEntry, collegeEntry, phoneEntry, addressEntry
    # global username, collegeName, phone, address
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + " ) VALUES ( '"
                       + username + "', '" + collegeName + "', '" +
                       address + "', " + str(phone) + " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")



def delll():
    global nameEntry, collegeEntry, phoneEntry, addressEntry
    # global username, collegeName, phone, address
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    
    messagebox.showinfo("Success", "Data Clear Successfully.")


def clse():
    root.destroy()
    return


def destroyRootWindow():
    root.destroy()
    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Student Record System",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()
    
    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="College Name")
    tree.heading("three", text="Address")
    tree.heading("four", text="Phone Number")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()


#llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll

def search():
    root.destroy()
    secondWindow = tk.Tk()
    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Search Student Here",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()


    
    cursor = connection.execute("select * from management_table")
    data=cursor.fetchall()
    connection.close()
    
    for i in data:
        insert(END,str(i)+"\n")

    secondWindow.mainloop()

#llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll


# def printDetails():
#     for singleItem in list:
#         print("Student name is: %s\nCollege name is: %s\nPhone number is: %d\nAddress is: %s" %
#               (singleItem.studentName, singleItem.collegeName, singleItem.phoneNumber, singleItem.address))
#         print("****************************************")

button = tk.Button(root, text="ENTER DATA", command=lambda :takeNameInput())
button.grid(row=5, column=0, pady=30)

button = tk.Button(root, text="CLOSE", command=lambda :clse())
button.grid(row=6, column=0, pady=30) 

button = tk.Button(root, text="CLEAR DATA", command=lambda :delll())
button.grid(row=6, column=1, pady=30)

button = tk.Button(root, text="CLEAR DATA", command=lambda :search())
button.grid(row=7, column=0, pady=30)
displayButton = tk.Button(root, text="DISPLAY DATA", command=lambda :destroyRootWindow())
displayButton.grid(row=5, column=1, pady=30)

root.mainloop() 
