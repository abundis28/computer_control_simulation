import math
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

###########      VARIABLES      ###########
input_ref = 0
p_input = 0
p_output = 0
sampling_interval = 0
retraso = 0
active_Flag = False
k = 0.0
graph_range = 20
graph_y_range = 100
gain_static = 0.0
gain_contr = 0.0
tau = 0.0
theta_p = 0.0
theta = 0.0
m = 0.0
ti = 0.0
td = 0.0
control_mode = 0    # Open loop = 0 // Closed loop = 1
model_mode = 0      # ARX = 0 // 1st Order = 1
coeff_a = [0.0] * 5
coeff_b = [0.0] * 6
betas =   [0.0] * 3
entrada = [0.0] * graph_range
salida =  [0.0] * graph_range
error =   [0.0] * graph_range
ref =     [0.0] * graph_range

###########      FUNCTIONS      ###########
def CreateGUI():
    # Text fields
    tk.Label(master, text="PLANTA", font=("Arial", 20), background='black', fg="white").grid(row=1, column=0, columnspan=13, sticky='ew')

    tk.Radiobutton(master, text="ARX",       font=("Arial", 20), variable = model_tk, value = 0).grid(row = 2, column = 1, columnspan= 5)
    tk.Radiobutton(master, text="1er orden", font=("Arial", 20), variable = model_tk, value = 1).grid(row = 2, column = 7, columnspan= 5)

    tk.Label(master, text="A1: ", font=("Arial", 20), background="gray").grid(row=3, column=0, sticky='e')
    tk.Label(master, text="A2: ", font=("Arial", 20), background="gray").grid(row=4, column=0, sticky='e')
    tk.Label(master, text="A3: ", font=("Arial", 20), background="gray").grid(row=5, column=0, sticky='e')
    tk.Label(master, text="A4: ", font=("Arial", 20), background="gray").grid(row=6, column=0, sticky='e')
    tk.Label(master, text="A5: ", font=("Arial", 20), background="gray").grid(row=7, column=0, sticky='e')

    a1.grid(row=3, column=1, columnspan=3, sticky='e')
    a2.grid(row=4, column=1, columnspan=3, sticky='e')
    a3.grid(row=5, column=1, columnspan=3, sticky='e')
    a4.grid(row=6, column=1, columnspan=3, sticky='e')
    a5.grid(row=7, column=1, columnspan=3, sticky='e')

    tk.Label(master, text="B0: ", font=("Arial", 20), background="gray").grid(row= 3, column=5, sticky='e')
    tk.Label(master, text="B1: ", font=("Arial", 20), background="gray").grid(row= 4, column=5, sticky='e')
    tk.Label(master, text="B2: ", font=("Arial", 20), background="gray").grid(row= 5, column=5, sticky='e')
    tk.Label(master, text="B3: ", font=("Arial", 20), background="gray").grid(row= 6, column=5, sticky='e')
    tk.Label(master, text="B4: ", font=("Arial", 20), background="gray").grid(row= 7, column=5, sticky='e')
    tk.Label(master, text="B5: ", font=("Arial", 20), background="gray").grid(row= 8, column=5, sticky='e')

    b0.grid(row= 3, column=6, columnspan=3, sticky='e')
    b1.grid(row= 4, column=6, columnspan=3, sticky='e')
    b2.grid(row= 5, column=6, columnspan=3, sticky='e')
    b3.grid(row= 6, column=6, columnspan=3, sticky='e')
    b4.grid(row= 7, column=6, columnspan=3, sticky='e')
    b5.grid(row= 8, column=6, columnspan=3, sticky='e')

    tk.Label(master, text="PE: ",    font=("Arial", 20), background="gray").grid(row=3, column=9, sticky='e')
    tk.Label(master, text="PS: ",    font=("Arial", 20), background="gray").grid(row=4, column=9, sticky='e')
    tk.Label(master, text="T: ",     font=("Arial", 20), background="gray").grid(row=5, column=9, sticky='e')
    tk.Label(master, text="d: ",     font=("Arial", 20), background="gray").grid(row=6, column=9, sticky='e')
    
    pe.grid(   row=3, column=10, columnspan=3, sticky='e')
    ps.grid(   row=4, column=10, columnspan=3, sticky='e')
    t.grid(    row=5, column=10, columnspan=3, sticky='e')
    d.grid(    row=6, column=10, columnspan=3, sticky='e')

    tk.Label(master, text=" ", font=("Arial", 20), background="gray").grid(row=9, column=0, columnspan=13, sticky='ew')

    tk.Label(master, text="Tau: ", font=("Arial", 20), background="gray").grid(row=10, column=0, sticky='e')
    tk.Label(master, text=u'\u03F4\u0027' + ': ', font=("Arial", 20), background="gray").grid(row=10, column=5, sticky='e')
    tk.Label(master, text="K: ", font=("Arial", 20), background="gray").grid(row=10, column=9, sticky='e')

    tau_tk.grid(   row=10, column=1,  columnspan=3, sticky='e')
    theta_tk.grid( row=10, column=6, columnspan=3, sticky='e')
    gain_s_tk.grid( row=10, column=10, columnspan=3, sticky='e')

    tk.Label(master, text=" ", font=("Arial", 20), background="gray").grid(row=11, column=0, columnspan=13, sticky='ew')
    tk.Label(master, text="CONTROL", font=("Arial", 20), background='black', fg="white").grid(row=12, column=0, columnspan=13, sticky='ew')

    tk.Radiobutton(master, text="Manual", font=("Arial", 20), variable = mode_tk, value = 0).grid(row = 13, column = 1, columnspan= 5)
    tk.Radiobutton(master, text="Auto",   font=("Arial", 20), variable = mode_tk, value = 1).grid(row = 13, column = 7, columnspan= 5)

    tk.Label(master, text="Kc: ", font=("Arial", 20), background="gray").grid(row=14, column=0, sticky='e')
    tk.Label(master, text="Ti: ", font=("Arial", 20), background="gray").grid(row=14, column=5, sticky='e')
    tk.Label(master, text="Td: ", font=("Arial", 20), background="gray").grid(row=14, column=9, sticky='e')

    gain_c_tk.grid(row=14, column=1,  columnspan=3, sticky='e')
    ti_tk.grid(  row=14, column=6,  columnspan=3, sticky='e')
    td_tk.grid(  row=14, column=10,  columnspan=3, sticky='e')

    tk.Label(master, text=" ", font=("Arial", 20), background="gray").grid(row=15, column=0, columnspan=13, sticky='ew')
    tk.Label(master, text="ACCIONES", font=("Arial", 20), background='black', fg="white").grid(row=16, column=0, columnspan=13, sticky='ew')
    tk.Label(master, text="M/R0: ",  font=("Arial", 20), background="gray").grid(row=17, column=5, sticky='e')
    m_in.grid( row=17, column=6, columnspan=2, sticky='e')

    tk.Label(master, text=" ", font=("Arial", 20), background="gray").grid(row=18, column=0, columnspan=13, sticky='ew')
    tk.Button(master, text="Stop/Reset", font=("Arial", 20), command=lambda: reset()).grid(row=19, column=0, columnspan=6)
    tk.Button(master, text="Start/Update", font=("Arial", 20), command=lambda: updateStart()).grid(row=19, column=7, columnspan=6)

