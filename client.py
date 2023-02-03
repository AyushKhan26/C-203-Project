from tkinter import *
from tkinter import ttk
import socket
from threading import Thread

#nickname = input('Enter your nickname here')

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 5501

client.connect((ip_address,port))

class GUI:
   
 def goAhead(self,name):
  self.login.destroy()
  self.layout(name)
  rcv = Thread(target= self.receive)
  rcv.start()



 def recieve(self):
    while True:
        try:
          message = client.recv(2048).decode('utf-8')
          if message == 'NICKNAME':
                client.send(self.name.encode('utf-8'))
          else :
             self.showMessage(message)
        except:
            print('Sorry! an eror has occured')
            client.close()
            break

 def __init__(self):
      self.Window = Tk()
      self.Window.withdraw()

      self.login = Toplevel()
      self.login.title('Login')
      self.login.resizable(width= False,height= False)
      self.login.configure(width= 400,height= 400,bg='grey')

      self.label = Label(self.login,text='Please login to continue',fg='black',font=('Helvetica 30',20))
      self.label.place(relx= 0.5,rely= 0.1)
       
      self.name_label= Label(self.login,text="NAME : ")
      self.name_label.place(relx=0.35,rely=0.3)

      self.entry_name= Entry(self.login,text=' ',font=('Calibri',10))
      self.entry_name.place(relx=0.65,rely=0.3)

      self.go = Button(self.login,text='CONTINUE',font="Helvetica 14 bold",command= lambda: self.goAhead(self.entry_name.get())) 
      self.go.place(relx=0.7,rely= 0.8)
      self.Window.mainloop()
      
 def layout(self,name):
   self.name = name
   self.Window.deiconify()
   self.Window.title('CHATROOM')
   self.Window.resizable(width= False,height= False)
   self.Window.configure(width=470,height=550,bg='#17202A')

   self.TopLabel = Label(self.Window,text=' ',width=20,bg='#17202A')
   self.TopLabel.place(rely=1,relx=1)
   
   self.textArea = Text(self.Window,width=95,bg='#17202A')
   self.textArea.place(x=100,y=50)

   self.scrollbar= Scrollbar(self.textArea)
   self.scrollbar.place(relheight=1,relx=1)
   self.scrollbar.config(command= self.textArea.yview)

   self.separator = ttk.Separator(self.Window,orient='horizontal')
   self.separator.place(x=0, y=110, relwidth=1, height=0.1)

   self.msgentry = Entry(self.Window,text=' x  ',width=10,height=7)
   self.msgentry.pack()
   self.msgentry.place(x= 200,y= 120)

   self.send_button = Button(self.Window,text='Send Message',width=3,height=3,command=self.sendButton())
   self.send_button.place(x=250,y=150)

 def sendButton(self,msg):
    self.textArea.config(state= DISABLED)
    self.msg = msg
    self.msgentry.delete(0,END)
    snd = Thread(target= self.write)
    snd.start()

 def showMessage(self,message):
    self.textArea.config(state = NORMAL)
    self.textArea.insert(END,message+'\n\n')
    self.textArea.config(state= DISABLED)
    self.textArea.see(END) 
 
 def write(self):
     self.textArea.config(state= DISABLED)
     while True:
        message = (f'{self.name}: {self.msg}')
        client.send(message.encode('utf-8')) 
        self.showMessage(message)
        break   

   


       

g = GUI()

#recieve_Thread = Thread(target= recieve)
#recieve_Thread.start()

#write_Thread = Thread(target= write)
#write_Thread.start()
