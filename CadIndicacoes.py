from PyQt5.QtWidgets import QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
import mysql.connector
import uuid

class CadIndicacoes(QWidget):

    def __init__(self):
        super().__init__()

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="3Ewu85B8bB",
            database="Odonto"
        )

        self.setWindowTitle('Indicações')
        vlayout = QVBoxLayout()
        vlayout.addWidget(QLabel('Descrição'))
        self.descricao = QLineEdit()
        vlayout.addWidget(self.descricao)

        def on_salvar():
            cursor = self.mydb.cursor()
            uid = str(uuid.uuid4())
            sql = 'INSERT INTO Indicacoes (Id, Descricao) VALUES (%s, %s)'
            val = (uid, str(self.descricao.text()))

            cursor.execute(sql, val)
            self.mydb.commit()

            alert = QMessageBox()
            alert.setText('commited! id %s' % uid)
            alert.exec_()
        
        btn_novo = QPushButton('Novo')
        btn_novo.clicked.connect(on_salvar)
        vlayout.addWidget(btn_novo)
        vlayout.addWidget(QPushButton('Salvar'))
        self.setLayout(vlayout)
        self.show()