import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,QLineEdit)

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Mi primera ventana con PyQt5")
ventana.setGeometry(200,200,600,400)  # tiene cuatro parametros (posicion en el eje x, posicion en el eje y, ancho, alto)

ventana.show()
sys.exit(app.exec_())
