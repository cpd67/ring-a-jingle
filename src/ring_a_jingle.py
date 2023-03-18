import os
from random import choice

from flask import Flask, url_for, request, send_file
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)


@app.route('/song', methods=['GET', 'POST'])
def get_song_url():
    """
    Main entrypoint for Twilio. Sends a response which tells Twilio where to
    get the song.
    """
    resp = VoiceResponse()
    try:
        resp.play(url_for("play_song", _external=True))
        return str(resp)
    except Exception:
        resp.say('ring-a-jingle is experiencing technical difficulties, please try again later.')


@app.route('/play', methods=['GET', 'POST'])
def play_song():
    """
    Send a random song to play.
    """
    song_dir = 'songs/'
    song_list = os.listdir(f'src/{song_dir}')
    selected_song = choice(song_list)

    # TODO host song files somewhere
    return send_file(f'{song_dir}{selected_song}', as_attachment=True, 
                     attachment_filename=selected_song, mimetype='audio/mpeg'
                     )


if __name__ == "__main__":
    app.run(debug=True)