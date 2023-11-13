# Names: Kyle Donovan, Philip Hopkins, Marco Scandroglio
# Course: CS 467 Fall 2023
# Project: Top-n Music Genre Classification Neural Network
# GitHub Repo: https://github.com/pdhopkins/CS467_music_NN
# Description: Converts music files to mp3 for use in the NN

import pydub
import youtube_dl

def audio_conversion(file_path, new_format):
    audio_piece = pydub.AudioSegment.from_file(file_path)
    audio_piece.export(file_path + ".wav", format=new_format)

# modified from https://stackoverflow.com/questions/27473526/download-only-audio-from-youtube-video-using-youtube-dl-in-python-script
def youtube_get_audio(genre_string, video_url):
    ydl_opts = {
        # 'outtmpl': 'temp_file_youtube.mp3',
        # 'outtmpl': '%(title)s_%(uploader)s.%(ext)s',
        'outtmpl': f'{genre_string}.mp3',
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
    songs_to_convert = [
        "https://www.youtube.com/watch?v=7VBex8zbDRs",
        "https://www.youtube.com/watch?v=yF4lhz0yhHY",
        "https://www.youtube.com/watch?v=t-JD2bnNQvY",
        "https://www.youtube.com/watch?v=KywhPwmS5Gg",
        "https://www.youtube.com/watch?v=XX6GHiFKovw",
        "https://www.youtube.com/watch?v=xrq_xtm_qqQ",
        "https://www.youtube.com/watch?v=w6XV5c0-eYw",
        "https://www.youtube.com/watch?v=IwJ9RJgsmOQ",
        "https://www.youtube.com/watch?v=aXgSHL7efKg",
        "https://www.youtube.com/watch?v=Z6dqIYKIBSU",
        "https://www.youtube.com/watch?v=1sqE6P3XyiQ",
        "https://www.youtube.com/watch?v=7Y8VPQcPHhY",
        "https://www.youtube.com/watch?v=TMZi25Pq3T8",
        "https://www.youtube.com/watch?v=UePtoxDhJSw",
        "https://www.youtube.com/watch?v=XJ5FMEjWr5Q",
        "https://www.youtube.com/watch?v=3zrSoHgAAWo",
        "https://www.youtube.com/watch?v=zTVlrOk9a8M",
        "https://www.youtube.com/watch?v=iU9YM1Lfvt8",
        "https://www.youtube.com/watch?v=WYfljBCpmE4",
        "https://www.youtube.com/watch?v=XphUURIAx5g",
        "https://www.youtube.com/watch?v=8ELbX5CMomE",
        "https://www.youtube.com/watch?v=AByfaYcOm4A",
        "https://www.youtube.com/watch?v=oygrmJFKYZY",
        "https://www.youtube.com/watch?v=TZiMSLu8M8I",
        "https://www.youtube.com/watch?v=Vd0gCqMV_Og",
        "https://www.youtube.com/watch?v=0CGI0lS1ir4",
        "https://www.youtube.com/watch?v=o1tj2zJ2Wvg",
        "https://www.youtube.com/watch?v=f-S3X2saSwM",
        "https://www.youtube.com/watch?v=yMoDJ4HWWaE"
    ]
    genre = "blues"
    current_index = 0
    for each_song in songs_to_convert:
        current_song = genre + str(current_index)
        youtube_get_audio(current_song, each_song)
        current_index += 1

    # audio_conversion("nirvana_smells_like_teen.mp3", "wav")
    # audio_conversion("slipknot_devil_in.mp3", "wav")