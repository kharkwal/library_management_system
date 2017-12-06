import tkinter.messagebox as tm
import pymysql
import win32com.client
import datetime
from datetime import date
#===========================================student login page=====================================================
def login():
   root=Tk()
   root.state("zoom")
   root.geometry("1200x1000")
   root.configure(bg="blue")
   f1=Frame(root,height=200,width=1200,bd=14,relief="raise")
   f1.pack(side=TOP)
   f2=Frame(root,height=500,width=300,bd=9,relief="raise")
   f2.pack()
   label2=Label(f1,font=("arial",35,"bold"),text="""LIBRARY MANAGEMENT SYSTEM
     SUTUDENT LOGIN""")
   label2.grid()
   label=Label(f2,text="Student ID",font=("arial",15))
   label.grid(row=0)
   label1=Label(f2,text="Password",font=('arial',15))
   label1.grid(row=1)
   entry=Entry(f2)
   entry1=Entry(f2,show="*")
   entry.grid(row=0,column=1)
   entry1.grid(row=1,column=1)
   button=Button(f2,text="SUBMIT")
   button.grid(row=2,column=1)
   root.mainloop()
#============================================admin login page==================================================================
def admin():
    def admin_login():
        admin_user_id=entry.get()
        admin_password=entry1.get()
        conn=pymysql.connect("localhost","root","kharkwal","library_management")
        cur=conn.cursor()
        cur.execute("select USER_ID,PASSWORD from admin")
        x=cur.fetchone()
        user=x[0]
        passw=x[1]
        if admin_user_id==user and admin_password==passw:

            pass

        else:
            tm.showwarning("Login alert!","User id or password is wrong.")
            return

        root = Tk()
        root.state("zoom")
        root.geometry("1200x1000")
        root.configure(bg="blue")
        speak = win32com.client.Dispatch("SAPI.SpVoice")
        voice = ("hello amardeep welcome in library management system")
        speak.Speak(voice)

        def search_book():

            root = Tk()
            root.title("Book search")
            root.state("zoom")
            root.geometry("1050x900")
            bookList=list()
            def searchBookItems():
                bookName=E1.get()
                conn=pymysql.connect("localhost","root","kharkwal","library_management")
                cur1=conn.cursor()
                search_q="select * from bd where bn='"+bookName+"'"
                # print(search_q)
                cur1.execute(search_q)
                totalBooks=cur1.fetchall()
                bookList=list()
                if(len(totalBooks)>0):
                    for i,bookItem in enumerate(totalBooks):
                        print(i+1,bookItem[0],bookItem[1],bookItem[2],bookItem[3])
                        l7.config(text=bookItem[2])
                        l8.config(text=bookItem[1])
                        l9.config(text=bookItem[3])
                        l10.config(text=bookItem[4])
                        #l12.config(text=bookItem[2])











            f1 = Frame(root, height=200, width=700, bd=12, relief="raise")
            f2 = Frame(root, height=400, width=1050, bd=8, relief="raise")
            l1 = Label(f1, text="BOOK NAME", font=("arial", 20, "bold"), justify="center", relief="sunken").grid()
            E1 = Entry(f1, font=("arial", 20, "bold"), justify="center", relief="sunken")
            E1.grid(row=1)
            b1 = Button(f1, font=("arial", 20, "bold"), text="search",command=searchBookItems).grid(row=2)
            l2 = Label(f2, text="ISBN", font=("arial", 17, "bold"), relief="sunken", justify="center", width=10).grid(
                row=0,
                column=0,
                padx=20)
            l3 = Label(f2, text="Book title", font=("arial", 17, "bold"), relief="sunken", justify="center",
                       width=10).grid(
                row=0, column=1, padx=20)
            l4 = Label(f2, text="Author name", font=("arial", 17, "bold"), relief="sunken", justify="center",
                       width=10).grid(
                row=0, column=2, padx=20)
            l5 = Label(f2, text="Edition", font=("arial", 17, "bold"), relief="sunken", justify="center",
                       width=10).grid(row=0,
                                      column=3,
                                      padx=20)
            l6 = Label(f2, text="Availablity", font=("arial", 17, "bold"), relief="sunken", justify="center",
                       width=10).grid(
                row=0, column=4, padx=20)
            #var1 = IntVar()
            #var2 = StringVar()
            #var3 = StringVar()
            #var4 = IntVar()
            #var1.set(bookList[0][0])
            #var2.set(bookList[0][1])
            #var3.set(bookList[0][2])
            #var4.set(bookList[0][3])

            l7 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15,)
            l7.grid(row=1, column=0, padx=20)
            l8 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15,)
            l8.grid(row=1, column=1,padx=20)
            l9 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15)
            l9.grid(row=1,column=2,padx=20)
            l10 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15)
            l10.grid(row=1,column=3,padx=20)
            l11 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15)
            l11.grid(row=1,column=4,padx=20)
            l12 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15)
            l12.grid(row=2, column=0,padx=20)

            l13 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15)
            l13.grid(row=2, column=1,padx=20)

            l14 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15)
            l14.grid(row=2, column=2,padx=20)

            l15 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15)
            l15.grid(row=2, column=3,padx=20)

            l16 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15)
            l16.grid(row=2, column=4,padx=20)

            l17 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15,
                        ).grid(row=3, column=0,padx=20)

            l18 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15,
                        ).grid(row=3, column=1,padx=20)

            l19 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15,
                        ).grid(row=3, column=2,padx=20)

            l20 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15,
                        ).grid(row=3, column=3,padx=20)

            l21 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15,
                        ).grid(row=3, column=4,padx=20)

            l22 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15,
                        ).grid(row=4, column=0,padx=20)

            l23 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15,
                       ).grid(row=4, column=1,padx=20)

            l24 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15,
                        ).grid(row=4, column=2,padx=20)

            l25 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15,
                        ).grid(row=4, column=3,padx=20)

            l26 = Label(f2, font=("arial", 17, "bold"), relief="sunken", justify="center", width=15,
                        ).grid(row=4, column=4,padx=20)


            f1.pack()
            f2.pack(padx=30)

            root.mainloop()

        f1 = Frame(root, width=1200, height=100, bd=14, relief="raise")
        f1.pack(side=TOP)
        l1 = Label(f1, font=("arial", 45, "bold"), text="LIBRARY MANAGEMENT SYSTEM", bd=15, fg="white", bg="black")
        l1.grid(row=0, column=0)
        f2 = Frame(root, height=900, width=700, bd=14, relief="raise")
        b1 = Button(f2, text="Manage Membership", bg="black", fg="white", bd=10, font=("arial", 20),
                    command=manage_membership).grid(row=0)
        b2 = Button(f2, text="Manage Book", bg="black", fg="white", bd=10, font=("arial", 20),
                    command=manage_book).grid(row=1)
        b3 = Button(f2, text="Search Book", bg="black", fg="white", bd=10, font=("arial", 20),
                    command=search_book).grid(row=2)
        b4 = Button(f2, text="Manage Borrower", bg="black", fg="white", bd=10, font=("arial", 20),
                    command=manage_borrower).grid(row=3)
        b5 = Button(f2, text="Manage Report", bg="black", fg="white", bd=10, font=("arial", 20)).grid(row=4)
        b6 = Button(f2, text="LOGOUT", bg="red", fg="white", bd=10, font=("arial", 20), command=exit).grid(row=5,
                                                                                                           pady=30)
        f2.configure(bg="black")
        f2.pack()
        root.mainloop()

    root = Tk()
    root.state("zoom")
    root.geometry("1200x1000")
    root.configure(bg="blue")
    f1 = Frame(root, height=200, width=1100, bd=14, relief="raise")
    f1.pack(side=TOP)
    f2 = Frame(root, height=500, width=300, bd=9, relief="raise")
    f2.pack()
    label2 = Label(f1, font=("arial", 35, "bold"), text="""LIBRARY MANAGEMENT SYSTEM
         ADMIN LOGIN""")
    label2.grid()
    label = Label(f2, text="Admin ID", font=("arial", 15))
    label.grid(row=0)
    label1 = Label(f2, text="Password", font=('arial', 15))
    label1.grid(row=1)
    entry = Entry(f2)
    entry1 = Entry(f2, show="*")
    entry.grid(row=0, column=1)
    entry1.grid(row=1, column=1)
    button = Button(f2, text="SUBMIT", command=admin_login)
    button.grid(row=2, column=1)
    root.mainloop()
