import database
from tkinter import *
from tkinter import messagebox

def register(bid, sub):
    deleteSql = "delete from books where bid = '"+bid+"'"
    deleteIssue = "delete from issued_books where bid = '"+bid+"'"
    try:
        database.cur.execute(deleteSql)
        database.con.commit()
        database.cur.execute(deleteIssue)
        database.con.commit()
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")

    print(bid)
    sub.destroy()

def delete(window):
    sub = Toplevel(window)
    sub.title("Delete Book")
    sub.minsize(width=400,height=400)
    sub.geometry("600x500")

    Canvas1 = Canvas(sub)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(sub,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Delete Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(sub,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)

    SubmitBtn = Button(sub,text="SUBMIT",bg='#d1ccc0', fg='black',command=lambda: register(bookInfo1.get(), sub))
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    quitBtn = Button(sub,text="Quit",bg='#f7f1e3', fg='black', command=sub.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)