import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import math

###########      VARIABLES      ###########
coeff_a = []
coeff_b = []
input_m = 0
p_input = 0
p_output = 0
sampling_interval = 0
entrada = []
salida = []
k = 0
error = []
tau = 0
theta = 0


###########      FUNCTIONS      ###########
def CreateGUI():
    # SYSTEM
    tk.Label(master, text="PLANTA", font=("Arial", 20), background='black').grid(row=1, column=0, columnspan=13, sticky='ew')
    
    tk.Label(master, text="A1: ", font=("Arial", 20), background="gray").grid(row=3, column=0, sticky='e')
    tk.Label(master, text="A2: ", font=("Arial", 20), background="gray").grid(row=4, column=0, sticky='e')
    tk.Label(master, text="A3: ", font=("Arial", 20), background="gray").grid(row=5, column=0, sticky='e')
    tk.Label(master, text="A4: ", font=("Arial", 20), background="gray").grid(row=6, column=0, sticky='e')

    a1.grid(row=3, column=1, columnspan=3, sticky='e')
    a2.grid(row=4, column=1, columnspan=3, sticky='e')
    a3.grid(row=5, column=1, columnspan=3, sticky='e')
    a4.grid(row=6, column=1, columnspan=3, sticky='e')

    tk.Label(master, text="B1: ", font=("Arial", 20), background="gray").grid(row= 3, column=5, sticky='e')
    tk.Label(master, text="B2: ", font=("Arial", 20), background="gray").grid(row= 4, column=5, sticky='e')
    tk.Label(master, text="B3: ", font=("Arial", 20), background="gray").grid(row= 5, column=5, sticky='e')
    tk.Label(master, text="B4: ", font=("Arial", 20), background="gray").grid(row= 6, column=5, sticky='e')

    b1.grid(row= 3, column=6, columnspan=3, sticky='e')
    b2.grid(row= 4, column=6, columnspan=3, sticky='e')
    b3.grid(row= 5, column=6, columnspan=3, sticky='e')
    b4.grid(row= 6, column=6, columnspan=3, sticky='e')

    tk.Label(master, text="PE: ", font=("Arial", 20), background="gray").grid(row=4, column=9, sticky='e')
    tk.Label(master, text="PS: ", font=("Arial", 20), background="gray").grid(row=5, column=9, sticky='e')
    tk.Label(master, text="T: ",  font=("Arial", 20), background="gray").grid(row=6, column=9, sticky='e')

    pe.grid(row=4, column=10, columnspan=3, sticky='e')
    ps.grid(row=5, column=10, columnspan=3, sticky='e')
    t.grid( row=6, column=10, columnspan=3, sticky='e')
    
    tk.Label(master, text="k: ", font=("Arial", 20), background="gray").grid(row=7, column=0, sticky='e')
    k_p.grid(row=7,  column=1, columnspan=3, sticky='e')
    tk.Label(master, text=u'\u03C4' + ': ', font=("Arial", 20), background="gray").grid(row=7, column=5, sticky='e')
    tau_p.grid(row=7, column=6, columnspan=3, sticky='e')
    tk.Label(master, text=u'\u03B8' + u'\u00B9' + ': ', font=("Arial", 20), background="gray").grid(row=7, column=9, sticky='e')
    theta_p.grid(row=7, column=11, columnspan=3, sticky='e')

    # ACTIONS
    tk.Label(master, text=" ", font=("Arial", 20), background="gray").grid(row=11, column=0, columnspan=13, sticky='ew')
    tk.Label(master, text="ACCIONES", font=("Arial", 20), background='black').grid(row=12, column=0, columnspan=13, sticky='ew')

    tk.Label(master, text=" ", font=("Arial", 20), background="gray").grid(row=13, column=0, columnspan=6, sticky='ew')
    tk.Label(master, text="Valor: ", font=("Arial", 20), background="gray").grid(row=13, column=7, sticky='e')
    m.grid(row=13, column=8, columnspan=5, sticky='e')
    tk.Label(master, text=" ", font=("Arial", 20), background="gray").grid(row=14, column=0, columnspan=13, sticky='ew')
    tk.Button(master, text="Enter", font=("Arial", 20), command=lambda: execute()).grid(row=15, column=0, columnspan=13)

def checkEmptyFields():
    global entrada
    global salida
    global error
    global coeff_a
    global coeff_b
    global p_input
    global p_output
    global k
    global tau
    global theta
    global input_m
    global sampling_interval

    for i, a in enumerate(coeff_a):
        if a == "":
            coeff_a[i] = 0

    for i, b in enumerate(coeff_b):
        if b == "":
            coeff_b[i] = 0
    
    if p_input == "":
        p_input = 0
    if input_m == "":
        input_m = 0
    if p_output == "":
        p_output = 0
    if tau == "":
        tau = 0
    if theta == "":
        theta = 0
    if sampling_interval == "":
        sampling_interval = 0

def print_vals():
    for i, a in enumerate(coeff_a):
        print("a{} = {}".format(i, a))
    for i, b in enumerate(coeff_b):
        print("b{} = {}".format(i, b))
    print("p_input = {}".format(p_input))
    print("p_output = {}".format(p_output))
    print("tau = {}".format(tau))
    print("theta = {}".format(theta))
    print("input_m = {}".format(input_m))
    print("sampling_interval = {}".format(sampling_interval))
    print("k = {}".format(k))

def execute():
    global entrada
    global salida
    global error
    global coeff_a
    global coeff_b
    global p_input
    global p_output
    global k
    global tau
    global theta
    global input_m
    global sampling_interval

    coeff_a.append(a1.get())
    coeff_a.append(a2.get())
    coeff_a.append(a3.get())
    coeff_a.append(a4.get())

    coeff_b.append(b0.get())
    coeff_b.append(b1.get())
    coeff_b.append(b2.get())
    coeff_b.append(b3.get())
    coeff_b.append(b4.get())
    

    input_m = m.get()
    p_input = pe.get()
    p_output = ps.get()
    sampling_interval = t.get()

    k = k_p.get()
    tau = tau_p.get()
    theta = theta_p.get()

    checkEmptyFields()
    print_vals()


############      MAIN      ###########
# Create and configure master
master = tk.Tk()
master.configure(background="gray")
master.title("Simulación de Proceso")
master.geometry("885x480")

# Definition of TK variables
a1 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
a2 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
a3 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
a4 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")

b0 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
b1 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
b2 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
b3 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
b4 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")

m =  tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
pe = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
ps = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
t =  tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")

k_p =     tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
tau_p =   tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
theta_p = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")

CreateGUI()



master.mainloop()