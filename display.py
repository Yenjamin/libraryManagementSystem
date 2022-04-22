from tkinter import *
from PIL import ImageTk,Image
import add
import delete
import view
import issue
import returnb

class display(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Library")
        self.minsize(width=400,height=400)
        self.geometry("600x500")

        n = 0.25
        same = True
        bg =Image.open("lib.jpg")
        [iWidth, iHeight] = bg.size
        newWidth = int(iWidth*n)
        if same:
            newHeight = int(iHeight*n) 
        else:
            newHeight = int(iHeight/n)
        bg = bg.resize((newWidth,newHeight),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(bg)
        
        Canvas1 = Canvas(self)
        Canvas1.create_image(300,340,image = img)      
        Canvas1.config(bg="white",width = newWidth, height = newHeight)
        Canvas1.pack(expand=True,fill=BOTH)

        headingFrame1 = Frame(self,bg="#FFBB00",bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
        headingLabel = Label(headingFrame1, text="Welcome to \n The Library", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

        btn1 = Button(self,text="Add Book",bg='black', fg='white', command=lambda: add.addBook(self))
        btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        btn2 = Button(self,text="Delete Book",bg='black', fg='white', command=lambda: delete.delete(self))
        btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        btn3 = Button(self,text="View Book List",bg='black', fg='white', command=lambda: view.view(self))
        btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
        btn4 = Button(self,text="Issue Book",bg='black', fg='white', command =lambda: issue.issue(self))
        btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
        btn5 = Button(self,text="Return Book",bg='black', fg='white', command =lambda: returnb.returnb(self))
        btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

        self.mainloop()