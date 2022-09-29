from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap

import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        # COMPLETAR

        self.logo = QLabel(self)
        pixeles_logo = QPixmap(p.RUTA_LOGO)
        self.logo.setPixmap(pixeles_logo)

        self.mensaje_user = QLabel('Ingresa tu nombre de usuario', self)
        self.caja_user = QLineEdit('', self)
        hbox_user = QHBoxLayout()
        hbox_user.addWidget(self.mensaje_user)
        hbox_user.addWidget(self.caja_user)

        self.mensaje_contrasena = QLabel('Ingresa tu contraseña', self)
        self.caja_contrasena = QLineEdit('', self)
        self.caja_contrasena.setEchoMode(QLineEdit.Password)
        hbox_contrasena = QHBoxLayout()
        hbox_contrasena.addWidget(self.mensaje_contrasena)
        hbox_contrasena.addWidget(self.caja_contrasena)

        self.boton_login = QPushButton('Ingresar', self)
        self.boton_login.clicked.connect(self.enviar_login)

        vbox_madre = QVBoxLayout()
        vbox_madre.addWidget(self.logo)
        vbox_madre.addStretch(1)
        vbox_madre.addLayout(hbox_user)
        vbox_madre.addLayout(hbox_contrasena)
        vbox_madre.addStretch(1)
        vbox_madre.addWidget(self.boton_login)
        self.setLayout(vbox_madre)

    def enviar_login(self):
        # COMPLETAR
        user = self.caja_user.text()
        contrasena = self.caja_contrasena.text()
        self.senal_enviar_login.emit(user, contrasena)

    def recibir_validacion(self, valid, errores):
        # COMPLETAR
        if valid:
            self.hide()
        if 'usuario' in errores:
            self.caja_user.setText('')
            self.caja_user.setPlaceholderText('usuario inválido')
        if 'contraseña' in errores:
            self.caja_contrasena.setText('')
            self.caja_contrasena.setPlaceholderText('contraseña inválida')
