from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class clue1():
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Treasure Hunt")

        self.var_ans=StringVar()

        lfrm=Frame(self.root,bd=5,relief=RIDGE,bg="skyblue")
        lfrm.place(x=10,y=20,width=580,height=550)

        lfrmt=Label(lfrm,text="The thing that lights up first in vizag",font=("ariel",15,"bold"),bg="skyblue",fg="black")
        lfrmt.place(x=80,y=100)
        lfrmt=Label(lfrm,text="every evening",font=("ariel",15,"bold"),bg="skyblue",fg="black")
        lfrmt.place(x=160,y=130)

        self.ansent=ttk.Entry(lfrm,textvariable=self.var_ans,width=20,font=("times new roman",15))
        self.ansent.place(x=160,y=260)

        reg1=Button(lfrm,text="Next Clue",command=self.click,cursor="hand2",font=("times new roman",16,"bold"),bg="maroon",fg="white")
        reg1.place(x=130,y=440,width=300,height=50)

        imgrfr=Image.open("E:\SoftSkills_ puzzle\images\light house.jpg")
        imgrfr=imgrfr.resize((580,550),Image.LANCZOS)
        self.photoimgrfr=ImageTk.PhotoImage(imgrfr)

        bg_rfr=Label(self.root,image=self.photoimgrfr)
        bg_rfr.place(x=600,y=20,width=580,height=550)

    def click(self):
        if self.var_ans.get()=="light house":
            
            self.new_window=Toplevel(self.root)
            self.app=clue2(self.new_window)


class clue2():
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Treasure Hunt")

        self.var_ans=StringVar()

        lfrm=Frame(self.root,bd=5,relief=RIDGE,bg="skyblue")
        lfrm.place(x=10,y=20,width=580,height=550)

        lfrmt=Label(lfrm,text="Surface that reflects",font=("ariel",20,"bold"),bg="skyblue",fg="black")
        lfrmt.place(x=80,y=100)

        self.ansent=ttk.Entry(lfrm,textvariable=self.var_ans,width=20,font=("times new roman",15))
        self.ansent.place(x=160,y=260)

        reg1=Button(lfrm,text="Next Clue",command=self.click,cursor="hand2",font=("times new roman",16,"bold"),bg="maroon",fg="white")
        reg1.place(x=130,y=440,width=300,height=50)

        imgrfr=Image.open("E:\SoftSkills_ puzzle\images\mirrorwater.webp")
        imgrfr=imgrfr.resize((580,550),Image.LANCZOS)
        self.photoimgrfr=ImageTk.PhotoImage(imgrfr)

        bg_rfr=Label(self.root,image=self.photoimgrfr)
        bg_rfr.place(x=600,y=20,width=580,height=550)

    def click(self):
        if self.var_ans.get()=="water":
            
            self.new_window=Toplevel(self.root)
            self.app=clue3(self.new_window)


class clue3():
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Treasure Hunt")

        self.var_ans=StringVar()

        lfrm=Frame(self.root,bd=5,relief=RIDGE,bg="skyblue")
        lfrm.place(x=10,y=20,width=580,height=550)

        lfrmt=Label(lfrm,text="People used this thing as a means",font=("ariel",15,"bold"),bg="skyblue",fg="black")
        lfrmt.place(x=80,y=100)
        lfrmt=Label(lfrm,text="to guess time",font=("ariel",15,"bold"),bg="skyblue",fg="black")
        lfrmt.place(x=160,y=130)

        self.ansent=ttk.Entry(lfrm,textvariable=self.var_ans,width=20,font=("times new roman",15))
        self.ansent.place(x=160,y=260)

        reg1=Button(lfrm,text="Next Clue",command=self.click,cursor="hand2",font=("times new roman",16,"bold"),bg="maroon",fg="white")
        reg1.place(x=130,y=440,width=300,height=50)

        imgrfr=Image.open("E:\SoftSkills_ puzzle\images\sunandwatch.jpg")
        imgrfr=imgrfr.resize((580,550),Image.LANCZOS)
        self.photoimgrfr=ImageTk.PhotoImage(imgrfr)

        bg_rfr=Label(self.root,image=self.photoimgrfr)
        bg_rfr.place(x=600,y=20,width=580,height=550)

    def click(self):
        if self.var_ans.get()=="sun":
            
            self.new_window=Toplevel(self.root)
            self.app=clue4(self.new_window)

