from tkinter import *
import backendDatabase

def get_selected_row(event):
    global selected_tuple
    index= list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backendDatabase.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backendDatabase.search(txtTitle.get(),txtAuthor.get(),txtYear.get(),txtISBN.get()):
        list1.insert(END,row)

def add_command():
    backendDatabase.insert(txtTitle.get(),txtAuthor.get(),txtYear.get(),txtISBN.get())
    list1.delete(0,END)
    list1.insert(END,(txtTitle.get(),txtAuthor.get(),txtYear.get(),txtISBN.get()))

def delete_command():
    backendDatabase.delete(selected_tuple[0])

def update_command():
    backendDatabase.update(selected_tuple[0],txtTitle.get(),txtAuthor.get(),txtYear.get(),txtISBN.get())

window = Tk()

window.wm_title("BookStore")

label1 = Label(window,text="Title")
label1.grid(row=0,column=0)

label2 = Label(window,text="Author")
label2.grid(row=0,column=2)


label3 = Label(window,text="Year")
label3.grid(row=1,column=0)


label4 = Label(window,text="ISBN")
label4.grid(row=1,column=2)

txtTitle= StringVar()
e1 = Entry(window,textvariable=txtTitle)
e1.grid(row=0, column=1)

txtAuthor= StringVar()
e2 = Entry(window,textvariable=txtAuthor)
e2.grid(row=0, column=3)

txtYear= StringVar()
e3 = Entry(window,textvariable=txtYear)
e3.grid(row=1, column=1)

txtISBN= StringVar()
e4 = Entry(window,textvariable=txtISBN)
e4.grid(row=1, column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width =12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width =12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width =12,command= add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width =12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width =12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width =12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
