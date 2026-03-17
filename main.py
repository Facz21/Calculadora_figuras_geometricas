import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import GeometryCalculator


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    QWidget {
        font-family: Segoe UI;
        font-size: 14px;
    }

    QPushButton {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 6px;
    }

    QPushButton:hover {
        background-color: #45a049;
    }

    QLineEdit {
        border: 1px solid #ccc;
        border-radius: 6px;
        padding: 4px;
    }

    QComboBox {
        padding: 4px;
        border-radius: 6px;
    }
    """)
    window = GeometryCalculator()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()