#=====================================admin window==============================================================================

#===========================================Manage Borrower====================================================================
def manage_borrower():
    def borrow_book():
        root = Tk()
        root.state("zoom")
        root.geometry("1200x1000")
        root.configure(bg="blue")

        def borrow():
            var1 = ee1.get()
            var2 = ee2.get()
            var3 = ee3.get()
            var4 = ee4.get()
            var5 = ee5.get()
            bs = datetime.date.today()
            rd = datetime.date.today() + datetime.timedelta(7)
            conn = pymysql.connect("localhost", "root", "kharkwal", "library_management")
            cur = conn.cursor()
            add = "insert into sd(si,bn,department,sn,isbn,bd,rd) values(%s,'%s','%s','%s',%s,'%s','%s')" % (
                str(var1), str(var3), str(var4), str(var2), str(var5), bs, rd)
            print(add)
            cur.execute(add)
            conn.commit()
            print(cur)






        f1 = Frame(root, height=100, width=1200, bd=14, relief="ra"
                                                               "ise")
        f1.pack(side=TOP)
        f2 = Frame(root, height=200, width=500, bd=14, relief="raise")
        f2.pack(pady=15)
        f3 = Frame(root, height=400, width=400, bd=14, relief="raise")
        f3.pack(side=LEFT)
        f4 = Frame(root, height=400, width=400, bd=14, relief="raise")
        f4.pack(side=RIGHT)
        f1.configure(bg="black")
        f2.configure(bg="black")
        f3.configure(bg="black")
        f4.configure(bg="black")
        ll1 = Label(f1, text="BORROW BOOK", font=("arial", 40, "bold"), bg="cyan").grid()
        ll2 = Label(f3, text="BOOK NAME", font=("arial", 30, "bold"), bg="cyan").grid(row=2)
        ll3 = Label(f3, text="DEPARTMENT", font=("arial", 30, "bold"), bg="cyan").grid(row=4)
        ll4 = Label(f2, text="STUDENT ID", font=("arial", 30, "bold"), bg="cyan").grid(row=0)
        ll5 = Label(f3, text="NAME", font=("arial", 30, "bold"), bg="cyan").grid(row=0)
        ll6 = Label(f4, text="ISBN NUMBER", font=("arial", 30, "bold"), bg="cyan").grid(row=0)
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = StringVar()

        ee1 = Entry(f2, font=("arial", 20, "bold"), textvariable=var1)
        ee1.grid(row=1, pady=10)
        ee2 = Entry(f3, font=("arial", 20, "bold"), textvariable=var2)
        ee2.grid(row=1, pady=10)
        ee3 = Entry(f3, font=("arial", 20, "bold"), textvariable=var3)
        ee3.grid(row=3, pady=10)
        ee4 = Entry(f3, font=("arial", 20, "bold"), textvariable=var4)
        ee4.grid(row=5, pady=10)
        ee5 = Entry(f4, font=("arial", 20, "bold"), textvariable=var5)
        ee5.grid(row=1, pady=10)
        bb1 = Button(f4, text="BORROW", font=("arial", 25, 'bold'), command=borrow, bg="red")
        bb1.grid(row=2, pady=15)

        root.mainloop()
    root=Tk()
    root.state("zoom")
    root.geometry("1200x1000")
    root.configure(bg="blue")
    f1=Frame(root,height=100,width=1200,bd=14,relief="raise")
    f1.pack(side=TOP)
    f2=Frame(root,height=800,width=400,bd=14,relief="raise")
    f2.pack()
    f1.configure(bg="black")
    f2.configure(bg="black")
    l1=Label(f1,text="MANAGE BORROWERS",font=("arial",40,"bold"),bg="cyan")
    l1.grid()
    b1=Button(f2,text="BORROW BOOK",font=("arial",25,"bold"),command=borrow_book,bg="cyan")
    b1.grid(row=0,column=0,pady=20,padx=20)
    b2=Button(f2,text="BORROWER'S LIST",font=("arial",25,"bold"),bg="cyan",command=borrowers_list)
    b2.grid(row=1,column=0,pady=20,padx=20)
    b3=Button(f2,text="RETURN BOOK",font=("arial",25,"bold"),bg="cyan",command=return_book)
    b3.grid(row=2,column=0,pady=20,padx=20)
    root.mainloop()
