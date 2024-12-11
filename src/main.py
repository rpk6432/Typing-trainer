import sys
from PyQt5.QtWidgets import QApplication
from gui import TypingTrainerGUI

def main():
    app = QApplication(sys.argv)
    gui = TypingTrainerGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