class clue4():
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Treasure Hunt")

        self.var_ans=StringVar()

        lfrm=Frame(self.root,bd=5,relief=RIDGE,bg="skyblue")
        lfrm.place(x=10,y=20,width=580,height=550)

        lfrmt=Label(lfrm,text="Key that cannot open any lock",font=("ariel",20,"bold"),bg="skyblue",fg="black")
        lfrmt.place(x=50,y=100)

        self.ansent=ttk.Entry(lfrm,textvariable=self.var_ans,width=20,font=("times new roman",15))
        self.ansent.place(x=160,y=260)

        reg1=Button(lfrm,text="Next Clue",command=self.click,cursor="hand2",font=("times new roman",16,"bold"),bg="maroon",fg="white")
        reg1.place(x=130,y=440,width=300,height=50)

        imgrfr=Image.open("E:\SoftSkills_ puzzle\images\pianokeys.jpg")
        imgrfr=imgrfr.resize((580,550),Image.LANCZOS)
        self.photoimgrfr=ImageTk.PhotoImage(imgrfr)

        bg_rfr=Label(self.root,image=self.photoimgrfr)
        bg_rfr.place(x=600,y=20,width=580,height=550)

    def click(self):
        if self.var_ans.get()=="piano" or self.var_ans.get()=="key board":
            
            self.new_window=Toplevel(self.root)
            self.app=clue5(self.new_window)

class clue5():
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Treasure Hunt")

        self.var_ans=StringVar()

        lfrm=Frame(self.root,bd=5,relief=RIDGE,bg="skyblue")
        lfrm.place(x=10,y=20,width=580,height=550)

        lfrmt=Label(lfrm,text="Guess the flower name",font=("ariel",15,"bold"),bg="skyblue",fg="black")
        lfrmt.place(x=120,y=100)
        lfrmt=Label(lfrm,text="Within the bloom that grace this land,",font=("ariel",15,"bold"),bg="skyblue",fg="black")
        lfrmt.place(x=90,y=140)
        lfrmt=Label(lfrm,text="a fortune may be found,",font=("ariel",15,"bold"),bg="skyblue",fg="black")
        lfrmt.place(x=120,y=180)
        lfrmt=Label(lfrm,text="But only with guarded hands,",font=("ariel",15,"bold"),bg="skyblue",fg="black")
        lfrmt.place(x=85,y=220)
        lfrmt=Label(lfrm,text="would be able to find the treasure",font=("ariel",15,"bold"),bg="skyblue",fg="black")
        lfrmt.place(x=90,y=250)

        self.ansent=ttk.Entry(lfrm,textvariable=self.var_ans,width=20,font=("times new roman",15))
        self.ansent.place(x=160,y=350)

        reg1=Button(lfrm,text="Next Clue",command=self.click,cursor="hand2",font=("times new roman",16,"bold"),bg="maroon",fg="white")
        reg1.place(x=130,y=440,width=300,height=50)

        imgrfr=Image.open("E:\SoftSkills_ puzzle\images\poses.jpg")
        imgrfr=imgrfr.resize((580,550),Image.LANCZOS)
        self.photoimgrfr=ImageTk.PhotoImage(imgrfr)

        bg_rfr=Label(self.root,image=self.photoimgrfr)
        bg_rfr.place(x=600,y=20,width=580,height=550)

    def click(self):
        if self.var_ans.get()=="rose":
            
            self.new_window=Toplevel(self.root)
            self.app=Treasure(self.new_window)
    
class Treasure():
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Treasure Hunt")

        imgstr=Image.open("E:\SoftSkills_ puzzle\images\strea.jpeg")
        imgstr=imgstr.resize((1200,600),Image.LANCZOS)
        self.photoimgstr=ImageTk.PhotoImage(imgstr)

        bg_str=Label(self.root,image=self.photoimgstr)
        bg_str.place(x=0,y=0,width=1200,height=600)

        


    



if __name__ == "__main__":
    root=Tk()
    obj=clue1(root)
    root.mainloop()