#============================================borrowers list===========================================================================================================
def borrowers_list():
    root=Tk()
    root.state("zoom")
    root.geometry("1200x1000")
    root.configure(bg="blue")
    f1=Frame(root,height=100,width=1200,bd=14,relief="raise")
    f1.pack(side=TOP)
    f2=Frame(root,height=600,width=1200,bd=10,relief="raise")
    f2.pack()
    l1=Label(f1,text="Borrow List",font=("arial",40,"bold"),bg="cyan").grid()
    l2=Label(f2,text="Student ID",font=("arial",17,),bg="cyan",relief="sunken",justify="center",width=11).grid(row=0,column=0,padx=5)
    l3=Label(f2,text="Name",font=("arial",17,),bg="cyan",relief="sunken",justify="center",width=11).grid(row=0,column=1,padx=5)
    l4=Label(f2,text="Batch",font=("arial",17,),bg="cyan",relief="sunken",justify="center",width=11).grid(row=0,column=2,padx=5)
    l5=Label(f2,text="Department",font=("arial",17,),bg="cyan",relief="sunken",justify="center",width=11).grid(row=0,column=3,padx=5)
    l6=Label(f2,text="ISBN",font=("arial",17,),bg="cyan",relief="sunken",justify="center",width=11).grid(row=0,column=4,padx=5)
    l7=Label(f2,text="Borrow Date",font=("arial",17,),bg="cyan",relief="sunken",justify="center",width=11).grid(row=0,column=5,padx=5)
    l8=Label(f2,text="Return Date",font=("arial",17,),bg="cyan",relief="sunken",justify="center",width=11).grid(row=0,column=6,padx=5)
    l9=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=1,column=0,padx=5)
    l10=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=1,column=1,padx=5)
    l11=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=1,column=2,padx=5)
    l12=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=1,column=3,padx=5)
    l13=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=1,column=4,padx=5)
    l14=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=1,column=5,padx=5)
    l15=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=1,column=6,padx=5)
    l16=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=2,column=0,padx=5)
    l17=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=2,column=1,padx=5)
    l18=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=2,column=2,padx=5)
    l19=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=2,column=3,padx=5)
    l20=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=2,column=4,padx=5)
    l21=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=2,column=5,padx=5)
    l22=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=2,column=6,padx=5)
    l23=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=3,column=0,padx=5)
    l24=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=3,column=1,padx=5)
    l25=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=3,column=2,padx=5)
    l26=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=3,column=3,padx=5)
    l27=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=3,column=4,padx=5)
    l28=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=3,column=5,padx=5)
    l29=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=3,column=6,padx=5)
    l30=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=4,column=0,padx=5)
    l31=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=4,column=1,padx=5)
    l32=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=4,column=2,padx=5)
    l33=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=4,column=3,padx=5)
    l34=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=4,column=4,padx=5)
    l35=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=4,column=5,padx=5)
    l36=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=4,column=6,padx=5)
    l37=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=5,column=0,padx=5)
    l38=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=5,column=1,padx=5)
    l39=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=5,column=2,padx=5)
    l40=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=5,column=3,padx=5)
    l41=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=5,column=4,padx=5)
    l42=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=5,column=5,padx=5)
    l43=Label(f2,font=("arial",17,"bold"),relief="sunken",justify="center",width=11).grid(row=5,column=6,padx=5)

    root.mainloop()
