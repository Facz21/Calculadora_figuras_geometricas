from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QComboBox, QTabWidget
)

from ui.draw_area import DrawArea

from shapes.circle import Circle
from shapes.square import Square
from shapes.rectangle import Rectangle
from shapes.equilateral_triangle import EquilateralTriangle
from shapes.right_triangle import RightTriangle

from shapes.sphere import Sphere
from shapes.cube import Cube
from shapes.cylinder import Cylinder
from shapes.cone import Cone
from shapes.pyramid import Pyramid


class GeometryCalculator(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Geométrica")

        layout = QVBoxLayout()

        self.tabs = QTabWidget()

        self.tabs.addTab(self.create2DTab(), "2D")
        self.tabs.addTab(self.create3DTab(), "3D")

        layout.addWidget(self.tabs)

        self.setLayout(layout)

    def create2DTab(self):

        widget = QWidget()
        layout = QVBoxLayout()

        self.shape2d = QComboBox()
        self.shape2d.addItems([
            "Circulo",
            "Cuadrado",
            "Rectangulo",
            "Triangulo Equilatero",
            "Triangulo Rectangulo"
        ])

        self.input1 = QLineEdit()
        self.input2 = QLineEdit()

        self.result2d = QLabel("Resultado")

        btn = QPushButton("Calcular")
        btn.clicked.connect(self.calculate2D)

        self.canvas2d = DrawArea()

        layout.addWidget(self.shape2d)
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(btn)
        layout.addWidget(self.result2d)
        layout.addWidget(self.canvas2d)

        widget.setLayout(layout)

        return widget

    def create3DTab(self):

        widget = QWidget()
        layout = QVBoxLayout()

        self.shape3d = QComboBox()
        self.shape3d.addItems([
            "Esfera",
            "Cubo",
            "Cilindro",
            "Cono",
            "Piramide"
        ])

        self.input3 = QLineEdit()
        self.input4 = QLineEdit()

        self.result3d = QLabel("Resultado")

        btn = QPushButton("Calcular")
        btn.clicked.connect(self.calculate3D)

        self.canvas3d = DrawArea()

        layout.addWidget(self.shape3d)
        layout.addWidget(self.input3)
        layout.addWidget(self.input4)
        layout.addWidget(btn)
        layout.addWidget(self.result3d)
        layout.addWidget(self.canvas3d)

        widget.setLayout(layout)

        return widget

    def calculate2D(self):

        try:

            a = float(self.input1.text())
            b = float(self.input2.text()) if self.input2.text() else 0

            shape = self.shape2d.currentText()

            if shape == "Circulo":
                fig = Circle(a)
                self.canvas2d.setShape("circle")

            elif shape == "Cuadrado":
                fig = Square(a)
                self.canvas2d.setShape("square")

            elif shape == "Rectangulo":
                fig = Rectangle(a, b)

            elif shape == "Triangulo Equilatero":
                fig = EquilateralTriangle(a)
                self.canvas2d.setShape("triangle")

            else:
                fig = RightTriangle(a, b)
                self.canvas2d.setShape("triangle")

            area = fig.area()
            peri = fig.perimeter()

            self.result2d.setText(f"Area: {area:.2f} | Perimetro: {peri:.2f}")

        except:
            self.result2d.setText("Entrada invalida")

    def calculate3D(self):

        try:

            a = float(self.input3.text())
            b = float(self.input4.text()) if self.input4.text() else 0

            shape = self.shape3d.currentText()

            if shape == "Esfera":
                fig = Sphere(a)

            elif shape == "Cubo":
                fig = Cube(a)

            elif shape == "Cilindro":
                fig = Cylinder(a, b)

            elif shape == "Cono":
                fig = Cone(a, b)

            else:
                fig = Pyramid(a, b)

            vol = fig.volume()
            surf = fig.surface()

            self.result3d.setText(f"Volumen: {vol:.2f} | Superficie: {surf:.2f}")

        except:
            self.result3d.setText("Entrada invalida")