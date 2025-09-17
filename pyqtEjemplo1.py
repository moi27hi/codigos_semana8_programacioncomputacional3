from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QRadioButton, QVBoxLayout,QLineEdit,QSpinBox,QDoubleSpinBox)
import sys

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Mi primera ventana con PyQt5")
ventana.setGeometry(200, 200, 600, 400)  # (x, y, width, height)
boton1 = QPushButton("Haz click aqui")
radio1 = QRadioButton("Opcion 1")
radio2 = QRadioButton("Opcion 2")
radio3 = QRadioButton("Opcion 3")
lineEdit1 = QLineEdit()
spin1 = QSpinBox()
dspin1 = QDoubleSpinBox()

layout = QVBoxLayout()  # Define the layout
layout.addWidget(boton1)
layout.addWidget(radio1)
layout.addWidget(radio2)
layout.addWidget(radio3)
layout.addWidget(lineEdit1)
layout.addWidget(spin1)
layout.addWidget(dspin1)
ventana.setLayout(layout)  # Set the layout on the window

ventana.show()
sys.exit(app.exec_())
