from PyQt5.QtWidgets import *
from PyQt5.QtCore import* 
from PyQt5.QtGui import*
from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore,uic
from PyQt5.QtPrintSupport import *
from PyQt5.uic import *
from PyQt5 import QtWidgets, uic
import sys,qdarkstyle,os

class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()


        loadUi("ui/select_cat.ui", self)         
       
        # Conectar la señal clicked del botón a un método, myButton es la variable asociada al botón
        self.myButton.clicked.connect(self.button_clicked_create_cat)
        self.search_cat.clicked.connect(self.button_clicked_search_cat)
      
        
        
    def button_clicked_create_cat(self):
        # Manejar el evento de clic del botón
        #print("Botón presionado")
        self.stacked_widget.setCurrentIndex(1)  # Cambiar a la página 1 del QStackedWidget

    def button_clicked_search_cat(self):
        # Manejar el evento de clic del botón
        #print("Botón presionado")
        self.stacked_widget.setCurrentIndex(2)  # Cambiar a la página 2 del QStackedWidget
          
    
    
class CreateCat(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.stacked_widget = None
        loadUi('ui/create_cat.ui', self)
        
        # Conectar la señal clicked del botón a un método, myButton es la variable asociada al botón
        self.guardar.clicked.connect(self.clicked_button_guardar)
        self.cancelar.clicked.connect(self.button_clicked)
        self.borrar.clicked.connect(self.clicked_button_borrar)

        #animacion
        self.animation = QtCore.QPropertyAnimation(self.borrar, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(self.borrar.geometry())
        endValue = self.borrar.geometry()
        endValue.setHeight(endValue.height() - 2)
        endValue.setWidth(endValue.width() - 2)
        self.animation.setEndValue(endValue)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.stop_animation)

    def clicked_button_guardar(self):
        #obtener y guardar datos
        text = self.inputtext_create_cat.toPlainText()
        
        # Abre el archivo en modo escritura
        with open("resources/"+text+".txt", "w") as archivo:
        # Escribe el texto en el archivo
            archivo.write(text)

       
    def clicked_button_borrar(self):
        
        self.inputtext_create_cat.clear()        
        # Iniciar la animación
        self.animation.start()
        
    def stop_animation(self):
        # Detener la animación y volver a la posición original
        self.animation.stop()
        self.borrar.setGeometry(self.animation.startValue())

    def button_clicked(self):        
        # Manejar el evento de clic del botón
        #print("Botón presionado")
        self.stacked_widget.setCurrentIndex(0)  # Cambiar a la página 0 del QStackedWidget

    

class ListCat(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi('ui/lista_cat.ui', self)
        
        # Conectar la señal clicked del botón a un método, myButton es la variable asociada al botón
        self.back.clicked.connect(self.button_clicked)
        
              

        # Ruta del directorio que contiene los archivos de texto
        directorio = 'resources'

        # Obtén la lista de archivos de texto en el directorio
        archivos_txt = [archivo.name for archivo in os.scandir(directorio) if archivo.is_file() and archivo.name.endswith('.txt')]


        # Leer cada archivo de texto y obtener el contenido en una lista de cadenas
        lineas = []
        for archivo_txt in archivos_txt:
            ruta_archivo = os.path.join(directorio, archivo_txt)
            with open(ruta_archivo, "r") as archivo:
                lineas.extend(archivo.readlines())

        # Crea un modelo de datos y establece los datos
        model = QStringListModel()
        model.setStringList(lineas)

        # Establece el modelo en el QListView
        self.lista_cat.setModel(model)   


        # Conecta la señal currentChanged del QStackedWidget a la función actualizar_lista
        stacked_widget.currentChanged.connect(self.actualizar_lista)


    
        #animacion
        self.animation = QtCore.QPropertyAnimation(self.back, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(self.back.geometry())
        endValue = self.back.geometry()
        endValue.setHeight(endValue.height() - 2)
        endValue.setWidth(endValue.width() - 2)
        self.animation.setEndValue(endValue)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.stop_animation)

    def actualizar_lista(self):
        # Obtén la lista de archivos de texto en el directorio
        directorio = 'resources'
        archivos_txt = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.txt')]

         # Leer cada archivo de texto y obtener el contenido en una lista de cadenas
        lineas = []
        for archivo_txt in archivos_txt:
            ruta_archivo = os.path.join(directorio, archivo_txt)
            with open(ruta_archivo, "r") as archivo:
                lineas.extend(archivo.readlines())

        # Crea un modelo de datos y establece los datos
        model = QStringListModel()
        model.setStringList(lineas)

        # Establece el modelo en el QListView
        self.lista_cat.setModel(model)
        
    def stop_animation(self):
        # Detener la animación y volver a la posición original
        self.animation.stop()
        self.borrar.setGeometry(self.animation.startValue())

    def button_clicked(self):        
        # Manejar el evento de clic del botón
        #print("Botón presionado")
        self.stacked_widget.setCurrentIndex(0)  # Cambiar a la página 0 del QStackedWidget

         
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    stacked_widget = QtWidgets.QStackedWidget()

    main_window = MainWindow()
    create_cat_window = CreateCat()
    search_cat_window = ListCat()

    stacked_widget.addWidget(main_window)
    stacked_widget.addWidget(create_cat_window)
    stacked_widget.addWidget(search_cat_window)

    main_window.stacked_widget = stacked_widget
    create_cat_window.stacked_widget = stacked_widget
    search_cat_window.stacked_widget = stacked_widget

   


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












