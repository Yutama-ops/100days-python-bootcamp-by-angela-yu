import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

account_sid = 'your account id here'
auth_token = 'your twilio token here'

client = Client(account_sid, auth_token, http_client=proxy_client)

# twilio api calls will now work from behind the proxy:
message = client.messages.create(to="...", from_='...', body='...')