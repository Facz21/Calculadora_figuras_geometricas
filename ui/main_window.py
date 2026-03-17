from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QComboBox, QTabWidget, QGridLayout
)

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


# 🔥 FACTORES DE CONVERSIÓN
UNIT_FACTORS = {
    "cm": 1,
    "m": 100,
    "in": 2.54
}


class GeometryCalculator(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora Geométrica")

        layout = QVBoxLayout()

        # Selector de unidades
        self.unitSelector = QComboBox()
        self.unitSelector.addItems(["cm", "m", "in"])

        layout.addWidget(QLabel("Unidad:"))
        layout.addWidget(self.unitSelector)

        self.tabs = QTabWidget()
        self.tabs.addTab(self.create2DTab(), "2D")
        self.tabs.addTab(self.create3DTab(), "3D")

        layout.addWidget(self.tabs)
        self.setLayout(layout)

    # =========================
    # 🔵 2D
    # =========================
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

        self.shape2d.currentTextChanged.connect(self.updateInputs2D)

        self.label1 = QLabel("Parametro 1")
        self.label2 = QLabel("Parametro 2")

        self.input1 = QLineEdit()
        self.input2 = QLineEdit()

        self.result2d = QLabel("Resultado")

        btn = QPushButton("Calcular")
        btn.clicked.connect(self.calculate2D)

        layout.addWidget(self.shape2d)
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        layout.addWidget(btn)
        layout.addWidget(self.result2d)

        layout.addStretch()

        widget.setLayout(layout)
        self.updateInputs2D(self.shape2d.currentText())

        return widget

    # =========================
    # 🔷 3D
    # =========================
    def create3DTab(self):

        widget = QWidget()
        main_layout = QVBoxLayout()

        self.shape3d = QComboBox()
        self.shape3d.addItems([
            "Esfera",
            "Cubo",
            "Cilindro",
            "Cono",
            "Piramide"
        ])

        self.shape3d.currentTextChanged.connect(self.updateInputs3D)

        grid = QGridLayout()

        self.label3 = QLabel("Parametro 1")
        self.input3 = QLineEdit()

        self.label4 = QLabel("Parametro 2")
        self.input4 = QLineEdit()

        grid.addWidget(self.label3, 0, 0)
        grid.addWidget(self.input3, 0, 1)
        grid.addWidget(self.label4, 1, 0)
        grid.addWidget(self.input4, 1, 1)

        btn = QPushButton("Calcular")
        btn.clicked.connect(self.calculate3D)

        self.result3d = QLabel("Resultado")

        main_layout.addWidget(self.shape3d)
        main_layout.addLayout(grid)
        main_layout.addWidget(btn)
        main_layout.addWidget(self.result3d)

        main_layout.addStretch()

        widget.setLayout(main_layout)

        self.updateInputs3D(self.shape3d.currentText())

        return widget

    # =========================
    # INPUTS
    # =========================
    def updateInputs2D(self, shape):

        config = {
            "Circulo": ("Radio", None),
            "Cuadrado": ("Lado", None),
            "Triangulo Equilatero": ("Lado", None),
            "Rectangulo": ("Ancho", "Alto"),
            "Triangulo Rectangulo": ("Cateto A", "Cateto B")
        }

        label1, label2 = config.get(shape, ("Parametro 1", "Parametro 2"))

        self.label1.setText(label1)

        if label2:
            self.label2.setText(label2)
            self.label2.show()
            self.input2.show()
        else:
            self.label2.hide()
            self.input2.hide()

    def updateInputs3D(self, shape):

        config = {
            "Esfera": ("Radio", None),
            "Cubo": ("Lado", None),
            "Cilindro": ("Radio", "Altura"),
            "Cono": ("Radio", "Altura"),
            "Piramide": ("Base", "Altura")
        }

        label1, label2 = config.get(shape, ("Parametro 1", "Parametro 2"))

        self.label3.setText(label1)

        if label2:
            self.label4.setText(label2)
            self.label4.show()
            self.input4.show()
        else:
            self.label4.hide()
            self.input4.hide()

    # =========================
    # CONVERSIÓN
    # =========================
    def to_cm(self, value):
        return value * UNIT_FACTORS[self.unitSelector.currentText()]

    def from_cm_area(self, value):
        factor = UNIT_FACTORS[self.unitSelector.currentText()]
        return value / (factor ** 2)

    def from_cm_volume(self, value):
        factor = UNIT_FACTORS[self.unitSelector.currentText()]
        return value / (factor ** 3)

    # =========================
    # CALCULAR
    # =========================
    def calculate2D(self):

        try:
            a = self.to_cm(float(self.input1.text()))
            b = self.to_cm(float(self.input2.text())) if self.input2.isVisible() else 0

            shape = self.shape2d.currentText()

            if shape == "Circulo":
                fig = Circle(a)
            elif shape == "Cuadrado":
                fig = Square(a)
            elif shape == "Rectangulo":
                fig = Rectangle(a, b)
            elif shape == "Triangulo Equilatero":
                fig = EquilateralTriangle(a)
            else:
                fig = RightTriangle(a, b)

            area = self.from_cm_area(fig.area())
            peri = fig.perimeter() / UNIT_FACTORS[self.unitSelector.currentText()]

            unit = self.unitSelector.currentText()

            self.result2d.setText(
                f"Área: {area:.2f} {unit}² | Perímetro: {peri:.2f} {unit}"
            )

        except:
            self.result2d.setText("Entrada inválida")

    def calculate3D(self):

        try:
            a = self.to_cm(float(self.input3.text()))
            b = self.to_cm(float(self.input4.text())) if self.input4.isVisible() else 0

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

            vol = self.from_cm_volume(fig.volume())
            surf = self.from_cm_area(fig.surface())

            unit = self.unitSelector.currentText()

            self.result3d.setText(
                f"Volumen: {vol:.2f} {unit}³ | Superficie: {surf:.2f} {unit}²"
            )

        except:
            self.result3d.setText("Entrada inválida")