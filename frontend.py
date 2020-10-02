from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]  # to get first value from tuple list1.curselection() we use [0]
    selected_tuple = list1.get(index)  # get full LIST id, title, author, year, isbn
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[3])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[2])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])
    # print(selected_tuple)


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def view_command():
    list1.delete(0, END)  # to clean the listbox
    for row in backend.view():
        list1.insert(END, row)  # new rows are inserted in the end of previous row


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)  # to clean the listbox
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


win = Tk()
win.title("My BookStore")
l1 = Label(win, text="Title")
l1.grid(row=0, column=0)

l2 = Label(win, text="Year")
l2.grid(row=1, column=0)

l3 = Label(win, text="Author")
l3.grid(row=0, column=2)

l4 = Label(win, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(win, textvariable=title_text)
e1.grid(row=0, column=1)

year_text = StringVar()
e2 = Entry(win, textvariable=year_text)
e2.grid(row=1, column=1)

author_text = StringVar()
e3 = Entry(win, textvariable=author_text)
e3.grid(row=0, column=3)

isbn_text = StringVar()
e4 = Entry(win, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(win, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(win)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row)  # "bind" method binds <<ListboxSelect>> and function get_selected_row

b1 = Button(win, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(win, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(win, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(win, text="Update entry", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(win, text="Delete entry", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(win, text="Close window", width=12, command=win.destroy)
b6.grid(row=7, column=3)

win.mainloop()
