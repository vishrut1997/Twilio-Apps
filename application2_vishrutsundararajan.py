import os
from flask import Flask,request,redirect
import twilio.twiml
from twilio.rest import Client
from twilio.twiml.voice_response import Dial,VoiceResponse,Say
import time

account = "AC33d941d44ccba8e8c03ea0b536ef1f8c"
token = "ee5b6e6e7cebb4ed25c42ea98e4a4275"
client = Client(account,token)

app = Flask(__name__)

@app.route("/sms", methods=('GET','POST'))

def conference():

	from_number = request.values.get('From',None)
	body_number = request.values.get('Body',None)

	call = client.calls.create(
		url="https://handler.twilio.com/twiml/EHc3e6476244f8b9a36de7e48944460a2b",
		to=from_number,
		from_="+12138552620"
		)

	time.sleep(10)
	call = client.calls.create(
		url="https://handler.twilio.com/twiml/EH15b6d14979e310393ea16202fe11fc13",
		to=body_number,
		from_="+12138552620"
		)


	return "return"

if __name__ == "__main__":
    app.run(debug=True)
