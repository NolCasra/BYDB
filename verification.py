
from login import *
import discord

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'{client.user} est en ligne !')

def quitter():
    exit(0)

def erreur_token():
    window = tk.Tk()
    window.title("Erreur")
    window.iconphoto(False, tk.PhotoImage(file="logo.png"))

    SCREEN_WIDTH = 350
    SCREEN_HEIGHT = 250

    window.configure(bg="#313338")
    window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    label = tk.Label(window, text="Veuillez mettre un token valide", font=("Comic Sans MS", 16), fg="red", bg="#313338")
    label.place(relx=0.5, rely=0.4, anchor="center")

    button = tk.Button(window, text="Quitter", font=("Comic Sans MS", 16), command=quitter)
    button.place(relx=0.5, rely=0.7, anchor="center")

    window.mainloop()


if token == "":
    erreur_token()

try:
    client.run(token)
except discord.LoginFailure:
    erreur_token()

