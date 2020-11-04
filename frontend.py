#-*-   coding:   utf-8   -*-
from tkinter import *
from tkinter import font
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END, title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

def display_man():
    mandrin = mandrin_text.get()
    list1.delete(0, END)
    list1.insert(END, mandrin)

def forward(nxt):
    global list1
    global button_forward
    global button_backward

    #list1 = Listbox(root, height = 6, width = 35, font = font.Font(size=9))
    list1.delete(0, END)
    mandrin = hanzi[nxt]
    list1.insert(END, mandrin)
    button_forward = Button(frame2, text = ">>", 
    command = lambda: forward(nxt + 1))
    if nxt == len(hanzi) - 1:
        button_forward = Button(frame2, text = ">>", state = DISABLED)
    button_forward.grid(row = 10, column = 1)

    status = Label(frame2, text =  str(nxt+1) + " out of " + str(len(hanzi)), 
    bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 11, column = 0, columnspan=5, sticky = W+E)

def backward(prvs):
    global list1
    global button_forward
    global button_backward

def nextpage(nxt):
    frames[nxt].grid(row = 0, column = 0)
    next_frame = Button(root, text = "--->", 
    command = lambda: nextpage(nxt + 1))
    next_frame.grid(row = 1, column = 0)

root = Tk()

root.wm_title("Flash Card")
root.iconbitmap('panda.ico')
frame1 = Frame(root)
frame2 = Frame(root)
#frame2.grid(row = 0, column = 0)
frames = [frame1, frame2]
hanzi = ["我", "愛", "你"]

holyword = Label(frame1, text ="We need light")
holyword.pack()

l1 = Label(frame2, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(frame2, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(frame2, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(frame2, text = "ISBN")
l4.grid(row = 1, column = 2)

label5 = Label(frame2, text = "读入")
label5.grid(row = 2, column = 0)

status = Label(frame2, text = "1 out of " + str(len(hanzi)), bd = 1, relief = SUNKEN, anchor = E)
status.grid(row = 11, column = 0, columnspan=5, sticky = W+E)

title_text=StringVar()
e1 = Entry(frame2, textvariable=title_text)
e1.grid(row = 0, column = 1)

author_text=StringVar()
e2 = Entry(frame2, textvariable=author_text)
e2.grid(row = 0, column = 3)

year_text=StringVar()
e3 = Entry(frame2, textvariable=year_text)
e3.grid(row = 1, column = 1)

isbn_text=StringVar()
e4 = Entry(frame2, textvariable=isbn_text)
e4.grid(row = 1, column = 3)

mandrin_text = StringVar()
e5 = Entry(frame2, textvariable = mandrin_text)
e5.grid(row = 2, column = 1)

list1 = Listbox(frame2, height = 6, width = 35, font = font.Font(size=15))
list1.grid(row = 3, column = 1, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(frame2)
sb1.grid(row = 3, column = 3, rowspan=6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

bView = Button(frame2, text="View all", width = 12, command = view_command)
bView.grid(row = 3, column = 0)

b2 = Button(frame2, text="Search entry", width = 12, command = search_command)
b2.grid(row = 4, column = 0)

b3 = Button(frame2, text="Add entry", width = 12, command = add_command)
b3.grid(row = 5, column = 0)

b4 = Button(frame2, text="Update", width = 12, command = update_command)
b4.grid(row = 6, column = 0)

b5 = Button(frame2, text="Delete Selected", width = 12, command = delete_command)
b5.grid(row = 7, column = 0)

b6 = Button(frame2, text="Close", width = 12, command = root.destroy)
b6.grid(row = 9, column = 0)

b7 = Button(frame2, text = "显示", width = 12, command = display_man)
b7.grid(row = 8, column = 0)

button_forward = Button(frame2, text = ">>", command = lambda: forward(0))
button_forward.grid(row = 10, column = 1)

button_backward = Button(frame2, text = "<<", command = lambda: backward(1))
button_backward.grid(row = 10, column = 0)

next_frame = Button(root, text = "--->", command = lambda: nextpage(0))
next_frame.grid(row = 1, column = 0)

root.mainloop()