def checkEmptyFields():
    global entrada
    global salida
    global error
    global coeff_a
    global coeff_b
    global p_input
    global p_output
    global retraso
    global input_ref
    global sampling_interval
    global theta_p
    global tau
    global gain_static
    global gain_contr
    global ti
    global td

    for i, a in enumerate(coeff_a):
        if a == "":
            coeff_a[i] = 0.0

    for i, b in enumerate(coeff_b):
        if b == "":
            coeff_b[i] = 0.0
    
    if p_input == "":
        p_input = 0.0
    if input_ref == "":
        input_ref = 0.0
    if p_output == "":
        p_output = 0.0
    if retraso == "":
        retraso = 0.0
    if sampling_interval == "":
        sampling_interval = 1
    if gain_static == "":
        gain_static = 1
    if gain_contr == "":
        gain_contr = 1
    if theta_p == "":
        theta_p = 0.0
    if tau == "":
        tau = 0.0
    if ti == "":
        ti = 0.0
    if td == "":
        td = 0.0

def printVals():
    print(entrada)
    print(salida)
    print(error)
    print("ck: {} - mk: {} - input_ref: {} - error: {} - T: {} - d: {} - t: {} - theta_p: {} - K: {} - Kc - ti: {} - td: {}".format(salida[0],entrada[0],input_ref,error[0],sampling_interval,retraso,tau,theta_p,gain_static,gain_contr,ti,td))
    print("--------------------------\n")

