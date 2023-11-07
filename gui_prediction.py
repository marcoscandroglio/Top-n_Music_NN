# Names: Kyle Donovan, Philip Hopkins, Marco Scandroglio
# Course: CS 467 Fall 2023
# Project: Top-n Music Genre Classification Neural Network
# GitHub Repo: https://github.com/pdhopkins/CS467_music_NN
# Description: TKinter GUI for Genre Prediction

from tkinter import *
from tkinter import filedialog
from genre_prediction import predict_genre
from music_file_conversion import youtube_get_audio
import os


window = Tk()
window.title("Top-N Genre Classification by Donovan, Hopkins, Scandroglio")
new_width = window.winfo_screenwidth() // 2
new_height = window.winfo_screenheight() // 2
window.geometry(f'{new_width}x{new_height}')


def open_music_file():
    window.filename = filedialog.askopenfilename(filetypes=((".wav", "*.wav"), (".mp3","*.mp3")))
    result_list = predict_genre(window.filename, "model_data")
    results_label_1 = Label(window, text=f"{result_list[0][0]} : {result_list[0][1] * 100}%")
    results_label_2 = Label(window,
                            text=f"{result_list[1][0]} : {result_list[1][1] * 100}%")
    results_label_3 = Label(window,
                            text=f"{result_list[2][0]} : {result_list[2][1] * 100}%")
    results_label_1.pack()
    results_label_2.pack()
    results_label_3.pack()

def open_url():
    url_to_use = url_input.get()
    youtube_get_audio(url_to_use)
    result_list = predict_genre("temp_file_youtube.mp3", "model_data")
    os.remove("temp_file_youtube.mp3")
    results_label_1 = Label(window,
                            text=f"{result_list[0][0]} : {result_list[0][1] * 100}%")
    results_label_2 = Label(window,
                            text=f"{result_list[1][0]} : {result_list[1][1] * 100}%")
    results_label_3 = Label(window,
                            text=f"{result_list[2][0]} : {result_list[2][1] * 100}%")
    results_label_1.pack()
    results_label_2.pack()
    results_label_3.pack()


get_file_button = Button(window, text="Open Music File", command=open_music_file)
get_file_button.pack()
url_explain = Label(window, text="Or use a YouTube URL").pack()
url_input = Entry(window)
url_input.pack()
get_url_button = Button(window, text="Open YouTube URL", command=open_url).pack()



window.mainloop()