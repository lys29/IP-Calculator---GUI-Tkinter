import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

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
            ip = ipaddress.ip_address(ip_entry.get())
            netmask = ipaddress.ip_address(netmask_entry.get())
            network = ipaddress.ip_network(f'{ip}/{netmask}', strict=False)

            network_label.config(text='Network: ' + str(network.network_address))
            broadcast_label.config(text='Broadcast: ' + str(network.broadcast_address))
            host_range_label.config(text='Host Range: ' + str(next(network.hosts())) + ' - ' + str(next(network.hosts())))

    #RIGHT OUTPUT
        #height = 1
        #width = 3
        #for i in range(height): #Rows
            #for j in range(width): #Columns
                #b = Entry(self, text="")
                #b.grid(row=i, column=j, padx=100)
                
        text = Label(self, text="IP Calculator Program", font=("ubuntu", 24), bg='light grey')
        text.grid(row=1, column=2, pady=50)
    #IP Address
        ia = Label(self, text="IP Address:", font=("Helvetica", 14), bg='light grey')
        ia.grid(row=2, column=1, sticky=W, padx=100)
        
        iae = Entry(self, font=("Helvetica", 14))
        iae.grid(row=3, column=1, sticky="we", columnspan=2, padx=93)
    #Subnet Mask 
        sm = Label(self, text="Subnet Mask:", font=("Helvetica", 14), bg='light grey')
        sm.grid(row=4, column=1, sticky=W, padx=100, pady=5)
        
        sme = Entry(self, font=("Helvetica", 14))
        sme.grid(row=4, column=2, sticky=W, columnspan=10)
    #Network
        n = Label(self, text="Network:", font=("Helvetica", 14), bg='light grey')
        n.grid(row=5, column=1, sticky=W, padx=100, pady=5)
        
        ne = Entry(self, font=("Helvetica", 14))
        ne.grid(row=5, column=2, sticky=W, columnspan=10)
    #Broadcast
        bc = Label(self, text="Broadcast:", font=("Helvetica", 14), bg='light grey')
        bc.grid(row=6, column=1, sticky=W, padx=100, pady=5)
        
        bce = Entry(self, font=("Helvetica", 14))
        bce.grid(row=6, column=2, sticky=W, columnspan=10)
    #Host Range
        har = Label(self, text="Host Address Range:", font=("Helvetica", 14), bg='light grey')
        har.grid(row=7, column=1, sticky=W, padx=100, pady=5)
        
        hare = Entry(self, font=("Helvetica", 14))
        hare.grid(row=8, column=1, sticky="we", columnspan=2, padx=93)
        
        Sub = Button(self, text="Calculate", command=solve, font=("Helvetica", 14))
        Sub.grid(row=9, column=2, sticky="we", columnspan=2, padx=100, pady=15)
        
root = tk.Tk()
app = Window(root)
root.title("IP Calculator")
root.geometry("1000x450")
root.mainloop()