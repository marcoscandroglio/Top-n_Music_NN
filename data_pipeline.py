# Names: Kyle Donovan, Philip Hopkins, Marco Scandroglio
# Course: CS 467 Fall 2023
# Project: Top-n Music Genre Classification Neural Network
# GitHub Repo: https://github.com/pdhopkins/CS467_music_NN
# Description: Data pre-processing program for creating training and validation dataset


import numpy as np
import os

def pre_process(data_directory: str) -> None:
    """
    Function that takes as an argument a directory path containing .npy files,
    concatenates the .npy files into a larger NumPy array while building
    a list of training labels, and saves both as .npy files in the current 
    working directory.
    """

    # validate function arguments
    # parse directory name and structure
    if not os.path.isdir(data_directory):
        raise FileNotFoundError(f'The directory {data_directory} does not exist or is not accessible.')
    # data_directory = args[0]
    data = []
    labels = []

    # iterate over files in subfolders
    for root, sub_dirs, files in os.walk(data_directory):
        subfolder_name = os.path.basename(root)

        for file in files:
            if file.endswith(".npy"):
                mel_spectrogram = np.load(os.path.join(root, file))
                # build lists of matrices and labels
                data.append(mel_spectrogram)
                labels.append(subfolder_name)

    # convert to NumPy arrays
    data = np.array(data)
    labels = np.array(labels)

    # shuffle data
    random_indices = np.random.permutation(len(data))
    data = data[random_indices] # fancy indexing
    labels = labels[random_indices] # fancy indexing

    # save NumPy arrays to current working directory
    np.save('data.npy', data)
    np.save('labels.npy', labels)
