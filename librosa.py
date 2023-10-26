# Names: Kyle Donovan, Philip Hopkins, Marco Scandroglio
# Course: CS 467 Fall 2023
# Project: Top-n Music Genre Classification Neural Network
# GitHub Repo: https://github.com/pdhopkins/CS467_music_NN
# Description: Model definition and training program for the Genre NN

import os
import librosa
import matplotlib.pyplot as plt
import numpy as np

# function to plot the spectrogram
def plot_spectrogram(Y, sr, hop_length, y_axis="linear"):
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(Y,
                             sr=sr,
                             hop_length=hop_length,
                             x_axis="time",
                             y_axis=y_axis)
    plt.colorbar(format="%+2.f")

# function to process audio/generate spectrograms
def process_audio_file(audio_file):
    # load audio file with Librosa, limiting the duration to first 30 seconds
    # if we want a selection which is 30 seconds from the middle and not the beginning,
    # then I will have to read more documentation
    y, sr = librosa.load(audio_file, duration=30.0)

    FRAME_SIZE = 2048
    HOP_SIZE = 512

    # extract Short-Time Fourier Transform
    # despite the single eltter variable names, this is how the documentation does it
    S = librosa.feature.melspectrogram(y=y, sr=sr,  n_fft=FRAME_SIZE, hop_length=HOP_SIZE)

    S_db = librosa.power_to_db(S, ref=np.max)

    spectrogram_file = os.path.splitext(audio_file)[0] + '_mel_spectrogram.txt'
    np.savetxt(spectrogram_file, S_db, fmt='%.2f', delimiter=',', comments='# ')


    # plot spectrograms
    plot_spectrogram(S_db, sr, HOP_SIZE)
    plt.title(f'Mel-Spectrogram for {os.path.basename(audio_file)} (30 seconds)')

# set the var audio_directory, x Directory containing some of my audio files on desktop
# SWITCH THIS
audio_directory = "/Users/kyledonovan/Desktop/musicForLibrosa"

# process all audio files in the folder
# edit to individual if individual file processing desired
for root, dirs, files in os.walk(audio_directory):
    for file in files:
        if file.lower().endswith(('.wav', '.mp3', '.au')):
            audio_file = os.path.join(root, file)
            process_audio_file(audio_file)

# show the spectrograms
plt.show()

