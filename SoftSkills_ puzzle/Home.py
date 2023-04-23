from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk,ImageFont,ImageDraw
from treasurehunt import clue1



class home:
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("1200x600+0+0")
        self.root.title("Home")

        imgstr=Image.open("E:\SoftSkills_ puzzle\images\hird.jpg")
        imgstr=imgstr.resize((1200,600),Image.LANCZOS)
        self.photoimgstr=ImageTk.PhotoImage(imgstr)

        bg_str=Label(self.root,image=self.photoimgstr)
        bg_str.place(x=0,y=0,width=1200,height=600)

        t1=Label(self.root,text="Welcome Aboard!!",font=("ariel",15,"bold","italic"),bg="teal",fg="white")
        t1.place(x=500,y=50)
        
        ht=Button(bg_str,text="Start the hunt",command=self.tre,cursor="hand2",font=("times new roman",25,"bold","italic"),bg="skyblue",fg="black")
        ht.place(x=500,y=490,width=250,height=50)
    def tre(self):
        self.new_window=Toplevel(self.root)
        self.app=clue1(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=home(root)
    root.mainloop()