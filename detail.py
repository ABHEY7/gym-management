from tkinter import*
from PIL import ImageTk, Image
import mysql.connector
import PIL
import home
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class getdetail:
    def __init__(self):
        self.root = Tk()
        self.root.title('Weather Application')
        self.root.state('zoomed')

    def loginFrame(self):
 
        self.login = Frame(self.root)
        self.login.place(x = 0, y = 0, width="2000", height="1333")

        self.image = Image.open("images/bvvv.jpg")
        self.bgImage = ImageTk.PhotoImage(self.image)
        self.bgLabel = Label(self.login, image=self.bgImage)
        self.bgLabel.place(x = 0, y = 0, width = "2000", height = "1333")

       
      #whiteframe
        Frame_login=Frame( self.root,bg="white")
        Frame_login.place(x=200,y=70,height=560,width=1060)
      #button
       
        self.back_2=Button(self.root,text=("BACK"),width=6,bg='blue',fg='white',font=("century",14,"bold"),command=self.back)
        self.back_2.place(x=20,y=30,height="35")
        
      #icon
        self.logo = Image.open("images/lll.png")
        self.bglogo = ImageTk.PhotoImage(self.logo)
        self.bgLabel1 = Label(Frame_login, image=self.bglogo,bg='white')
        self.bgLabel1.place(x = 40, y = 2, width = "125", height = "125")
     
     #labels
        self.label1=Label(Frame_login,text='Customer Details',bg='white',fg='blue',font=("century",34,"bold",'underline'))
        self.label1.place(x=250,y=15,height=100,width=500)

        connect=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="gym"
        )
        conn=connect.cursor()
        conn.execute('SELECT * FROM `entrybox` ORDER BY id ')
        tree=ttk.Treeview(Frame_login)
        tree['show']='headings'
        s=ttk.Treeview(Frame_login)
        #s.theme_use('clam')
      #  s.configure('.',font=('helvetica',11))
       # s.configure('Treeview.Heading',foreground='red',font=('Helvetica',11,'bold'))
        tree['columns']=('id','name','start','cont','adress')
        tree.column('id',width=50,minwidth=50)
        tree.column('name',width=100,minwidth=100)
        tree.column('start',width=100,minwidth=100)
        tree.column('cont',width=150,minwidth=150)
        tree.column('adress',width=150,minwidth=150)

        tree.heading('id',text='ID')
        tree.heading('name',text='NAME')
        tree.heading('start',text='STARTING DATE')
        tree.heading('cont',text='CONTACT')
        tree.heading('adress',text='ADDRESS')
        i=0
        for ro in conn:
            tree.insert('',i,text='',values=(ro[0],ro[1],ro[2],ro[3],ro[4]))

            i=i+1
        hsb=ttk.Scrollbar(Frame_login,orient='horizontal')
        tree.configure(xscrollcommand=hsb.set)
        hsb.place(x=60,y=460,width=895)    

        hsb=ttk.Scrollbar(Frame_login,orient='vertical')
        tree.configure(yscrollcommand=hsb.set)
        hsb.place(x=950,y=125,height=350)    

        tree.place(x=60,y=127,width=900,height=340)
        name=tk.StringVar()
        self.back_2=Button(Frame_login,text=("Insert"),width=6,bg='blue',fg='white',font=("century",14,"bold"))
        self.back_2.place(x=360,y=500,height="35")
       
        self.back_2=Button(Frame_login,text=("Delete"),width=6,bg='blue',fg='white',font=("century",14,"bold"))
        self.back_2.place(x=580,y=500,height="35")
               
    #def delete1(tree):
      #  selected_item=tree.selection()[0]
     #   uid=tree.item(selected_item)['values'][0]
    #    del_query='DELETE FROM `entrybox` WHERE id=%s'
   #     sel_data=(uid,)
  #      conn.execute(del_query,sel_data)
 #       connect.commit()
#        tree.delete(selected_item)
        #mb.showinfo('success','data delected')




        self.root.mainloop()
    def back(self):
        self.root.destroy()
      
        currentObj = home.AdminNav()
        currentObj.navframe()
        #  
      #scroller
        
        #scro_x=ttk.Scrollbar(Frame_login,orient='horizontal')
        #scro_y=ttk.Scrollbar(Frame_login,orient='vertical')
        #self.detail=ttk.Treeview(Frame_login,columns=('NAME','STRAING DATE','PHONE NUMBER','ADDRESS'),#xscrollcommand=scro_x.set,yscrollcommand=scro_y.set)
        #scro_x.pack(side=BOTTOM,fill=X)
        #scro_x.pack(side=BOTTOM,fill=Y)
        #scro_x=ttk.Scrollbar(command=self.detail.xview)
        #scro_y=ttk.Scrollbar(command=self.detail.yview)
        #self.detail.heading('NAME',text='NAME')
        #self.detail.heading('STRAING DATE',text='STRAING DATE')
        #self.detail.heading('PHONE NUMBER',text='PHONE NUMBER')
        #self.detail.heading('ADDRESS',text='ADDRESS')
        #self.detail['show']='heading'
        #self.detail.pack(fill=BOTH,expand=1)
        
                
if __name__ == "__main__":
    #loginObj = Login()
    loginObj = getdetail()
    loginObj.loginFrame()          
