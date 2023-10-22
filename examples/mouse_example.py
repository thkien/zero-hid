import logging
from zero_hid import Mouse

logging.basicConfig(level=logging.DEBUG)

m = Mouse()
for i in range(5):
    m.move_relative(5,5)
