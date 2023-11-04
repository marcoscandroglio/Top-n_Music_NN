import os
import librosa_conversion as libc
import data_pipeline as dp
import model_build_training as mbt
import genre_prediction as gp

# constants
DATA_DIRECTORY = 'genres_original'
TRAINING_DATASET_DIRECTORY = 'dataset_file'
MODEL_NAME = 'genre_model'
SAMPLE_FILE_DIRECTORY = 'samples'


# convert audio files to mel-spectrograms
libc.process_audio_database(DATA_DIRECTORY)

# build tensor from mel-spectrograms
tf_data, tf_labels = dp.pre_process(DATA_DIRECTORY)
tf_dataset = dp.create_tensorflow_dataset(tf_data, tf_labels)

tf_dataset.save(TRAINING_DATASET_DIRECTORY)

# display basic tensor information
print()
print('typical tensor element shape:')
print(tf_dataset.element_spec[0])
print()

# train model
if not os.path.exists(MODEL_NAME + '.keras'):
    mbt.train_model(TRAINING_DATASET_DIRECTORY, MODEL_NAME)
else:
    print(MODEL_NAME + '.keras' + ' exists')


# Check if "samples" exists
if os.path.exists(SAMPLE_FILE_DIRECTORY) and os.path.isdir(SAMPLE_FILE_DIRECTORY):
    # List files and directories in "samples"
    sample_contents = os.listdir(SAMPLE_FILE_DIRECTORY)

    # Iterate over the files in "samples" and return their full paths
    for item in sample_contents:
        item_path = os.path.join(SAMPLE_FILE_DIRECTORY, item)

        if os.path.isfile(item_path) and not item_path.endswith(".npy"):
            print()
            print(item_path)
            gp.predict_genre(item_path, MODEL_NAME)
else:
    print(f"The directory '{SAMPLE_FILE_DIRECTORY}' does not exist in '{DATA_DIRECTORY}'.")
