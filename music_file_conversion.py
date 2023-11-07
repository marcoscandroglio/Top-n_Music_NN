# Names: Kyle Donovan, Philip Hopkins, Marco Scandroglio
# Course: CS 467 Fall 2023
# Project: Top-n Music Genre Classification Neural Network
# GitHub Repo: https://github.com/pdhopkins/CS467_music_NN
# Description: Converts music files to mp3 for use in the NN

import pydub
import youtube_dl

def audio_conversion():
    audio_piece = pydub.AudioSegment.from_file("disturbed_ten_thousand_fists.wma")
    audio_piece.export("disturbed_ten_thousand_fists.mp3",format="mp3")

# modified from https://stackoverflow.com/questions/27473526/download-only-audio-from-youtube-video-using-youtube-dl-in-python-script
def youtube_get_audio(video_url):
    ydl_opts = {
        'outtmpl': 'temp_file_youtube.mp3',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    youtube_get_audio("https://www.youtube.com/watch?v=rY0WxgSXdEE")
