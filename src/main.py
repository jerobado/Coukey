"""
Coukey /ku-kee/ is a desktop application that can tally the keys that you typed on the keyboard. Nope, she's not a keylogger and will never be :)

Things that it she can do:
* Count the frequency of a specific key you typed
* Count the total number of keys you typed
* Display the last key you typed
* Satisfy your stat geekiness

Tools and Dependencies
* Python 3.7.1
* PyQt 5.11.3        # [x] TODO: what's your version?
* keyboard 0.13.2

Author: Jero Bado
Date created:  12 Jan 2019
License: GPL-3.0
"""

import sys
sys.path.append('..')
from PyQt5.QtWidgets import QApplication
from src.gui.main_gui import CoukeyWindow
from src.resources.constant import APP


def main():

    window = CoukeyWindow()
    window.show()
    return APP.exec()


if __name__ == '__main__':
    main()
