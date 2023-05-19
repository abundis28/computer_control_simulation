import tkinter as tk
import matplotlib.pyplot as plt
import time

###########      VARIABLES      ###########
input_m = 0
p_input = 0
p_output = 0
sampling_interval = 0
retraso = 0
active = False
coeff_a = [0] * 4
coeff_b = [0] * 5
entrada = [0] * 100
salida =  [0] * 100
error =   [0] * 100

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

    tk.Label(master, text="B0: ", font=("Arial", 20), background="gray").grid(row= 3, column=5, sticky='e')
    tk.Label(master, text="B1: ", font=("Arial", 20), background="gray").grid(row= 4, column=5, sticky='e')
    tk.Label(master, text="B2: ", font=("Arial", 20), background="gray").grid(row= 5, column=5, sticky='e')
    tk.Label(master, text="B3: ", font=("Arial", 20), background="gray").grid(row= 6, column=5, sticky='e')
    tk.Label(master, text="B4: ", font=("Arial", 20), background="gray").grid(row= 7, column=5, sticky='e')

    b0.grid(row= 3, column=6, columnspan=3, sticky='e')
    b1.grid(row= 4, column=6, columnspan=3, sticky='e')
    b2.grid(row= 5, column=6, columnspan=3, sticky='e')
    b3.grid(row= 6, column=6, columnspan=3, sticky='e')
    b4.grid(row= 7, column=6, columnspan=3, sticky='e')

    tk.Label(master, text="PE: ", font=("Arial", 20), background="gray").grid(row=3, column=9, sticky='e')
    tk.Label(master, text="PS: ", font=("Arial", 20), background="gray").grid(row=4, column=9, sticky='e')
    tk.Label(master, text="T: ",  font=("Arial", 20), background="gray").grid(row=5, column=9, sticky='e')
    tk.Label(master, text="d: ",  font=("Arial", 20), background="gray").grid(row=6, column=9, sticky='e')

    pe.grid(row=3, column=10, columnspan=3, sticky='e')
    ps.grid(row=4, column=10, columnspan=3, sticky='e')
    t.grid( row=5, column=10, columnspan=3, sticky='e')
    d.grid( row=6,  column=10, columnspan=3, sticky='e')

    # ACTIONS
    tk.Label(master, text=" ", font=("Arial", 20), background="gray").grid(row=11, column=0, columnspan=13, sticky='ew')
    tk.Label(master, text="ACCIONES", font=("Arial", 20), background='black').grid(row=12, column=0, columnspan=13, sticky='ew')

    tk.Label(master, text=" ", font=("Arial", 20), background="gray").grid(row=13, column=0, columnspan=6, sticky='ew')
    tk.Label(master, text="Entrada: ", font=("Arial", 20), background="gray").grid(row=13, column=7, sticky='e')
    m.grid(row=13, column=8, columnspan=5, sticky='e')
    tk.Label(master, text=" ", font=("Arial", 20), background="gray").grid(row=14, column=0, columnspan=13, sticky='ew')
    tk.Button(master, text="Start", font=("Arial", 20), command=lambda: execute()).grid(row=15, column=0, columnspan=13)

def checkEmptyFields():
    global entrada
    global salida
    global error
    global coeff_a
    global coeff_b
    global p_input
    global p_output
    global retraso
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
    if retraso == "":
        retraso = 1
    if sampling_interval == "":
        sampling_interval = 0

def printVals():
    print("--------------------------")
    for i, a in enumerate(coeff_a):
        print("a{} = {} // type = {}".format(i, a, type(a)))
    for i, b in enumerate(coeff_b):
        print("b{} = {} // type = {}".format(i, b, type(b)))
    print("p_input = {} // type = {}".format(p_input, type(p_input)))
    print("p_output = {} // type = {}".format(p_output, type(p_output)))
    print("input_m = {} // type = {}".format(input_m, type(input_m)))
    print("sampling_interval = {} // type = {}".format(sampling_interval, type(sampling_interval)))
    print("d = {} // type = {}".format(retraso, type(retraso)))

def getVals():
    global entrada
    global salida
    global error
    global coeff_a
    global coeff_b
    global p_input
    global p_output
    global input_m
    global sampling_interval
    global retraso

    coeff_a[0] = a1.get()
    coeff_a[1] = a2.get()
    coeff_a[2] = a3.get()
    coeff_a[3] = a4.get()

    coeff_b[0] = b0.get()
    coeff_b[1] = b1.get()
    coeff_b[2] = b2.get()
    coeff_b[3] = b3.get()
    coeff_b[4] = b4.get()
    
    input_m = m.get()
    p_input = pe.get()
    p_output = ps.get()
    sampling_interval = t.get()
    retraso = d.get()

    try: 
        coeff_a = list(map(float, coeff_a))
        coeff_b = list(map(float, coeff_b))
        input_m = float(input_m)
        p_input = float(p_input)
        p_output = float(p_output)
        sampling_interval = float(sampling_interval)
        retraso = float(retraso)
    except:
        print("Missing value(s)")

def calcOutput():
    global entrada
    global salida
    global error
    print("Calculating output...\n")

def updateGraphs():
    pass

def execute():
    getVals()

    while True:
        master.update_idletasks()
        master.update()
        checkEmptyFields()
        printVals()
        calcOutput()
        updateGraphs()

        time.sleep(sampling_interval)


############      MAIN      ###########
# Create and configure master
master = tk.Tk()
master.configure(background="gray")
master.title("Simulación de Proceso")
master.geometry("885x375")

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
d =  tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")

CreateGUI()

master.mainloop()