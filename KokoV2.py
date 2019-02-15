from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import xml.etree.ElementTree as et



def login_click():
    login = Toplevel()
    login.title("Login")
    username_label = Label(login, text="USERNAME: ").grid(row=0, column=0, padx=10, pady=10)
    username_entry = Entry(login)
    username_entry.grid(row=0, column=1, padx=10, pady=10)
    username_entry.focus()
    password_label = Label(login, text="PASSWORD: ").grid(row=1, column=0, padx=10, pady=10)
    password_entry = Entry(login, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)
    submit_button = Button(login, text="Submit", command=lambda: login_submit(username_entry.get(),\
                                                                              password_entry.get(), login))
    submit_button.grid(row=3, column=0, padx=10, pady=10)
    cancel_button = Button(login, text="Cancel", command=login.destroy).grid(row=3, column=1, columnspan=2, padx=10, pady=10)
    login.bind('<Return>', (lambda event: login_submit(username_entry.get(),\
                                                                              password_entry.get(), login)))


def account_click():
    create = Toplevel()
    create.title("Create Account")
    username_label = Label(create, text="USERNAME: ").grid(row=0, column=0, padx=10, pady=10)
    username_entry = Entry(create)
    username_entry.grid(row=0, column=1, padx=10, pady=10)
    username_entry.focus()
    password_label = Label(create, text="PASSWORD: ").grid(row=1, column=0, padx=10, pady=10)
    password_entry = Entry(create, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)
    submit_button = Button(create, text="Submit", command=lambda: create_account_submit(username_entry.get(),\
                                                password_entry.get(), create)).grid(row=3, column=0, padx=10, pady=10)
    cancel_button = Button(create, text="Cancel", command=create.destroy).grid(row=3, column=1, columnspan=2, padx=10,
                                                                               pady=10)
    create.bind('<Return>', (lambda event: create_account_submit(username_entry.get(),\
                                                password_entry.get(), create)))



def about_menu():
    about = Toplevel()
    canvas = Canvas(about, height =100)
    about.title("About Koko")
    canvas.create_text(70, 50, fill="green", font="Times 50 italic bold", text="KoKoV2", anchor=W)
    canvas.grid(row=0, column=0)
    text = Text(about, wrap=WORD, width=50, height=5, bg=root["bg"], relief="raised", highlightbackground="grey",\
                highlightthickness=1)
    text.tag_configure("center", justify='center')
    text.insert(END, "This is a password management platform built by two amateur developers."
                     " We have tried our best to bring this program to you to manage your passwords as effectively"
                     " and efficiently as possible. Thank you for trying our software. We hope you like it.")
    text.config(state=DISABLED)
    text.tag_add("center", "1.0", "end")
    text.grid(row=2, column=0, sticky =N, padx=10, pady=10)


def help_menu():
    about = Toplevel()
    canvas = Canvas(about, height=100)
    about.title("About Koko")
    canvas.create_text(70, 50, fill="darkblue", font="Times 50 italic bold", text="KoKoV2", anchor=W)
    canvas.grid(row=0, column=0)
    text = Text(about, wrap=WORD, width=50, height=5, bg=root["bg"], relief="raised", highlightbackground="grey",\
                highlightthickness=1)
    text.tag_configure("center", justify='center')
    text.insert(END, "Welcome to Koko. First you will have to create a account and then sign in to it."
                     " Then you will be able to add, edit or delete password entry as desired. Your passwords"
                     " will remain safe and secure with us. Thank You for using our software.")
    text.tag_configure("center", justify='center')
    text.config(state=DISABLED)
    text.grid(row=2, column=0, sticky=N, padx=10, pady=10)

def reset_menu():
    answer = messagebox.askquestion("RESET", "Do you really want to reset? All your data will be removed.")
    if answer == "yes":
        os.remove("passwords.xml")
        file = open(xml_file, "w")
        file.write("<myUsers></myUsers>")
        file.close()
        messagebox.showinfo("Success", "Reset done Successfully")



def close_click():
    answer = messagebox.askquestion("Exit", "Do you really want to exit?")
    if answer == "yes":
        root.destroy()


