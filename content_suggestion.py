import os
import ast
import csv
import numpy as np
import pandas as pd
import genre_prediction as gp


def build_recommender_db(audio_dir: str, model_name: str, file_name: str) -> None:
    """
    Function that takes as an argument a string that represents a directory containing audio files.
    This function iterates through the audio files to build a database/csv file containing
    audio titles and the genre predictions created by the trained model and saves it.
    """
    if not os.path.exists(audio_dir):
        print(f'ERROR: {audio_dir} is not a valid directory path')
        return

    file_types = ['.mp3', '.wav']

    # create .csv file with column names
    csv_file_path = f'./{file_name}'
    column_names = ['title', 'genre_predictions']

    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(column_names)

        # iterate over audio files and store track name and prediction vector to .csv file
        for root, sub_dirs, files in os.walk(audio_dir):

            for track_name in files:
                track_path = os.path.join(audio_dir, track_name)
                _, file_extension = os.path.splitext(track_path)
                if file_extension in file_types:
                    track_prediction = gp.predict_genre(track_path, model_name, return_list=True)
                    csv_writer.writerow([track_name, f'[{",".join(map(str, track_prediction))}]'])


def calculate_absolute_difference(input_array: list, content_array: list) -> float:
    """
    Function that takes two arrays of numbers, performs an element-wise difference,
    and returns a float that is the sum of the elements of the resulting array.
    """
    # element-wise difference of arrays
    abs_diff = np.abs(content_array - input_array)
    return np.sum(abs_diff)


def recommender(genre_prediction: list, content_db_dir: str, rec_num: int) -> None:
    """
    Function that takes a list of genre predictions for one audio file,
    performs the calculations in calculate_absolute_difference() with a preprocessed
    database, and returns a specified number of content recommendations.
    Content recommendations are determined by finding the content with a minimal
    difference in genre prediction values.
    """

    # load preprocessed content .csv as pandas dataframe object
    df = pd.read_csv(content_db_dir, converters={'genre_predictions': ast.literal_eval})
    # convert lists in dataframe to numpy arrays before calculating differences
    df['genre_predictions'] = df['genre_predictions'].apply(np.array)
    # convert to numpy array
    np_genre_prediction = np.array(genre_prediction)
    # create new column in dataframe with difference values
    df['absolute_difference'] = df['genre_predictions'].apply(
        lambda row: calculate_absolute_difference(np_genre_prediction, row)
    )
    # sort dataframe by difference values
    df = df.sort_values(by='absolute_difference', ascending=True)

    result_df = df.head(rec_num)[['title', 'absolute_difference']]
    result_df_str = result_df.to_string(index=False)
    print(result_df_str)


if __name__ == "__main__":

    # navigate to git directory and run: python3 content_suggestion.py
    RECOMMENDER_DB = './content_suggestion/test_csv'
    MODEL_TO_USE = './content_suggestion/genre_model'
    PATH_TO_AUDIO = './content_suggestion/samples'
    TRACK_FOR_RECOMMENDER = './content_suggestion/nirvana_smells_like_teen.wav'
    NUMBER_OF_RECOMMENDATIONS = 3

    if not os.path.exists(RECOMMENDER_DB):
        build_recommender_db(PATH_TO_AUDIO, MODEL_TO_USE, RECOMMENDER_DB)

    prediction_list = gp.predict_genre(TRACK_FOR_RECOMMENDER, MODEL_TO_USE, return_list=True)
    recommender(prediction_list, RECOMMENDER_DB, NUMBER_OF_RECOMMENDATIONS)
