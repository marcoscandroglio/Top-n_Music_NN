# Names: Kyle Donovan, Philip Hopkins, Marco Scandroglio
# Course: CS 467 Fall 2023
# Project: Top-n Music Genre Classification Neural Network
# GitHub Repo: https://github.com/pdhopkins/CS467_music_NN
# Description: Converts music files to mp3 for use in the NN

import pydub
import yt_dlp


def audio_conversion(file_path, new_format):
    audio_piece = pydub.AudioSegment.from_file(file_path)
    audio_piece.export(file_path + ".wav", format=new_format)

# modified from https://stackoverflow.com/questions/27473526/
# download-only-audio-from-youtube-video-using-youtube-dl-in-python-script/


def youtube_get_audio(video_url, genre_string="temp_file_youtube"):
    ydl_opts = {
        # 'outtmpl': 'temp_file_youtube.mp3',
        # 'outtmpl': '%(title)s_%(uploader)s.%(ext)s',
        'outtmpl': f'{genre_string}',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


if __name__ == "__main__":
    songs_to_convert = [
        "https://www.youtube.com/watch?v=9VSerKr1vBM"
    ]
    genre = "valrock"
    current_index = 0
    for each_song in songs_to_convert:
        current_song = genre + str(current_index)
        youtube_get_audio(each_song, current_song)
        current_index += 1

    # audio_conversion("nirvana_smells_like_teen.mp3", "wav")
    # audio_conversion("slipknot_devil_in.mp3", "wav")
