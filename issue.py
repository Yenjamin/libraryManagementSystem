from distutils.command.build_scripts import build_scripts_2to3
from tkinter import *
import database
from tkinter import messagebox

def register(bid, issueto, sub):
    allbids = []
    bids = "select bid from books"
    try:
        database.cur.execute(bids)
        database.con.commit()
        for i in database.cur:
            allbids.append(i[0])
        if bid in allbids:
            checkAvail = "select status from books where bid = '"+bid+"'"
            database.cur.execute(checkAvail)
            database.con.commit()
            for i in database.cur:
                check = i[0]
            if check == 'avail':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")

    insertinto = "insert into issued_books values ('"+bid+"','"+issueto+"')"
    updateStatus = "update books set status = 'issued' where bid = '"+bid+"'"
    try:
        if bid in allbids and status == True:
            database.cur.execute(insertinto)
            database.con.commit()
            database.cur.execute(updateStatus)
            database.con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
        else:
            messagebox.showinfo('Message',"Book Already Issued")
        print(bid)
        print(issueto)
        sub.destroy()
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")

def issue(window):
    sub = Toplevel(window)
    sub.title("Issue Book")
    sub.minsize(width=400,height=400)
    sub.geometry("600x500")

    Canvas1 = Canvas(sub)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(sub,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(sub,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)

    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)

    issueBtn = Button(sub,text="Issue",bg='#d1ccc0', fg='black',command=lambda: register(inf1.get(), inf2.get(), sub))
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(sub,text="Quit",bg='#aaa69d', fg='black', command=sub.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)