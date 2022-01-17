from functools import partial
from tkinter import *
import random
import pandas
import pyperclip
import pyttsx3


data = pandas.read_csv("./translated_words.csv")
formatted_data = data.to_dict(orient="records")

current_word_dict = {}

window = Tk()
window.title("Learn")
window.config(padx=50, pady=50, bg="#F0ECE3")


def generate_word():
    global current_word_dict
    current_word = random.choice(formatted_data)
    current_word_dict = current_word
    print(current_word)
    # print(current_word["DE"])


generate_word()


def copy_word(lang):
    pyperclip.copy(current_word_dict[lang])

    if lang == "DE":
        voice_id = int(voice_DE.get())
    if lang == "EN":
        voice_id = int(voice_EN.get())
    if lang == "RO":
        voice_id = int(voice_RO.get())

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    # for voice in voices:
    #     print("Voice: %s" % voice.name)
    #     print(" - ID: %s" % voice.id)
    #     print(" - Languages: %s" % voice.languages)
    #     print("\n")

    engine.setProperty("voice", voices[voice_id].id)
    engine.setProperty('rate', 140)
    engine.say(current_word_dict[lang])
    engine.runAndWait()


label_DE = Label(text="DE")
label_DE.grid(row=1, column=0)

label_RO = Label(text="RO")
label_RO.grid(row=1, column=1)

label_EN = Label(text="EN")
label_EN.grid(row=1, column=2)

# Voices
voice_DE = Entry(width=2)
voice_DE.insert(END, 2)
voice_DE.grid(row=0, column=0)

voice_RO = Entry(width=2)
voice_RO.insert(END, 0)
voice_RO.grid(row=0, column=1)

voice_EN = Entry(width=2)
voice_EN.insert(END, 3)
voice_EN.grid(row=0, column=2)
#

white_space = Label()
white_space.config(pady=20)
white_space.grid(row=2, column=1)

word_DE = Button(text=current_word_dict["DE"], command=partial(
    copy_word, "DE"))
word_DE.grid(row=3, column=0)
test_DE = Label(text=current_word_dict["DE"])

word_RO = Button(text=current_word_dict["RO"], command=partial(
    copy_word, "RO"))
word_RO.grid(row=3, column=1)

word_EN = Button(text=current_word_dict["EN"], command=partial(
    copy_word, "EN"))
word_EN.grid(row=3, column=2)


def next_word():
    global current_word_dict
    current_word_dict = {}
    generate_word()
    word_DE.config(text=current_word_dict["DE"])
    word_RO.config(text=current_word_dict["RO"])
    word_EN.config(text=current_word_dict["EN"])


next_word_button = Button(text="Next word", command=next_word)
next_word_button.grid(row=2, column=1)


window.mainloop()