def entry_click():
    add_entry = Toplevel()
    add_entry.title("Add Entry")
    description_label = Label(add_entry, text="DESCRIPTION: ", ).grid(row=0, column=0, padx=10, pady=10)
    description_entry = Entry(add_entry)
    description_entry.grid(row=0, column=1, padx=10, pady=10)
    description_entry.focus()
    username_label = Label(add_entry, text="USERNAME: ").grid(row=1, column=0, padx=10, pady=10)
    username_entry = Entry(add_entry)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    password_label = Label(add_entry, text="PASSWORD: ").grid(row=2, column=0, padx=10, pady=10)
    password_entry = Entry(add_entry, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    submit_button = Button(add_entry, text="Submit", command=lambda: add_entry_submit(description_entry.get(),\
                        username_entry.get(), password_entry.get(), add_entry)).grid(row=3, column=0, padx=10, pady=10)
    cancel_button = Button(add_entry, text="Cancel", command=add_entry.destroy).grid(row=3, column=1, columnspan=2,
                                                                                     padx=10, pady=10)
    add_entry.bind('<Return>', (lambda event: add_entry_submit(description_entry.get(),\
                        username_entry.get(), password_entry.get(), add_entry)))



def delete_click():
    if entered == 0:
        messagebox.showinfo("Error", "No Entry Added Currently to Delete")
    else:
        answer = messagebox.askquestion("Delete", "Do you really want to delete this record?")
        if answer == "yes":
            print(tree.focus())
            selected_item = tree.selection()[0]
            index = (tree.index(selected_item))
            index += 2
            del rootxml[i][index]
            treexml.write(xml_file)
            refresh()
            messagebox.showinfo("Success", "Record Deleted Successfully")



def edit_click():
    edit_entry = Toplevel()
    edit_entry.title("Edit Recorf")

    description_label = Label(edit_entry, text="NEW DESCRIPTION: ").grid(row=0, column=0, padx=10, pady=10)
    description_entry = Entry(edit_entry)
    description_entry.grid(row=0, column=1, padx=10, pady=10)
    description_entry.focus()
    username_label = Label(edit_entry, text="NEW USERNAME: ").grid(row=1, column=0, padx=10, pady=10)
    username_entry = Entry(edit_entry)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    password_label = Label(edit_entry, text="NEW PASSWORD: ").grid(row=2, column=0, padx=10, pady=10)
    password_entry = Entry(edit_entry, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    submit_button = Button(edit_entry, text="Submit", command=lambda: edit_entry_submit(description_entry.get(),\
                    username_entry.get(), password_entry.get(), edit_entry)).grid(row=3, column=0, padx=10, pady=10)
    cancel_button = Button(edit_entry, text="Cancel", command=edit_entry.destroy).grid(row=3, column=1, columnspan=2,
                                                                                      padx=10, pady=10)
    edit_entry.bind('<Return>', (lambda event: edit_entry_submit(description_entry.get(),\
                    username_entry.get(), password_entry.get(), edit_entry)))


def refresh():
    tree.delete(*tree.get_children())
    if len(rootxml[i]) > 2:
        for l in range(2, len(rootxml[i])):
            num = str(int(l - 1))
            raw_info = rootxml[i][l].text
            info = raw_info.split('🔠')
            tree.insert('', 'end', text=num + ".", values=(info[0], info[1], info[2]))
            child_id = tree.get_children()[0]
            tree.focus(child_id)
            tree.selection_set(child_id)
            globals()['entered'] = 1
    else:
        tree.insert('', 'end', text="Please Add New Entries", values=("", "", ""))
        globals()['entered'] = 0



def login_submit(username, password, login, event=None):
    for j in range(len(rootxml)):
        if username == rootxml[j][0].text:
            print(rootxml[j][1].text)
            if password == rootxml[j][1].text:
                messagebox.showinfo("Success", "Validation Successful")
                labeltext.set("USER: " + username.upper())
                globals()['i'] = j
                login.destroy()
                refresh()
                newEntryButton.config(state="normal")
                deleteEntryButton.config(state="normal")
                editEntryButton.config(state="normal")
                break
            else:
                messagebox.showerror("Error", "Invalid Password")
                login.destroy()
                break
    else:
        messagebox.showerror("Error", "Invalid Username")
        login.destroy()


def create_account_submit(username, password, create, event=None):
    for j in range(len(rootxml)):
        if username == rootxml[j][0].text:
            messagebox.showinfo("Error", "Username Exists, Try another one.")
            create.destroy()
            break
    else:
        new_entry = et.SubElement(rootxml, "USER")
        new_entry_user = et.SubElement(new_entry, "USERNAME")
        new_entry_pass = et.SubElement(new_entry, "PASSWORD")
        new_entry_user.text = username
        new_entry_pass.text = password
        treexml.write(xml_file)
        messagebox.showinfo("Success", "Account Added Successfully")
        create.destroy()


def add_entry_submit(description, username, password, add_entry, event=None):
    entry = description + "🔠" + username + "🔠" + password
    et.SubElement(rootxml[i], 'STORED')
    ll = len(rootxml[i]) - 1
    rootxml[i][ll].text = str(entry)
    treexml.write(xml_file)
    messagebox.showinfo("Success", "Entry Added Successfully")
    refresh()
    add_entry.destroy()


def edit_entry_submit(description, username, password, edit_entry, event=None):
    selected_item = tree.selection()[0]
    index = (tree.index(selected_item))
    index += 2
    entry = description + "🔠" + username + "🔠" + password
    rootxml[i][index].text = entry
    refresh()
    messagebox.showinfo("Success", "Entry Edited Successfully")
    edit_entry.destroy()




xml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "passwords.xml")
if not os.path.exists(xml_file):
    file = open(xml_file, "w")
    file.write("<myUsers></myUsers>")
    file.close()
treexml = et.parse(xml_file)
rootxml = treexml.getroot()


root = Tk()
root.title("KOKOv2")
root.geometry("1000x350")
root.resizable(False, False)
menu = Menu(root)
menu.add_command(label="About", command=about_menu)
menu.add_command(label="Help", command=help_menu)
menu.add_command(label="RESET", command=reset_menu)
root.config(menu=menu)
titleFrame = Frame(root).grid(row=0, column=1)
label = Label(titleFrame, text="Welcome to KokoV2", relief="groove", font=(None, 15))
label.grid(row=0, column=2, pady=(10, 10))
labeltext = StringVar()
labeltext.set("NOT LOGGED IN")
label = Label(titleFrame, textvariable=labeltext, font='Helvetica 10 bold').grid(row=0, column=5, padx=0, pady=20)
displayFrame = Frame(root).grid(row=1, column=1,  sticky='nw')
tree = Treeview(root, columns=('Description', 'Username', 'Password'))
tree.heading('#0', text='SL. NO.')
tree.heading('#1', text='Description')
tree.heading('#2', text='Username')
tree.heading('#3', text='Password')
tree.column('#3', stretch=YES)
tree.column('#1', stretch=YES)
tree.column('#2', stretch=YES)
tree.column('#0', stretch=YES)
tree.grid(row=1, column=1, columnspan=3, rowspan=3, padx=(15,0))
tree.insert('', 'end', text="Please Log In.", values=("", "", ""))
vsb = Scrollbar(displayFrame, orient="vertical", command=tree.yview)
vsb.grid(row=1, column=4, sticky='w'+'n'+'s', rowspan=3)
loginFrame = Frame(root).grid()
loginButton = Button(loginFrame, text="Login", command=login_click).grid(row=4, column=1, padx=(5,0))
CreateAccountButton = Button(loginFrame, text="Create Account",  command=account_click).grid(row=4, column=2)
CloseButton = Button(loginFrame, text="Close", command=close_click).grid(row=4, column=3, padx=10, pady=10)
buttonFrame = Frame(root).grid()
newEntryButton = Button(loginFrame, text="New Entry", command=entry_click, state=DISABLED)
newEntryButton.grid(row=1, column=5,padx=(30,10))
deleteEntryButton = Button(loginFrame, text="Delete Entry", command=delete_click, state=DISABLED)
deleteEntryButton.grid(row=2, column=5, padx=(30, 10))
editEntryButton = Button(loginFrame, text="Edit Entry", command=edit_click, state=DISABLED)
editEntryButton.grid(row=3, column=5, padx=(30, 10))
root.mainloop()
