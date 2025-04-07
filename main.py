import googletrans
from googletrans import Translator
from tkinter import *
from tkinter import ttk, messagebox
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import winsound
import os
import time


lang_dict = {
    'English': 'en',
    'Hindi': 'hi',
    'Tamil': 'ta',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Chinese (Simplified)': 'zh-cn',
    'Chinese (Traditional)': 'zh-tw',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Russian': 'ru',
    'Arabic': 'ar',
    'Bengali': 'bn',
    'Gujarati': 'gu',
    'Punjabi': 'pa',
    'Urdu': 'ur'
}

win = Tk()
win.geometry("1150x800")
win.title("🌍 AI Travel Translator")

Label(win, text="🌍 AI Travel Translator", font=("Arial", 24, "bold")).pack(pady=20)

text1 = Text(win, height=10, width=100, font=("Arial", 12))
text1.place(x=80, y=100)

text2 = Text(win, height=10, width=100, font=("Arial", 12))
text2.place(x=80, y=400)

def trans():
    button.set("Translating...")
    text2.delete(1.0, "end-1c")
    inp = text1.get(1.0, "end-1c")
    translator = Translator()

    try:
        src_lang = lang_dict[lang_1.get()]
        dest_lang = lang_dict[lang_2.get()]
        result = translator.translate(inp, src=src_lang, dest=dest_lang)
        text2.insert(END, result.text)
    except:
        messagebox.showwarning("Warning", "⚠️ Please check your internet connection or language selection.")
    finally:
        button.set("Translate")



def record_voice():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 400

    with sr.Microphone() as source:
        text1.delete(1.0, "end-1c")

        # Say the message aloud
        try:
            tts = gTTS("You can speak after the beep", lang='en')
            tts.save("speak_prompt.mp3")
            playsound("speak_prompt.mp3")
            os.remove("speak_prompt.mp3")
        except:
            pass

        recognizer.adjust_for_ambient_noise(source, duration=2)

        try:
            # Beep
            try:
                winsound.Beep(1000, 300)
            except ImportError:
                print("\a")

            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            text1.insert(END, text)

        except sr.WaitTimeoutError:
            messagebox.showerror("Error", "⏰ Listening timed out. Try again.")
        except sr.UnknownValueError:
            messagebox.showerror("Error", "❌ Could not understand your speech.")
        except sr.RequestError:
            messagebox.showerror("Error", "🌐 Could not connect to the recognition service.")




def speak_text():
    output_text = text2.get(1.0, "end-1c").strip()
    if not output_text:
        messagebox.showerror("Error", "🗣️ No translated text to speak.")
        return

    try:
        lang_code = lang_dict[lang_2.get()]
        tts = gTTS(text=output_text, lang=lang_code)
        tts.save("temp.mp3")
        playsound("temp.mp3")
        os.remove("temp.mp3")
    except Exception as e:
        messagebox.showerror("Error", f"🎧 Could not play audio: {e}")

lang_1 = StringVar()
lang_2 = StringVar()
button = StringVar()

ttk.Label(win, text="From Language", font=("Arial", 12)).place(x=80, y=65)
ttk.Label(win, text="To Language", font=("Arial", 12)).place(x=80, y=365)

combo = ttk.Combobox(win, height=10, width=25, state='readonly', textvariable=lang_1, font=("Arial", 11))
combo['value'] = tuple(lang_dict.keys())
combo.current(0)
combo.place(x=200, y=65)

combo_1 = ttk.Combobox(win, height=10, width=25, state='readonly', textvariable=lang_2, font=("Arial", 11))
combo_1['value'] = tuple(lang_dict.keys())
combo_1.current(1)
combo_1.place(x=200, y=365)

btn_translate = Button(win, height=2, width=20, textvariable=button, command=trans, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
button.set("Translate")
btn_translate.place(x=480, y=730)

btn_record = Button(win, height=2, width=20, text="🎤 Voice Input", command=record_voice, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
btn_record.place(x=220, y=730)

btn_speak = Button(win, height=2, width=20, text="🔊 Speak Output", command=speak_text, bg="#FF5722", fg="white", font=("Arial", 12, "bold"))
btn_speak.place(x=740, y=730)

win.mainloop()
