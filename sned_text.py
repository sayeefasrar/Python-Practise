from twilio.rest import TwilioRestClient

#account_sid = "AC74de65b6df842fcea26dbc26e1c77829" # Your Account SID from www.twilio.com/console
#auth_token  = "bdc43a63c7b1bd6045ce143ba2e0fbc4"  # Your Auth Token from www.twilio.com/console

#client = TwilioRestClient(account_sid, auth_token)
client = TwilioRestClient()
#message = client.messages.create(body="Hello from Python",
    #to="+8801731360960",    # Replace with your phone number
    #from_="+12345678901") # Replace with your Twilio number 
client.messages.create(from_="(880) 1731360960",
                       to="(+880) 01731360960",
                       body="Python")
print(message.sid)
