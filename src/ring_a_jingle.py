import os

from flask import Flask
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)


@app.route('/song', methods=['GET', 'POST'])
def play_song():
    resp = VoiceResponse()
    try:

    except Exception:
        resp.say("Unable to obtain a jingle. Please try again later.", voice='alice')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)