#========================================borrow book=============================================================================================================


#========================================RETURN BOOK=============================================================================================================
def return_book():
    root = Tk()
    root.state('zoom')
    root.geometry("1100x900")

    def return1_book():
        x = st_id.get()
        print(x)
        conn1 = pymysql.connect("localhost", "root", "kharkwal", "library_management")
        cur = conn1.cursor()
        p = 'select * from sd where si='+str(x)
        cur.execute(p)
        p1 = cur.fetchall()
        for i, std in enumerate(p1):
            l17.config(text=std[4])
            l18.config(text=std[2])
            l19.config(text=std[5])
            l10.config(text=std[2])
            l11.config(text=std[4])
            l12.config(text=std[5])
        d0 = datetime.date.today()
        d1 = d0
        d2 = std[5]
        fine = d1 - d2
        k = fine.days
        print(fine.days)
        print(d0)
        l13.config(text=d1)
        l14.config(text=str(fine.days) + " days")
        charges = k * 2
        l15.config(text="Rs. " + str(charges))

    def cancel():
        x = st_id.get()
        conn = pymysql.connect("localhost", "root", "kharkwal", "library_management")
        cur = conn.cursor()
        p = 'select * from sd where si=' + x
        cur.execute(p)
        p1 = cur.fetchall()
        for i, std in enumerate(p1):
            l17.config(text=std[4])
            l18.config(text=std[2])
        cur1 = conn.cursor()
        p1 = 'delete from sd where isbn=' + str(std[2])
        cur1.execute(p1)
        conn.commit()

    f1 = Frame(root, width=400, height=80, bd=14, relief="raise")
    f2 = Frame(root, width=600, height=200, bd=14, relief="raise")
    f3 = Frame(root, width=500, height=700, bd=14, relief="raise")
    f4 = Frame(root, width=500, height=700, bd=14, relief="raise")
    f5 = Frame(f4, width=200, height=100, relief="sunken")
    f6 = Frame(f4, width=500, height=600, relief="raise")
    f7 = Frame(f4, width=500, height=100, relief="sunken")
    l1 = Label(f1, text="RETURN BOOK", font=("arial", 40, "bold"), relief="sunken", justify="center")
    l1.grid()
    l2 = Label(f2, text="STUDENT ID", font=("arial", 30, "bold"), relief="sunken", justify="center",
               width=30)
    l2.grid(row=0, column=0)

    st_id = StringVar()
    e1 = Entry(f2, textvariable=st_id, font=("arial", 30, "bold"), width=30)
    e1.grid(row=1, column=0)
    bbb1 = Button(f2, font=("arial", 20, "bold"), text="search", width=20, command=return1_book).grid(row=2,
                                                                                                      column=0)
    l3 = Label(f3, text="RETURN INFO", font=("arial", 35, "bold"), relief="sunken", justify="center").grid(
        row=0)
    l4 = Label(f3, text="ISBN:", font=("arial", 20, "bold"), relief="sunken", width=10).grid(row=1,
                                                                                             column=0)
    l5 = Label(f3, text="Borrow Date:", font=("arial", 20, "bold"), relief="sunken", width=10).grid(row=2,
                                                                                                    column=0)
    l6 = Label(f3, text="Return Date:", font=("arial", 20, "bold"), relief="sunken", width=10).grid(row=3,
                                                                                                    column=0)
    l7 = Label(f3, text="Today Date:", font=("arial", 20, "bold"), relief="sunken", width=10).grid(row=4,
                                                                                                   column=0)
    l8 = Label(f3, text="Late:", font=("arial", 20, "bold"), relief="sunken", width=10).grid(row=5,
                                                                                             column=0)
    l9 = Label(f3, text="Late fee:", font=("arial", 20, "bold"), relief="sunken", width=10).grid(row=6,
                                                                                                 column=0)
    bb1 = Button(f3, text="RETURN", font=("arial", 20, "bold"), width=10, bg="blue", command=cancel).grid(
        row=7,
        column=1,
        pady=20)
    l10 = Label(f3, font=("arial", 20, "bold"), relief="sunken", width=8)
    l10.grid(row=1, column=1)
    l11 = Label(f3, font=("arial", 20, "bold"), relief="sunken", width=8)
    l11.grid(row=2, column=1)
    l12 = Label(f3, font=("arial", 20, "bold"), relief="sunken", width=8)
    l12.grid(row=3, column=1)
    l13 = Label(f3, font=("arial", 20, "bold"), relief="sunken", width=8)
    l13.grid(row=4, column=1)
    l14 = Label(f3, font=("arial", 20, "bold"), relief="sunken", width=8)
    l14.grid(row=5, column=1)
    l15 = Label(f3, font=("arial", 20, "bold"), relief="sunken", width=8)
    l15.grid(row=6, column=1)
    l17 = Label(f6, text="ISBN", font=("arial", 20, "bold"), relief="sunken", width=10)
    l17.grid(row=0, column=0, padx=5)
    l18 = Label(f6, text="Borrow Date", font=("arial", 20, "bold"), relief="sunken", width=10)
    l18.grid(row=0, column=1, padx=5)

    l19 = Label(f6, text="Return Date", font=("arial", 20, "bold"), relief="sunken", width=10)
    l19.grid(row=0, column=2, padx=5)

    l16 = Label(f5, text="Borrowed Book", font=("arial", 40, "bold"), relief="sunken").grid()
    b1 = Button(f7, font=("arial", 20, "bold"), width=32, command=return_book).grid(row=0, column=0)
    l17 = Label(f7, font=("arial", 15, "bold"), width=10, relief="sunken")
    l17.grid(row=0, columnspan=1)
    l18 = Label(f7, font=("arial", 15, "bold"), width=10, relief="sunken")
    l18.grid(row=0, stick="w", padx=5)
    l19 = Label(f7, font=("arial", 15, "bold"), width=10, relief="sunken")
    l19.grid(row=0, sticky="e", padx=5)
    b2 = Button(f7, font=("arial", 20, "bold"), width=32).grid(row=1, column=0, pady=5)
    l20 = Label(f7, font=("arial", 15, "bold"), width=10, relief="sunken").grid(row=1, columnspan=1)
    l21 = Label(f7, font=("arial", 15, "bold"), width=10, relief="sunken").grid(row=1, stick="w", padx=5)
    l22 = Label(f7, font=("arial", 15, "bold"), width=10, relief="sunken").grid(row=1, sticky="e", padx=5)
    b3 = Button(f7, font=("arial", 20, "bold"), width=32).grid(row=2, column=0, pady=5)
    l23 = Label(f7, font=("arial", 15, "bold"), width=10, relief="sunken").grid(row=2, columnspan=1)
    l24 = Label(f7, font=("arial", 15, "bold"), width=10, relief="sunken").grid(row=2, stick="w", padx=5)
    l25 = Label(f7, font=("arial", 15, "bold"), width=10, relief="sunken").grid(row=2, sticky="e", padx=5)
    b4 = Button(f7, font=("arial", 20, "bold"), width=32).grid(row=3, column=0, pady=5)
    l26 = Label(f7, font=("arial", 15, "bold"), width=10, relief="sunken").grid(row=3, columnspan=1)
    l27 = Label(f7, font=("arial", 15, "bold"), width=10, relief="sunken").grid(row=3, stick="w", padx=5)
    l28 = Label(f7, font=("arial", 15, "bold"), width=10, relief="sunken").grid(row=3, sticky="e", padx=5)

    f1.pack(side=TOP)
    f2.pack(side=TOP)
    f3.pack(side=LEFT)
    f4.pack(side=RIGHT)
    f5.grid(row=0)
    f6.grid(row=1)
    f7.grid(row=2)

    root.mainloop()