def getVals():
    global entrada
    global salida
    global error
    global coeff_a
    global coeff_b
    global p_input
    global p_output
    global input_ref
    global sampling_interval
    global retraso
    global control_mode
    global tau
    global theta_p
    global theta
    global m
    global gain_static
    global gain_contr
    global ti
    global td
    global control_mode
    global model_mode

    coeff_a[0] = a1.get()
    coeff_a[1] = a2.get()
    coeff_a[2] = a3.get()
    coeff_a[3] = a4.get()
    coeff_a[4] = a5.get()

    coeff_b[0] = b0.get()
    coeff_b[1] = b1.get()
    coeff_b[2] = b2.get()
    coeff_b[3] = b3.get()
    coeff_b[4] = b4.get()
    coeff_b[5] = b5.get()

    input_ref = m_in.get()
    p_input = pe.get()
    p_output = ps.get()
    sampling_interval = t.get()
    retraso = d.get()
    gain_static = gain_s_tk.get()
    gain_contr = gain_c_tk.get()
    tau = tau_tk.get()
    theta_p = theta_tk.get()
    ti = ti_tk.get()
    td = td_tk.get()
    control_mode = mode_tk.get()
    model_mode = model_tk.get()

    checkEmptyFields()

    try: 
        coeff_a = list(map(float, coeff_a))
        coeff_b = list(map(float, coeff_b))
        input_ref = float(input_ref)
        p_input = float(p_input)
        p_output = float(p_output)
        sampling_interval = float(sampling_interval)
        retraso = int(retraso)
        tau = float(tau)
        gain_static = float(gain_static)
        gain_contr = float(gain_contr)
        theta_p = float(theta_p)
        control_mode = int(control_mode)
        model_mode = int(model_mode)
        ti = float(ti)
        td = float(td)
    except:
        print("Wrong value(s)")

    if model_mode:              # 1st order
        retraso = int(theta_p/sampling_interval)
        theta = theta_p - retraso * sampling_interval
        m = 1 - (theta/sampling_interval)
        coeff_a = [0.0] * 5
        coeff_b = [0.0] * 6
        coeff_a[0] = gain_static * math.exp(-sampling_interval/tau)
        coeff_b[0] = gain_static * (1 - math.exp((-m * sampling_interval) / tau))
        coeff_b[1] = gain_static * (math.exp((-m * sampling_interval) / tau) - math.exp(-sampling_interval / tau))
    
    if control_mode:
        betas[0] = gain_contr * (1 + (sampling_interval / ti) + (td / sampling_interval))
        betas[1] = gain_contr * (-1 - 2 * (td / sampling_interval))
        betas[2] = gain_contr * (td / sampling_interval)

def shiftLists():
    global entrada
    global salida
    global error
    global ref

    entrada = entrada[-1:] +  entrada[:-1]
    salida  = salida[-1:]  +  salida[:-1]
    error   = error[-1:]   +  error[:-1]
    ref     = ref[-1:]   +  ref[:-1]

