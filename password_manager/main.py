from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle




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







# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = user_name_entry.get()
    password = password_entry.get()
    if len(website)== 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message= "website and password cannot be empty enter some values")
    else:
        is_ok =messagebox.askokcancel(title="website", message=f"The password details are: \n website:{website}\n password:{password} \n mail:{email}")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
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

website_entry = Entry(width=50,)
website_entry.grid(column=1, row=1, columnspan=2)
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






window.mainloop()