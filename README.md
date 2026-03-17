# Calculadora Geométrica

Aplicación desarrollada en Python con PyQt6 que permite calcular propiedades de figuras geométricas en 2D y 3D.

---

## Características

* Cálculo de figuras 2D:

  * Círculo
  * Cuadrado
  * Rectángulo
  * Triángulo equilátero
  * Triángulo rectángulo

* Cálculo de figuras 3D:

  * Esfera
  * Cubo
  * Cilindro
  * Cono
  * Pirámide

* Selector de unidades:

  * Centímetros (cm)
  * Metros (m)
  * Pulgadas (in)

* Conversión automática de unidades:

  * Área en unidades cuadradas
  * Volumen en unidades cúbicas

---

## Funcionamiento

1. El usuario selecciona una figura.
2. Ingresa los parámetros requeridos.
3. El sistema convierte automáticamente los valores a centímetros (cm) como base interna.
4. Se realizan los cálculos utilizando programación orientada a objetos.
5. El resultado se muestra en la unidad seleccionada.

---

## Estructura del proyecto

```
project/
│
├── ui/
│   └── main_window.py
│
├── shapes/
│   ├── circle.py
│   ├── square.py
│   ├── rectangle.py
│   ├── equilateral_triangle.py
│   ├── right_triangle.py
│   ├── sphere.py
│   ├── cube.py
│   ├── cylinder.py
│   ├── cone.py
│   └── pyramid.py
│
└── main.py
```

---

## Ejecución

Instalar dependencias:

```
pip install PyQt6
```

Ejecutar la aplicación:

```
python main.py
```

---

## Tecnologías utilizadas

* Python
* PyQt6
* Programación Orientada a Objetos

---

## Notas

* La aplicación no incluye visualización gráfica de figuras en esta versión.
* El diseño es modular, lo que facilita su mantenimiento y escalabilidad.

---

## Posibles mejoras

* Implementación de historial de cálculos
* Exportación de resultados
* Mejora de la interfaz de usuario
* Visualización gráfica de figuras

---

## Autor

Andrés Felipe Cortés Zambrano