#==========================================SEARCH BOOK===================================================================================================================


 #================================================MANAGE MEMEBERSHIP========================================================================================================
def manage_membership():
    root = Tk()
    root.geometry("1100x900")
    root.state("zoom")

    def add_membership():
        root1= Tk()
        root1.geometry("1100x900")
        root1.state("zoom")

        def add_membership1():
            e11=e1.get()
            e22=e2.get()
            e33=e3.get()
            e44=e4.get()
            e55=e5.get()
            e66=e6.get()
            var22=r1.get()
            var11=r2.get()
            conn=pymysql.connect("localhost","root","kharkwal","library_management")
            cur=conn.cursor()
            add="insert into STUDENTS_RECORD(STUDENT_ID,STUDENT_NAME,DEPARTMENT,CONTACT,EMAIL,PASSWORD,MEMBERSHIP) values("+str(e11)+",' "+e66+" ' ,' "+e22+" ',"+str(e33)+",' "+e44+" ',' "+e55+" ',' "+var11+" ',' "+var22+" ')"

            cur.execute(add)
            conn.commit()
            cur.close()
            conn.close()


        f1 = Frame(root1, height=100, width=600, relief="raise", bd=10)
        f2 = Frame(root1, height=800, width=600, relief="raise", bd=10)
        l1 = Label(f1, text="ADD MEMBERSHIP", font=("arial", 35, "bold")).grid()
        l2 = Label(f2, text="Student ID :", font=("arial", 20, "bold")).grid(row=0, column=0)
        l2 = Label(f2, text="Student Name :", font=("arial", 20, "bold")).grid(row=1, column=0)

        l3 = Label(f2, text="Department :", font=("arial", 20, "bold")).grid(row=2, column=0)
        l4 = Label(f2, text="Contact no. :", font=("arial", 20, "bold")).grid(row=3, column=0)
        l5 = Label(f2, text="email id :", font=("arial", 20, "bold")).grid(row=4, column=0)
        l6 = Label(f2, text="password :", font=("arial", 20, "bold")).grid(row=5, column=0)
        l7 = Label(f2, text="MEMBERSHIP", font=("arial", 20, "bold")).grid(row=6, column=0, pady=20)

        var11=StringVar()
        var22=StringVar()

        r2 = Radiobutton(f2, text="1 Year", font=("arial", 20, "bold"), width=10, value="1 year",variable=var11)
        r2.grid(row=8, column=0 )
        r1 = Radiobutton(f2, text="6 Month", font=("arial", 20, "bold"), relief="sunken", width=10, value="6 months",variable=var22)
        r1.grid(row=7, column=0 )
        e11=IntVar()
        e22=StringVar()
        e33=IntVar()
        e44=StringVar()
        e55=StringVar()
        e66=StringVar()
        e1 = Entry(f2, font=("arial", 20, "bold"), textvariable=e11)
        e1.grid(row=0, column=1)
        e6 = Entry(f2, font=("arial", 20, "bold"), textvariable=e66)
        e6.grid(row=1, column=1)

        e2 = Entry(f2, font=("arial", 20, "bold"), textvariable=e22)
        e2.grid(row=2, column=1)
        e3 = Entry(f2, font=("arial", 20, "bold"), textvariable=e33)
        e3.grid(row=3, column=1)
        e4 = Entry(f2, font=("arial", 20, "bold"), textvariable=e44)
        e4.grid(row=4, column=1)
        e5 = Entry(f2, font=("arial", 20, "bold"), textvariable=e55)
        e5.grid(row=5, column=1)

        b1 = Button(f2, text="ADD", font=("arial", 20, "bold"), bg="blue",command=add_membership1)
        b1.grid(row=8, column=1)


        f1.pack(side=TOP)
        f2.pack()
        root1.mainloop()
    f1 = Frame(root, height=100, width=500, relief="raise", bd=10)
    f2 = Frame(root, height=600, width=400, relief="raise")
    l1 = Label(f1, text="MANAGE MEMEBERSHIP", font=("arial", 40, "bold")).pack()
    b1 = Button(f2, text="ADD MEMBERSHIP", font=("arial", 25, "bold"), width=20, bg="blue",command=add_membership).grid(row=0, pady=10)
    b1 = Button(f2, text="UPDATE MEMBERSHIP", font=("arial", 25, "bold"), width=20, bg="blue",command=update_membership).grid(row=1, pady=10)

    f1.pack(side=TOP, pady=15)
    f2.pack(pady=10)
    root.mainloop()
