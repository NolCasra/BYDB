
import tkinter as tk

token = ""

def save_token():
    global token
    with open("token.txt", "w") as file:
        token = entry.get()
        file.write(entry.get())
        window.destroy()


window = tk.Tk()
window.title("Login")
window.iconphoto(False, tk.PhotoImage(file="logo.png"))

SCREEN_WIDTH = 1050
SCREEN_HEIGHT = 600


window.configure(bg="#313338")
window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

label = tk.Label(window, text="Entrer votre token ici", font=("Comic Sans MS", 35), fg="white", bg="#313338")
label.place(relx=0.5, rely=0.4, anchor="center")

entry = tk.Entry(window, font=("Comic Sans MS", 16), width=75, bg="#383a40", fg="#FFFFFF")
entry.place(relx=0.5, rely=0.5, anchor="center")

button = tk.Button(window, text="Se connecter", font=("Comic Sans MS", 16), command=save_token)
button.place(relx=0.5, rely=0.6, anchor="center")


window.mainloop()
