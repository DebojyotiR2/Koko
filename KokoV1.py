import xml.etree.ElementTree as et
import os
from prettytable import PrettyTable


def print_name():
    print("")
    print("")
    print("")
    print("Welcome to KOKO")
    print("A password management platform")
    print("Created and developed by two amateurs.")
    print("")
    print("")
    print("                  _              _            _              _        ")
    print("                /\_\           /\ \         /\_\           /\ \       ")
    print("               / / /  _       /  \ \       / / /  _       /  \ \      ")
    print("              / / /  /\_\    / /\ \ \     / / /  /\_\    / /\ \ \     ")
    print("             / / /__/ / /   / / /\ \ \   / / /__/ / /   / / /\ \ \    ")
    print("            / /\_____/ /   / / /  \ \_\ / /\_____/ /   / / /  \ \_\   ")
    print("           / /\_______/   / / /   / / // /\_______/   / / /   / / /   ")
    print("          / / /\ \ \     / / /   / / // / /\ \ \     / / /   / / /    ")
    print("         / / /  \ \ \   / / /___/ / // / /  \ \ \   / / /___/ / /     ")
    print("        / / /    \ \ \ / / /____\/ // / /    \ \ \ / / /____\/ /      ")
    print("        \/_/      \_\_\\/_________/ \/_/      \_\_\\/_________/       ")
    print("")
    print("")
    print("")
    return


def login_form():
    print("Do you have an account on Koko ? (Y = Yes, N = No)")
    reply = input("Y/N : ").upper()
    if reply == "Y":
        validate_account()
    elif reply == "N":
        add_account()
    else:
        print("Enter either 'Y' or 'N'")
        return login_form()


def validate_account():
    print("Please enter your username:")
    user = str(input("USERNAME = "))
    print("Please enter your Password:")
    password = str(input("PASSWORD = "))

    for j in range(len(list(root))):
        if user == root[j][0].text:
            if password == root[j][1].text:
                print("Validation Successful")
                globals()['i'] = j
                prompt()
                break
            else:
                print("Invalid Password")
                login_form()
    else:
        print("Invalid Username")
        login_form()


def add_account():
    print("Please enter your new username:")
    user = str(input("USERNAME = "))
    print("Please enter your new Password:")
    password = str(input("PASSWORD = "))
    new_entry = et.SubElement(root, "USER")
    new_entry_user = et.SubElement(new_entry, "USERNAME")
    new_entry_pass = et.SubElement(new_entry, "PASSWORD")
    new_entry_user.text = user
    new_entry_pass.text = password
    tree.write(xml_file)
    print("")
    print("Account added successfully")
    print("Please Log in to your new account")
    login_form()


def prompt():
    print("")
    print("Welcome " + root[i][0].text)
    print("You can add, delete or modify your passwords here:")
    print("")
    print_passwords()
    print("")
    print("Please select the desired option and hit enter:")
    print("Press 1 to add a new password")
    print("Press 2 to modify an existing password")
    print("Press 3 to delete an existing password")
    print("Press 4 to exit")
    print("")
    option = str(input("OPTION: "))
    if option == "1":
        add_password_prompt()
    elif option == "2":
        modify_password_prompt()
    elif option == "3":
        delete_password_prompt()
    elif option == "4":
        quit()
    else:
        print("Please choose a correct option.")
        print("")
        return prompt()


def modify_password_prompt():
    print("")
    print("Please enter the 'SL. No/' of the entry you wish to modify:")
    input_user = int(input("OPTION: "))
    record = input_user + 1
    print("")
    print("Please enter a short description of your entry:")
    description = str(input("DESCRIPTION = "))
    print("Please enter the username to store:")
    username = str(input("USERNAME = "))
    print("Please enter the Password to store:")
    password = str(input("PASSWORD = "))
    entry = description + "🔠" + username + "🔠" + password
    root[i][record].text = entry
    print("Record Modified Successfully.")
    return prompt()


def delete_password_prompt():
    print("Please enter the 'SL. No/' of the entry you wish to remove:")
    input_user = int(input("OPTION: "))
    record = input_user + 1
    print(i)
    print(record)
    print(type(i))
    print(type(record))
    del root[i][record]
    tree.write(xml_file)
    print("Removed Successfully.")
    return prompt()


def add_password_prompt():
    print("")
    print("Please enter a short description of your entry:")
    description = str(input("DESCRIPTION = "))
    print("Please enter the username to store:")
    username = str(input("USERNAME = "))
    print("Please enter the Password to store:")
    password = str(input("PASSWORD = "))
    entry = description + "🔠" + username + "🔠" + password

    et.SubElement(root[i], 'STORED')
    ll = len(root[i]) - 1
    root[i][ll].text = str(entry)
    tree.write(xml_file)

    return prompt()


def print_passwords():
    print("")
    print("Your Current List of passwords will appear here.")
    print("")

    x = PrettyTable()
    x.field_names = ["SL. NO", "DESCRIPTION", "USERNAME", "PASSWORD"]
    for l in range(2, len(root[i])):
        num = str(l - 1) + "."
        raw_info = root[i][l].text
        info = raw_info.split('🔠')
        x.add_row([num, info[0], info[1], info[2]])
    print(x)
    return


def ini_xml():
    base_path = os.path.dirname(os.path.realpath(__file__))
    xml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "passwords.xml")
    if not os.path.exists(xml_file):
        file = open(xml_file, "w")
        file.write("<myUsers></myUsers>")
        file.close()
    return xml_file



xml_file = ini_xml()
tree = et.parse(xml_file)
root = tree.getroot()
print_name()
login_form()








