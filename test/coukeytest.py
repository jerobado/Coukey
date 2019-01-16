# Main test of Coukey

import sys
sys.path.append('..')
import unittest
from collections import Counter
import keyboard
from PyQt5.QtCore import Qt

# [] TODO: start testing coukey.py
# from src.core.coukey import *
from src.main import main
from src.gui.main_gui import (CoukeyWindow,
                              __appname__,
                              __version__)

# [] TODO: how do you test a separate GUI?
LAST_KEY = None
KEY_TOTAL = 0
__test_appname__ = 'Coukey'
__test_version__ = '0.1.1'

class CoukeyTest(unittest.TestCase):

    def setUp(self):

        self.window = CoukeyWindow()
        # main()
        self.TEST_LAST_KEY = 'enter'
        self.TEST_LAST_KEY_FREQUENCY = 0
        self.TEST_KEY_TOTAL = 0
        self.TEST_KEY_COUNTER = Counter()
        keyboard.hook(self.__test_key_listener)

    def __test_key_listener(self, event):
        """ Hook keyboard to listen to key strokes """

        if event.event_type == 'down':
            self.TEST_KEY_TOTAL += 1
            self.TEST_LAST_KEY = event.name

            if self.TEST_LAST_KEY not in self.TEST_KEY_COUNTER.keys():
                self.TEST_KEY_COUNTER[self.TEST_LAST_KEY] = 1
            else:
                self.TEST_KEY_COUNTER[self.TEST_LAST_KEY] += 1

            self.TEST_LAST_KEY_FREQUENCY = self.TEST_KEY_COUNTER[self.TEST_LAST_KEY]

            print(f'[TEST] {self.TEST_KEY_TOTAL}: {self.TEST_LAST_KEY} ({self.TEST_LAST_KEY_FREQUENCY})')
      
    def test_main(self):
        """ Test if the app exited gracefully """

        self.assertEqual(main(), 0)

    def test_keyFrequencyLabel_text(self):

        self.assertEqual(self.window.LAST_KEY_FREQUENCY, self.TEST_LAST_KEY_FREQUENCY)  # [] TODO: test passing, result is 0 == 0 

    # [x] TODO: refactor this to ~properties
    def test_CoukeyWindow_properties(self):

        self.assertEqual(self.window.windowTitle(), f'{__test_appname__} {__test_version__}')
    
    def test_CoukeyWindow_objectNames(self):

        self.assertEqual(self.window.keyLabel.objectName(), 'keyLabel')
        self.assertEqual(self.window.keyFrequencyLabel.objectName(), 'keyFrequencyLabel')
        self.assertEqual(self.window.keyTotalLabel.objectName(), 'keyTotalLabel')
        self.assertEqual(self.window.objectName(), 'CoukeyWindow')
