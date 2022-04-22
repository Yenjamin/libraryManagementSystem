from tkinter import *
import database
from tkinter import messagebox

def register(bid, title, author, status, sub):
    status = status.lower()

    insertBooks = "insert into books values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        database.cur.execute(insertBooks)
        database.con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)
    print(status)
    sub.destroy()

def addBook(window):
    sub = Toplevel(window)
    sub.title("Add Book")
    sub.minsize(width=400,height=400)
    sub.geometry("600x500")

    Canvas1 = Canvas(sub)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(sub,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(sub,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    lb1 = Label(labelFrame,text="Book ID: ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    lb2 = Label(labelFrame,text="Title: ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    SubmitBtn = Button(sub,text="SUBMIT",bg='#d1ccc0', fg='black',command=lambda: register(bookInfo1.get(), bookInfo2.get(), bookInfo3.get(), bookInfo4.get(), sub))
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(sub,text="Quit",bg='#f7f1e3', fg='black', command=sub.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)