from flask import Flask, render_template, request

app = Flask(__name__)

# function to determine the genre of the uploaded song


def determine_genre(song_path):
    # placeholder for determining genre
    return "Rock"


def process_youtube_url(url):
    # placeholder for processing YouTube URL
    return [("Genre1", 0.7), ("Genre2", 0.2), ("Genre3", 0.1)]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'song' in request.files:
        # file upload
        song = request.files['song']

        if song.filename == '':
            return render_template('error.html', error_message="No file selected for upload")

        predicted_genre = determine_genre(song)
        return render_template('results.html', predicted_genre=predicted_genre)

    elif 'url' in request.form:
        # YouTube URL input
        url = request.form['url']

        if not url:
            return render_template('error.html', error_message="No URL provided")

        result_list = process_youtube_url(url)
        return render_template('results.html', predicted_genre=result_list[0][0])

    return "Invalid request"


if __name__ == '__main__':
    app.run(debug=True)
