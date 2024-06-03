import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser
global gender_var

def button1():
    global w1,tt4,tt5,gender_var
    name=tt4.get()
    sel=tt5.get()
    uh=tt10.get()
    select=w1.get()
    hyy=gender_var.get()
    
    if name!="" and sel!="" and select!="" and hyy!="" and uh=="DEEPCODERS":
        if hyy == "MALE":
            greeting = "Mr."
        elif hyy == "FEMALE":
            greeting = "Mrs."
        else:
            greeting = "" 
        success_message = f"Success! {greeting} {name}, Your Account Has Been Created Successfully!"
        
        messagebox.showinfo("STATUS", success_message)
        
        
        if select == "PYTHON":
            webbrowser.open('https://www.python.org/')
        elif select == "C":
            webbrowser.open('https://www.geeksforgeeks.org/c-programming-language/')
        elif select == "JAVA":
            webbrowser.open('https://www.javatpoint.com/java-tutorial')
        elif select == "DJANGO":
            webbrowser.open('https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django')
        elif select == "MACHINE LEARNING":
            webbrowser.open('https://www.geeksforgeeks.org/machine-learning/')
        elif select == "MERN STACK":
            webbrowser.open('https://www.geeksforgeeks.org/mern-stack-development-roadmap/')
        elif select == "FRONTEND":
            webbrowser.open('https://www.w3schools.com/whatis/whatis_frontenddev.asp')
        elif select == "BACKEND":
            webbrowser.open('https://www.geeksforgeeks.org/back-end-developer-roadmap/')
        elif select == "SQL AND DATABASE":
            webbrowser.open('https://www.geeksforgeeks.org/learn-sql-and-database/?ref=shm')
        elif select == "MONGODB":
            webbrowser.open('https://www.geeksforgeeks.org/mongodb-tutorial/?ref=shm')
        elif select == "C++":
            webbrowser.open('https://www.geeksforgeeks.org/learn-cpp-programming-step-by-step-a-20-day-curriculum/')
        else:
            messagebox.showinfo("STATUS","SORRY,COURSE IS NOT AVAILABLE!")
    else:         
        message = ""
    
    if name == "":
        message += "Fill the Name Field.\n"
    if sel == "":
        message += "Fill the Surname Field.\n"
    if select == "":
        message += "Select a Course.\n"
    if hyy == "":
        message += "Select a Gender.\n"
    if uh == "":
        message += "Fill the Pre-Defined Password"
    if uh != "" and uh != "DEEPCODERS":
        message += "Invalid Password"
    if message != "":
        messagebox.showinfo("STATUS", message)

def base2():
    root.destroy()
    
    root1=tkinter.Tk()
    root1.title("CREATE ACCOUNT")
    root1.geometry("400x400")
    root1.configure(bg="lightblue")
    label3=tkinter.Label(root1,text="NAME:",background="lightblue")
    label3.grid(column=0,row=0)

    #entry
    global tt4
    tt4=Entry(root1,width=20)
    tt4.grid(row=0,column=1)

    label4=tkinter.Label(root1,text="SURNAME:",background="lightblue")
    label4.grid(column=0,row=1)

    #entry
    global tt5
    tt5=Entry(root1,width=20)
    tt5.grid(row=1,column=1)
    
    label10=tkinter.Label(root1,text="PRE-DEFINED PASSWORD:",background="lightblue")
    label10.grid(column=0,row=2)
    #entry
    global tt10
    tt10=Entry(root1,width=20)
    tt10.grid(row=2,column=1)
    
    label7=tkinter.Label(root1,text="GENDER:",background="lightblue")
    label7.grid(row=3,column=0)
    global gender_var
    gender_var=tkinter.StringVar()
    rb=Radiobutton(root1,text="MALE",variable=gender_var,value=1,background="lightblue").grid(row=3,column=1,padx=(0,10))
    rb1=Radiobutton(root1,text="FEMALE",variable=gender_var,value=2,background="lightblue").grid(row=3,column=2,padx=(0,10))
    rb2=Radiobutton(root1,text="OTHERS",variable=gender_var,value=3,background="lightblue").grid(row=3,column=3)
    
    
    label8=tkinter.Label(root1,text="AVAILABLE COURSES:",background="lightblue")
    label8.grid(row=4,column=0)
    n=tkinter.StringVar()
    global w1
    w1=ttk.Combobox(root1,width=27,textvariable=n)
    w1['values']=("PYTHON",
                      "C",
                      "C++",
                      "JAVA",
                      "DJANGO",
                      "TKINTER",
                      "MACHINE LEARNING",
                      "BACKEND",
                      "FRONTEND",
                      "MERN STACK",
                      "SQL AND DATABASE",
                      "MONGODB")
    w1.grid(row=4,column=1)
    w1.current()
    
    
    bs=Button(root1,text="DONE",bg="black",fg="white",command=button1).grid(column=1,row=5)
 ##main    
    
root=tkinter.Tk()
root.title("basic")
root.geometry("400x400")
root.configure(bg="lightblue")
#1ST PART CREATE ACC OR LOGIN ACC

#1ST entry

label2=tkinter.Label(root,text="HIII GUYS..",font=("Times new Roman",8)).grid(row=0,column=0,padx=10,pady=10)
root.columnconfigure(0,weight=1)
label11=tkinter.Label(root,text="HERE , DEEPVIBER03..!",font=("Times new Roman",15)).grid(row=1,column=0,padx=10,pady=10)
root.columnconfigure(0,weight=1)
labbel=tkinter.Label(root,text="->THIS  PROJECT  MAINLY  HELPS  YOU  TO  CHOOSE  ROADMAP  FOR  YOUR  CHOOSEN  COURSE !")
labbel.grid(row=2,column=0)
label1=tkinter.Label(root,text="CREATE ACCOUNT:   --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->")
label1.grid(column=0,row=3,padx=10,pady=10,sticky="w")
b1=Button(root,text="CLICK HERE",bg="black",fg="white",command=base2).grid(column=1,row=3,padx=10,pady=10,sticky="e")

root.mainloop()