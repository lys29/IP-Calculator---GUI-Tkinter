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
        IMAGE_PATH = 'bg.png'
        WIDTH, HEIGHT = 1050, 450
        
        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
        lbl = tk.Label(self, image=img)
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
                #b = Entry(self, text="")
                #b.grid(row=i, column=j, padx=100)
                
        text = Label(self, text="IP Calculator Program", font=("ubuntu", 24), bg='light grey')
        text.grid(row=1, column=1, pady=50)
    #IP Address
        ia = Label(self, text="IP Address:", font=("Helvetica", 14), bg='light grey')
        ia.grid(row=2, column=1, sticky=W, padx=100)
        
        ip_entry = Entry(self, font=("Helvetica", 14))
        ip_entry.grid(row=3, column=1, sticky="we", columnspan=2, padx=93)
    #Subnet Mask 
        sm = Label(self, text="Subnet Mask:", font=("Helvetica", 14), bg='light grey')
        sm.grid(row=4, column=1, sticky=W, padx=100, pady=5)
        
        subnet_entry = Entry(self, font=("Helvetica", 14))
        subnet_entry.grid(row=4, column=2, sticky=W, columnspan=10)
    #Network Address
        n = Label(self, text="Network Address:", font=("Helvetica", 14), bg='light grey')
        n.grid(row=5, column=1, sticky=W, padx=100, pady=5)
        network_address = StringVar()
        network_address_entry = Entry(self, font=("Helvetica", 14), textvariable=network_address, state="readonly")
        network_address_entry.grid(row=5, column=2, sticky=W, columnspan=10)
    #Broadcast Address
        bc = Label(self, text="Broadcast Address:", font=("Helvetica", 14), bg='light grey')
        bc.grid(row=6, column=1, sticky=W, padx=100, pady=5)
        broadcast_address = StringVar()
        broadcast_address_entry = Entry(self, font=("Helvetica", 14), textvariable=broadcast_address, state="readonly" )
        broadcast_address_entry.grid(row=6, column=2, sticky=W, columnspan=10)
    #Total Number of Hosts
        noa = Label(self, text="Total Number of Hosts:", font=("Helvetica", 14), bg='light grey')
        noa.grid(row=7, column=1, sticky=W, padx=100, pady=5)
        Total_Number_of_Hosts = StringVar()
        Total_Number_of_Hosts_Entry = Entry(self, font=("Helvetica", 14), textvariable=Total_Number_of_Hosts, state="readonly")
        Total_Number_of_Hosts_Entry.grid(row=8, column=1, sticky="we", columnspan=2, padx=93)
        
        Sub = Button(self, text="Calculate", command=solve, font=("Helvetica", 14))
        Sub.grid(row=9, column=2, sticky="we", columnspan=2, padx=100, pady=15)
        
root = tk.Tk()
app = Window(root)
root.title("IP Calculator")
root.geometry("750x440")
root.mainloop()