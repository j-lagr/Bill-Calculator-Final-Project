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

quantity = IntVar()
menu_item= StringVar()
price= IntVar()
total_cost = StringVar()

label_quantity= Label(root, text= "Quantity:").place(x=25,y=25)
label_menu_item= Label(root, text= "Menu Item: ").place(x=25,y=75)
label_price= Label(root, text= "Price:").place(x=25,y=125)

entry_quantity= Entry(root, textvariable= quantity).place(x=150,y=25)
entry_menu_item= Entry(root, textvariable= menu_item).place(x=150,y=75)
entry_price= Entry(root, textvariable= price).place(x=150,y=125)

add_item_button= Button(root,text="Add Item",width=15,command=list_menu).place(x=300,y=25)
total_bill_button= Button(root,text="Total Bill",width=15,command=bill_total).place(x=300,y=75)

label_list_quantity= Label(root, text= "Quantity:").place(x=25,y=180)
listbox_quantity= Listbox(root,height=10,width=15)
listbox_quantity.place(x=25,y=200)

label_list_menu_item= Label(root, text= "Menu Item:").place(x=150,y=180)
listbox_menu_item= Listbox(root,height=10,width=20)
listbox_menu_item.place(x=150,y=200)

label_list_price= Label(root, text= "Price:").place(x=300,y=180)
listbox_menu_price= Listbox(root,height=10,width=18)
listbox_menu_price.place(x=300,y=200)

label_total_cost= Label(root, text= "Total cost:").place(x=200,y=380)
labeloutputnetvalue = Label(root, width=15, borderwidth=2, relief="sunken", textvariable=total_cost, anchor="center")
labeloutputnetvalue.place(x=300, y=380)

root.mainloop()