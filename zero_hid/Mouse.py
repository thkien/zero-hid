from .hid.mouse import send_mouse_event
from typing import SupportsInt


class RelativeMoveRangeError(Exception):
    pass


class Mouse:
    HID_DEV=None

    def __init__(self, dev_path='/dev/hidg1') -> None:
        self.dev_path = dev_path

        if Mouse.HID_DEV:
            self.dev = Mouse.HID_DEV
        else:
            try:
                Mouse.HID_DEV=open(dev_path, 'ab+')
                self.dev = Mouse.HID_DEV
            except Exception as e:
                self.dev = None
                print(f"Failed to open HID device: '{dev_path}'")
                print(e)

    def left_click(self):
        if self.dev:
            send_mouse_event(self.dev, 0x1, 0, 0, 0, 0)
            send_mouse_event(self.dev, 0x0, 0, 0, 0, 0)

    def right_click(self):
        if self.dev:
            send_mouse_event(self.dev, 0x1, 0, 0, 0, 0)
            send_mouse_event(self.dev, 0x2, 0, 0, 0, 0)

    def move_relative(self, x, y):
        """
        move the mouse in relative mode
        x,y should be in range of -127 to 127
        """
        if not -127 <= x <= 127:
            raise RelativeMoveRangeError(f"Value of x: {x} out of range (-127 - 127)")
        if not -127 <= y <= 127:
            RelativeMoveRangeError(f"Value of x: {y} out of range (-127 - 127)")
        if self.dev:
            send_mouse_event(self.dev, 0x0, x, y, 0, 0)

    def _clean_resources(self):
        if Mouse.HID_DEV:
            Mouse.HID_DEV.close()
            self.dev = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._clean_resources()

    def __del__(self):
        self._clean_resources()

    def close(self):
        self._clean_resources()