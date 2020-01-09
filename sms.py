from twilio.rest import Client

account_sid = 'ACef298bc6b1a9737581075c308063a42a'
auth_token = '45ecf2cc48e9d1ee27243203b553a9b3'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+18174403705',
    body="I can't believe this works",
    to='+18132635097'
)

print(message.sid)