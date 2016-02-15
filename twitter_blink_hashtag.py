import time
import RPi.GPIO as GPIO
from twython import TwythonStreamer
    
# Search terms
TERMS = '#TheWalkingDead'
    
# GPIO pin number of LED
LED = 18
    
# Twitter application authentication
APP_KEY = '<YOUR CONSUMER KEY>'
APP_SECRET = '<YOUR CONSUMER SECRET>'
OAUTH_TOKEN = '<YOUR ACCESS TOKEN>'
OAUTH_TOKEN_SECRET = '<YOUR ACCESS TOKEN SECRET>'
    
# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
            print
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED, GPIO.LOW)
    
# Setup GPIO as output
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
    
# Create streamer
try:
    stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
    GPIO.cleanup()
