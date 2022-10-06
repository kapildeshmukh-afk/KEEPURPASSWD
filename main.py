from tkinter import *
# MESSAGEBOX IS NOT LIBRARY WHICH IS FOUND IN TKINTER CLASS
from tkinter import messagebox

#
import pyperclip

#
import json

# PASSWORD GENERATION
from random import *
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
num_letters = randint(8, 10)
num_numbers = randint(2, 4)
num_symbols = randint(2, 4)
password_list = []
password_letter = [choice(letters) for _ in range(num_letters)]
password_numbers = [choice(letters) for _ in range(num_numbers)]
password_symbols = [choice(letters) for _ in range(num_symbols)]
            # for char in range(num_letters):
            #     password_list.append(random.choice(letters))
            # for no in range(num_numbers):
            #     password_list.append(random.choice(numbers))
            # for symb in range(num_symbols):
            #     password_list.append(random.choice(symbols))

password_list = password_letter + password_numbers + password_symbols
shuffle(password_list)
password = "".join(password_list)


#UI PART
window = Tk()
window.title("PASSWORD MANAGER")
window.minsize(height=450, width=450)
window.config(pady=50, padx=50)
canvas = Canvas(height=200, width=190)
imgLink = PhotoImage(file="lock.jpg")
lock_image = canvas.create_image(100, 95, image=imgLink)
canvas.grid(column=1, row=0)


site_label = Label(text="Website :")
site_label.grid(column=0, row=1)


id_label = Label(text="User ID :")
id_label.grid(column=0, row=2)


passwd_label = Label(text="PASSWORD :")
passwd_label.grid(column=0, row=3)

# SEARCH BUTTON
def search():
    search_website = site_entry.get().title()
    try:
        with open("./MyPasswd.json", "r") as seach_file:
            search_data = json.load(seach_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR!!", message="No Data File Found")
    else:
        if search_website in search_data:
            your_email = search_data[search_website]["email"]
            your_password = search_data[search_website]["password"]
            messagebox.askokcancel(title=search_website, message=f"Email: {your_email}\nPassword: {your_password}")
        else:
            messagebox.askretrycancel(title=search_website, message="DATA NOT FOUND")

site_entry = Entry(width=34)
site_entry.grid(row=1, column=1)
site_entry.focus()
search_button = Button(text="     Search  ", command=search)
search_button.grid(row=1, column=2)

id_entry = Entry(width=45,)
id_entry.grid(row=2, column=1, columnspan=2)
id_entry.insert(0, "abc@gmail.com")
passwd_entry = Entry(width=34)
passwd_entry.grid(row=3, column=1)


# INSERTING PASSWORD INTO PASSWORD ENTRY FIELD
def passwordInsert():
    global password
    passwd_entry.insert(0, password)
    pyperclip.copy(password)


generate_button = Button(text=" Generate ", command=passwordInsert)
generate_button.grid(row=3, column=2)


# CHECKING THE ENTRIES IN EACH ROW.
def save():
    website = site_entry.get().title()
    user_id = id_entry.get()
    user_password = passwd_entry.get()
    new_data = {
        website:{
            "email":user_id,
            "password":user_password,
        }
    }

    if len(website) == 0 or len(user_password) == 0 or len(user_id) == 0:
        messagebox.askretrycancel("Oops!!", "Fill all the entries before adding!")
    else:
        try:
            with open("./MyPasswd.json", "r") as data_file:
                # READING OLD DATA
                data = json.load(data_file)
        except FileNotFoundError:
            with open("./MyPasswd.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # UPDATING DATA
            data.update(new_data)
            with open("./MyPasswd.json", "w") as data_file:
                # SAVING UPDATED DATA
                json.dump(data, data_file, indent=4)
        finally:
            site_entry.delete(0, END)
            passwd_entry.delete(0, END)


add_button = Button(text="Add", width=38, command=save)
add_button.grid(row=4, column=1, columnspan=2)


# ENDS
window.mainloop()