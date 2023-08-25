from PyQt5.QtWidgets import *
from PyQt5.QtCore import* 
from PyQt5.QtGui import*
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore,uic
from PyQt5.QtPrintSupport import *
from PyQt5.uic import *
from PyQt5 import QtWidgets, uic
import sys,qdarkstyle

class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()


        loadUi("ui/select_cat.ui", self)         
       
        # Conectar la señal clicked del botón a un método, myButton es la variable asociada al botón
        self.myButton.clicked.connect(self.button_clicked)

        self.animation = QtCore.QPropertyAnimation(self.myButton, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(self.myButton.geometry())
        endValue = self.myButton.geometry()
        endValue.setHeight(endValue.height() - 5)
        endValue.setWidth(endValue.width() - 5)
        self.animation.setEndValue(endValue)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.stop_animation)
        
        
    def button_clicked(self):
        # Iniciar la animación
        self.animation.start()
        # Manejar el evento de clic del botón
        #print("Botón presionado")
        self.stacked_widget.setCurrentIndex(1)  # Cambiar a la página 1 del QStackedWidget

        

    def stop_animation(self):
        # Detener la animación y volver a la posición original
        self.animation.stop()
        self.myButton.setGeometry(self.animation.startValue())

    
class CreateCat(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/create_cat.ui', self)
        self.setWindowTitle("ConoBase")
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        #self.setGeometry(0, 0, 400, 400)
        self.setFixedSize(400, 400)
        # Ruta al archivo de icono
        icon_path = "images/logo_app.png"
        self.setWindowIcon(QtGui.QIcon(icon_path))
        # Conectar la señal clicked del botón a un método, myButton es la variable asociada al botón
        self.cancelar.clicked.connect(self.button_clicked)


    def button_clicked(self):        
        # Manejar el evento de clic del botón
        #print("Botón presionado")
        self.stacked_widget.setCurrentIndex(0)  # Cambiar a la página 0 del QStackedWidget


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    stacked_widget = QtWidgets.QStackedWidget()

    main_window = MainWindow()
    create_cat_window = CreateCat()

    stacked_widget.addWidget(main_window)
    stacked_widget.addWidget(create_cat_window)

    main_window.stacked_widget = stacked_widget
    create_cat_window.stacked_widget = stacked_widget

    stacked_widget.setCurrentIndex(0)  # Mostrar la página 0 inicialmente

    # Cambia el título y las banderas de la ventana del QStackedWidget
    stacked_widget.setWindowTitle("ConoBase")
    stacked_widget.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
    # Ruta al archivo de icono
    icon_path = "images/logo_app.png"
    stacked_widget.setWindowIcon(QtGui.QIcon(icon_path))
    #self.setGeometry(0, 0, 400, 400)
    stacked_widget.setFixedSize(400, 400)
    
    #centrar ventana
    windowSize =  stacked_widget.geometry()
    desktopCenter = QtWidgets.QDesktopWidget().availableGeometry().center()
    windowSize.moveCenter(desktopCenter)
    stacked_widget.move(windowSize.topLeft())


    # Muestra el QStackedWidget en lugar de mostrar directamente la instancia de MainWindow
    stacked_widget.show()
    sys.exit(app.exec())












