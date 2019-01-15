# Static/constant variables should be coded here

import sys
from PyQt5.QtWidgets import QApplication

__appname__ = 'Coukey'
__version__ = '0.1.1'

APP = QApplication(sys.argv)


COUKEY_QSS_FILE = open('..\qss\coukey.qss').read()

