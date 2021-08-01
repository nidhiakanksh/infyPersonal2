from fastapi import FastAPI
import uvicorn ##ASGI 
from twilio.twiml.messaging_response import MessagingResponse
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
   return "Hello, World!"
    
@app.get('/{sms}')
def get_name(name: str):
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))

    return str(resp)



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=7000)
#uvicorn Handwriting_Recognition_api:app --reload