import janelas
import janelas_clientes
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
sys.path.append("imagens")
import img_qrc

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

janelas.widget = widget
janelas_clientes.widget = widget

mainwindow = janelas.Login()
widget.addWidget(mainwindow)
widget.setFixedWidth(981)
widget.setFixedHeight(680)
widget.show()
app.exec_()