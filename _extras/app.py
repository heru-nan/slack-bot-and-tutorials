from slack import WebClient
from nestorbot import NestorBot
import os
import logging
from flask import Flask
from slackeventsapi import SlackEventAdapter

print(os.environ.get("SLACK_TOKEN"));
print(os.environ.get("SLACK_EVENTS_TOKEN"));
app = Flask(__name__)
slack_events_adapter = SlackEventAdapter(os.environ.get("SLACK_EVENTS_TOKEN"), "/slack/events", app)

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

def say_hola(channel):
    # Create a new JamesBot
    james_bot = NestorBot(channel)

    # Get the onboarding message payload
    message = james_bot.get_message_payload()

    # Post the onboarding message in Slack
    slack_web_client.chat_postMessage(**message)


# When a 'message' event is detected by the events adapter, forward that payload
# to this function.
@slack_events_adapter.on("message")
def message(payload):
    """Parse the message event, and if the activation string is in the text,
    send a responde from James.
    """

    # Get the event data from the payload
    event = payload.get("event", {})

    # Get the text from the event that came through
    text = event.get("text")

    # Check and see if the activation phrase was in the text of the message.
    # If so, execute the code to flip a coin.
    if "hola james" in text.lower():
        # Since the activation phrase was met, get the channel ID that the event
        # was executed on
        channel_id = event.get("channel")
        # Execute the flip_coin function and send the results of
        # flipping a coin to the channel
        return say_hola(channel_id)

if __name__ == "__main__":
    # Create the logging object
    logger = logging.getLogger()

    # Set the log level to DEBUG. This will increase verbosity of logging messages
    logger.setLevel(logging.DEBUG)

    # Add the StreamHandler as a logging handler
    logger.addHandler(logging.StreamHandler())

    # Run our app on our externally facing IP address on port 3000 instead of
    # running it on localhost, which is traditional for development.
    app.run(host='0.0.0.0', port=3000)
