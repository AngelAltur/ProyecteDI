import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from calendari import CalendarioApp


class PedirCita(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('HealthMate')
        self.setGeometry(250, 250, 550, 850)
        self.setStyleSheet("background-color: rgb(70, 130, 180);")

        self.initUI()
    
    def initUI(self):
        # Agregar el calendario directamente al QStackedWidget
        self.stacked_widget = QStackedWidget(self)
        calendario_widget = CalendarioApp()

        # Añadir un cuadro de texto para mostrar las citas
        self.cuadro_texto = QTextEdit(self)
        self.cuadro_texto.setReadOnly(True)

        # Crear un layout vertical para organizar las etiquetas y widgets
        layout = QVBoxLayout()

        # Agregar un QLabel para el título
        texto_perfil = QLabel("Pedir Cita", self)
        texto_perfil.setAlignment(Qt.AlignCenter)
        layout.addWidget(texto_perfil)

        # Crear los QComboBox para seleccionar el tipo de mascota y el servicio
        self.tipo_mascota_combo = QComboBox()
        self.tipo_mascota_combo.addItems(["Tipo de mascota", "Perro", "Gato", "Ave", "Reptil", "Roedor", "Pez", "Conejo", "Caballo", "Otro"])
        self.tipo_mascota_combo.setCurrentText("Tipo de mascota")  # opción por defecto

        self.servicio = QComboBox()
        self.servicio.addItems(["Seleccione servicio", "Vacunación", "Revisión", "Urgencias"])
        self.servicio.setCurrentText("Seleccione servicio")

        layout.addWidget(self.servicio)
        layout.addWidget(self.tipo_mascota_combo)
        layout.addWidget(calendario_widget)
        layout.addWidget(self.cuadro_texto)

        # Crear un widget contenedor y asignar el diseño
        container_widget = QWidget(self)
        container_widget.setLayout(layout)

        self.stacked_widget.addWidget(container_widget)
        self.setCentralWidget(self.stacked_widget)

        # Mostrar directamente el calendario
        self.stacked_widget.setCurrentIndex(0)

        # Conectar la señal de la cita al método para mostrarla en el cuadro de texto
        calendario_widget.cita_agendada.connect(self.mostrarCita)

        # Agregar botón para volver al menú
        self.btn_volver_menu = QPushButton('Volver al Menú', self)
        self.btn_volver_menu.clicked.connect(self.mostrarMenu)
        layout.addWidget(self.btn_volver_menu, alignment=Qt.AlignTop | Qt.AlignLeft)

    def mostrarCita(self, fecha, usuario):
        # Obtener las opciones seleccionadas de los QComboBox
        tipo_mascota = self.tipo_mascota_combo.currentText()
        servicio = self.servicio.currentText()

        # Verificar si las opciones seleccionadas no son las opciones por defecto
        if tipo_mascota != "Tipo de mascota" and servicio != "Seleccione servicio":
            # Agregar la cita al cuadro de texto incluyendo las opciones seleccionadas
            texto_cita = f'·Cita agendada para el día {fecha.toString("dd-MM-yyyy")} por el usuario {usuario}.'
            texto_cita += f'\n --Tipo de mascota: {tipo_mascota}'
            texto_cita += f'\n --Servicio seleccionado: {servicio}\n'
            self.cuadro_texto.append(texto_cita)
        else:
            # Mostrar un mensaje de error en caso de que las opciones seleccionadas sean las por defecto
            QMessageBox.warning(self, "Error", "Por favor seleccione un tipo de mascota y un servicio antes de pedir cita.")

    def mostrarMenu(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    pedir_cita = PedirCita()
    pedir_cita.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
