
from cgitb import text
from pickle import OBJ
from struct import pack
from tkinter import *
from tkinter import ttk

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("library management system")
        self.root.geometry("1550x800+0+0")
        
 
        lbtitle=Label(self.root,text="Library Management System",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new romen",50,"bold"),padx=2,pady=6)
        lbtitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)
        #=============================================================dataframe left===========================================================#
        DataFrameLeft=LabelFrame(frame,text="Library Members details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new romen",12,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=900,height=350)
        
        lblmember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblmember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,state="readonly",font=("arial",12,"bold"),width=27)
        comMember["value"]=("Admin Staff", "student","Lecturer")
        comMember.grid(row=0,column=1)
        
        LBLPRN_NO=Label(DataFrameLeft,bg="powder blue",text="Prn no", font=("times new roman",12,"bold"),padx=2,pady=6)
        LBLPRN_NO.grid(row=1,column=0,sticky=W)
        TXTPRN_NO=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        TXTPRN_NO.grid(row=1,column=1)
        
         
        LblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No", font=("times new roman",12,"bold"),padx=2,pady=6)
        LblTitle.grid(row=2,column=0,sticky=W)
        LblTitle=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        LblTitle.grid(row=2,column=1)
        
         
        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="FirstName", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        lblFirstName=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblFirstName.grid(row=3,column=1)
        
        
        lblLatName=Label(DataFrameLeft,bg="powder blue",text="Last Name", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblLatName.grid(row=4,column=0,sticky=W)
        lblLatName=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblLatName.grid(row=4,column=1)
        
        lblDateOverdate=Label(DataFrameLeft,bg="powder blue",text="Date Over Due", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateOverdate.grid(row=7,column=2,sticky=W)
        lblDateOverdate=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblDateOverdate.grid(row=7,column=3)
        

        lblAdress1=Label(DataFrameLeft,bg="powder blue",text="Address1", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAdress1.grid(row=5,column=0,sticky=W)
        lblAdress1=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblAdress1.grid(row=5,column=1)
        
        lblAdress2=Label(DataFrameLeft,bg="powder blue",text="Address2", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAdress2.grid(row=6,column=0,sticky=W)
        lblAdress2=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblAdress2.grid(row=6,column=1)
        
        
        lblpostcode=Label(DataFrameLeft,bg="powder blue",text="Post Code", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblpostcode.grid(row=7,column=0,sticky=W)
        lblpostcode=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblpostcode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=8,column=0,sticky=W)
        lblMobile=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblMobile.grid(row=8,column=1)
        
        lblBooktitle=Label(DataFrameLeft,bg="powder blue",text="Book Title", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBooktitle.grid(row=1,column=2,sticky=W)
        lblBooktitle=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblBooktitle.grid(row=1,column=3)
        
        
        lblBookid=Label(DataFrameLeft,bg="powder blue",text="Book Id", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblBookid.grid(row=0,column=2,sticky=W)
        lblBookid=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblBookid.grid(row=0,column=3)
        
        
        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Auther Name", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=2,column=2,sticky=W)
        lblMobile=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblMobile.grid(row=2,column=3)
        
        lblDateborrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDateborrowed.grid(row=3,column=2,sticky=W)
        lblDateborrowed=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblDateborrowed.grid(row=3,column=3)
        
        
        
        lblDaysONBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDaysONBook.grid(row=4,column=2,sticky=W)
        lblDaysONBook=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblDaysONBook.grid(row=4,column=3)
        
        
        
        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        lblDaysOnBook=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblDaysOnBook.grid(row=5,column=3)
        
        
        lbllateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine", font=("times new roman",12,"bold"),padx=2,pady=6)
        lbllateReturnFine.grid(row=6,column=2,sticky=W)
        lbllateReturnFine=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lbllateReturnFine.grid(row=6,column=3)
        
        
        
        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="", font=("times new roman",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=2,column=2,sticky=W)
        lblActualPrice=Entry(DataFrameLeft,font=("times new roman",13,"bold"),width=29)
        lblActualPrice.grid(row=2,column=3)
         
        
        
        
        
        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("times new romen",12,"bold"),padx=20,pady=6)
        DataFrameRight.place(x=870,y=5,width=500,height=350)
        
        #=============================================BOTTONS FRAME========================================================
        
        
        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=0,y=540,width=1530,height=70)
        #=================================================information frame =====================================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=195)
if __name__==   "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
    
    
    
    