from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])

def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    #the chatbot logic
    responded = False
    if 'quote' in incoming_msg:
        #return a quote to the response here
        r = requests.get('https://api.quotable.io/random')
        if r.status_code ==200:
            data=r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'heyy! I could not retrieve a quote at this time, sorry!'
        msg.body(quote)
        responded = True
    
    if 'cat' in incoming_msg:
        #return a cat picture to the response here
        msg.media('https://cataas.com/cat') 
        responded = True
    if not responded:
        #return a generic response
        msg.body('Oops! I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__== '_main_':
    app.run()