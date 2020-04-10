import sys , Mundo
from PyQt5 import uic, QtWidgets
from Mundo import Mundo
qtCreatorFile = "Covid19.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.m1 = Mundo()
        self.m1.insertarContagiado()
        self.m1.insertarContagiado()
        self.m1.insertarContagiado()
        self.inicializarLabels()
        self.NuevoDia.clicked.connect(self.actualizarDatos)

    def inicializarLabels(self):
        self.nDia.setText(str(self.m1.diasTranscurridos))
        self.nDia.setText(str(self.m1.diasTranscurridos))
        self.nPoblacion.setText(str(self.m1.poblacion))
        self.nContagiados.setText(str(self.m1.contagiados))
        self.nCurados.setText(str(self.m1.curados))
        self.nMuertos.setText(str(self.m1.muertos))


    def actualizarDatos(self):
        self.m1.nuevoDia()
        self.nDia.setText(str(self.m1.diasTranscurridos))
        self.nPoblacion.setText(str(self.m1.poblacion))
        self.nContagiados.setText(str(self.m1.contagiados))
        self.nCurados.setText(str(self.m1.curados))
        self.nMuertos.setText(str(self.m1.muertos))


if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())