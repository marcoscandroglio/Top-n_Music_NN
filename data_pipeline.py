# Names: Kyle Donovan, Philip Hopkins, Marco Scandroglio
# Course: CS 467 Fall 2023
# Project: Top-n Music Genre Classification Neural Network
# GitHub Repo: https://github.com/pdhopkins/CS467_music_NN
# Description: Data pre-processing program for creating training and validation dataset

import os
import numpy as np
import tensorflow as tf


def pre_process(data_directory: str) -> tuple:
    """
    Function that takes as an argument a directory path containing .npy files,
    concatenates the .npy files into a larger NumPy array while building
    a list of training labels, and saves both as .npy files in the current
    working directory.
    """

    # validate function arguments
    # parse directory name and structure
    if not os.path.isdir(data_directory):
        raise FileNotFoundError(f'{data_directory} does not exist or is not accessible.')
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
    data = data[random_indices]  # fancy indexing
    labels = labels[random_indices]  # fancy indexing

    # save NumPy arrays to current working directory
    # np.save('data.npy', data)
    # np.save('labels.npy', labels)

    return data, labels


def create_tensorflow_dataset(data_np_arr, labels_np_arr):
    """
    Function to convert .npy files to tensorflow dataset.
    Used for streaming application.
    """
    return tf.data.Dataset.from_tensor_slices((data_np_arr, labels_np_arr))


# TODO: Create function to save dataset file.

# demo script functions
def create_directories(dir_name: str, subfolder_names: list) -> None:
    """
    Function that creates a new directory with subdirectories.
    """

    os.makedirs(dir_name)

    for subfolder in subfolder_names:
        os.makedirs(os.path.join(dir_name, subfolder))


def create_numpy_arrays(dir_name: str, subfolder_names: list, array_rows: int,
                        array_columns: int, num_files: int) -> None:
    """
    Function that creates random matices in subfolders.
    """

    for subfolder in subfolder_names:
        subfolder_path = os.path.join(dir_name, subfolder)

        for i in range(num_files):

            random_matrix = np.random.rand(array_rows, array_columns)
            file_name = f'{subfolder}random_matrix_{i}.npy'
            np.save(os.path.join(subfolder_path, file_name), random_matrix)


if __name__ == "__main__":

    # beginning of demo script
    # Note: delete 'Demo_Database_Test' folder (if it exists) before running script
    # creates following folder structure that mimics database structure:
    # ~/current directory (where 'python3 data_pipeline.py' is run)
    #   > 'Demo_Database_Test' (becomes working directory during test script)
    #       > 'Demo_Database_Folder'
    #           > 'blues'
    #           > 'classical'
    #           > 'jazz'

    # create demo folder and make it the current working directory
    WORKING_DIRECTORY = 'Demo_Database_Test'
    os.makedirs(WORKING_DIRECTORY, exist_ok=True)
    os.chdir(WORKING_DIRECTORY)

    # mock-database folders and subfolders
    TEST_DATABASE_NAME = 'Demo_Database_Folder'
    SUBFOLDER_NAMES = ['blues', 'classical', 'jazz']

    # mock-mel-spectrograms
    ARRAY_ROWS = 4
    ARRAY_COLUMNS = 6
    NUM_FILES = 3  # .npy files per subdirectory

    create_directories(TEST_DATABASE_NAME, SUBFOLDER_NAMES)
    create_numpy_arrays(TEST_DATABASE_NAME, SUBFOLDER_NAMES, ARRAY_ROWS, ARRAY_COLUMNS, NUM_FILES)
    # pre_process(TEST_DATABASE_NAME)

    tf_data, tf_labels = pre_process(TEST_DATABASE_NAME)

    tf_dataset = create_tensorflow_dataset(tf_data, tf_labels)

    print()
    print('typical tensor element shape:')
    print(tf_dataset.element_spec[0])
    print()

    for element in tf_dataset:
        element_data, element_label = element
        print(element_label)
        print(element_data)
        print()

    # # load files created by pre_process() function
    # data = np.load('data.npy')
    # labels = np.load('labels.npy')

    # # display tensor shape
    # print()
    # print(f'tensor shape: {np.shape(data)}')
    # print()

    # # display contents of.npy files in terminal
    # for count, matrix in enumerate(data):
    #     print(f'{labels[count]} matrix:')
    #     print()
    #     print(matrix)
    #     print()

    # print('labels list:')
    # print()
    # print(labels)
