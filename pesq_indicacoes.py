from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtCore import Qt
from ui_pesq_indicacoes import Ui_PesqIndicacoes
from repository import Repository

class PesqIndicacoes(QDialog):
    def __init__(self):
        super().__init__()
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setModal(True)
        self.repository = Repository('Indicacoes')
        self.ui = Ui_PesqIndicacoes()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Id', 'Nome'])
        self.selected = False
        self.__setupEvents()
        self.filtrar("")

    def __setupEvents(self):
        def on_confirmar():
            self.selected = self.ui.tableWidget.rowCount() > 0
            self.close()
        
        def on_cancelar():
            self.close()

        self.ui.btnConfirmar.clicked.connect(on_confirmar)
        self.ui.btnCancelar.clicked.connect(on_cancelar)
        self.ui.tableWidget.doubleClicked.connect(on_confirmar)

    def filtrar(self, nome):
        self.ui.tableWidget.clear()
        rows = []

        if self.ui.edtNome.text():
            rows = self.repository.get_where(['Id', 'Nome'], {'Nome': self.ui.edtNome.text()})
        else:
            rows = self.repository.get_all(['Id', 'Nome'])

        if not rows:
            return

        for row in rows:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)         
            for i, column in enumerate(row):
                item = QTableWidgetItem(str(column))
                item.setFlags(Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(rowPosition, i, item)

    def pesquisar(self):
        self.exec_()

        if self.selected:
            row = self.ui.tableWidget.currentItem().row()
            return int(self.ui.tableWidget.item(row, 0).text())