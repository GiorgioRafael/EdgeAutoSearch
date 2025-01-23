import time
import pyautogui as pa
import pyperclip
import requests
import random
from pynput import keyboard

stop_typing = False

def get_random_words():
    number_of_words = random.randint(1, 4)
    url = f"https://random-word-api.herokuapp.com/word?number={number_of_words}"
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
        return False  # Stop the listener

# Start the keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

pa.PAUSE = 0.25
pa.press('win')
pa.write('pesquisador bing')
pa.press('enter')
time.sleep(1)

for i in range(1, 31):
    if stop_typing:
        break

    print(f"Pesquisa {i} de 30 ({i}/30)")

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

# Wait for the listener to stop
listener.join()