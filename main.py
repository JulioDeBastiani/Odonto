from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from CadIndicacoes import CadIndicacoes

def main():
    app = QApplication([])
    window = CadIndicacoes()
    app.exec_()

if __name__ == '__main__':
    main()