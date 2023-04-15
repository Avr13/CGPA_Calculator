import tkinter as tk

master = tk.Tk()

master.title("MARKSHEET")
master.geometry("700x250")

e1 = tk.Entery(master)
e2 = tk.Entery(master)
e3 = tk.Entery(master)
e4 = tk.Entery(master)
e5 = tk.Entery(master)
e6 = tk.Entery(master)
e7 = tk.Entery(master)

def display():
    tot = 0
    if e4.get() == "A":
        tk.Label(master, text = "40").grid(row=3, column=4)
        tot +=40

    if e4.get() == "B":
        tk.Label(master, text = "36").grid(row=3, column=4)
        tot +=36
    if e4.get() == "C":
        tk.Label(master, text = "32").grid(row=3, column=4)
        tot +=32
    if e4.get() == "D":
        tk.Label(master, text = "28").grid(row=3, column=4)
        tot +=28  
        
    if e5.get() == "A":
        tk.Label(master, text = "40").grid(row=3, column=4)
        tot +=40

    if e5.get() == "B":
        tk.Label(master, text = "36").grid(row=3, column=4)
        tot +=36
    if e5.get() == "C":
        tk.Label(master, text = "32").grid(row=3, column=4)
        tot +=32
    if e5.get() == "D":
        tk.Label(master, text = "28").grid(row=3, column=4)
        tot +=28  
    if e6.get() == "A":
        tk.Label(master, text = "40").grid(row=3, column=4)
        tot +=40

    if e6.get() == "B":
        tk.Label(master, text = "36").grid(row=3, column=4)
        tot +=36
    if e6.get() == "C":
        tk.Label(master, text = "32").grid(row=3, column=4)
        tot +=32
    if e6.get() == "D":
        tk.Label(master, text = "28").grid(row=3, column=4)
        tot +=28
    if e7.get() == "A":
        tk.Label(master, text = "40").grid(row=3, column=4)
        tot +=40

    if e7.get() == "B":
        tk.Label(master, text = "36").grid(row=3, column=4)
        tot +=36
    if e7.get() == "C":
        tk.Label(master, text = "32").grid(row=3, column=4)
        tot +=32
    if e7.get() == "D":
        tk.Label(master, text = "28").grid(row=3, column=4)
        tot +=28 
    tk.Label(master,text=str(tot)).grid(row=7,column=4)
    tk.Label(master,text=str(tot/15)).grid(row=8,column=4)

tk.Label(master, text="Name").grid(row=0,column=0)
tk.Label(master, text="Registration Number").grid(row=0,column=3)
tk.Label(master, text="Roll Number").grid(row=1,column=0)

master.mainloop()