import tkinter as tk
from tkinter import *

root = Tk()
root.geometry ("450x500")
root.title ("Restaurant Bill")

def Quantity():
    q = quantity.get()
    return q

def Menu_Item():
    m = menu_item.get()
    return m