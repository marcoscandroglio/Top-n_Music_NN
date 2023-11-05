from flask import Flask, render_template, request

app = Flask(__name__)

# function to determine the genre of the uploaded song
def determine_genre(song):
    # placeholder until integration with team code
    predicted_genre = "Rock"  # placeholder for predicted genre

    return predicted_genre

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    song = request.files['song'] if 'song' in request.files else None

    if not song or song.filename == '':
        return "No file selected"

    predicted_genre = determine_genre(song)
    return f'The predicted genre of the song is: {predicted_genre}'

if __name__ == '__main__':
    app.run(debug=True)
