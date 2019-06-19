import os
from slackclient import SlackClient

slack_token = "xoxb-603964104007-605325579425-BnvTzdtWG1DZylpQQRoex4AH"
sc = SlackClient(slack_token)

# sc.api_call(
#   "chat.postMessage",
#   channel="CHS8MP814",
#   text="Social Calendar Slacker Bot - Coded by ray! :tada:"
# )

# class Slack:

def post(message):
    sc.api_call("chat.postMessage",channel="CHS8MP814",text= message)


post('send this test message')
