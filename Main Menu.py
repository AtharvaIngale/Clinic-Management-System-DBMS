from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
from patient_form import Patient
from appointment_form import Appointment
root=Tk()

def main():
    root = Tk()
    app= MainWindow(root)
#MAIN WINDOW FOR LOG IN
class MainWindow:
    # constructor
    def __init__(self,master):
        self.master = master
        self.master.title("CLINIC MANAGMENT SYSTEM")
        self.master.geometry("800x600+0+0")
        self.master.config(bg="white")
        self.frame = Frame(self.master,bg="white")
        self.frame.pack()
       
        self.lblTitle = Label(self.frame,text = "CLINIC MANAGMENT SYSTEM", font="Helvetica 20 bold",bg="light blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)

        self.lblTitle = Label(self.frame,text = "MAIN MENU", font="Helvetica 20 bold",bg="WHITE")
        self.lblTitle.grid(row =1 ,column = 0,columnspan=2,pady=50)
        
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="orange",bd=20)
        self.LoginFrame.grid(row=2,column=0)
        #===========BUTTONS============= 
        self.button1 = Button(self.LoginFrame,text = "1.PATIENT REGISTRATION", width =30,font="Helvetica 14 bold",bg="yellow",command=self.Patient_Reg)       
        self.button1.grid(row=1,column=0,pady=10)
        
        self.button2 = Button(self.LoginFrame, text="2.BOOK APPOINTMENT",width =30,font="Helvetica 14 bold",bg="yellow",command=self.Appointment_Form)
        self.button2.grid(row=2,column=0,pady=10)
        
        self.button3 = Button(self.LoginFrame, text="3.EXIT",width =30,font="Helvetica 14 bold",bg="yellow",command = self.Exit)
        self.button3.grid(row=3,column=0,pady=10)
    # public member function  
   #Function to Exit Menu Window
    def Exit(self):
        self.master.destroy()

    
    #Function to open Patient Registration Window   
    def Patient_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient(self.newWindow)
        
    #Function to open Appointment Window
    def Appointment_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Appointment(self.newWindow)

if __name__ == "__Menu__":
    Menu()
root=mainloop()




if __name__ == "__main__":
    main()
root=mainloop()