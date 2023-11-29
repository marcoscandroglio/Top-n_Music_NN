# Top-N  Music Genre Neural Network 
README for CS 467 Top-N Music Genre Neural Network, by Kyle Donovan, Philip Hopkins, Marco Scandroglio

## Note on usage
This software is distributed as-is, and any use of this software in a way that would violate any laws is strictly prohibited.

# Project Description
This project seeks to automate the process of determining the genre of a provided music sample. Artificial intelligence is a major factor in this project, and neural networks in particular are uniquely positioned to mimic the human functionality of determining genre of music by comparing the provided sample to previous samples of music with defined genres. The project seeks to use Python, and Python packages, to accomplish these tasks. In particular, the conversion of audio files to numeric data will be accomplished using the Librosa package to perform short-time Fourier transforms, and TensorFlow will be used for the neural network. This also presents the opportunity for our group, which has experience with Python but little to no experience with TensorFlow or Librosa, to work with new technologies and expand our knowledge of artificial intelligence while creating a usable product.

## Requirements
This software requires the following Python packages, as well as any associated dependencies:
+ TensorFlow
+ Flask
+ FFMPEG (installed, and part of the PATH variable)
+ yt-dlp
This software also requires Python to be installed, at a version equal to or greater than 3.xx

# How to Install and Run
1.	Download zip of Github repository, then extract. 
2.	Using the command line, install dependencies: 
3.	Navigate to extracted folder using command line/terminal, then run application. You need python installed, run command `python app.py` or python3 `app.py`
4.	A series of messages should appear in terminal. Using a browser, navigate to the http address listed. Default is http://127.0.0.1:5000 
5.	The page should display similarly to this:
   ![image](https://github.com/pdhopkins/CS467_music_NN/assets/97189054/c401958d-f6e2-4b96-a43a-eac9e666f0cf)
7. From here, you should be able to upload song files (mp3/aac formats) or select a YouTube song link to determine a genre. For further instructions, please see the How to Use section

# How to Use
1.	Once you have completed the steps in How to Install and Run, you should have a webpage opened at the address from the command line. 
2.	At the webpage, you should see three buttons, one to choose file, one to upload, and one to predict genre. 
3A.	Local File Upload: If you want to upload a song file from your computer, select Choose File and find the desired song from your local machine. Then, when the No file chosen text changes to the song file, click the upload button and wait for the genre results to appear.
3B.	Youtube Link: If you want to predict the genre from a YouTube link, copy and paste the YouTube link into the “Or use a YouTube URL” section and click the “Predict Genre” button and wait for the genre results to appear. 


# Credits
Created by Kyle Donovan(https://github.com/kylemdonovan), Phillip Hopkins(https://github.com/pdhopkins/CS467_music_NN), and Marco Scandroglio (https://github.com/marcoscandroglio)

# License
???
