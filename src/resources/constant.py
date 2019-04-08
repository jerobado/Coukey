# Static/constant variables should be coded here

import os
import sys
from PyQt5.QtWidgets import QApplication

__appname__ = 'Coukey'
__version__ = '0.1.2'

APP = QApplication(sys.argv)


# [] TODO: make this part of the __init__ process to identify dev or live mode
def resource_path(relative_path):
    """ Get absolute path of data files. """

    try:
        print('we are skiing in freeze mode # no pun intended :) #live')
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        print('we are not freeze yet #developing')
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# development files
# COUKEY_QSS_FILE = open('..\qss\coukey.qss').read()

# # live files
COUKEY_QSS_FILE = open(resource_path('qss\coukey.qss')).read()
