from tkinter import *
from tkinter import messagebox
import backend
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()
        # print(index[0]+1)
        selected_tuple=list1.get(index)
        #selected_tuple=b
        st_id=selected_tuple.split("-")[0]
        # print(type(selected_tuple[0]))
        # print("selected_tuple:",selected_tuple)
        # print(st_id)

        selected_st=backend.search_row(st_id)
        # print("select_st:",selected_st)
        e1.delete(0,END)
        e1.insert(END,selected_st[0][1])
        e2.delete(0,END)
        e2.insert(END,selected_st[0][2])
        e3.delete(0,END)
        e3.insert(END,selected_st[0][3])
        e4.delete(0,END)
        e4.insert(END,selected_st[0][4])
        e5.delete(0,END)
        e5.insert(END,selected_st[0][5])
        e6.delete(0,END)
        e6.insert(END,selected_st[0][6])
    except IndexError:
        pass



def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,str(row[0])+"-"+row[1])
def add_command():
    backend.insert(name_text.get(),phone_text.get(),doa_text.get(),fees_text.get(),lastpay_text.get(),paydate_text.get())
    messagebox.showinfo('Info','your data is save success fully',parent=window)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    view_command()
def update_command():
    backend.update(selected_tuple[0],name_text.get(),phone_text.get(),doa_text.get(),fees_text.get(),lastpay_text.get(),paydate_text.get())
    messagebox.showinfo('Info','your data is Update success fully',parent=window)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    view_command()

def search_command():
    list1.delete(0,END)
    search=backend.search(name_text.get(),phone_text.get(),doa_text.get(),fees_text.get(),lastpay_text.get(),paydate_text.get())
    for st in search:
        list1.insert(END,str(st[0])+"-"+st[1])
        print(st)

    # e1.delete(0,END)
    # e1.insert(END,search[0][1])
    # e2.delete(0,END)
    # e2.insert(END,search[0][2])
    # e3.delete(0,END)
    # e3.insert(END,search[0][3])
    # e4.delete(0,END)
    # e4.insert(END,search[0][4])
    # e5.delete(0,END)
    # e5.insert(END,search[0][5])
    # e6.delete(0,END)
    # e6.insert(END,search[0][6])
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)

def delete_command():
    # print(selected_tuple[0])
    if messagebox.askyesno('delete', "Are you sure", icon='warning',parent=window) == True:
        backend.delete(selected_tuple[0])
        messagebox.showinfo('Info','your data is Remove success fully',parent=window)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        view_command()


backend.connect()
window=Tk()
window.title("Student_manemgement")
window.geometry("800x600+400+50")

l1=Label(window,text="Name")
l1.grid(row=0,column=0,padx=10,pady=10)
l1.configure(font=('Times',12,'bold'))

l1=Label(window,text="Gurdian's phone no:")
l1.grid(row=0,column=2,padx=10,pady=10)
l1.configure(font=('Times',12,'bold'))

l1=Label(window,text="Date of addmission:")
l1.grid(row=1,column=0,padx=10,pady=10)
l1.configure(font=('Times',12,'bold'))

l1=Label(window,text="Fees:")
l1.grid(row=1,column=2,padx=10,pady=10)
l1.configure(font=('Times',12,'bold'))

l1=Label(window,text="Last Payment:")
l1.grid(row=2,column=0,padx=10,pady=10)
l1.configure(font=('Times',12,'bold'))

l1=Label(window,text="Payment date:")
l1.grid(row=2,column=2,padx=10,pady=10)
l1.configure(font=('Times',12,'bold'))

name_text=StringVar()
e1=Entry(window,textvariable=name_text,font=("Times",13),relief='sunken',bd=2)
e1.grid(row=0,column=1,pady=10)

phone_text=StringVar()
e2=Entry(window,textvariable=phone_text,font=("Times",13),relief='sunken',bd=2)
e2.grid(row=0,column=3,pady=10)

doa_text=StringVar()
e3=Entry(window,textvariable=doa_text,font=("Times",13),relief='sunken',bd=2)
e3.grid(row=1,column=1,pady=10)

fees_text=StringVar()
e4=Entry(window,textvariable=fees_text,font=("Times",13),relief='sunken',bd=2)
e4.grid(row=1,column=3,pady=10)

lastpay_text=StringVar()
e5=Entry(window,textvariable=lastpay_text,font=("Times",13),relief='sunken',bd=2)
e5.grid(row=2,column=1,pady=10)

paydate_text=StringVar()
e6=Entry(window,textvariable=paydate_text,font=("Times",13),relief='sunken',bd=2)
e6.grid(row=2,column=3,pady=10)


list1=Listbox(window,height=25,width=37,font=('Times',12,'bold'))
list1.grid(row=3,column=0,rowspan=25,columnspan=2)

scroll=Scrollbar(window,orient=VERTICAL,command=list1.yview)
scroll.grid(row=5,column=1,columnspan=2,rowspan=18,sticky=N+S)
list1.bind('<<ListboxSelect>>',get_selected_row)


b7=Button(window,text="Clear",font=('Times',12,'bold'),width=20,command=clear)
b7.configure(bd=4,relief='raised')
b7.grid(row=5,column=3)

b1=Button(window,text="View All",font=('Times',12,'bold'),width=20,command=view_command)
b1.configure(bd=4,relief='raised')
b1.grid(row=7,column=3)

b2=Button(window,text="Search",font=('Times',12,'bold'),width=20,command=search_command)
b2.configure(bd=4,relief='raised')
b2.grid(row=9,column=3)

b3=Button(window,text="Add Student",font=('Times',12,'bold'),width=20,command=add_command)
b3.configure(bd=4,relief='raised')
b3.grid(row=11,column=3)

b4=Button(window,text="Update Student",font=('Times',12,'bold'),width=20,command=update_command)
b4.configure(bd=4,relief='raised')
b4.grid(row=13,column=3)

b5=Button(window,text="Delete Student",font=('Times',12,'bold'),width=20,command=delete_command)
b5.configure(bd=4,relief='raised')
b5.grid(row=15,column=3)

b6=Button(window,text="Close",font=('Times',12,'bold'),width=20,command=window.quit)
b6.configure(bd=4,relief='raised')
b6.grid(row=17,column=3)
window.resizable(0,0)


mainloop()