#=========================================ADD MEMEBERSHIP==========================================================================================================


 #=========================================UPDATE MEMEBERSHIP=====================================================================================================
def update_membership():
    root = Tk()
    v = IntVar()
    root.geometry("1100x900")
    root.state("zoom")
    f1 = Frame(root, height=100, width=600, relief="sunken", bd=5)
    f2 = Frame(root, height=900, width=600, relief="sunken", bd=5)
    f3 = Frame(root, height=100, width=600, relief="raise")
    l1 = Label(f1, text="UPDATE MEMBERSHIP", font=("arial", 35, "bold")).grid()
    l2 = Label(f3, text="Student ID", font=("arial", 25, "bold")).grid(row=0, padx=10)
    e1 = Entry(f3, font=("arial", 20, "bold")).grid(row=1, pady=10)
    l3 = Label(f2, text="Student Name :", relief="sunken", width=15, font=("arial", 20, "bold")).grid(row=1, column=0)
    l3 = Label(f2, text="Department :", relief="sunken", width=15, font=("arial", 20, "bold")).grid(row=2, column=0)
    l4 = Label(f2, text="Contact no. :", relief="sunken", width=15, font=("arial", 20, "bold")).grid(row=3, column=0)
    l5 = Label(f2, text="email id :", relief="sunken", width=15, font=("arial", 20, "bold")).grid(row=4, column=0)
    l6 = Label(f2, text="MEMBERSHIP", font=("arial", 20, "bold")).grid(row=5, column=0, pady=20)
    var1=StringVar()
    var2=StringVar()
    r2 = Radiobutton(f2, text="1 Year", font=("arial", 20, "bold"),variable=var1,value="1 year" ,relief="sunken", width=10)
    r2.grid(row=7, column=0 )
    r1 = Radiobutton(f2, text="6 Month", font=("arial", 20, "bold"), variable=var2,value="6 months",relief="sunken", width=10)
    r1.grid(row=6, column=0 )
    b1 = Button(f2, text="Extend", font=("arial", 20, "bold"), bg="blue").grid(row=8, column=0)
    b1 = Button(f2, text="Cancel", font=("arial", 20, "bold"), bg="blue").grid(row=8, column=1)
    l6 = Label(f2, font=("arial", 20, "bold"), relief="sunken", width=15).grid(row=1, column=1, pady=5, padx=5)
    l6 = Label(f2, font=("arial", 20, "bold"), relief="sunken", width=15).grid(row=2, column=1, pady=5, padx=5)
    l6 = Label(f2, font=("arial", 20, "bold"), relief="sunken", width=15).grid(row=4, column=1, pady=5, padx=5)
    l6 = Label(f2, font=("arial", 20, "bold"), relief="sunken", width=15).grid(row=3, column=1, pady=5, padx=5)

    f1.pack(side=TOP)
    f3.pack(side=TOP)
    f2.pack()
    root.mainloop()


