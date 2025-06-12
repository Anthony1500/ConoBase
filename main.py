import sys
import os
import re
import time
from datetime import datetime

from PyQt5 import QtWidgets, QtCore, QtGui, QtPrintSupport, uic
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QStyledItemDelegate, QVBoxLayout, QPushButton, QLabel, QDialog, QStackedWidget, QStyle, QHBoxLayout, QStyleFactory, QMessageBox
)
from PyQt5.QtCore import (
    Qt, QTimer, QDate, QDateTime, QStringListModel, QSortFilterProxyModel, QRect, QEvent, QSize
)
from PyQt5.QtGui import (
    QIcon, QFont, QStandardItemModel, QStandardItem, QColor, QPen
)
from PyQt5.QtPrintSupport import (
    QPrinter, QPrintDialog
)
from PyQt5.uic import loadUi
import qdarkstyle


directorio = 'recursos'
archivos_txt = [os.path.splitext(archivo)[0] for archivo in os.listdir(
    directorio) if archivo.endswith('.txt')]
nombres = [nombre.split("_")[1] for nombre in archivos_txt]


def get_current_date_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


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
        # print("Botón presionado")
        # Cambiar a la página 1 del QStackedWidget
        self.stacked_widget.setCurrentIndex(1)

    def button_clicked_search_cat(self):
        # Manejar el evento de clic del botón
        # print("Botón presionado")
        # Cambiar a la página 2 del QStackedWidget
        self.stacked_widget.setCurrentIndex(2)


class CreateCat(QtWidgets.QDialog):
    def __init__(self, my_object):
        super().__init__()

        self.stacked_widget = None
        self.my_object = my_object
        loadUi('ui/create_cat.ui', self)
        stacked_widget.currentChanged.connect(self.actualizar_cat)

        # quitar el espacio adicional entre párrafos en el QTextEdit
        # Conectar la señal clicked del botón a un método, myButton es la variable asociada al botón
        self.guardar.clicked.connect(self.clicked_button_guardar)
        self.cancelar.clicked.connect(self.button_clicked)
        self.borrar.clicked.connect(self.clicked_button_borrar)

       # animacion
        self.animation = QtCore.QPropertyAnimation(self.borrar, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(self.borrar.geometry())
        endValue = self.borrar.geometry()
        endValue.setHeight(endValue.height() - 2)
        endValue.setWidth(endValue.width() - 2)
        self.animation.setEndValue(endValue)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.stop_animation)

    def actualizar_cat(self):
        # obtener y guardar datos
        text = self.inputtext_create_cat.toPlainText()
        my_object.set_text(text)
        self.inputtext_create_cat.clear()

    def clicked_button_guardar(self):
        text = self.inputtext_create_cat.toPlainText()
        if not text.strip():
            # El texto está vacío
            # Crear la ventana emergente aquí
            self.panel = QDialog()
            frame = QtWidgets.QFrame()

            # Establecer el color de fondo del QFrame
            self.panel.setStyleSheet("border: 1px solid red;")
            self.panel.setWindowFlags(Qt.Popup)

            layout = QVBoxLayout(self.panel)
            # Configurar un margen de 0 para el QVBoxLayout
            layout.setContentsMargins(1, 1, 1, 1)
            # Cargar el archivo .ui aquí
            form = uic.loadUi('ui/alert_dialog.ui')
            layout.addWidget(form)

            # Configurar la ventana emergente aquí
            dialog_text = form.dialog_text  # Acceder al  formulario
            dialog_text.setWordWrap(True)
            dialog_text.setText(
                "Error: Por favor, asegúrate de ingresar algún texto.")

            # Acceder al QLabel
            label = form.findChild(QtWidgets.QLabel, "dialog_image")
            # Cargar la imagen en un QPixmap
            pixmap = QtGui.QPixmap('images/cancelar.png')

            # Establecer el QPixmap en el QLabel
            label.setPixmap(pixmap)

            self.panel.setGeometry(form.geometry())

           # Colocar el diálogo en la parte superior de la ventana principal
            desktop = QApplication.desktop()
            main_window = QApplication.activeWindow()  # Obtener la ventana principal
            dialog_rect = self.panel.geometry()

            if main_window is not None:
                x = main_window.frameGeometry().center().x() - dialog_rect.width() / 2
                y = main_window.frameGeometry().top()  # Colocar en la parte superior
                x = int(x)
                y = int(y)
                self.panel.move(x, y)

            # Mostrar la ventana emergente
            self.panel.show()
        else:
            directorio = 'recursos'
            archivos_txt = [os.path.splitext(archivo)[0] for archivo in os.listdir(
                directorio) if archivo.endswith('.txt')]
            nombres = [nombre.split("_")[1] for nombre in archivos_txt]

           # Verificar si el nuevo nombre ya está en la lista
            if text not in nombres:
               # Abre el archivo en modo escritura
                with open("recursos/"+"cat_"+text+".txt", "w") as archivo:
                    # Escribe el texto en el archivo
                    archivo.write(text+"\n"+get_current_date_time())
                self.stacked_widget.setCurrentIndex(3)
                my_object.set_text(text)

            else:
                # El nuevo nombre ya está en la lista, no hacer nada
                # Crear la ventana emergente aquí
                self.panel = QDialog()
                frame = QtWidgets.QFrame()

                # Establecer el color de fondo del QFrame
                self.panel.setStyleSheet("border: 1px solid red;")
                self.panel.setWindowFlags(Qt.Popup)

                layout = QVBoxLayout(self.panel)
                # Configurar un margen de 0 para el QVBoxLayout
                layout.setContentsMargins(1, 1, 1, 1)
                # Cargar el archivo .ui aquí
                form = uic.loadUi('ui/alert_dialog.ui')
                layout.addWidget(form)

                # Configurar la ventana emergente aquí
                dialog_text = form.dialog_text  # Acceder al  formulario
                dialog_text.setWordWrap(True)
                dialog_text.setText("¡Error!: ya existe esa categoría.")

                # Acceder al QLabel
                label = form.findChild(QtWidgets.QLabel, "dialog_image")
                # Cargar la imagen en un QPixmap
                pixmap = QtGui.QPixmap('images/cancelar.png')

                # Establecer el QPixmap en el QLabel
                label.setPixmap(pixmap)

                self.panel.setGeometry(form.geometry())

                # Colocar el diálogo en la parte superior de la ventana principal
                desktop = QApplication.desktop()
                main_window = QApplication.activeWindow()  # Obtener la ventana principal
                dialog_rect = self.panel.geometry()

                if main_window is not None:
                    x = main_window.frameGeometry().center().x() - dialog_rect.width() / 2
                    y = main_window.frameGeometry().top()  # Colocar en la parte superior
                    x = int(x)
                    y = int(y)
                    self.panel.move(x, y)

                # Mostrar la ventana emergente
                self.panel.show()

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
        # print("Botón presionado")
        # Cambiar a la página 0 del QStackedWidget
        self.stacked_widget.setCurrentIndex(0)


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

            pass
        else:
            super(MyTextEdit, self).keyPressEvent(event)


