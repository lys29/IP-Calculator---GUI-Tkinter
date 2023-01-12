import tkinter as tk
from tkinter import *

class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.pack(padx=100, pady=50, fill="both", expand=True)
    
        def solve():
            ip = ipaddress.ip_address(ip_entry.get())
            netmask = ipaddress.ip_address(netmask_entry.get())
            network = ipaddress.ip_network(f'{ip}/{netmask}', strict=False)

            network_label.config(text='Network: ' + str(network.network_address))
            broadcast_label.config(text='Broadcast: ' + str(network.broadcast_address))
            host_range_label.config(text='Host Range: ' + str(next(network.hosts())) + ' - ' + str(next(network.hosts())))

    
        text = Label(self, text="IP Calculator Program", font=("Helvetica", 18))
        text.grid(row=1, column=2)
    #IP Address
        ia = Label(self, text="IP Address:", font=("Helvetica", 12))
        ia.grid(row=2, column=1, sticky=W)
        
        iae = Entry(self)
        iae.grid(row=3, column=1, sticky="we", columnspan=2)
    #Subnet Mask 
        sm = Label(self, text="Subnet Mask:", font=("Helvetica", 12))
        sm.grid(row=4, column=1, sticky=W)
        
        sme = Entry(self)
        sme.grid(row=4, column=2, sticky="we", columnspan=2)
    #Network
        n = Label(self, text="Network:", font=("Helvetica", 12))
        n.grid(row=5, column=1, sticky=W)
        
        ne = Entry(self)
        ne.grid(row=5, column=2, sticky="we", columnspan=2)
    #Broadcast
        bc = Label(self, text="Broadcast:", font=("Helvetica", 12))
        bc.grid(row=6, column=1, sticky=W)
        
        bce = Entry(self)
        bce.grid(row=6, column=2, sticky="we", columnspan=2)
    #Host Range
        har = Label(self, text="Host Address Range:", font=("Helvetica", 12))
        har.grid(row=7, column=1, sticky=W)
        
        hare = Entry(self)
        hare.grid(row=8, column=1, sticky="we", columnspan=3)
        
        Sub = Button(self, text="Calculate", command=solve)
        Sub.grid(row=9, column=2, sticky="we", columnspan=2)
         
root = tk.Tk()
app = Window(root)
root.title("IP Calculator")
root.geometry("800x400")
root.mainloop()