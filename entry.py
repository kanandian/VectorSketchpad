import components
import sys
from PyQt5.QtWidgets import QApplication


def main():
    app = 0
    app = QApplication(sys.argv)
    application = components.Sketchpad()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
