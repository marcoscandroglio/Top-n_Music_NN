# import os
import ast
import numpy as np
import pandas as pd
# import genre_prediction as gp


def build_recommender_db(audio_dir: str) -> None:
    """
    Function that takes as an argument a string that represents a directory containing audio files.
    This function iterates through the audio files to build a database/csv file containing
    audio titles and the genre predictions created by the trained model and saves it.
    """
    pass


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
        lambda row: calculate_absolute_difference(np_genre_prediction, row['genre_predictions']),
        axis=1
    )
    # sort dataframe by difference values
    df = df.sort_values(by='absolute_difference', ascending=False)

    result_df = df.head(rec_num)[['title', 'absolute_difference']]
    print(result_df)
