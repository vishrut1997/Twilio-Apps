from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    resp = VoiceResponse()
    resp.play("https://iptelephonylab4.s3.amazonaws.com/IP+Telephony+Lab+4.mp3")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

