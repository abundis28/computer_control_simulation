import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import math

# VARIABLES

# FUNCTIONS

# MAIN
root = tk.Tk()
root.title("tab")
tabControl = ttk.Notebook(root)

auto = ttk.Frame(tabControl)
manual = ttk.Frame(tabControl)
title = ttk.Label(tabControl)

tabControl.add(title, text="Simulador Controlador")
tabControl.add(auto, text="Automatico")
tabControl.add(manual, text="Manual")
tabControl.pack(expand=1, fill="both")

root.mainloop()