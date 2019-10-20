# email-blinker (TopInbox)
Basic RPi gmail visualizer
Connor Ennis & Daniel Fogle, 2019

As an entry for the 2019 CuHackit event (Clemson University, SC),
this basic pair of scripts uses Google's gmail api to create a
visualizer using NeoPixel compatible (WS2812) LEDs

When connected to an inbox, the LEDs each represent unread emails,
from newest to oldest, color coded based on Google's labelling system.

# Build Instructions
- Install python 2.7.X & pip
- pip install the following:
  - ws2812
  - google-api-python-client
  - google-auth-httplib2
  - google-auth-oauthlib

NOTE: You cannot use the official adafruit-circuitpython-neopixel
driver in python 2. Thus, you need to manually remove the
neopixel.py file from that library and import from that file.
