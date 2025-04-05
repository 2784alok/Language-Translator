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

