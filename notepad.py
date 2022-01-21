import time
import webbrowser
import sys


from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import uic
import os

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("notepad.ui",self)
        self.pencere()
        self.menu()

    def menu(self):
        self.Dosya_ac.setShortcut("Ctrl+O")
        self.Dosya_ac.triggered.connect(self.openfile)
        self.actionDosyaya_Yaz.setShortcut("Ctrl+S")
        self.actionDosyaya_Yaz.triggered.connect(self.writefile)
        self.actionMetni_Sil.setShortcut("Ctrl+F")
        self.actionMetni_Sil.triggered.connect(self.temizle)
        self.actionYaz.triggered.connect(self.write)
        self.actionCikis.triggered.connect(self.quit)
        self.setWindowTitle("NotePad")



    def pencere(self):
        self.pushButton.clicked.connect(self.openfile)
        self.pushButton_2.clicked.connect(self.writefile)
        self.pushButton_3.clicked.connect(self.temizle)
        self.pushButton_4.clicked.connect(self.write)
        self.pushButton_5.clicked.connect(self.quit)
        self.pushButton_6.clicked.connect(self.quicksave)
        self.textEdit.setPlaceholderText("Buraya yaz")
        self.textBrowser.setPlaceholderText("Buradan oku")
        self.show()




    def quit(self):
        qApp.quit()
    def writefile(self):
        dosya_ismi = QFileDialog.getSaveFileName(self, "Dosya Kaydet", os.getenv("HOME"))

        with open(dosya_ismi[0], "w", encoding = "utf-8") as file:
            file.write(self.text)

    def openfile(self):
        self.dosya_ismi = QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("HOME"))
        with open(self.dosya_ismi[0],"r",encoding = "utf-8") as file:
            self.textBrowser.setText(file.read())

    def choosefile(self):
        pass

    def quicksave(self):
        try:
            with open(self.dosya_ismi[0], "w", encoding = "utf-8") as file:
                file.write(self.text)
        except:
            self.textBrowser.setText("Hata Once dosya secin")
    def write(self):
        kodlar = "Hazırlayan\nDoruk\nmusic"
        self.text = self.textEdit.toPlainText()
        if self.text == "Hazırlayan":
           self.textBrowser.setText("Bedirhan\nBu program Bedirhan Yalcin tarafindan hazirlandi")
        elif self.text == "music":
            self.textBrowser.setText("Acalim")

            webbrowser.open("music.youtube.com")
        elif self.text == "kodlar":
            self.textBrowser.setText(kodlar)
        elif self.text == "Doruk" or self.text == "doruk":
            self.textBrowser.setText("doruk peker ama ben pekmem \nDoruk peeker  yani peekleyici kimse")

        else:
            self.textBrowser.setText(self.text)

    def temizle(self):
        self.textEdit.setText("")
        self.textBrowser.setText("")



app = QtWidgets.QApplication(sys.argv)
main = main()
sys.exit(app.exec_())
