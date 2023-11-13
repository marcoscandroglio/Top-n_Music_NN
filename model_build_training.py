# Names: Kyle Donovan, Philip Hopkins, Marco Scandroglio
# Course: CS 467 Fall 2023
# Project: Top-n Music Genre Classification Neural Network
# GitHub Repo: https://github.com/pdhopkins/CS467_music_NN
# Description: Model definition and training program for the Genre NN

# Model layers were inspired by the Keras documentation,
# https://keras.io/getting_started/intro_to_keras_for_engineers

# imports
# import sys
import tensorflow as tf
import keras
from keras import layers

# Demo training flag set to true to demonstrate training on the MNIST dataset
DEMO_TRAINING = False


def build_model():
    """
    Creates the model for the Genre Neural Network.
    :return: returns a Keras Model object, that can then be used for training
    """
    number_of_genres = 10
    # Shape of MNIST is 28 by 28, will update with project shape
    input = keras.Input(shape=(128, 1292, 1))
    # Rescaling puts everything in the range of [0, 1]
    output = layers.Rescaling(scale=1.0/80, offset=1.0)(input)
    # Convolutional layer makes numerous levels of the tensors
    # Relu activation is a rectified logic unit - makes negatives go to zero
    output = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu")(output)
    # Average pooling layer pools every 2x2 to its average
    output = layers.MaxPooling2D(pool_size=(2, 2))(output)
    output = layers.Dropout(0.25)(output)
    output = layers.Conv2D(filters=64, kernel_size=(3, 3), activation="relu")(output)
    output = layers.MaxPooling2D(pool_size=(2, 2))(output)
    output = layers.Dropout(0.25)(output)
    output = layers.Conv2D(filters=128, kernel_size=(3, 3), activation="relu")(output)
    output = layers.MaxPooling2D(pool_size=(2, 2))(output)
    # Flatten takes the entire system down to a 1D tensor
    output = layers.Flatten()(output)
    # Dropout randomly sets values to zero, to help with overfitting
    output = layers.Dropout(0.5)(output)

    # The last dense layer provides the "output" of 10 nodes
    output = layers.Dense(number_of_genres, activation="softmax")(output)
    return keras.Model(input, output)


def train_model(path_to_dataset: str, model_name: str) -> None:
    """
    Function that passes existing dataset to model created
    with build_model() saving a trained model.
    """
    # path_to_dataset = "dataset_file"
    # path_to_val_set = sys.argv[2]
    # generate the genre and validation datasets
    genre_dataset = tf.data.Dataset.load(path_to_dataset)
    # print(genre_data.shape())
    # val_dataset = tf.data.Dataset.load(path_to_val_set)
    model = build_model()
    model.compile(optimizer="RMSprop",
                  loss="sparse_categorical_crossentropy",
                  metrics=[keras.metrics.SparseCategoricalAccuracy(name="Accuracy")])
    model.fit(genre_dataset,
              epochs=10,
              # validation_data=val_dataset
              )

    model.save(model_name + ".keras")


def main():
    if DEMO_TRAINING is True:
        # Load in MNIST data as both training and testing sets
        (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

        train_labels = train_labels[:5000]
        test_labels = test_labels[5000:]

        train_images = train_images[:5000]
        test_images = test_images[5000:]

        model = build_model()
        # Compile model with RMSprop omtimizer, and using sparse categorical
        # crossentropy for the loss function. This is because of the use
        # of integers for categories, rather than one-hot
        model.compile(optimizer="RMSprop",
                      loss="sparse_categorical_crossentropy",
                      metrics=[keras.metrics.SparseCategoricalAccuracy(name="Accuracy")])
        # Fit the model over 10 epochs, validating each time
        model.fit(train_images,
                  train_labels,
                  epochs=5,
                  validation_data=(test_images, test_labels))
        # Saves the model data to load back in later, or to be used in predictions
        model.save("D:/model_data.keras")

    else:
        # path_to_dataset = "dataset_file_batch25"
        # path_to_val_set = "validation_set_batch1"
        path_to_val_set = "dataset_file_batch1"
        path_to_dataset = "validation_set_batch1"
        # generate the genre and validation datasets
        genre_dataset = tf.data.Dataset.load(path_to_dataset)
        # print(genre_data.shape())
        val_dataset = tf.data.Dataset.load(path_to_val_set)
        model = build_model()
        # model.load_weights("model_data_batch25_twoconvlayer.keras")
        model.compile(optimizer="RMSprop",
                      loss="sparse_categorical_crossentropy",
                      metrics=[keras.metrics.SparseCategoricalAccuracy(name="Accuracy")])
        model.fit(genre_dataset,
                  epochs=20,
                  validation_data=val_dataset
                  )
        model.save("model_data_val1_posscale_threeconvlayer_20epoch.keras")


if __name__ == "__main__":
    main()
