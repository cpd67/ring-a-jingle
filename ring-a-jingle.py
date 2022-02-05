import boto3
from flask import Flask
from twilio.twiml.voice_response import VoiceResponse


app = Flask(__name__)

@app.route('/song', methods=['GET', 'POST'])
def play_song():
    resp = VoiceResponse()
    try:
        # Connect to AWS S3 and grab song names
        s3_client = boto3.client('s3')
        songs = [k['Key'] for k in s3_client.list_objects_v2(Bucket='ring.a.jingle')['Contents']]
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': 'ring.a.jingle', 'Key': songs[0]},
            ExpiresIn=120
        )

        # Have twilio play the song
        resp.play(url)
    except Exception:
        resp.say("Something went wrong.")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)