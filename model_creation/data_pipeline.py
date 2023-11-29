# Names: Kyle Donovan, Philip Hopkins, Marco Scandroglio
# Course: CS 467 Fall 2023
# Project: Top-n Music Genre Classification Neural Network
# GitHub Repo: https://github.com/pdhopkins/CS467_music_NN
# Description: Data pre-processing program for creating training and validation dataset

import os
import json
import numpy as np
import tensorflow as tf


def pre_process(data_directory: str) -> tuple[np.ndarray, np.ndarray]:
    """
    Concatenate .npy files into a NumPy array and build a list of training labels.

    Args:
        data_directory (str): Directory path containing .npy files.

    Returns:
        tuple[np.ndarray, np.ndarray]: NumPy arrays representing data and labels.

    Raises:
        FileNotFoundError: If 'data_directory' does not exist or is not accessible.

    Example:
        data, labels = pre_process("path/to/data/directory")
    """

    # validate function arguments
    # parse directory name and structure
    if not os.path.isdir(data_directory):
        raise FileNotFoundError(f'{data_directory} does not exist or is not accessible.')
    # data_directory = args[0]
    data = []
    labels = []
    dict_genre_labels = {}
    last_unused_label = 0
    file_count = 0

    # iterate over files in subfolders
    for root, sub_dirs, files in os.walk(data_directory):
        subfolder_name = os.path.basename(root)

        for file in files:
            if file.endswith(".npy"):
                mel_spectrogram = np.load(os.path.join(root, file))
                # build lists of matrices and labels
                data.append(mel_spectrogram)
                if subfolder_name not in dict_genre_labels:
                    dict_genre_labels[subfolder_name] = last_unused_label
                    last_unused_label += 1
                labels.append(dict_genre_labels[subfolder_name])
                file_count += 1
                print(f'Processed file: {file_count}', end='\r')

    with open("../genre_labels.json", "w") as output_file:
        json.dump(dict_genre_labels, output_file)

    print(f'{file_count} files were added to the dataset!')

    # convert to NumPy arrays
    data = np.array(data)
    data = data[:, :, :, np.newaxis]
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
    Convert NumPy arrays to a TensorFlow dataset.

    Args:
        data_np_arr (np.ndarray): NumPy array representing data.
        labels_np_arr (np.ndarray): NumPy array representing labels.

    Returns:
        tf.data.Dataset: TensorFlow dataset.

    Example:
        dataset = create_tensorflow_dataset(data, labels)
    """
    return tf.data.Dataset.from_tensor_slices((data_np_arr, labels_np_arr)).batch(1)


# demo script functions
def create_directories(dir_name: str, subfolder_names: list) -> None:
    """
    Create a new directory with subdirectories.

    Args:
        dir_name (str): Name of the main directory.
        subfolder_names (list): List of subdirectory names.

    Returns:
        None

    Example:
        create_directories("path/to/main/directory", ["subfolder1", "subfolder2"])
    """

    os.makedirs(dir_name)

    for subfolder in subfolder_names:
        os.makedirs(os.path.join(dir_name, subfolder))


def create_numpy_arrays(dir_name: str, subfolder_names: list, array_rows: int,
                        array_columns: int, num_files: int) -> None:
    """
    Create random matrices in subfolders.

    Args:
        dir_name (str): Name of the main directory.
        subfolder_names (list): List of subdirectory names.
        array_rows (int): Number of rows in the random matrices.
        array_columns (int): Number of columns in the random matrices.
        num_files (int): Number of random matrices to create in each subfolder.

    Returns:
        None

    Example:
        create_numpy_arrays("path/to/main/directory", ["subfolder1", "subfolder2"], 100, 100, 5)
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
    # WORKING_DIRECTORY = 'Demo_Database_Test'
    # os.makedirs(WORKING_DIRECTORY, exist_ok=True)
    # os.chdir(WORKING_DIRECTORY)
    #
    # # mock-database folders and subfolders
    # TEST_DATABASE_NAME = 'Demo_Database_Folder'
    # SUBFOLDER_NAMES = ['blues', 'classical', 'jazz']
    #
    # # mock-mel-spectrograms
    # ARRAY_ROWS = 4
    # ARRAY_COLUMNS = 6
    # NUM_FILES = 3  # .npy files per subdirectory
    #
    # create_directories(TEST_DATABASE_NAME, SUBFOLDER_NAMES)
    # create_numpy_arrays(TEST_DATABASE_NAME, SUBFOLDER_NAMES, ARRAY_ROWS, ARRAY_COLUMNS, NUM_FILES)
    # pre_process(TEST_DATABASE_NAME)

    print()
    tf_data, tf_labels = pre_process("genres_original")
    print()

    tf_dataset = create_tensorflow_dataset(tf_data, tf_labels)

    tf_dataset.save("dataset_file")

    print()
    print('typical tensor element shape:')
    print(tf_dataset.element_spec[0])
    print()

    # for element in tf_dataset:
    #     element_data, element_label = element
    #     print(element_label)
    #     print(element_data)
    #     print()

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
