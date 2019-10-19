#Software to Hardware for Gmail Email Visualizer

import time
from neopixel import *
import argparse
import email_category_collector


 
# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#Defining different colors
#Important- red
#Social- yellow
#Personal- green
#Fourms- blue
#updates- orange

color_dict = {
    "red":Color(0,64,0),
    "yellow":Color(64,64,0),
    "green":Color(64,0,0),
    "blue":Color(0,0,64),
    "orange":Color(32,64,0),
    "white":Color(0,64,64)
}

def color_strip(strip, color):
    for i in range(0,len(color)):
        strip.setPixelColor(i, color[i])
    strip.show()

#Main Program logic follows:
def main():
    #Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # INtialize the library (must be called once before other functions).
    strip.begin()
    
    colors_name = email_category_collector.get_colors()
    colors = []
    for color in colors_name:
        colors.append(color_dict[color])
    color_strip(strip, colors)

if __name__ == "__main__":
    main()
