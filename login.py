
import tkinter as tk
import discord

client = discord.Client(intents=discord.Intents.all())


def save_token():
    token = entry.get()
    with open("token.txt", "w") as file:
        file.write(token)

    try:
        client.run(token)
    except discord.LoginFailure:
        label = tk.Label(window, text="Token invalide, veuillez relancer le code", font=("Comic Sans MS", 16), fg="red", bg="#313338")
        label.place(relx=0.5, rely=0.7, anchor="center")


window = tk.Tk()
window.title("Login")

window.iconphoto(False, tk.PhotoImage(file="logo.png"))

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

window.configure(bg="#313338")
window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

label = tk.Label(window, text="Entrer votre token ici", font=("Comic Sans MS", 16), fg="white", bg="#313338")
label.place(relx=0.5, rely=0.4, anchor="center")

entry = tk.Entry(window, font=("Comic Sans MS", 16), width=36, bg="#383a40", fg="#FFFFFF")
entry.place(relx=0.5, rely=0.5, anchor="center")

button = tk.Button(window, text="Enregistrer", font=("Comic Sans MS", 16), command=save_token)
button.place(relx=0.5, rely=0.6, anchor="center")

window.mainloop()