class ListCat(QtWidgets.QDialog):
    def __init__(self, stacked_widget, my_object2, my_object3):
        super().__init__()
        loadUi('ui/lista_cat.ui', self)
        self.stacked_widget = stacked_widget
        self.my_object2 = my_object2
        self.my_object3 = my_object3
        model = QStringListModel()
        # Instala el filtro de eventos en el viewport de la lista y en la ventana principal
        self.lista_cat.viewport().installEventFilter(self)
        self.installEventFilter(self)
        self.lista_cat.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

        # Conectar la señal clicked del botón a un método, myButton es la variable asociada al botón
        self.back.clicked.connect(self.button_clicked)
        self.inputtext_search_cat.textChanged.connect(self.handle_search)

        directorio = 'recursos'
        archivos_txt = [os.path.splitext(archivo)[0] for archivo in os.listdir(
            directorio) if archivo.endswith('.txt')]
        nombres = [nombre.split("_")[1] for nombre in archivos_txt]

        model = QStandardItemModel()
        for archivo in archivos_txt:
            nombre = archivo.split("_")[1]
            with open(os.path.join(directorio, archivo+".txt"), 'r') as f:
                lines = f.readlines()
                if len(lines) >= 2:
                    fecha_hora = lines[1].strip()
                else:
                    fecha_hora = "Fecha desconocida"  # O algún valor por defecto

                # item = QStandardItem(f'Archivo: {nombre}\nFecha y hora: {fecha_hora}')
                item = QStandardItem(f'{nombre}\n{fecha_hora}')
                gray_color = QColor(128, 128, 128)
                item.setForeground(gray_color)
                model.appendRow(item)

        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(model)
        myDelegate = CustomItemDelegate(
            self.stacked_widget, self.my_object2, self.my_object3)
        self.lista_cat.setItemDelegate(myDelegate)
        self.lista_cat.setModel(self.proxy_model)

        # Conecta la señal currentChanged del QStackedWidget a la función actualizar_lista
        self.stacked_widget.currentChanged.connect(self.actualizar_lista)

        # animacion
        self.animation = QtCore.QPropertyAnimation(self.back, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(self.back.geometry())
        endValue = self.back.geometry()
        endValue.setHeight(endValue.height() - 2)
        endValue.setWidth(endValue.width() - 2)
        self.animation.setEndValue(endValue)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.stop_animation)

    def handle_search(self):

        text = self.inputtext_search_cat.toPlainText()

        # Set the filter regexp of the model to match the search text
        self.proxy_model.setFilterRegExp(text)
        if len(text) > 24:
            self.inputtext_search_cat.setPlainText(text[:24])

    def eventFilter(self, obj, event):
        if obj == self or obj == self.lista_cat.viewport():
            if event.type() == QEvent.MouseButtonPress:
                self.lista_cat.clearSelection()
        return super().eventFilter(obj, event)

    def actualizar_lista(self):
        """
        # Obtén la lista de archivos de texto en el directorio
        directorio = 'recursos'
        archivos_txt = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.txt')]

         # Leer cada archivo de texto y obtener el contenido en una lista de cadenas
        lineas = []
        for archivo_txt in archivos_txt:
            ruta_archivo = os.path.join(directorio, archivo_txt)
            with open(ruta_archivo, "r") as archivo:
                lineas.extend(archivo.readlines())
        """
        self.inputtext_search_cat.textChanged.connect(self.handle_search)

        directorio = 'recursos'
        archivos_txt = [os.path.splitext(archivo)[0] for archivo in os.listdir(
            directorio) if archivo.endswith('.txt')]
        nombres = [nombre.split("_")[1] for nombre in archivos_txt]

        model = QStandardItemModel()
        for archivo in archivos_txt:
            nombre = archivo.split("_")[1]
            with open(os.path.join(directorio, archivo+".txt"), 'r') as f:
                lines = f.readlines()
                if len(lines) >= 2:
                    fecha_hora = lines[1].strip()
                else:
                    fecha_hora = "Fecha desconocida"  # O algún valor por defecto

                item = QStandardItem(f'{nombre}\n{fecha_hora}')
                # Cambiar el color de la letra para la fecha y hora
                gray_color = QColor(128, 128, 128)
                item.setForeground(gray_color)
                model.appendRow(item)

        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(model)
        myDelegate = CustomItemDelegate(
            self.stacked_widget, self.my_object2, self.my_object3)
        self.lista_cat.setItemDelegate(myDelegate)
        self.lista_cat.setModel(self.proxy_model)

    def stop_animation(self):
        # Detener la animación y volver a la posición original
        self.animation.stop()
        self.borrar.setGeometry(self.animation.startValue())

    def button_clicked(self):
        # Manejar el evento de clic del botón
        # print("Botón presionado")
        self.inputtext_search_cat.clear()
        # Cambiar a la página 0 del QStackedWidget
        self.stacked_widget.setCurrentIndex(0)


