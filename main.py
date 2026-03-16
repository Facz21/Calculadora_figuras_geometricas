import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import GeometryCalculator


def main():
    app = QApplication(sys.argv)

    window = GeometryCalculator()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()