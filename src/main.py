"""
Coukey /ku-kee/ is a desktop application that can tally the keys that you typed on the keyboard. Nope, she's not a keylogger and will never be :)

Things that it she can do:
* Count the frequency of a specific key you typed
* Count the total number of keys you typed
* Display the last key you typed
* Satisfy your stat geekiness

Tools and Dependencies
* Python 3.7.1
* PyQt 5.11.
* keyboard 0.13.2

Author: Jero Bado
Date created:  12 Jan 2019
License: GPL-3.0
"""

import sys
sys.path.append('..')
from PyQt5.QtWidgets import QApplication
from src.gui.main_gui import CoukeyWidget

APP = QApplication(sys.argv)

def main():

    window = CoukeyWidget()
    window.show()
    return APP.exec()


if __name__ == '__main__':
    main()
