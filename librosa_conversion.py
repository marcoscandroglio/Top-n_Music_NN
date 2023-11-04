# Names: Kyle Donovan, Philip Hopkins, Marco Scandroglio
# Course: CS 467 Fall 2023
# Project: Top-n Music Genre Classification Neural Network
# GitHub Repo: https://github.com/pdhopkins/CS467_music_NN
# Description: Librosa conversion of audio files into mel-spectrograms

import os
import librosa
import matplotlib.pyplot as plt
import numpy as np

# function to plot the spectrogram


def plot_spectrogram(y, sr, hop_length, y_axis="linear"):
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(y,
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
    song_length = librosa.get_duration(path=audio_file)
    start_time = 0
    if song_length > 65.0:
        start_time = song_length // 2

    y, sr = librosa.load(audio_file, offset=start_time, duration=30.0)

    frame_size = 2048
    hop_size = 512

    # extract Short-Time Fourier Transform
    # despite the single eltter variable names, this is how the documentation does it
    audio_spec = librosa.feature.melspectrogram(y=y, sr=sr,  n_fft=frame_size, hop_length=hop_size)

    audio_spec_db = librosa.power_to_db(audio_spec, ref=np.max)

    spectrogram_file = os.path.splitext(audio_file)[0] + '_mel_spectrogram.txt'
    np.save(spectrogram_file, audio_spec_db)

    # plot spectrograms
    # plot_spectrogram(audio_spec_db, sr, hop_size)
    # plt.title(f'Mel-Spectrogram for {os.path.basename(audio_file)} (30 seconds)')

# set the var audio_directory, x Directory containing some of my audio files on desktop
# SWITCH THIS


audio_directory = "genres_original"

# process all audio files in the folder
# edit to individual if individual file processing desired
for root, dirs, files in os.walk(audio_directory):
    for file in files:
        if file.lower().endswith(('.wav', '.mp3', '.au')):
            audio_file = os.path.join(root, file)
            process_audio_file(audio_file)

# show the spectrograms
# plt.show()