def calcOutput():
    global entrada
    global salida
    global error
    global ref
    global betas
    
    sum_a = 0
    for i, val in enumerate(coeff_a):
        sum_a += val * salida[i]
    sum_b = 0
    for i, val in enumerate(coeff_b):
        sum_b += val * entrada[i + retraso - 1]
    salida_o = sum_a + sum_b + p_output

    entrada_i = input_ref + p_input
    if control_mode:        # automatic control
        for i, beta in enumerate(betas):
            entrada_i += error[i] * beta

    if entrada_i < 0:
        entrada_i = 0
    elif entrada_i > 100:
        entrada_i = 100
    
    shiftLists()
    error[0] = input_ref - salida_o
    entrada[0] = entrada_i
    salida[0] = salida_o

def setupGraphs():
    graph_m.set_title('m(k)')
    graph_m.set_ylim([0, graph_y_range])
    graph_m.grid(True)

    graph_c.set_title('c(k)')
    graph_c.set_ylim([0, graph_y_range])
    graph_c.grid(True)

def updateGraphs():
    if active_Flag:
        graph_m.cla()
        graph_c.cla()
        setupGraphs()

        graph_m.plot(np.arange(k - graph_range, k, sampling_interval), entrada[::-1], 'g', label='c(k)')
        graph_c.plot(np.arange(k - graph_range, k, sampling_interval), salida[::-1],  'b', label='m(k)')
    
def updateStart():
    global active_Flag
    active_Flag = True
    getVals()

def reset():
    global entrada
    global salida
    global error
    global coeff_a
    global coeff_b
    global p_input
    global p_output
    global input_ref
    global sampling_interval
    global retraso
    global control_mode
    global model_mode
    global tau
    global theta_p
    global gain_static
    global gain_contr
    global active_Flag
    global k
    global ti
    global td
    global ref
    global betas

    input_ref = 0
    p_input = 0
    p_output = 0
    sampling_interval = 0
    retraso = 0
    active_Flag = False
    k = 0.0
    gain_static = 0.0
    tau = 0.0
    theta_p = 0.0
    ti = 0.0
    td = 0.0
    gain_static = 0.0
    gain_contr = 0.0
    control_mode = 0    # Open loop = 0 // Closed loop = 1
    model_mode = 0      # ARX = 0 // 1st order = 1
    coeff_a = [0.0] * 5
    coeff_b = [0.0] * 6
    betas =   [0.0] * 3
    entrada = [0.0] * graph_range
    salida =  [0.0] * graph_range
    error =   [0.0] * graph_range
    ref =     [0.0] * graph_range

############      MAIN      ###########
# Create and configure TKinter components
master = tk.Tk()
master.configure(background="gray")
master.title("Simulación de Proceso")
master.geometry("1110x760")

a1 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
a2 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
a3 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
a4 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
a5 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")

b0 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
b1 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
b2 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
b3 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
b4 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
b5 = tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")

m_in =  tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
pe =    tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
ps =    tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
t =     tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
d =     tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")

mode_tk =           tk.IntVar()
gain_static_tk =    tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
tau_tk =            tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
theta_tk =          tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
ti_tk =             tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
td_tk =             tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
gain_s_tk =         tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
gain_c_tk =         tk.Entry(master, font=("Arial", 20), fg="black", background="dark gray")
model_tk =          tk.IntVar()

# Create graphical user interface
CreateGUI()

# Create graphs
graph, (graph_m, graph_c) = plt.subplots(nrows=2, ncols=1, figsize=(8,5))
graph.tight_layout(pad=2.0)
graph_m.axis([k - graph_range, k, 0, graph_y_range])
graph_c.axis([k - graph_range, k, 0, graph_y_range])
setupGraphs()

# Main loop
while True:
    master.update_idletasks()
    master.update()

    plt.pause(0.1)

    if active_Flag:
        plt.pause(sampling_interval)
        calcOutput()
        k += sampling_interval
        updateGraphs()
        # printVals()
