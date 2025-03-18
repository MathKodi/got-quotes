from tkinter import *
from PIL import Image, ImageTk
import requests

def get_quote():
    response = requests.get(url="https://api.gameofthronesquotes.xyz/v1/random")
    response.raise_for_status()
    data = response.json()
    name = data["character"]["name"]
    sentence = data["sentence"]

    canvas.itemconfig(quote_text, text=sentence + " by " +name)


window = Tk()
window.title("Someone in GoT Says...")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=300, height=414)
background_img = PhotoImage(file="background.png")

canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="GOT Quote Goes HERE", width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

img = Image.open("got.png")
img = img.resize((150, 150))
got_img = ImageTk.PhotoImage(img)


got_btn = Button(window, image=got_img, highlightthickness=0, command=get_quote)
got_btn.image = got_img
got_btn.grid(row=1, column=0)

window.mainloop()
