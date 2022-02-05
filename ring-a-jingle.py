import boto3
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)

# https://demo.twilio.com/welcome/voice/
@app.route('/song', methods=['GET', 'POST'])
def play_song():
    resp = VoiceResponse()
    resp.say('Ello, Yello!')
    return resp


if __name__ == "__main__":
    app.run(debug=True)