class ListsubCat(QtWidgets.QDialog):
    def __init__(self, stacked_widget, my_object2, my_object3):
        super().__init__()
        loadUi('ui/lista_subcat.ui', self)
        self.stacked_widget = stacked_widget
        self.my_object2 = my_object2
        self.my_object3 = my_object3
        model = QStringListModel()
        # Instala el filtro de eventos en el viewport de la lista y en la ventana principal
        self.lista_subcat.viewport().installEventFilter(self)
        self.installEventFilter(self)
        self.lista_subcat.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.back_2.clicked.connect(self.button_clicked_nuevo)

        # Conectar la señal clicked del botón a un método, myButton es la variable asociada al botón
        self.back.clicked.connect(self.button_clicked)
        self.inputtext_search_subcat.textChanged.connect(self.handle_search)

        # Conecta la señal currentChanged del QStackedWidget a la función actualizar_lista
        stacked_widget.currentChanged.connect(self.actualizar_lista)

        # animacion
        self.animation = QtCore.QPropertyAnimation(self.back, b"geometry")
        self.animation.setDuration(500)
        self.animation.setStartValue(self.back.geometry())
        endValue = self.back.geometry()
        endValue.setHeight(endValue.height() - 2)
        endValue.setWidth(endValue.width() - 2)
        self.animation.setEndValue(endValue)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuad)
        self.animation.finished.connect(self.stop_animation)

    def handle_search(self):

        text = self.inputtext_search_subcat.toPlainText()

        # Set the filter regexp of the model to match the search text
        self.proxy_model.setFilterRegExp(text)
        if len(text) > 24:
            self.inputtext_search_subcat.setPlainText(text[:24])

    def button_clicked_nuevo(self):
        text = self.my_object3.get_text()
        self.inputtext_search_subcat.clear()
        # Cambiar a la página 0 del QStackedWidget
        self.stacked_widget.setCurrentIndex(5)

    def get_data(self):
        data = self.my_object2.get_text()
        return data

    def eventFilter(self, obj, event):
        if obj == self or obj == self.lista_subcat.viewport():
            if event.type() == QEvent.MouseButtonPress:
                self.lista_subcat.clearSelection()
        return super().eventFilter(obj, event)

    def actualizar_lista(self):
        """
        # Obtén la lista de archivos de texto en el directorio
        directorio = 'recursos'
        archivos_txt = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.txt')]

         # Leer cada archivo de texto y obtener el contenido en una lista de cadenas
        lineas = []
        for archivo_txt in archivos_txt:
            ruta_archivo = os.path.join(directorio, archivo_txt)
            with open(ruta_archivo, "r") as archivo:
                lineas.extend(archivo.readlines())
        """
        self.inputtext_search_subcat.textChanged.connect(self.handle_search)
        model = QStandardItemModel()

        # Crear un modelo vacío para la lista
        model = QStandardItemModel()
        self.lista_subcat.setModel(model)

        # Crear un proxy model y un delegado de elementos para la lista
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(model)
        my_stacked_widget = QStackedWidget()  # Crear una instancia de QStackedWidget
        myDelegate = CustomItemDelegatesubcat(
            my_stacked_widget, my_object2)  # Crear una instancia de
        self.lista_subcat.setItemDelegate(myDelegate)
        self.lista_subcat.setModel(self.proxy_model)

        # Crear un QTimer
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)  # Establecer el intervalo en milisegundos
        # Conectar la señal timeout a la función update_data
        self.timer.timeout.connect(self.update_data)
        self.timer.start()  # Iniciar el QTimer

    def stop_animation(self):
        # Detener la animación y volver a la posición original
        self.animation.stop()
        self.borrar.setGeometry(self.animation.startValue())

    def button_clicked(self):
        # Manejar el evento de clic del botón
        # print("Botón presionado")
        self.my_object2.set_text('')
        self.subcat_cat_text.clear()
        self.inputtext_search_subcat.clear()
        # Cambiar a la página 0 del QStackedWidget
        self.stacked_widget.setCurrentIndex(2)

    def update_data(self):
        model = QStandardItemModel()
        model = self.lista_subcat.model()
        proxy_model = self.lista_subcat.model()
        # Obtener el modelo fuente del modelo proxy
        model = proxy_model.sourceModel()
        # Limpiar el modelo para eliminar los elementos existentes
        # model.clear()
        datos = self.get_data()
        if datos != '':
            self.subcat_cat_text.setText(datos)
            file_name = 'recursos/cat_'+datos+'.txt'
            with open(file_name, 'r') as f:
                text = f.read()
                pattern = r'(?<=\*{100}\n)(.+)\n(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\n'
                matches = re.findall(pattern, text)
                for match in matches:
                    title = match[0]
                    date_time = match[1]
                    item_text = f'{title}\n{date_time}'

                    # Buscar ítems existentes con el mismo texto
                    existing_items = model.findItems(item_text)

                    # Si no se encontraron ítems existentes, agregar un nuevo ítem al modelo
                    if len(existing_items) == 0:
                        item = QStandardItem(item_text)
                        gray_color = QColor(128, 128, 128)
                        item.setForeground(gray_color)
                        model.appendRow(item)


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Establecer el tamaño fijo de la ventana
        self.setFixedSize(500, 100)  # 500 -alto  y 400 -ancho.

        # Quitar el signo de interrogación
        self.setWindowFlags(self.windowFlags() & ~
                            Qt.WindowContextHelpButtonHint)

        self.setStyleSheet("""
            QDialog { 
                background-color: #f5f5f5; 
                font-family: 'Roboto', sans-serif;
            }
            QPushButton {
                border: 1px solid #8f8f91;
                border-radius: 4px;
                background-color: #f1f1f2;
                min-width: 80px;
                padding: 5px;
            }
            QPushButton:hover {
                border: 1px solid #5e5e5e;
                background-color: #e7e7e8;
            }
            QPushButton:pressed {
                background-color: #d7d7d8;
            }
            
        """)  # Estilos CSS para el diálogo y los botones

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 20, 20)  # Márgenes

        self.label = QLabel("Etiqueta del diálogo")
        self.label.setFont(QFont("Roboto", 10))  # Fuente moderna
        self.label.setWordWrap(True)  # Habilitar el ajuste de línea
        self.label.adjustSize()  # Ajustar el tamaño al contenido

        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(8)  # Espaciado entre botones
        self.yes_button = QPushButton("Sí")
        # Botón de acción con fondo verde y texto blanco, con sombra
        self.yes_button.setStyleSheet(
            "QPushButton { background-color: #D3D3D3; color: #000000; border-radius: 5px; } QPushButton:hover { background-color: #66BB6A; color: #FFFFFF; }")
        self.yes_button.setFixedWidth(80)
        self.no_button = QPushButton("No")
        # Botón secundario con fondo gris
        self.no_button.setStyleSheet(
            "QPushButton { background-color: #D3D3D3; color: #000000; border-radius: 5px; } QPushButton:hover { background-color: #e18484; color: #FFFFFF; }")
        self.no_button.setFixedWidth(80)

        self.button_layout.addWidget(self.yes_button)
        self.button_layout.addWidget(self.no_button)
        self.yes_button.clicked.connect(self.accept)
        self.no_button.clicked.connect(self.reject)

        self.layout.addWidget(self.label)
        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

        self.setStyle(QStyleFactory.create('Fusion'))  # Estilo moderno

    def question(self, title, question):
        self.setWindowTitle(title)
        self.label.setText(question)
        return self.exec_()


