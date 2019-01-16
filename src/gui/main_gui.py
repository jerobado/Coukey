# Main Graphical User Interface (GUI) of Coukey

# standard library
from collections import Counter

# third-party libraries
import keyboard
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QLabel,
                             QHBoxLayout,
                             QVBoxLayout)

# coukey files
from src.resources.constant import (__appname__,
                                    __version__,
                                    COUKEY_QSS_FILE)


class CoukeyWindow(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.LAST_KEY = 'start typing'
        self.LAST_KEY_FREQUENCY = 0
        self.KEY_TOTAL = 0
        self.KEY_COUNTER = Counter()
        self._widgets()
        self._properties()
        self._layouts()
        keyboard.hook(self.__key_listener)

    def _widgets(self):

        self.keyLabel = QLabel(self.LAST_KEY)
        self.keyFrequencyLabel = QLabel(f'Frequency: {self.LAST_KEY_FREQUENCY}')
        self.keyTotalLabel = QLabel(f'Total: {self.KEY_TOTAL}')

    def _properties(self):

        self.keyLabel.setObjectName('keyLabel')
        self.keyLabel.setAlignment(Qt.AlignCenter)

        self.keyFrequencyLabel.setObjectName('keyFrequencyLabel')
        self.keyFrequencyLabel.setAlignment(Qt.AlignCenter)

        self.keyTotalLabel.setObjectName('keyTotalLabel')
        self.keyTotalLabel.setAlignment(Qt.AlignCenter)
        
        self.setObjectName('CoukeyWindow')
        self.setStyleSheet(COUKEY_QSS_FILE)
        self.setWindowTitle(f'{__appname__} {__version__}')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.resize(253, 73)

    def _layouts(self):

        vertical = QVBoxLayout()
        vertical.addWidget(self.keyLabel)
        vertical.addWidget(self.keyFrequencyLabel)
        vertical.addWidget(self.keyTotalLabel)
    
        self.setLayout(vertical)

    def __key_listener(self, event):

        if event.event_type == 'down':
            # tally key pressed
            self.KEY_TOTAL += 1
            self.LAST_KEY = event.name

            if self.LAST_KEY not in self.KEY_COUNTER.keys():
                self.KEY_COUNTER[self.LAST_KEY] = 1
            else:
                self.KEY_COUNTER[self.LAST_KEY] += 1
            
            self.LAST_KEY_FREQUENCY = self.KEY_COUNTER[self.LAST_KEY]
            
            # display results in GUI and console
            self.keyLabel.setText(self.LAST_KEY)
            self.keyFrequencyLabel.setText(f'Frequency: {self.LAST_KEY_FREQUENCY}')
            self.keyTotalLabel.setText(f'Total: {self.KEY_TOTAL}')

            print(f'{self.KEY_TOTAL}: {self.LAST_KEY} ({self.KEY_COUNTER[self.LAST_KEY]})')            

    def keyPressEvent(self, event):

        if event.modifiers() & Qt.ControlModifier and event.key() == Qt.Key_Q:
            self.close()

    def resizeEvent(self, event):

        print(f'{self.width()} x {self.height()}')
