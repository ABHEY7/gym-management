from tkinter import*
from PIL import ImageTk, Image
import PIL
from tkinter import messagebox
import home,create_account,database

class Login:
    def __init__(self):
        self.root = Tk()
        self.root.title('Weather Application')
        self.root.state('zoomed')


        #to make window in center
        self.fullwidth=self.root.winfo_screenwidth()
        self.fullheight=self.root.winfo_screenheight()
        self.width=int((self.fullwidth-1370)/2)
        self.height=int((self.fullheight-750)/2)
        s="1370x750+" +str(self.width)+ "+" +str(self.height)
        self.root.resizable(height=False,width=False)

#    def loginFrame(self):
    def loginFrame(self):
 
        self.login = Frame(self.root)
        self.login.place(x = 0, y = 0, width="2000", height="1333")

        self.image = Image.open("images/bvvv.jpg")
        self.bgImage = ImageTk.PhotoImage(self.image)
        self.bgLabel = Label(self.login, image=self.bgImage)
        self.bgLabel.place(x = 0, y = 0, width = "2000", height = "1333")

       
      #whiteframe
        Frame_login=Frame( self.root,bg="white")
        Frame_login.place(x=700,y=100,height=460,width=480)
    
      #icon
        self.logo = Image.open("images/lll.png")
        self.bglogo = ImageTk.PhotoImage(self.logo)
        self.bgLabel1 = Label(Frame_login, image=self.bglogo,bg='white')
        self.bgLabel1.place(x = 340, y = 10, width = "130", height = "130")

     #title

        title=Label(Frame_login,text="LOGIN HERE",font=("impact",34,"bold"),fg="blue",bg="white")
        title.place(x=70,y=25)     
        title=Label(Frame_login,text=" GYM LOGIN AREA",font=("century",10,"bold"),fg="blue",bg="white")
        title.place(x=98,y=80) 
        #lables
        self.name=Label(Frame_login,text="NAME :- ",font=("century",12,"bold"),fg="black",bg="white")
        self.name.place(x=40,y=150,width=90,height=20)
        self.password=Label(Frame_login,text="PASSWORD :-",fg="black",bg="white",font=("century",12,"bold"))
        self.password.place(x=40,y=230,width=150,height=20)

        #entrys 
        self.nam=Entry(Frame_login,width=50,bg='lightgrey')
        self.nam.place(x=50,y=178,height=35)
        self.passw=Entry(Frame_login,width=50,bg='lightgrey')
        self.passw.place(x=50,y=258,height=35)

        #buttons
        self.login_1=Button(self.root,text=("SIGN IN"),width=12,bg='blue',fg='white',font=("century",14,"bold"),command=self.loginUser)
        self.login_1.place(x=820,y=470,height="40")
        
        self.login_1=Button(self.root,text=("SIGN UP"),bg='blue',fg='white',font=("century",7,"bold"),command=self.create)
        self.login_1.place(x=960,y=410,height="16",width='55')
        
       
        self.login_1=Label(self.root,text=("Don't have any account ?"),width=22,bg='white',fg='black',font=("century",8,'bold'))
        self.login_1.place(x=780,y=407)
              

        # so screen cant be resized
        self.root.resizable(height=False,width=False)
         # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        

        self.root.mainloop()
    #def submit(self):
     #   self.root.destroy()
      #  home.AdminNav()
    def create(self):
        self.root.destroy()
        create_account.Login()
 #   loginObj.loginFrame()

    def loginUser(self):
        data = (
            self.nam.get(),
            self.passw.get()
        )

        if self.nam.get() == '':
            messagebox.showinfo('Alert', 'Please enter an username.')
        if self.passw.get() == '':
            messagebox.showinfo('Alert', 'Please enter your password.')
        else:
            res = database.login(data)
            print(res)
            if res:
                messagebox.showinfo('Success', 'Login Successfully')
                self.root.destroy()
                #home.AdminNav()
                homeObj = home.AdminNav()
                homeObj.navframe()
    
            else:
                messagebox.showinfo('Alert', 'Invalid username and/or password')
if __name__ == "__main__":
    #loginObj = Login()
    loginObj = Login()
    loginObj.loginFrame()          

         
# root=Tk()
# root.title("weather")
# root.geometry("400x400")

# image = Image.open("jki.jpg")

# bgImage = ImageTk.PhotoImage(image)
# bgLabel = Label(root, image=bgImage)
# bgLabel.pack()
# root.mainloop()
# #LABELS




# lable_1=Label(root,text="")
# lable_1.grid(row=0,column=0)

# lable_2=Label(root,text="")
# lable_2.grid(row=1,column=1)


# lable_3=Label(root,text="")
# lable_3.grid(row=2,column=2)

# lable_4=Label(root,text="")
# lable_4.grid(row=3,column=2)

# lable_5=Label(root,text="")
# lable_5.grid(row=5,column=1)

# lable_7=Label(root,text="NAME -")
# lable_7.grid(row=4,column=1)

# lable_8=Label(root,text="PASWORD -")
# lable_8.grid(row=6,column=1)

# lable_6=Label(root,text="")
# lable_6.grid(row=7,column=1)
# #ENTERS

# entry_1=Entry(root,width=50)
# entry_1.grid(row=4,column=2)

# entry_2=Entry(root,width=50)
# entry_2.grid(row=6,column=2)


# #button

# login=Button(root,text="LOGIN",bg="black",fg="white")
# login.grid(row=9,column=2)
# register=Button(root,text="REGISTER",width=10,height=1)
# register.grid(row=8,column=2)
# #functionlogin
# editor=Tk()
# editor.geometry("400x400")


# lable_a=Label(editor,text="")
# lable_a.grid(row=0,column=0)

# lable_b=Label(editor,text="")
# lable_b.grid(row=1,column=1)


# lable_c=Label(editor,text="")
# lable_c.grid(row=4,column=2)

# lable_d=Label(editor,text="")
# lable_d.grid(row=3,column=2)
# lable_f=Label(editor,text="CREATE SIGN UP FORM")
# lable_f.grid(row=2,column=2)
# lable_g=Label(editor,text="USERNAME:-")
# lable_g.grid(row=5,column=1)
# lable_h=Label(editor,text="PASSWORD:-")
# lable_h.grid(row=7,column=1)
# lable_i=Label(editor,text="CONFIRM-PASSWORD:-")
# lable_i.grid(row=9,column=1)
# lable_j=Label(editor,text="")
# lable_j.grid(row=6,column=1)
# lable_k=Label(editor,text="")
# lable_k.grid(row=8,column=1)


# #entery
# name=Entry(editor,width=35)
# name.grid(row=5,column=2)
# name=Entry(editor,width=35)
# name.grid(row=7,column=2)
# name=Entry(editor,width=35)
# name.grid(row=9,column=2)


# #image
# # bg=ImageTk.PhotoImage(file="image\ty.jpg")
# # bg_image=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)




# root.mainloop()