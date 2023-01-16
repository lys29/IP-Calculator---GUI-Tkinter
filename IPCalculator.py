import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import ipaddress

class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH)
        
    #Background
        IMAGE_PATH = 'bg.jpg'
        WIDTH, HEIGHT = 870, 480
        
        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        lbl = tk.Label(root, image=img)
        root.wm_attributes("-transparentcolor", 'grey')
        lbl.img = img 
        lbl.place(relx=0.5, rely=0.5, anchor='center') 
    
        def solve():
            try:
                ip_network = ipaddress.ip_network(ip_entry.get() + "/" + subnet_entry.get())
                network_address.set(str(ip_network.network_address))
                broadcast_address.set(str(ip_network.broadcast_address))
                Total_Number_of_Hosts.set(str(ip_network.num_addresses))
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            
    #RIGHT OUTPUT
        #height = 1
        #width = 3
        #for i in range(height): #Rows
            #for j in range(width): #Columns
                #b = Entry(root, text="")
                #b.grid(row=i, column=j, padx=100)
                
        text = Label(root, text="IP Calculator", font=("ubuntu", 28), bg='light grey')
        text.place(x=100, y=85, anchor='sw')
    #IP Address
        ia = Label(root, text="IP Address:", font=("Helvetica", 20), bg='light grey')
        ia.place(x=55, y=135, anchor='sw')
        
        ip_entry = Entry(root, font=("Helvetica", 20))
        ip_entry.place(x=240, y=135, anchor='sw', width=210)
    #Subnet Mask 
        sm = Label(root, text="Subnet Mask:", font=("Helvetica", 20), bg='light grey')
        sm.place(x=55, y=190, anchor='sw')
        
        subnet_entry = Entry(root, font=("Helvetica", 20))
        subnet_entry.place(x=240, y=155, width=210)
    #Network Address
        n = Label(root, text="Network Address:", font=("Helvetica", 20), bg='light grey')
        n.place(x=55, y=250, anchor='sw')
        network_address = StringVar()
        network_address_entry = Entry(root, font=("Helvetica", 20), textvariable=network_address, state="readonly")
        network_address_entry.place(x=305,y=210, width=210)
    #Broadcast Address
        bc = Label(root, text="Broadcast Address:", font=("Helvetica", 20), bg='light grey')
        bc.place(x=55, y=300, anchor='sw')
        broadcast_address = StringVar()
        broadcast_address_entry = Entry(root, font=("Helvetica", 20), textvariable=broadcast_address, state="readonly" )
        broadcast_address_entry.place(x=305, y=260, width=210)
    #Total Number of Hosts
        noa = Label(root, text="Total Number of Hosts:", font=("Helvetica", 20), bg='light grey')
        noa.place(x=55, y=345, anchor='sw')
        Total_Number_of_Hosts = StringVar()
        Total_Number_of_Hosts_Entry = Entry(root, font=("Helvetica", 20), textvariable=Total_Number_of_Hosts, state="readonly")
        Total_Number_of_Hosts_Entry.place(x=355, y=310, width=210)
        
        Sub = Button(root, text="Calculate", command=solve, font=("Inter", 19), border=0, background='light grey')
        Sub.place(x=160, y=425, anchor='sw')
        
root = tk.Tk()
app = Window(root)
root.title("IP Calculator")
root.geometry("791x445")
root.mainloop()