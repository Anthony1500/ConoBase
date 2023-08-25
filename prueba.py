import os,re

def add_box(file_name, title, date):
        with open(file_name, 'r') as file:
              lines = file.readlines()

        with open(file_name, 'w') as file:
             add_asterisks = False  # Bandera para indicar cuándo agregar la caja de asteriscos
             for line in lines:
                 file.write(line)
                 if line.strip() == '*' * 105:  # Verificar si la línea es una caja de asteriscos
                     add_asterisks = False  # Desactivar la bandera si la caja ya existe
                     continue
                 if title in line and date in line:
                     add_asterisks = True  # Activar la bandera para agregar la caja en la próxima iteración

                 if add_asterisks:
                    file.write('\n')
                    file.write('*' * 105 + '\n')                    
                    file.write('self.inputtext_create_cat_2.toPlainText()'+ '\n')
                    file.write('get_current_date_time()'+ '\n')
                    file.write('\n')
                    file.write('self.inputtext_create_cat_3.toPlainText()'+ '\n')
                    file.write('\n')
                    file.write('*' * 105 + '\n')
                    add_asterisks = False  # Desactivar la bandera





# Ejemplo de uso
file_name = 'resources/cat_Prueba fecha y hora.txt'
title = '3'
date = '2023-08-17 17:23:25'
add_box(file_name, title, date)




       



