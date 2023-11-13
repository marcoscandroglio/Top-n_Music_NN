# Names: Kyle Donovan, Philip Hopkins, Marco Scandroglio
# Course: CS 467 Fall 2023
# Project: Top-n Music Genre Classification Neural Network
# GitHub Repo: https://github.com/pdhopkins/CS467_music_NN
# Description: Genre prediction program for the Genre NN

# imports
import os
import json
import numpy as np
# import tensorflow as tf
import keras
# from keras import layers
import librosa
# import librosa_conversion as libc


def save_json_genre_labels():
    data_directory = "genres_original"
    if not os.path.isdir(data_directory):
        raise FileNotFoundError(f'{data_directory} does not exist or is not accessible.')
    dict_genre_labels = {}
    last_unused_label = 0

    # iterate over files in subfolders
    for root, sub_dirs, files in os.walk(data_directory):
        subfolder_name = os.path.basename(root)

        for file in files:
            if file.endswith(".npy"):
                # build lists of matrices and labels
                if subfolder_name not in dict_genre_labels:
                    dict_genre_labels[subfolder_name] = last_unused_label
                    last_unused_label += 1

    with open("genre_labels.json", "w") as output_file:
        json.dump(dict_genre_labels, output_file)


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

    audio_spec_db = audio_spec_db[:, :, np.newaxis]
    audio_spec_db = np.expand_dims(audio_spec_db, axis=0)
    return audio_spec_db

# AUDIO_FILE_TO_PREDICT = "aerosmith_rag_doll.mp3"
# AUDIO_FILE_TO_PREDICT = "archspire_drone_corpse_aviator.mp3"
# AUDIO_FILE_TO_PREDICT = "disturbed_ten_thousand_fists.mp3"
# AUDIO_FILE_TO_PREDICT = "queen_another_one_bites.mp3"


def predict_genre(audio_file_dir: str, model_name: str, return_list=False) -> list:
    """
    Function that takes as an argument a path to an audio file
    and prints a list of genre predictions.
    """
    audio_file_array = process_audio_file(audio_file_dir)
    trained_model = keras.models.load_model(model_name + '.keras')
    results = trained_model(audio_file_array)
    results = results.numpy()
    results = results.flatten()
    results = results.tolist()

    with open("genre_labels.json") as input_file:
        loaded_json_genres = json.load(input_file)

    results_dictionary = {}
    for each_key in loaded_json_genres.keys():
        results_dictionary[each_key] = results[loaded_json_genres[each_key]]

    results_list = results_dictionary.items()
    sorted_results = sorted(results_list, key=lambda genre: genre[1], reverse=True)
    if return_list:
        return [x[1] * 100 for x in results_list]  # list of percentages only
    return sorted_results


if __name__ == "__main__":
    audio_paths = [
        "./sample_songs/aerosmith_rag_doll.mp3",
        "./sample_songs/archspire_drone_corpse_aviator.mp3",
        "./sample_songs/disturbed_ten_thousand_fists.mp3",
        "./sample_songs/queen_another_one_bites.mp3",
        "./sample_songs/nirvana_smells_like_teen.wav",
        "./sample_songs/slipknot_devil_in.wav"
    ]
    for each_path in audio_paths:
        predict_results = predict_genre(each_path, "model_data_val1_posscale_threeconvlayer_20epoch")
        print(each_path)
        for each_tuple in predict_results:
            # print(audio_file_dir)
            if each_tuple[1] * 100 > 1:
                print(f"{each_tuple[0]} : {(each_tuple[1] * 100):.4f} %")
