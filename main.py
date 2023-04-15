import tkinter as tk

master = tk.Tk()

master.title("MARKSHEET")
master.geometry("700x250")

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)

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



master.mainloop()