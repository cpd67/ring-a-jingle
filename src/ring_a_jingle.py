from flask import Flask
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)


@app.route('/song', methods=['GET', 'POST'])
def play_song():
    resp = VoiceResponse()
    try:
        # Connect to AWS S3 and grab song names
        resp.say("ring-a-jingle is currently down. It will return at a later date.")
    except Exception:
        resp.say("Unable to obtain a jingle. Please try again later.", voice='alice')
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)