import json
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import json




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def add_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)

# --------------------------------------------------------------------------------
#show password

def show_password():
    search = website_entry.get()
    try:
        with open("data.json","r") as file:
            readed_file = json.load(file)
    except:
        messagebox.showinfo(title="check the input",message="No data file found")
    else:
        try:
            email = readed_file[search]["email"]
            password = readed_file[search]["password"]
        except:
            messagebox.showinfo(message = "enter the correct website name")
        else:
            messagebox.showinfo(title="Details",message=f"email : {email} \n password : {password}")







# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = user_name_entry.get()
    password = password_entry.get()
    new_data = {
        website: {"email": email,
                 "password": password}
    }
    if len(website)== 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message= "website and password cannot be empty enter some values")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)


        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MY password manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
my_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=32,)
website_entry.grid(column=1, row=1)
website_entry.focus()

user_name_entry = Entry(width=50)
user_name_entry.grid(column=1, row=2, columnspan=2)
user_name_entry.insert(0, "somu@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password",command=add_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text = "Search",command = show_password)
search_button.grid(column = 2,row =1)






window.mainloop()