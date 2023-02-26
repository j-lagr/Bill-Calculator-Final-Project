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

def Price():
    p = price.get()
    return p

def list_menu():
    Quantity()
    Menu_Item()
    Price()
    for n in range(1):
        n=0
        listbox_quantity.insert(n,Quantity())
        listbox_menu_item.insert(n,Menu_Item())
        listbox_menu_price.insert(n,Price())

def bill_total():
    quan = []
    total = []
    for item in listbox_quantity.get(0, "end"):
        quan.append(item)
    print(quan)
    for item in listbox_menu_price.get(0, "end"):
        total.append(item)
    print(total)
    products=[]
    for quan,total in zip(quan,total):
        products.append(quan*total)
    total_bill= sum(products)
    print(total_bill)
    total_cost.set("${:,.2f}".format(float(total_bill)))
    return total_cost