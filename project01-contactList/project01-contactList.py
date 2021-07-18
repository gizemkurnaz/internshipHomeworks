from _csv import reader
from tkinter import *
import csv

window = Tk()
window.geometry('500x500')
window.config(bg='#f4f1de')
window.resizable(0, 0)
window.title('Contact List')

with open('contactList.csv', 'r') as file:
    csv_reader = reader(file)
    contactList = list(csv_reader)

Name = StringVar()
Number = StringVar()

frame = Frame(window)
frame.place(x=140, y=250)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12, width=25, font='Arial')
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def selectedLine():
    return int(select.curselection()[0])


def addContact():
    contactList.append([Name.get(), Number.get()])
    selectSet()
    with open('contactList.csv', 'w', newline='') as file:
        write = csv.writer(file)
        write.writerows(contactList)
    file.close()


def editContact():
    contactList[selectedLine()] = [Name.get(), Number.get()]
    selectSet()
    with open('contactList.csv', 'w', newline='') as file:
        write = csv.writer(file)
        write.writerows(contactList)
    file.close()


def deleteContact():
    del contactList[selectedLine()]
    selectSet()
    with open('contactList.csv', 'w', newline='') as file:
        write = csv.writer(file)
        write.writerows(contactList)
    file.close()


def viewContact():
    NAME, PHONE = contactList[selectedLine()]
    Name.set(NAME)
    Number.set(PHONE)
    with open('contactList.csv', 'w', newline='') as file:
        write = csv.writer(file)
        write.writerows(contactList)
    file.close()


def callContact():
    NAME, PHONE = contactList[selectedLine()]
    callLabel.config(text=NAME + '  calling...', bg='#a2d2ff')


def exit():
    window.destroy()


def selectSet():
    contactList.sort()
    select.delete(0, END)
    for name, phone in contactList:
        select.insert(END, name)


selectSet()

Label(window, text='Name :', font='arial 12 bold').place(x=100, y=90)
Entry(window, textvariable=Name).place(x=250, y=90)
Label(window, text='Phone Number :', font='arial 12 bold').place(x=100, y=115)
Entry(window, textvariable=Number).place(x=250, y=115)

Label(window, text='Contact List', font='arial 16 bold').place(x=180, y=210)
callLabel = Label(window, text='', font='arial 14')
callLabel.place(x=180, y=150)

Button(window, text='ADD', font='arial 12 bold', bg='#6d6875', command=addContact).place(x=50, y=10)
Button(window, text='EDIT', font='arial 12 bold', bg='#6d6875', command=editContact).place(x=120, y=10)
Button(window, text='DELETE', font='arial 12 bold', bg='#6d6875', command=deleteContact).place(x=190, y=10)
Button(window, text='VIEW', font='arial 12 bold', bg='#6d6875', command=viewContact).place(x=280, y=10)
Button(window, text='CALL', font='arial 12 bold', bg='#6d6875', command=callContact).place(x=350, y=10)
Button(window, text='EXIT', font='arial 12 bold', bg='#9d0208', command=exit).place(x=410, y=450)

window.mainloop()
