import os
from random import choice

from flask import Flask, url_for, send_from_directory, request
from twilio.twiml.messaging_response import MessagingResponse
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
    # TODO host song files somewhere
    songs_dir = os.environ.get('SONG_DIR', 'songs')
    song_list = os.listdir(songs_dir)
    selected_song = choice(song_list)
    return send_from_directory(
        songs_dir,
        selected_song,
        as_attachment=True,
        mimetype='audio/mpeg'
    )


@app.route('/sms', methods=['GET', 'POST'])
def handle_sms():
    """
    Send a response to an incoming SMS text message.
    """
    resp = MessagingResponse()
    # Acceptable things that can be asked for
    valid_inputs = ['joke', 'clams', 'puppies']

    # Check to see what was asked for and respond accordingly
    resp_msg = ''
    body = request.values.get('Body')
    if body is not None:
        incoming_msg = body.lower()
        match incoming_msg:
            case "joke":
                resp_msg = 'Why did the chicken cross the road? To get to the other side!'
            case "clams":
                resp_msg = 'What do clams do on their birthday? They shellabrate!'
            case "puppies":
                resp_msg = 'What tiny puppy loves bubble baths? A shampoodle!'
            case _:
                resp_msg = f'I did not understand that. Try asking for one of the following: {", ".join(valid_inputs)}'
    else:
        resp_msg = "You need to tell me what you want! Use one word, like 'joke'"
    resp.message(resp_msg)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)