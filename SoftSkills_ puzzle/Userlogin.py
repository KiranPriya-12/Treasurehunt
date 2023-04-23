from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import registration
import mysql.connector
from Home import home

class User_login():
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("User Login")

        imgplrlg=Image.open("E:\SoftSkills_ puzzle\images\player.jpg")
        imgplrlg=imgplrlg.resize((1200,600),Image.LANCZOS)
        self.photoimgplrlg=ImageTk.PhotoImage(imgplrlg)

        bg_plr=Label(self.root,image=self.photoimgplrlg)
        bg_plr.place(x=0,y=0,width=1200,height=600)

        plrtxt=Label(bg_plr,text="User Id",font=("times new roman",20),bg="teal",fg="black")
        plrtxt.place(x=550,y=230)

        self.plrtxtent=ttk.Entry(bg_plr,width=20,font=("times new roman",15))
        self.plrtxtent.place(x=550,y=280)

        passplrtxt=Label(bg_plr,text="Password",font=("times new roman",20),bg="teal",fg="black")
        passplrtxt.place(x=550,y=340)

        self.passplrtxtent=ttk.Entry(bg_plr,width=20,font=("times new roman",15))
        self.passplrtxtent.place(x=550,y=390)

        lgnplr=Button(bg_plr,text="Login",command=self.treasure,cursor="hand2",font=("times new roman",25,"bold"),bd=3,relief=RIDGE,bg="teal",fg="black")
        lgnplr.place(x=580,y=450,width=150,height=50)

        regplr=Button(bg_plr,text="New User Register",command=self.nreglg,cursor="hand2",font=("times new roman",10),borderwidth=0,fg="teal")
        regplr.place(x=550,y=520)

        frgt=Button(bg_plr,text="Forgot Password",command=self.frgtpass,cursor="hand2",font=("times new roman",10),borderwidth=0,fg="teal")
        frgt.place(x=550,y=550)

    def regilg(self):
        self.new_window=Toplevel(self.root)
        self.app=registration(self.new_window)
    def treasure(self):
        self.new_window=Toplevel(self.root)
        self.app=home(self.new_window)

#===============reset password==========
    def ck_pass(self):
        if self.seccmb.get()=="Select":
            messagebox.showerror("Error","Select a security question")
        elif self.secaent.get()=="":
            messagebox.showerror("Error","Please enter an answer")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Cheruku@12",database="logindetails")
            cur=conn.cursor()
            query=("select password from registration where email=%s and securityQ=%s and securityA=%s") 
            value=(self.plrtxtent.get(),self.seccmb.get(),self.secaent.get())
            cur.execute(query,value)
            row=cur.fetchone()
            messagebox.showinfo("Password",row)
           



# ============forgot pass window==========
    def frgtpass(self):
        if self.plrtxtent.get()=="":
            messagebox.showerror("Error","Please enter the Email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Cheruku@12",database="logindetails")
            cur=conn.cursor()
            query=("select password from registration where email=%s") 
            value=(self.plrtxtent.get(),)
            cur.execute(query,value)
            row=cur.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter the valid userid")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("300x400+450+150")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20),bg="teal",fg="black")
                l.place(x=0,y=10,relwidth=1)

                sec=Label(self.root2,text="Security question",font=("times new roman",15),bg="white",fg="black")
                sec.place(x=30,y=100)

                self.seccmb=ttk.Combobox(self.root2,width=20,font=("times new roman",15))
                self.seccmb["values"]=("Select","Your birth place","First school","First pet's name")
                self.seccmb.place(x=30,y=150)
                self.seccmb.current(0)

                seca=Label(self.root2,text="Security Answer",font=("times new roman",15),bg="white",fg="black")
                seca.place(x=30,y=200)

                self.secaent=ttk.Entry(self.root2,font=("times new roman",15))
                self.secaent.place(x=30,y=250)

                

                frgt=Button(self.root2,text="Check Password",command=self.ck_pass,cursor="hand2",font=("times new roman",15),bg="teal",fg="black")
                frgt.place(x=80,y=300)
    
    def nreglg(self):
        self.new_window=Toplevel(self.root)
        self.app=registration(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=User_login(root)
    root.mainloop()