#======================================================MANAGE BOOK============================================================================================================

def manage_book():
    root = Tk()
    root.geometry("1100x900")
    root.state("zoom")
    root.config(bg="black")



    # ========================================================================ADD NEW BOOK=========================================================================================
    def add_new_book():
        root_new_book = Tk()
        root_new_book.geometry("1100x900")
        root_new_book.state("zoom")
        root_new_book.config(bg="black")

        def new_book():
            e_id = e111.get()
            e_book = e222.get()
            e_isbn = e333.get()
            e_author = e444.get()
            e_edition = e555.get()
            conn = pymysql.connect("localhost", "root", "kharkwal", "library_management")
            curl = conn.cursor()
            sq = "INSERT INTO bd VALUES(" + str(e_id) + ",'" + e_book + "'," + str(e_isbn) + ",'" + e_author + "'," + str(e_edition) + ")"
            print(sq)
            curl.execute(sq)
            conn.commit()
            curl.close()
            conn.close()





        f1 = Frame(root_new_book, height=100, width=500, relief="raise", bd=10, bg="blue")
        f2 = Frame(root_new_book, height=500, width=500, relief="raise", bd=10, bg="blue")
        l1 = Label(f1, text="ADD NEW BOOK", font=("arial", 40, "bold"), bg="blue").pack()
        l2 = Label(f2, text="ID :", font=("arial", 25, "bold"), width=15, bg="blue").grid(row=0, column=0)
        l3 = Label(f2, text="Book Title :", font=("arial", 25, "bold"), width=15, bg="blue").grid(row=1, column=0)
        l4 = Label(f2, text="ISBN :", font=("arial", 25, "bold"), width=15, bg="blue").grid(row=2, column=0)
        l5 = Label(f2, text="Author Name:", font=("arial", 25, "bold"), width=15, bg="blue").grid(row=3, column=0)
        l6 = Label(f2, text="EDITION:", font=("arial", 25, "bold"), width=15, bg="blue").grid(row=4, column=0)
        id_n = IntVar()
        book_n = StringVar()
        isbn_n = IntVar()
        author_n = StringVar()
        Edition = IntVar()
        e111 = Entry(f2, font=("arial", 25, "bold"), textvariable=id_n, width=15)
        e111.grid(row=0, column=1)
        e222 = Entry(f2, font=("arial", 25, "bold"), textvariable=book_n, width=15)
        e222.grid(row=1, column=1)
        e333 = Entry(f2, font=("arial", 25, "bold"), textvariable=isbn_n, width=15)
        e333.grid(row=2, column=1)
        e444 = Entry(f2, font=("arial", 25, "bold"), textvariable=author_n, width=15)
        e444.grid(row=3, column=1)
        e555 = Entry(f2, font=("arial", 25, "bold"), textvariable=Edition, width=15)
        e555.grid(row=4, column=1)

        b1 = Button(f2, text="Submit", font=("arial", 25, "bold"), bg="red", command=new_book).grid(row=5)

        f1.pack(side=TOP, pady=20)
        f2.pack(pady=20)
        root_new_book.mainloop()

    # ====================================================EDIT BOOK INFORMATION==================================================================================================

    f1 = Frame(root, height=100, width=500, relief="raise", bd=10, bg="blue")
    f2 = Frame(root, height=500, width=500, relief="raise", bd=10, bg="blue")
    l1 = Label(f1, text="MANAGE BOOK", font=("arial", 40, "bold"), bg="blue").pack()
    b1 = Button(f2, text="Add New Book", font=("arial", 30, "bold"), bg="white",command=add_new_book).grid(row=0, column=0, pady=20, padx=20)
    b2 = Button(f2, text="Edit Book Information", font=("arial", 30, "bold"), bg="white").grid(row=1, column=0, pady=20,
                                                                                               padx=20)

    f1.pack(side=TOP, pady=20)
    f2.pack(pady=20)
    root.mainloop()



