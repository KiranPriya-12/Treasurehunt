from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class registration():
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Registration")

        #variables
        self.var_fn=StringVar()
        self.var_ln=StringVar()
        self.var_cnt=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_passc=StringVar()
        self.var_secq=StringVar()
        self.var_seca=StringVar()

        imgreg=Image.open("E:\SoftSkills_ puzzle\images\egistr.jpg")
        imgreg=imgreg.resize((1200,600),Image.LANCZOS)
        self.photoimgreg=ImageTk.PhotoImage(imgreg)

        bg_reg=Label(self.root,image=self.photoimgreg)
        bg_reg.place(x=0,y=0,width=1200,height=600)

        frame=Frame(bg_reg,background="white")
        frame.place(x=200,y=50,width=800,height=500)

        rgstr=Label(frame,text="Registration",font=("times new roman",20,"bold"),fg="black",bg="white")
        rgstr.place(x=300,y=15)


        nmfst=Label(frame,text="First Name",font=("times new roman",15),bg="white",fg="black")
        nmfst.place(x=100,y=60)

        self.nmfstent=ttk.Entry(frame,textvariable=self.var_fn,width=20,font=("times new roman",15))
        self.nmfstent.place(x=100,y=100)

        nmlst=Label(frame,text="Last Name",font=("times new roman",15),bg="white",fg="black")
        nmlst.place(x=440,y=60)

        self.nmlstent=ttk.Entry(frame,textvariable=self.var_ln,width=20,font=("times new roman",15))
        self.nmlstent.place(x=440,y=100)

        cnt=Label(frame,text="Contact Number",font=("times new roman",15),bg="white",fg="black")
        cnt.place(x=100,y=140)

        self.cntent=ttk.Entry(frame,textvariable=self.var_cnt,width=20,font=("times new roman",15))
        self.cntent.place(x=100,y=180)

        email=Label(frame,text="Email",font=("times new roman",15),bg="white",fg="black")
        email.place(x=440,y=140)

        self.emlent=ttk.Entry(frame,textvariable=self.var_email,width=20,font=("times new roman",15))
        self.emlent.place(x=440,y=180)

        passw=Label(frame,text="Password",font=("times new roman",15),bg="white",fg="black")
        passw.place(x=100,y=220)

        self.passent=ttk.Entry(frame,textvariable=self.var_pass,width=20,font=("times new roman",15))
        self.passent.place(x=100,y=260)

        cpass=Label(frame,text="Confirm Password",font=("times new roman",15),bg="white",fg="black")
        cpass.place(x=440,y=220)

        self.cpassent=ttk.Entry(frame,textvariable=self.var_passc,width=20,font=("times new roman",15))
        self.cpassent.place(x=440,y=260)

        sec=Label(frame,text="Security question",font=("times new roman",15),bg="white",fg="black")
        sec.place(x=100,y=300)

        self.seccmb=ttk.Combobox(frame,textvariable=self.var_secq,width=20,font=("times new roman",10))
        self.seccmb["values"]=("Select","Your birth place","First school","First pet's name")
        self.seccmb.place(x=100,y=340)
        self.seccmb.current(0)

        seca=Label(frame,text="Security Answer",font=("times new roman",15),bg="white",fg="black")
        seca.place(x=440,y=300)

        self.secaent=ttk.Entry(frame,textvariable=self.var_seca,width=20,font=("times new roman",15))
        self.secaent.place(x=440,y=340)

        reg1=Button(frame,command=self.regdata,text="Register",cursor="hand2",font=("times new roman",16,"bold"),bg="maroon",fg="white")
        reg1.place(x=350,y=420,height=30)

        

    def regdata(self):
        if self.var_fn.get()=="" or self.var_email.get()=="" or self.var_secq.get()=="Select" or self.var_ln.get()=="" or self.var_cnt.get()=="" or self.var_pass.get()=="" or self.var_passc.get()=="" or self.var_seca.get()=="" :
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_passc.get():
            messagebox.showerror("Error","Password and confirm password are not same")
        elif len(self.var_cnt.get())!=10:
            messagebox.showerror("Error","Enter a valid contact number")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Cheruku@12",database="logindetails")
            cur=conn.cursor()
            query=("select * from registration where email=%s") 
            value=(self.var_email.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists,please try another email")
            else:
                cur.execute("insert into registration values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fn.get(),
                                                                                        self.var_ln.get(),
                                                                                        self.var_cnt.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_secq.get(),
                                                                                        self.var_seca.get(),
                                                                                        self.var_pass.get()
                                                                                        
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration completed Successfully")


    


if __name__ == "__main__":
    root=Tk()
    obj=registration(root)
    root.mainloop()