class CustomItemDelegate(QStyledItemDelegate):
    def __init__(self, stacked_widget, my_object2, my_object3, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stacked_widget = stacked_widget
        self.my_object2 = my_object2
        self.my_object3 = my_object3
        self.panel = None
        self.button_rect_trash = QRect()
        self.button_rect_right = QRect()

    def editorEvent(self, event, model, option, index):
        # Obtener el nombre del archivo a eliminar
        respuesta = None
        # Crear una instancia de QMessageBox
        messagebox = CustomDialog(self.parent())
        nombre_archivo = model.data(index, Qt.DisplayRole).split('\n')[0]
        if event.type() == QEvent.MouseButtonRelease:
            if self.button_rect_trash.contains(event.pos()):

                # Configurar el icono antes de mostrar el cuadro de diálogo
                messagebox.setWindowIcon(QIcon('images/trash.png'))

                # Mostrar un cuadro de diálogo preguntando al usuario si desea eliminar el archivo
                respuesta = messagebox.question(
                    "Eliminar archivo", f"¿Estás seguro de que deseas eliminar la categoría: <b>{nombre_archivo}</b> con sus entradas?")

                # Si el usuario acepta, eliminar el archivo
            if respuesta == QDialog.Accepted:
                # Construir la ruta del archivo
                directorio = 'recursos'
                ruta_archivo = os.path.join(
                    directorio, "cat_"+nombre_archivo+".txt")

                # Eliminar el archivo
                os.remove(ruta_archivo)

                # Actualizar el modelo y la vista
                model.removeRow(index.row())
                topLeft = model.index(0, 0)
                bottomRight = model.index(model.rowCount() - 1, 0)
                model.dataChanged.emit(topLeft, bottomRight)

                self.panel = QDialog()
                frame = QtWidgets.QFrame()

                # Establecer el color de fondo del QFrame
                self.panel.setStyleSheet("border: 1px solid green;")
                self.panel.setWindowFlags(Qt.Popup)

                layout = QVBoxLayout(self.panel)
                # Configurar un margen de 0 para el QVBoxLayout
                layout.setContentsMargins(1, 1, 1, 1)
                # Cargar el archivo .ui aquí
                form = uic.loadUi('ui/alert_dialog.ui')
                layout.addWidget(form)

                # Configurar la ventana emergente aquí
                dialog_text = form.dialog_text  # Acceder al  formulario
                dialog_text.setWordWrap(True)
                dialog_text.setText(
                    "¡Éxito! La categoría seleccionada ha sido eliminada correctamente.")

                # Acceder al QLabel
                label = form.findChild(QtWidgets.QLabel, "dialog_image")
                # Cargar la imagen en un QPixmap
                pixmap = QtGui.QPixmap('images/correct.png')

                # Establecer el QPixmap en el QLabel
                label.setPixmap(pixmap)
                self.panel.setGeometry(form.geometry())
                # Colocar el diálogo en la parte superior de la ventana principal
                desktop = QApplication.desktop()
                main_window = QApplication.activeWindow()  # Obtener la ventana principal
                dialog_rect = self.panel.geometry()

                if main_window is not None:
                    x = main_window.frameGeometry().center().x() - dialog_rect.width() / 2
                    y = main_window.frameGeometry().top()  # Colocar en la parte superior
                    x = int(x)
                    y = int(y)
                    self.panel.move(x, y)

                    # Mostrar la ventana emergente
                self.panel.show()

            elif self.button_rect_right.contains(event.pos()):
                # Cambiar a la página 4 del QStackedWidget
                self.stacked_widget.setCurrentIndex(4)
                data = index.data().split('\n')[0]
                text_cat = index.data()
                self.my_object2.set_text(data)
                self.my_object3.set_text(text_cat)

        else:

            if event.type() == QEvent.MouseButtonPress:
                item_rect = option.rect
                item_center = item_rect.center()

                # Verifica si el clic está en la mitad izquierda del ítem
                if event.pos().x() < item_center.x():
                    # Realiza las acciones deseadas para la mitad izquierda del ítem
                    # ...

                    data = index.data().split('\n')[0]

                    # Crear la ventana emergente aquí
                    self.panel = QDialog()
                    self.panel.setWindowFlags(Qt.Popup)

                    layout = QVBoxLayout(self.panel)
                    # Configurar un margen de 0 para el QVBoxLayout
                    layout.setContentsMargins(1, 1, 1, 1)
                    # Cargar el archivo .ui aquí
                    form = uic.loadUi('ui/list_cat_dialog.ui')
                    layout.addWidget(form)
                    # Configurar la ventana emergente aquí
                    cat_title = form.cat_title
                    cat_data = form.cat_data
                    cat_number = form.cat_number  # Acceder al  formulario
                    cat_data.setText(data)
                    cat_title.setText('Categoría: ')
                    with open("recursos/cat_"+data+".txt", 'r') as file:
                        lines = file.readlines()
                        num_boxes = 0
                        in_box = False
                        for line in lines:
                            if line.startswith('****'):
                                if not in_box:
                                    in_box = True
                                else:
                                    in_box = False
                                    num_boxes += 1
                    if num_boxes > 1:
                        cat_number.setText(str(num_boxes)+" entradas")
                    else:
                        cat_number.setText(str(num_boxes)+" entrada")

                    self.panel.setGeometry(form.geometry())

                    # Colocar el diálogo en la parte superior de la ventana principal
                    desktop = QApplication.desktop()
                    main_window = QApplication.activeWindow()  # Obtener la ventana principal
                    dialog_rect = self.panel.geometry()

                    if main_window is not None:
                        x = main_window.frameGeometry().center().x() - dialog_rect.width() / 2
                        y = main_window.frameGeometry().top()  # Colocar en la parte superior
                        x = int(x)
                        y = int(y)
                        self.panel.move(x, y)

                    # Mostrar la ventana emergente
                    self.panel.show()

                # Retorna False para evitar que se procese la selección
                return False

        return super().editorEvent(event, model, option, index)

    def sizeHint(self, option, index):
        size = super().sizeHint(option, index)
        # Margen inferior de 10 píxeles entre filas
        size.setHeight(size.height() + 9)
        size.setWidth(size.width() + 20)
        return size

    def paint(self, painter, option, index):
        option.rect.adjust(8, 1, 0, 0)
        painter.save()

        # Establecer el ícono en el método paint
        icon_path_back = "images/background_list.png"
        icon_path_font = "images/trash.png"
        icon_path_arrow = "images/flecha_right.png"
        self.icon = QtGui.QIcon(icon_path_font)
        self.icon1 = QtGui.QIcon(icon_path_back)
        self.icon2 = QtGui.QIcon(icon_path_arrow)

        super(CustomItemDelegate, self).paint(painter, option, index)
        rect = option.rect
        iconSize = QtCore.QSize(140, 707)
        iconRect1 = QtCore.QRect(int(rect.right() - iconSize.width()),
                                 # background
                                 int(rect.top() + (rect.height() -
                                     iconSize.height()) / 2),
                                 int(iconSize.width()), int(iconSize.height()))
        rect = option.rect
        button_size_trash = QSize(21, 21)
        self.button_rect_trash = QtCore.QRect(int(rect.right() - button_size_trash.width() - 79),
                                              # button trash
                                              int(rect.top() + (rect.height() -
                                                  button_size_trash.height()) / 2),
                                              int(button_size_trash.width()), int(button_size_trash.height()))
        rect = option.rect
        button_size_right = QSize(21, 21)
        self.button_rect_right = QtCore.QRect(int(rect.right() - button_size_right.width() - 4),
                                              # button arrow right
                                              int(rect.top() + (rect.height() -
                                                  button_size_right.height()) / 2),
                                              int(button_size_right.width()), int(button_size_right.height()))

        selection_rect = option.rect
        # Establece el color de fondo del elemento seleccionado
        if option.state & QStyle.State_Selected:
            brush = QtGui.QBrush(QtGui.QColor(250, 204, 247))  # Color de fondo
            # Limitar la anchura de la selección
            selection_rect.setWidth(226 if len(nombres) > 6 else 240)
            painter.fillRect(selection_rect, brush)
        elif option.state & QStyle.State_MouseOver:
            # Color de fondo cuando se pasa el mouse
            brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
            # Limitar la anchura de la selección
            selection_rect.setWidth(226 if len(nombres) > 6 else 240)
            painter.fillRect(selection_rect, brush)
        else:
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            # Limitar la anchura de la selección
            selection_rect.setWidth(226 if len(nombres) > 6 else 240)
            # Color de fondo personalizado
            painter.fillRect(selection_rect, brush)

           # Dibuja una línea o un borde en la parte inferior del elemento
        bottom_line_rect = option.rect.adjusted(
            0, option.rect.height() - 1, 0, 0)
        painter.setPen(QPen(Qt.gray, 1))  # Color y grosor del borde
        painter.drawLine(bottom_line_rect.bottomLeft(),
                         bottom_line_rect.bottomRight())

        # Establece el estilo del texto
        font = painter.font()
        font.setPointSize(11)  # Tamaño de fuente personalizado
        painter.setFont(font)

        # Establece el color del texto
        pen = painter.pen()
        pen.setColor(Qt.black)  # Color del texto personalizado
        painter.setPen(pen)

        # Dibuja el ícono

        self.icon1.paint(painter, iconRect1, QtCore.Qt.AlignCenter)
        painter.drawPixmap(self.button_rect_trash,
                           self.icon.pixmap(button_size_trash))
        painter.drawPixmap(self.button_rect_right,
                           self.icon2.pixmap(button_size_right))

        # Define el rectángulo dentro del cual se dibujará el texto
        textRect = QtCore.QRect(option.rect.left(), option.rect.top(
        ), option.rect.width() - 50, option.rect.height())

        # Dibuja el texto dentro del rectángulo
        painter.drawText(textRect, Qt.AlignLeft, index.data())

        painter.restore()


class CustomItemDelegatesubcat(QStyledItemDelegate):
    def __init__(self, stacked_widget, my_object3, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stacked_widget = stacked_widget
        self.my_object3 = my_object3
        self.panel = None
        self.button_rect_trash = QRect()
        self.button_rect_right = QRect()

    def editorEvent(self, event, model, option, index):
        # Obtener el nombre del archivo a eliminar
        respuesta = None
        nombre_archivo = model.data(index, Qt.DisplayRole).split('\n')[0]
        if event.type() == QEvent.MouseButtonRelease:
            if self.button_rect_trash.contains(event.pos()):

                # Mostrar un cuadro de diálogo preguntando al usuario si desea eliminar el archivo
                respuesta = QMessageBox.question(self.parent(
                ), "Eliminar archivo", f"¿Estás seguro de que deseas eliminar esta entrada: <b>{nombre_archivo}</b>?")

            # Si el usuario acepta, eliminar el archivo
            if respuesta == QMessageBox.Yes:
                # Construir la ruta del archivo
                text = self.my_object3.get_text().split('\n')[0]
                file_name = "recursos/cat_"+text+".txt"
                title = model.data(index, Qt.DisplayRole).split('\n')[0]
                date = model.data(index, Qt.DisplayRole).split('\n')[1]
                self.remove_content(file_name, title, date)

                # Actualizar el modelo y la vista
                model.removeRow(index.row())
                topLeft = model.index(0, 0)
                bottomRight = model.index(model.rowCount() - 1, 0)
                model.dataChanged.emit(topLeft, bottomRight)

                self.panel = QDialog()
                frame = QtWidgets.QFrame()

                # Establecer el color de fondo del QFrame
                self.panel.setStyleSheet("border: 1px solid green;")
                self.panel.setWindowFlags(Qt.Popup)

                layout = QVBoxLayout(self.panel)
                # Configurar un margen de 0 para el QVBoxLayout
                layout.setContentsMargins(1, 1, 1, 1)
                # Cargar el archivo .ui aquí
                form = uic.loadUi('ui/alert_dialog.ui')
                layout.addWidget(form)

                # Configurar la ventana emergente aquí
                dialog_text = form.dialog_text  # Acceder al  formulario
                dialog_text.setWordWrap(True)
                dialog_text.setText(
                    "¡Éxito! La entrada seleccionada ha sido eliminada correctamente.")

                # Acceder al QLabel
                label = form.findChild(QtWidgets.QLabel, "dialog_image")
                # Cargar la imagen en un QPixmap
                pixmap = QtGui.QPixmap('images/correct.png')

                # Establecer el QPixmap en el QLabel
                label.setPixmap(pixmap)
                self.panel.setGeometry(form.geometry())
                # Colocar el diálogo en la parte superior de la ventana principal
                desktop = QApplication.desktop()
                main_window = QApplication.activeWindow()  # Obtener la ventana principal
                dialog_rect = self.panel.geometry()

                if main_window is not None:
                    x = main_window.frameGeometry().center().x() - dialog_rect.width() / 2
                    y = main_window.frameGeometry().top()  # Colocar en la parte superior
                    x = int(x)
                    y = int(y)
                    self.panel.move(x, y)

                    # Mostrar la ventana emergente
                self.panel.show()

            elif self.button_rect_right.contains(event.pos()):
                self.get_data()
                print(self.get_data())
        else:

            if event.type() == QEvent.MouseButtonPress:
                item_rect = option.rect
                item_center = item_rect.center()

                # Verifica si el clic está en la mitad izquierda del ítem
                if event.pos().x() < item_center.x():
                    # Realiza las acciones deseadas para la mitad izquierda del ítem
                    # ...

                    data = index.data().split('\n')[0]
                    datahour = index.data().split('\n')[1]

                    # Crear la ventana emergente aquí
                    self.panel = QDialog()
                    # Establecer el color de fondo del QFrame
                    self.panel.setStyleSheet("border: 1px solid black;")
                    self.panel.setWindowFlags(Qt.Popup)
                    # Establecer el estilo de la ventana emergente para redondear las esquinas

                    layout = QVBoxLayout(self.panel)
                    # Configurar un margen de 0 para el QVBoxLayout
                    layout.setContentsMargins(1, 1, 1, 1)
                    # Cargar el archivo .ui aquí
                    form = uic.loadUi('ui/list_subcat_dialog.ui')
                    layout.addWidget(form)
                    # Configurar la ventana emergente aquí
                    cat_name = form.cat_name
                    text_contem = form.text_contem
                    text_title_sub = form.text_title_sub
                    back = form.back
                    text_date_hour = form.text_date_hour  # Acceder al  formulario
                    text_ca = self.get_data()
                    cat_name.setText(text_ca)
                    text_title_sub.setText(data)
                    text_date_hour.setText(datahour)
                    # contenido
                    file_name = 'recursos/cat_'+text_ca+'.txt'
                    title = data
                    date = datahour
                    content = self.find_content(file_name, title, date)
                    text_contem.setText(content)

                    # cerrar ventana
                    back.clicked.connect(self.panel.close)

                    self.panel.setGeometry(form.geometry())

                    # Colocar el diálogo en la parte superior de la ventana principal
                    desktop = QApplication.desktop()
                    main_window = QApplication.activeWindow()  # Obtener la ventana principal
                    dialog_rect = self.panel.geometry()

                    if main_window is not None:
                        x = main_window.frameGeometry().right() + 9
                        y = main_window.frameGeometry().top()  # Colocar en la parte superior
                        x = int(x)
                        y = int(y)
                        self.panel.move(x, y)

                        # Verificar si la ventana secundaria se oculta detrás del borde de la pantalla
                        screen_rect = desktop.availableGeometry(self.panel)
                        if self.panel.frameGeometry().right() > screen_rect.right():
                            x = main_window.frameGeometry().left() - self.panel.frameGeometry().width() - 9
                            self.panel.move(x, y)

                            # Mostrar la ventana emergente
                    self.panel.show()

                # Retorna False para evitar que se procese la selección
                return False

        return super().editorEvent(event, model, option, index)

    def get_data(self):
        data = self.my_object3.get_text()
        return data

    def remove_content(self, filename, title, date):
        # Crea una expresión regular para buscar el bloque que deseas eliminar
        regex = r"\n\*+\n" + re.escape(title) + \
            r"\n" + re.escape(date) + r"\n.*?\n\*+\n"
        # Abre el archivo y lee su contenido
        with open(filename, "r") as f:
            content = f.read()
        # Busca y elimina el bloque especificado utilizando la expresión regular
        new_content = re.sub(regex, "", content, flags=re.DOTALL)
        # Escribe el contenido modificado en el archivo
        with open(filename, "w") as f:
            f.write(new_content)

    def find_content(self, file_name, title, date):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.strip() == title and lines[i+1].strip() == date:
                    # Encontramos la entrada del título y la fecha
                    content = []
                    for j in range(i+3, len(lines)):
                        if lines[j].startswith('*'):
                            # Encontramos el separador de asteriscos
                            break
                        content.append(lines[j])
                    return ''.join(content)
        return None

    def sizeHint(self, option, index):
        size = super().sizeHint(option, index)
        # Margen inferior de 10 píxeles entre filas
        size.setHeight(size.height() + 9)
        size.setWidth(size.width() + 20)
        return size

    def handle_button_click(self):
        print("hola")

    def paint(self, painter, option, index):
        option.rect.adjust(8, 1, 0, 0)
        painter.save()

        # Establecer el ícono en el método paint
        icon_path_back = "images/background_list.png"
        icon_path_font = "images/trash.png"
        icon_path_arrow = "images/flecha_right.png"
        self.icon = QtGui.QIcon(icon_path_font)
        self.icon1 = QtGui.QIcon(icon_path_back)
        self.icon2 = QtGui.QIcon(icon_path_arrow)

        super(CustomItemDelegatesubcat, self).paint(painter, option, index)
        rect = option.rect
        iconSize = QtCore.QSize(140, 707)
        iconRect1 = QtCore.QRect(int(rect.right() - iconSize.width()),
                                 # background
                                 int(rect.top() + (rect.height() -
                                     iconSize.height()) / 2),
                                 int(iconSize.width()), int(iconSize.height()))
        rect = option.rect
        button_size_trash = QSize(21, 21)
        self.button_rect_trash = QtCore.QRect(int(rect.right() - button_size_trash.width() - 48),
                                              # button trash
                                              int(rect.top() + (rect.height() -
                                                  button_size_trash.height()) / 2),
                                              int(button_size_trash.width()), int(button_size_trash.height()))

        selection_rect = option.rect
        # Establece el color de fondo del elemento seleccionado
        if option.state & QStyle.State_Selected:
            brush = QtGui.QBrush(QtGui.QColor(250, 204, 247))  # Color de fondo
            # Limitar la anchura de la selección
            selection_rect.setWidth(226 if len(nombres) > 6 else 240)
            painter.fillRect(selection_rect, brush)
        elif option.state & QStyle.State_MouseOver:
            # Color de fondo cuando se pasa el mouse
            brush = QtGui.QBrush(QtGui.QColor(220, 220, 220))
            # Limitar la anchura de la selección
            selection_rect.setWidth(226 if len(nombres) > 6 else 240)
            painter.fillRect(selection_rect, brush)
        else:
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            # Limitar la anchura de la selección
            selection_rect.setWidth(226 if len(nombres) > 6 else 240)
            # Color de fondo personalizado
            painter.fillRect(selection_rect, brush)

           # Dibuja una línea o un borde en la parte inferior del elemento
        bottom_line_rect = option.rect.adjusted(
            0, option.rect.height() - 1, 0, 0)
        painter.setPen(QPen(Qt.gray, 1))  # Color y grosor del borde
        painter.drawLine(bottom_line_rect.bottomLeft(),
                         bottom_line_rect.bottomRight())

        # Establece el estilo del texto
        font = painter.font()
        font.setPointSize(11)  # Tamaño de fuente personalizado
        painter.setFont(font)

        # Establece el color del texto
        pen = painter.pen()
        pen.setColor(Qt.black)  # Color del texto personalizado
        painter.setPen(pen)

        # Dibuja el ícono

        self.icon1.paint(painter, iconRect1, QtCore.Qt.AlignCenter)
        painter.drawPixmap(self.button_rect_trash,
                           self.icon.pixmap(button_size_trash))
        # painter.drawPixmap(self.button_rect_right, self.icon2.pixmap(button_size_right))
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
        self.guardar.clicked.connect(self.button_clicked_guardar)

        # Obtener datos
        value = my_object.get_text()
        self.data_category.setText(value)

        stacked_widget.currentChanged.connect(self.actualizar_cat)

    def update_data_category(self, value):
        self.data_category.setText(value)

    def button_clicked_guardar(self):
        text = self.inputtext_create_cat_2.toPlainText()
        text1 = self.inputtext_create_cat_3.toPlainText()

        if not text.strip() and not text1.strip():
            # El texto está vacío
            # Crear la ventana emergente aquí

            self.panel = QDialog()
            frame = QtWidgets.QFrame()
            # Establecer el color de fondo del QFrame
            self.panel.setStyleSheet("border: 1px solid red;")
            self.panel.setWindowFlags(Qt.Popup)

            layout = QVBoxLayout(self.panel)
            # Configurar un margen de 0 para el QVBoxLayout
            layout.setContentsMargins(1, 1, 1, 1)
            # Cargar el archivo .ui aquí
            form = uic.loadUi('ui/alert_dialog.ui')
            layout.addWidget(form)

            # Configurar la ventana emergente aquí
            dialog_text = form.dialog_text  # Acceder al  formulario
            dialog_text.setWordWrap(True)
            dialog_text.setText(
                "Error: Por favor, asegúrate de ingresar algún texto en los campos.")

            # Acceder al QLabel
            label = form.findChild(QtWidgets.QLabel, "dialog_image")
            # Cargar la imagen en un QPixmap
            pixmap = QtGui.QPixmap('images/cancelar.png')

            # Establecer el QPixmap en el QLabel
            label.setPixmap(pixmap)
            self.panel.setGeometry(form.geometry())
            # Colocar el diálogo en la parte superior de la ventana principal
            desktop = QApplication.desktop()
            main_window = QApplication.activeWindow()  # Obtener la ventana principal
            dialog_rect = self.panel.geometry()

            if main_window is not None:
                x = main_window.frameGeometry().center().x() - dialog_rect.width() / 2
                y = main_window.frameGeometry().top()  # Colocar en la parte superior
                x = int(x)
                y = int(y)
                self.panel.move(x, y)

            # Mostrar la ventana emergente
            self.panel.show()
        else:
            if text == my_object.get_text():
              # El texto está vacío
              # Crear la ventana emergente aquí

                self.panel = QDialog()
                frame = QtWidgets.QFrame()

                # Establecer el color de fondo del QFrame
                self.panel.setStyleSheet("border: 1px solid red;")
                self.panel.setWindowFlags(Qt.Popup)

                layout = QVBoxLayout(self.panel)
                # Configurar un margen de 0 para el QVBoxLayout
                layout.setContentsMargins(1, 1, 1, 1)
                # Cargar el archivo .ui aquí
                form = uic.loadUi('ui/alert_dialog.ui')
                layout.addWidget(form)

                # Configurar la ventana emergente aquí
                dialog_text = form.dialog_text  # Acceder al  formulario
                dialog_text.setWordWrap(True)
                dialog_text.setText(
                    "Error: Por favor, asegúrate de ingresar algún texto diferente a la categoría.")

                # Acceder al QLabel
                label = form.findChild(QtWidgets.QLabel, "dialog_image")
                # Cargar la imagen en un QPixmap
                pixmap = QtGui.QPixmap('images/cancelar.png')

                # Establecer el QPixmap en el QLabel
                label.setPixmap(pixmap)

                self.panel.setGeometry(form.geometry())

            #  Colocar el diálogo en la parte superior de la ventana principal
                desktop = QApplication.desktop()
                main_window = QApplication.activeWindow()  # Obtener la ventana principal
                dialog_rect = self.panel.geometry()

                if main_window is not None:
                    x = main_window.frameGeometry().center().x() - dialog_rect.width() / 2
                    y = main_window.frameGeometry().top()  # Colocar en la parte superior
                    x = int(x)
                    y = int(y)
                    self.panel.move(x, y)

                # Mostrar la ventana emergente
                self.panel.show()
            else:
                contenido = "\n\n*********************************************************************************************************\n"+self.inputtext_create_cat_2.toPlainText(
                )+"\n"+get_current_date_time()+"\n\n"+self.inputtext_create_cat_3.toPlainText()+"\n\n*********************************************************************************************************\n"
                with open("recursos/" + "cat_" + my_object.get_text() + ".txt", "a") as archivo:
                    archivo.write(contenido)
                # Cambiar a la página 2 del QStackedWidget
                self.stacked_widget.setCurrentIndex(2)
                self.inputtext_create_cat_2.clear()
                self.inputtext_create_cat_3.clear()

    def button_clicked_cancelar(self):
        # Manejar el evento de clic del botón
        # print("Botón presionado")
        # Construir la ruta del archivo
        directorio = 'recursos'
        ruta_archivo = os.path.join(
            directorio, "cat_"+my_object.get_text()+".txt")
        # Eliminar el archivo
        os.remove(ruta_archivo)

        self.inputtext_create_cat_2.clear()
        self.inputtext_create_cat_3.clear()
        # Cambiar a la página 0 del QStackedWidget
        self.stacked_widget.setCurrentIndex(0)

    def actualizar_cat(self):
        # Obtener datos
        value = my_object.get_text()
        self.data_category.setText(value)

    def actualizar_cat(self):
        # Obtener datos
        value = my_object.get_text()
        self.data_category.setText(value)


class ComtensubCat(QtWidgets.QDialog):
    def __init__(self, my_object3):
        super().__init__()
        self.stacked_widget = None
        self.my_object2 = my_object2

        loadUi('ui/comten_subcat.ui', self)
        self.cancelar.clicked.connect(self.button_clicked_cancelar)
        self.guardar.clicked.connect(self.button_clicked_guardar)

        # Obtener datos
        value = my_object3.get_text().split('\n')[0]
        self.data_category.setText(value)

        stacked_widget.currentChanged.connect(self.actualizar_cat)

    def update_data_category(self, value):
        self.data_category.setText(value)

    def button_clicked_guardar(self):
        text = self.inputtext_create_cat_2.toPlainText()
        text1 = self.inputtext_create_cat_3.toPlainText()

        if not text.strip() and not text1.strip():
            # El texto está vacío
            # Crear la ventana emergente aquí

            self.panel = QDialog()
            frame = QtWidgets.QFrame()
            # Establecer el color de fondo del QFrame
            self.panel.setStyleSheet("border: 1px solid red;")
            self.panel.setWindowFlags(Qt.Popup)

            layout = QVBoxLayout(self.panel)
            # Configurar un margen de 0 para el QVBoxLayout
            layout.setContentsMargins(1, 1, 1, 1)
            # Cargar el archivo .ui aquí
            form = uic.loadUi('ui/alert_dialog.ui')
            layout.addWidget(form)

            # Configurar la ventana emergente aquí
            dialog_text = form.dialog_text  # Acceder al  formulario
            dialog_text.setWordWrap(True)
            dialog_text.setText(
                "Error: Por favor, asegúrate de ingresar algún texto en los campos.")

            # Acceder al QLabel
            label = form.findChild(QtWidgets.QLabel, "dialog_image")
            # Cargar la imagen en un QPixmap
            pixmap = QtGui.QPixmap('images/cancelar.png')

            # Establecer el QPixmap en el QLabel
            label.setPixmap(pixmap)
            self.panel.setGeometry(form.geometry())
            # Colocar el diálogo en la parte superior de la ventana principal
            desktop = QApplication.desktop()
            main_window = QApplication.activeWindow()  # Obtener la ventana principal
            dialog_rect = self.panel.geometry()

            if main_window is not None:
                x = main_window.frameGeometry().center().x() - dialog_rect.width() / 2
                y = main_window.frameGeometry().top()  # Colocar en la parte superior
                x = int(x)
                y = int(y)
                self.panel.move(x, y)

            # Mostrar la ventana emergente
            self.panel.show()
        else:
            if text == my_object3.get_text():
              # El texto está vacío
              # Crear la ventana emergente aquí

                self.panel = QDialog()
                frame = QtWidgets.QFrame()

                # Establecer el color de fondo del QFrame
                self.panel.setStyleSheet("border: 1px solid red;")
                self.panel.setWindowFlags(Qt.Popup)

                layout = QVBoxLayout(self.panel)
                # Configurar un margen de 0 para el QVBoxLayout
                layout.setContentsMargins(1, 1, 1, 1)
                # Cargar el archivo .ui aquí
                form = uic.loadUi('ui/alert_dialog.ui')
                layout.addWidget(form)

                # Configurar la ventana emergente aquí
                dialog_text = form.dialog_text  # Acceder al  formulario
                dialog_text.setWordWrap(True)
                dialog_text.setText(
                    "Error: Por favor, asegúrate de ingresar algún texto diferente a la categoría.")

                # Acceder al QLabel
                label = form.findChild(QtWidgets.QLabel, "dialog_image")
                # Cargar la imagen en un QPixmap
                pixmap = QtGui.QPixmap('images/cancelar.png')

                # Establecer el QPixmap en el QLabel
                label.setPixmap(pixmap)

                self.panel.setGeometry(form.geometry())

            #  Colocar el diálogo en la parte superior de la ventana principal
                desktop = QApplication.desktop()
                main_window = QApplication.activeWindow()  # Obtener la ventana principal
                dialog_rect = self.panel.geometry()

                if main_window is not None:
                    x = main_window.frameGeometry().center().x() - dialog_rect.width() / 2
                    y = main_window.frameGeometry().top()  # Colocar en la parte superior
                    x = int(x)
                    y = int(y)
                    self.panel.move(x, y)

                # Mostrar la ventana emergente
                self.panel.show()
            else:
                # uso del llenado segun el praton establecido
                file_name = 'recursos/cat_' + \
                    my_object3.get_text().split('\n')[0]+'.txt'
                title = my_object3.get_text().split('\n')[0]
                date = my_object3.get_text().split('\n')[1]
                self.add_box(file_name, title, date)

                # Cambiar a la página 2 del QStackedWidget
                self.stacked_widget.setCurrentIndex(4)
                self.inputtext_create_cat_2.clear()
                self.inputtext_create_cat_3.clear()

    def button_clicked_cancelar(self):
        self.inputtext_create_cat_2.clear()
        self.inputtext_create_cat_3.clear()
        # Cambiar a la página 0 del QStackedWidget
        self.stacked_widget.setCurrentIndex(4)

    def add_box(self, file_name, title, date):
        with open(file_name, 'r') as file:
            lines = file.readlines()

        with open(file_name, 'w') as file:
            add_asterisks = False  # Bandera para indicar cuándo agregar la caja de asteriscos
            added_box = False  # Bandera para indicar si ya se agregó la caja
            for line in lines:
                file.write(line)
                if line.strip() == '*' * 105:  # Verificar si la línea es una caja de asteriscos
                    add_asterisks = False  # Desactivar la bandera si la caja ya existe
                    continue
                    # Verificar si la línea contiene el título
                    # Verificar si la línea comienza con el título
                if line.strip().startswith(title):
                    add_asterisks = True  # Activar la bandera para la próxima iteración
                    continue
                # Verificar si la línea contiene la fecha (en la línea siguiente)
                if add_asterisks and date in line:
                    if added_box:
                        add_asterisks = False  # Desactivar la bandera si ya se agregó la caja
                    else:
                        file.write('\n')
                        file.write('*' * 105 + '\n')
                        file.write(
                            self.inputtext_create_cat_2.toPlainText() + '\n')
                        file.write(get_current_date_time() + '\n')
                        file.write('\n')
                        file.write(
                            self.inputtext_create_cat_3.toPlainText() + '\n')
                        file.write('\n')
                        file.write('*' * 105 + '\n')
                        add_asterisks = False  # Desactivar la bandera

    def actualizar_cat(self):
        # Obtener datos
        value = my_object3.get_text().split('\n')[0]
        self.data_category.setText(value)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    stacked_widget = QtWidgets.QStackedWidget()

    my_object = Poo()
    my_object2 = Poo()
    my_object3 = Poo()

    main_window = MainWindow(my_object)
    create_cat_window = CreateCat(my_object)
    search_cat_window = ListCat(stacked_widget, my_object2, my_object3)
    comten_cat_window = ComtenCat(my_object)
    search_subcat_window = ListsubCat(stacked_widget, my_object2, my_object3)
    comten_subcat_window = ComtensubCat(my_object3)

    stacked_widget.addWidget(main_window)
    stacked_widget.addWidget(create_cat_window)
    stacked_widget.addWidget(search_cat_window)
    stacked_widget.addWidget(comten_cat_window)
    stacked_widget.addWidget(search_subcat_window)
    stacked_widget.addWidget(comten_subcat_window)

    main_window.stacked_widget = stacked_widget
    create_cat_window.stacked_widget = stacked_widget
    search_cat_window.stacked_widget = stacked_widget
    comten_cat_window.stacked_widget = stacked_widget
    search_subcat_window.stacked_widget = stacked_widget
    comten_subcat_window.stacked_widget = stacked_widget

    stacked_widget.setCurrentIndex(0)

    stacked_widget.setWindowTitle("ConoBase")
    stacked_widget.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint |
                                  QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
    icon_path = "images/logo_app.png"
    stacked_widget.setWindowIcon(QtGui.QIcon(icon_path))
    stacked_widget.setFixedSize(401, 401)

    windowSize = stacked_widget.geometry()
    desktopCenter = QtWidgets.QDesktopWidget().availableGeometry().center()
    windowSize.moveCenter(desktopCenter)
    stacked_widget.move(windowSize.topLeft())

    stacked_widget.show()
    sys.exit(app.exec())