#==========================================







#=======================================management system===========================================================================================================

from tkinter import*

root = Tk()
root.state("zoom")

root.geometry("1200x1000")
root.configure(bg="black")
f1 = Frame(root, height=160, width=1200, bd=14, relief="raise")
f1.pack(side=TOP)
f2 = Frame(root, height=400, width=500, bd=12, relief="raise")
f2.pack(side=LEFT)
f3 = Frame(root, height=400, width=500, bd=12, relief="raise")
f3.pack(side=RIGHT)
f11 = Frame(f1, height=120, width=900, bd=9, relief="raise")
f11.pack()
f12 = Frame(f2, height=300, width=400, bd=9, relief="raise")
f12.pack()
f13 = Frame(f3, height=300, width=400, bd=9, relief="raise")
f13.pack()
f1.configure(bg="blue")
f3.configure(bg="blue")
f2.configure(bg="blue")
l1 = Label(f11, text="WELCOME IN LIBRARY MANAGEMENT SYSTEM", font=("arial", 35, "bold"), bd=10)
l1.grid(row=0, column=0)
b1 = Button(f12, text="Student Login", font=("arial", 20, "bold"), command=login)
b1.grid()
b2 = Button(f13, text="Admin Login", font=("arial", 20, "bold"), command=admin)
b2.grid()

root.mainloop()
