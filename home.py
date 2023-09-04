from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
import PIL
import entry,login,detail



class AdminNav:
     def __init__(self):
        self.root = Tk()
        self.root.title('Weather Application')
        self.root.state('zoomed')
     
        self.root.configure(bg="#d7dae2")

       #to make window in center
        self.fullwidth=self.root.winfo_screenwidth()
        self.fullheight=self.root.winfo_screenheight()
        self.width=int((self.fullwidth-1370)/2)
        self.height=int((self.fullheight-750)/2)
        s="1370x750+" +str(self.width)+ "+" +str(self.height)
        self.root.resizable(height=False,width=False)
        
        #center
      
        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        self.width = int((self.fullwidth-1380)/2)
        self.height=int((self.fullheight-750)/2)

        s = "1280x750+" +str(self.width)+ "+" +str(self.height)
    

        self.menu=Menu()
        self.weather = Menu(self.menu)
        self.menu.add_cascade(label= "profile" , menu=self.weather)
        self.weather.add_command(label="New Entry",command=self.entery)
        self.weather.add_command(label="Details",command=self.details)

        
        self.account = Menu(self.menu)
        self.menu.add_cascade(label = "Account", menu = self.account)
        self.account.add_command(label="Logout",command=self.logout)


        self.root.config(menu= self.menu)

     def navframe(self):
        self.navfra = Frame(self.root,bg="white",)
        self.navfra.place(x=0, y=0, width="1380", height="750")
        self.root.resizable(height=False, width=False)  


              
        self.image2 = Image.open("images/mkll.jpg")
        self.bgImage2 = ImageTk.PhotoImage(self.image2)
        self.bgLabel2 = Label(self.navfra, image=self.bgImage2)
        self.bgLabel2.place(x = 0, y = 0, width = "1400", height = "750")
     
        
      #lables
      
        #self.name=Label(self.mainframe,text="london :-",font=("arial",30,"bold"),fg="black",bg="#d7dae2")
        #self.name.place(x=100,y=60)

        self.root.mainloop()
     def logout(self):
        t=messagebox.askyesno("ALERT","Do You Realy Want To Exit")
        if t:
            self.root.destroy()
            obj = login.Login()
            obj.loginFrame()
     def entery(self):
            self.root.destroy()
            currentObj = entry.Login()
            currentObj.loginFrame()
      
     def details(self):
            self.root.destroy()
            currentObj = detail.getdetail()
            currentObj.loginFrame()
         #  
if __name__=='__main__':
     obj1 = AdminNav()
     obj1.navframe()

    # def openCurrent(self):
      #self.root.destroy()
      #currentObj = copy_search.search('with_login')
      #currentObj.search_frame()

     #def openFiveDay(self):
      #self.root.destroy()
      #fiveObj = search_five_days.search()
      #fiveObj.search_frame()

     #def logout(self):
        #t=messagebox.askyesno("ALERT","Do You Realy Want To Exit")
        #if t:
           # self.root.destroy()
            #obj = login.loginWindow()
            #obj.loginFrame()


     #def entery(self):
      #self.root.destroy()
      #currentObj = entry.Login()
      #currentObj.loginFrame()
    # def logout(self):
   #     self.root.destroy()
  #      login.Login()
#if __name__=='__main__':
 #   obj1 = AdminNav()
 #   obj1.navframe()
        

        
        
        
