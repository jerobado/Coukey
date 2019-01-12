# Main test of Coukey

import sys
sys.path.append('..')
import unittest

import keyboard

from src.core.coukey import *
from src.main import main
from src.gui.main_gui import (CoukeyWidget,
                              __appname__,
                              __version__)


LAST_KEY = None
KEY_TOTAL = 0


class CoukeyTest(unittest.TestCase):

    def setUp(self):

        self.window = CoukeyWidget()
        self.TEST_LAST_KEY = 'enter'
        self.TEST_KEY_TOTAL = 0
        keyboard.hook(self.__test_key_listener)

    def __test_key_listener(self, event):
        """ Hook keyboard to listen to key strokes """

        if event.event_type == 'down':
            self.TEST_KEY_TOTAL += 1
            self.TEST_LAST_KEY = event.name
            print(f'[TEST] {self.TEST_KEY_TOTAL}: {self.TEST_LAST_KEY}')
      
    def test_main(self):
        """ Test if the app exited gracefully """

        self.assertEqual(main(), 0)

    def test_CoukeyWidget_windowTitle(self):

        self.assertEqual(self.window.windowTitle(), f'{__appname__} {__version__}')
    