import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import math

###########      VARIABLES      ###########
coeff_a = []
coeff_b = []
d = 0
input_m = 0
p_input = 0
p_output = 0
sampling_interval = 0


###########      FUNCTIONS      ###########


############      MAIN      ###########
# Create and configure window
master = tk.Tk()
master.configure(background="gray")
master.title("Simulación de Proceso")
master.geometry("700x250")

# Definition of TK variables
a1 = tk.Entry(master, font=("Arial", 18))
a2 = tk.Entry(master, font=("Arial", 18))
a3 = tk.Entry(master, font=("Arial", 18))
a4 = tk.Entry(master, font=("Arial", 18))

b0 = tk.Entry(master, font=("Arial", 18))
b1 = tk.Entry(master, font=("Arial", 18))
b2 = tk.Entry(master, font=("Arial", 18))
b3 = tk.Entry(master, font=("Arial", 18))
b4 = tk.Entry(master, font=("Arial", 18))

m =  tk.Entry(master, font=("Arial", 18))
pe = tk.Entry(master, font=("Arial", 18))
ps = tk.Entry(master, font=("Arial", 18))
t =  tk.Entry(master, font=("Arial", 18))

k_ent =     tk.Entry(master, font=("Arial", 18))
tau_ent =   tk.Entry(master, font=("Arial", 18))
theta_ent = tk.Entry(master, font=("Arial", 18))

kC_ent =    tk.Entry(master, font=("Arial", 18))
tauI_ent =  tk.Entry(master, font=("Arial", 18))
tauD_ent =  tk.Entry(master, font=("Arial", 18))
rk_ent =    tk.Entry(master, font=("Arial", 18))

master.mainloop()