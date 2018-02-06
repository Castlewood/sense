#!/usr/bin/python3
import datetime
import numpy as np
import time
from random import randint
import sys
import threading
import astro_logging
import astro_display
import astro_cabin_alt

#main program
#coded by Caitlin, Cerys, Harrison, Holly, James and Liam

astro_display.setup()
astro_display.updateDisplay()
astro_logging.setup()
astro_logging.log()
astro_cabin_alt.display_cabin_alt()
