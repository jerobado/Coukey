# Main test of Coukey

import sys
sys.path.append('..')
import unittest

import keyboard

# from src.core.coukey import *
from src.main import main
from src.gui.main_gui import (CoukeyWindow,
                              __appname__,
                              __version__)

# [] TODO: how do you test a separate GUI?
LAST_KEY = None
KEY_TOTAL = 0
__test_appname__ = 'Coukey'
__test_version__ = '0.1'

class CoukeyTest(unittest.TestCase):

    def setUp(self):

        self.window = CoukeyWindow()
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

    def test_CoukeyWindow_windowTitle_version(self):

        self.assertEqual(self.window.windowTitle(), f'{__test_appname__} {__test_version__}')
    
    def test_CoukeyWindow_objectNames(self):

        self.assertEqual(self.window.keyLabel.objectName(), 'keyLabel')
        self.assertEqual(self.window.keyFrequencyLabel.objectName(), 'keyFrequencyLabel')
        self.assertEqual(self.window.keyTotal.objectName(), 'keyTotal')
        self.assertEqual(self.window.objectName(), 'CoukeyWindow')
