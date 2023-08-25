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
    def __init__(self, my_object):
        super().__init__()

        self.my_object = my_object

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
   def __init__(self, my_object):
        super().__init__()

        self.stacked_widget = None
        self.my_object = my_object
        loadUi('ui/create_cat.ui', self)
        stacked_widget.currentChanged.connect(self.actualizar_cat)
        # Crear el QTextEdit
        self.inputtext_create_cat = QTextEdit()
        
        self.inputtext_create_cat.textChanged.connect(self.remove_Extra_Spacing)
        #quitar el espacio adicional entre párrafos en el QTextEdit
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
        

   def remove_Extra_Spacing(self):
    # Desconectar temporalmente la señal textChanged
    self.inputtext_create_cat.textChanged.disconnect(self.remove_Extra_Spacing)

    # Cambiar el contenido del QTextEdit
    
    self.inputtext_create_cat.setStyleSheet("margin-bottom: 0px;")
    # Volver a conectar la señal textChanged
    self.inputtext_create_cat.textChanged.connect(self.remove_Extra_Spacing)


   def actualizar_cat(self):
        #obtener y guardar datos
        text = self.inputtext_create_cat.toPlainText()        
        my_object.set_text(text)
        self.inputtext_create_cat.clear()  
        
   def clicked_button_guardar(self):
        #obtener y guardar datos
        text = self.inputtext_create_cat.toPlainText()        
        
        # Abre el archivo en modo escritura
        with open("resources/"+text+".txt", "w") as archivo:
        # Escribe el texto en el archivo
            archivo.write(text)
        self.stacked_widget.setCurrentIndex(3)
        my_object.set_text(text)
        
        
       

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


   
    
class Poo:
    def __init__(self):
        self._text = ''

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value
class MyTextEdit(QtWidgets.QTextEdit):
    def __init__(self, *args, **kwargs):
        super(MyTextEdit, self).__init__(*args, **kwargs)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            # Aquí puedes agregar tu código para manejar el evento de la tecla Enter
            pass
        else:
            super(MyTextEdit, self).keyPressEvent(event)
            
class ListCat(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        loadUi('ui/lista_cat.ui', self)

        myDelegate = CustomItemDelegate(self)
        self.lista_cat.setItemDelegate(myDelegate)
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

class CustomItemDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        size = super().sizeHint(option, index)
        size.setHeight(size.height() + 5)  # Margen inferior de 5 píxeles entre filas
        return size

    def paint(self, painter: QPainter, option, index):
        painter.save()

        # Establece el color de fondo del elemento seleccionado
        if option.state & QStyle.State_Selected:
            brush = self.parent().palette().highlight()
            painter.fillRect(option.rect, brush)
        elif option.state & QStyle.State_MouseOver:
            brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))  # Color de fondo cuando se pasa el mouse
            painter.fillRect(option.rect, brush)
        else:
            painter.fillRect(option.rect, QtGui.QBrush(QtGui.QColor(255, 255, 255)))  # Color de fondo personalizado


         # Dibuja una línea o un borde en la parte inferior del elemento
        bottom_line_rect = option.rect.adjusted(0, option.rect.height() - 1, 0, 0)
        painter.setPen(QPen(Qt.gray, 1))  # Color y grosor del borde
        painter.drawLine(bottom_line_rect.bottomLeft(), bottom_line_rect.bottomRight())
        
        # Establece el estilo del texto
        font = painter.font()
        font.setPointSize(12)  # Tamaño de fuente personalizado
        painter.setFont(font)

        # Establece el color del texto
        pen = painter.pen()
        pen.setColor(Qt.black)  # Color del texto personalizado
        painter.setPen(pen)
        
       

        # Dibuja el texto del elemento
        painter.drawText(option.rect, Qt.AlignLeft, index.data())

        painter.restore()

class ComtenCat(QtWidgets.QDialog):
    def __init__(self, my_object):
        super().__init__()
        self.stacked_widget = None
        self.my_object = my_object

        loadUi('ui/comten_cat.ui', self)
        self.cancelar.clicked.connect(self.button_clicked_cancelar)    
        
       
        # Obtener datos
        value = my_object.get_text()
        self.data_category.setText(value)
        

        stacked_widget.currentChanged.connect(self.actualizar_cat)

    def update_data_category(self, value):
        self.data_category.setText(value)

    def button_clicked_cancelar(self):        
        # Manejar el evento de clic del botón
        #print("Botón presionado")
        self.inputtext_create_cat_2.clear()   
        self.inputtext_create_cat_3.clear() 
        self.stacked_widget.setCurrentIndex(0)  # Cambiar a la página 0 del QStackedWidget

    def actualizar_cat(self):        
        # Obtener datos
        value = my_object.get_text()
        self.data_category.setText(value)
        



    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    stacked_widget = QtWidgets.QStackedWidget()

    my_object = Poo()
    
    main_window = MainWindow(my_object)
    create_cat_window = CreateCat(my_object)
    
   
    search_cat_window = ListCat()
    comten_cat_window = ComtenCat(my_object)
    
    stacked_widget.addWidget(main_window)
    stacked_widget.addWidget(create_cat_window)
    stacked_widget.addWidget(search_cat_window)
    stacked_widget.addWidget(comten_cat_window)

    main_window.stacked_widget = stacked_widget
    create_cat_window.stacked_widget = stacked_widget
    search_cat_window.stacked_widget = stacked_widget
    comten_cat_window.stacked_widget = stacked_widget

    stacked_widget.setCurrentIndex(0)

    stacked_widget.setWindowTitle("ConoBase")
    stacked_widget.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
    icon_path = "images/logo_app.png"
    stacked_widget.setWindowIcon(QtGui.QIcon(icon_path))
    stacked_widget.setFixedSize(400, 400)
    
    windowSize =  stacked_widget.geometry()
    desktopCenter = QtWidgets.QDesktopWidget().availableGeometry().center()
    windowSize.moveCenter(desktopCenter)
    stacked_widget.move(windowSize.topLeft())

    stacked_widget.show()
    sys.exit(app.exec())












