from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from ui_cad_indicacoes import Ui_CadIndicacoes
from pesq_indicacoes import PesqIndicacoes
from repository import Repository

class CadIndicacoes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.repository = Repository('Indicacoes')
        self.inserting = False
        self.ui = Ui_CadIndicacoes()
        self.ui.setupUi(self)
        self.__setupEvents()
        self.ui.edtId.setText(str(self.repository.get_next_id()))


    def __setupEvents(self):
        def on_novo():
            self.inserting = True
            self.ui.edtId.setText(str(self.repository.get_next_id()))
            self.ui.edtNome.clear()
            self.ui.set_mode(True)

        def on_salvar():
            if not self.ui.edtNome.text():
                self.alert("Preencha o nome")
                return

            values_dict = {
                'Nome': str(self.ui.edtNome.text())
            }

            if self.inserting:
                self.repository.insert(values_dict)
            else:
                self.repository.update(int(self.ui.edtId.text()), values_dict)

            self.ui.set_mode(False)
            self.ui.edtId.setText(str(self.repository.get_next_id()))
            self.ui.edtNome.clear()
            self.inserting = False

        def on_pesquisar():
            pesq = PesqIndicacoes()
            id = pesq.pesquisar()

            if id:
                id, nome = self.repository.get_by_id(id)

            if nome:
                self.ui.edtId.setText(str(id))
                self.ui.edtNome.setText(nome)
                self.ui.set_mode(True)

        def on_remover():
            if not self.inserting:
                self.repository.delete(int(self.ui.edtId.text()))

            self.inserting = False
            self.ui.edtId.setText(str(self.repository.get_next_id()))
            self.ui.edtNome.clear()
            self.ui.set_mode(False)

        def on_id_editing_finished():
            if (not self.ui.edtId.text()) or (self.inserting):
                return

            id, nome = self.repository.get_by_id(int(self.ui.edtId.text()))

            if nome:
                self.ui.edtNome.setText(nome)
                self.ui.set_mode(True)

        def on_sair():
            self.close()

        self.ui.btnNovo.clicked.connect(on_novo)
        self.ui.btnSalvar.clicked.connect(on_salvar)
        self.ui.btnPesquisar.clicked.connect(on_pesquisar)
        self.ui.btnRemover.clicked.connect(on_remover)
        self.ui.btnSair.clicked.connect(on_sair)
        self.ui.edtId.editingFinished.connect(on_id_editing_finished)

    def alert(self, message):
        alertd = QMessageBox()
        alertd.setText(message)
        alertd.exec_()

    def keyPressEvent(self, event):
        if not event.isAutoRepeat():
            if event.key() == Qt.Key_Escape:
                if not self.ui.edtId.isEnabled():
                    self.inserting = False
                    self.ui.edtId.setText(str(self.repository.get_next_id()))
                    self.ui.edtNome.clear()
                    self.ui.set_mode(False)
                else:
                    self.close()
