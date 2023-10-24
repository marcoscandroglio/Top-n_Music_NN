# Names: Kyle Donovan, Philip Hopkins, Marco Scandroglio
# Course: CS 467 Fall 2023
# Project: Top-n Music Genre Classification Neural Network
# GitHub Repo: https://github.com/pdhopkins/CS467_music_NN
# Description: Model definition and training program for the Genre NN

# Model layers were inspired by the Keras documentation,
# https://keras.io/getting_started/intro_to_keras_for_engineers

# imports
import tensorflow as tf
import keras
from keras import layers
import sys


def build_model():
    """
    Creates the model for the Genre Neural Network.
    :return: returns a Keras Model object, that can then be used for training
    """
    number_of_genres = 10
    input = keras.Input(shape=(None, None, 1))
    output = layers.Rescaling(scale=1/100)(input)
    output = layers.Conv2D(filters=32, kernel_size=(4, 4))(output)
    output = layers.GlobalAvgPool2D()(output)
    output = layers.Dense(number_of_genres)(output)
    return keras.Model(input, output)


def main():
    path_to_dataset = sys.argv[1]
    # Probably need path to validation dataset as well
    genre_dataset = tf.data.Dataset.load(path_to_dataset)
    model = build_model()
    model.compile(optimizer="rmsprop",
                  loss="sparse_categorical_crossentropy",
                  metrics=[keras.metrics.SparseCategoricalAccuracy(name="Accuracy")])
    model.fit(genre_dataset, epochs=10)  # probably need validation_data=
    model.save("model_data.keras")


if __name__ == "__main__":
    main()
