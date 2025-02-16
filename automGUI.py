import time
import pyautogui as pa
import requests
import random
from pynput import keyboard
from tkinter import *

stop_typing = False

def get_random_words():
    number_of_words = random.randint(1, 3)
    url = f"https://random-word-api.vercel.app/api?words={number_of_words}"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            words = response.json()
            return words
        except requests.exceptions.JSONDecodeError:
            print("Error: Unable to parse JSON response")
            return []
    else:
        print(f"Error: Received status code {response.status_code}")
        return []

def write_text_letter_by_letter(text):
    for letter in text:
        pa.write(letter)
        time.sleep(random.uniform(0.01, 0.03))

def on_press(key):
    global stop_typing
    if key == keyboard.Key.esc:
        stop_typing = True
        return False

def start_search():
    global stop_typing
    stop_typing = False
    num_searches = int(entry.get())
    
    pa.PAUSE = 0.25
    pa.press('win')
    time.sleep(0.25)
    pa.write('pesquisador bing')
    time.sleep(0.5)
    pa.press('enter')
    time.sleep(4)

    for i in range(1, num_searches + 1):
        if stop_typing:
            break

        status_label.config(text=f"Pesquisa {i} de {num_searches} ({i}/{num_searches})")
        window.update_idletasks()

        words = get_random_words()
        print(words)

        # Concatenate the words into a single sentence
        sentence = ' '.join(words)
        print(sentence)

        # Write the concatenated sentence letter by letter
        pa.click(-1397, 122)
        pa.hotkey('ctrl', 'a')
        pa.press('delete')
        write_text_letter_by_letter(sentence)
        pa.press('enter')

        # Delay between 5-8 seconds
        time.sleep(random.uniform(5, 8))

    status_label.config(text="Pesquisas completas", fg="green", bg="white")
    window.update_idletasks()

# Start the keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Tkinter interface
window = Tk()
window.geometry("500x400")
window.title("Bing Auto Search Script")

label = Label(window, text="Enter the number of searches:")
label.pack(pady=10)

entry = Entry(window)
entry.pack(pady=10)
entry.insert(0, "30")  # Default value

button = Button(window, text="Start Search", command=start_search)
button.pack(pady=20)

# Label to display the current status of searches
status_label = Label(window, text="", fg="blue", font=("Helvetica", 16))
status_label.pack(pady=10)

window.mainloop()