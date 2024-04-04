import customtkinter as c
import tkinter
import tkinter.messagebox
c.set_appearance_mode('dark')
c.set_default_color_theme('dark-blue')

root = c.CTk()

root.geometry("500x350")

def login():
    print("Login")


frame = c.CTkFrame(root)
frame.pack(pady=20,padx=60, fill='both', expand=True)

label = c.CTkLabel(master=frame, text="Login system", font=("Roboto",24))
label.pack(pady=12, padx=10)

entry1 = c.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = c.CTkEntry(master=frame, placeholder_text="password", show="*")
entry2.pack(pady=12, padx=10)

button = c.CTkButton(master=frame, text="login", command=login)
button.pack(pady=12, padx=10)

check = c.CTkCheckBox(master=frame, text="remember me")
check.pack(pady=12, padx=10)

root.mainloop()

