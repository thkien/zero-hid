import logging
from zero_hid import Keyboard, KeyCodes

logging.basicConfig(level=logging.DEBUG)


k = Keyboard()
k.type('Hello world!')
