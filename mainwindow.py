# -*- coding: utf-8 -*-
"""
Created on Sat May  4 20:34:01 2019

@author: celal
"""
import sys
from PyQt5 import QtWidgets,QtGui,QtCore
from secondwindow import SecondWindow

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mainwindow()
    def mainwindow(self):
        #Anasayfa yapısı
        self.second_window=QtWidgets.QStackedWidget()
        self.setStyleSheet("background: white;")
        self.setWindowTitle("Celal Akçelik Bitirme Tezi")
        self.setWindowIcon(QtGui.QIcon('images/igulogo.jpg'))
        self.setMinimumSize(1200,900)
        self.setMaximumSize(1200,900)
        
        #logo
        self.logo=QtWidgets.QLabel(self)
        self.logo.setPixmap(QtGui.QPixmap("images/igulogo.jpg"))
        self.logo.setScaledContents(True)
        self.logo.resize(200,200)
        self.logo.move(500,0)
        
        #tez konusu
        self.tez_konusu=QtWidgets.QLabel(self)
        self.tez_konusu.setText("TEZ KONUSU: \nDERİN ÖĞRENME TABANLI BİLGİSAYARLI GÖRÜŞ \nİLE\nYÜZ TANIMA")
        self.tez_konusu.setFont(QtGui.QFont("MS Shell Dlg 2", 25))
        self.tez_konusu.setAlignment(QtCore.Qt.AlignCenter)
        self.tez_konusu.resize(750,191)
        self.tez_konusu.move(230,200)
        
        #Programa geçiş butonu
        self.prog_gecis_buton=QtWidgets.QPushButton(self)
        self.prog_gecis_buton.setText("YÜZ TANIMLAMAYA\nBAŞLA")
        self.prog_gecis_buton.setStyleSheet("background-color:#c39435;color:#ffffff;border-radius:20px;border-style: solid;")
        self.prog_gecis_buton.setFont(QtGui.QFont("MS Shell Dlg 2", 12,QtGui.QFont.Bold))
        self.prog_gecis_buton.resize(191,51)
        self.prog_gecis_buton.move(510,410)
        
        
        #tez danışmanları
        self.tez_danismanlari=QtWidgets.QLabel(self)
        self.tez_danismanlari.setText("TEZ DANIŞMANLARI")
        self.tez_danismanlari.setFont(QtGui.QFont("MS Shell Dlg 2", 25))
        self.tez_danismanlari.setAlignment(QtCore.Qt.AlignCenter)
        self.tez_danismanlari.resize(307,40)
        self.tez_danismanlari.move(60,500)
        
        #Ali Okatan
        self.ali_okatan_img=QtWidgets.QLabel(self)
        self.ali_okatan_img.setPixmap(QtGui.QPixmap("images/ali okatan.jpg"))
        self.ali_okatan_img.setScaledContents(True)
        self.ali_okatan_img.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.ali_okatan_img.resize(160,200)
        self.ali_okatan_img.move(30,570)
    
        self.ali_okatan_text=QtWidgets.QLabel(self)
        self.ali_okatan_text.setText("Prof. Dr. Ali OKATAN")
        self.ali_okatan_text.setFont(QtGui.QFont("MS Shell Dlg 2", 10,QtGui.QFont.Bold))
        self.ali_okatan_text.setAlignment(QtCore.Qt.AlignCenter)
        self.ali_okatan_text.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.ali_okatan_text.resize(160,50)
        self.ali_okatan_text.move(30,780)
        
        #Ali Çetinkaya
        self.ali_cetinkaya_img=QtWidgets.QLabel(self)
        self.ali_cetinkaya_img.setPixmap(QtGui.QPixmap("images/ali cetinkaya.png"))
        self.ali_cetinkaya_img.setScaledContents(True)
        self.ali_cetinkaya_img.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.ali_cetinkaya_img.resize(160,200)
        self.ali_cetinkaya_img.move(220,570)
        
        self.ali_cetinkaya_text=QtWidgets.QLabel(self)
        self.ali_cetinkaya_text.setText("Yük.Müh. Ali\nÇETİNKAYA")
        self.ali_cetinkaya_text.setFont(QtGui.QFont("MS Shell Dlg 2", 10,QtGui.QFont.Bold))
        self.ali_cetinkaya_text.setAlignment(QtCore.Qt.AlignCenter)
        self.ali_cetinkaya_text.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.ali_cetinkaya_text.resize(160,50)
        self.ali_cetinkaya_text.move(220,780)
        
        #tez yazarı
        self.tez_danismanlari=QtWidgets.QLabel(self)
        self.tez_danismanlari.setText("TEZ YAZARI")
        self.tez_danismanlari.setFont(QtGui.QFont("MS Shell Dlg 2", 25))
        self.tez_danismanlari.setAlignment(QtCore.Qt.AlignCenter)
        self.tez_danismanlari.resize(211,40)
        self.tez_danismanlari.move(475,500)
        
        #Celal Akçelik
        self.celal_akcelik_img=QtWidgets.QLabel(self)
        self.celal_akcelik_img.setPixmap(QtGui.QPixmap("images/celal.jpeg"))
        self.celal_akcelik_img.setScaledContents(True)
        self.celal_akcelik_img.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.celal_akcelik_img.resize(160,200)
        self.celal_akcelik_img.move(500,570)
        
        self.celal_akcelik_text=QtWidgets.QLabel(self)
        self.celal_akcelik_text.setText("Celal AKÇELİK")
        self.celal_akcelik_text.setFont(QtGui.QFont("MS Shell Dlg 2", 10,QtGui.QFont.Bold))
        self.celal_akcelik_text.setAlignment(QtCore.Qt.AlignCenter)
        self.celal_akcelik_text.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.celal_akcelik_text.resize(160,50)
        self.celal_akcelik_text.move(500,780)
        
         #tezde yardımcı olan sınıf arkadaşları
        self.tez_yard_olan_ark=QtWidgets.QLabel(self)
        self.tez_yard_olan_ark.setText("TEZDE YARDIMCI OLAN SINIF\nARKADAŞLARI")
        self.tez_yard_olan_ark.setFont(QtGui.QFont("MS Shell Dlg 2", 25))
        self.tez_yard_olan_ark.setAlignment(QtCore.Qt.AlignCenter)
        self.tez_yard_olan_ark.resize(461,92)
        self.tez_yard_olan_ark.move(730,470)
        
        #Ali Şükran Özdemir
        self.ali_ozdemir_img=QtWidgets.QLabel(self)
        self.ali_ozdemir_img.setPixmap(QtGui.QPixmap("images/ali şükran özdemir.jpeg"))
        self.ali_ozdemir_img.setScaledContents(True)
        self.ali_ozdemir_img.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.ali_ozdemir_img.resize(160,200)
        self.ali_ozdemir_img.move(770,570)
        
        self.ali_ozdemir_text=QtWidgets.QLabel(self)
        self.ali_ozdemir_text.setText("Ali Şükran\nÖZDEMİR")
        self.ali_ozdemir_text.setFont(QtGui.QFont("MS Shell Dlg 2", 10,QtGui.QFont.Bold))
        self.ali_ozdemir_text.setAlignment(QtCore.Qt.AlignCenter)
        self.ali_ozdemir_text.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.ali_ozdemir_text.resize(160,50)
        self.ali_ozdemir_text.move(770,780)
        
        #İbrahim Demirkılıç
        self.ibrahim_demirkilic_img=QtWidgets.QLabel(self)
        self.ibrahim_demirkilic_img.setPixmap(QtGui.QPixmap("images/ibrahim demirkilic.jpg"))
        self.ibrahim_demirkilic_img.setScaledContents(True)
        self.ibrahim_demirkilic_img.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.ibrahim_demirkilic_img.resize(160,200)
        self.ibrahim_demirkilic_img.move(980,570)
        
        self.ibrahim_demirkilic_text=QtWidgets.QLabel(self)
        self.ibrahim_demirkilic_text.setText("İbrahim DEMİRKILIÇ")
        self.ibrahim_demirkilic_text.setFont(QtGui.QFont("MS Shell Dlg 2", 10,QtGui.QFont.Bold))
        self.ibrahim_demirkilic_text.setAlignment(QtCore.Qt.AlignCenter)
        self.ibrahim_demirkilic_text.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.ibrahim_demirkilic_text.resize(160,50)
        self.ibrahim_demirkilic_text.move(980,780)
        self.prog_gecis_buton.clicked.connect(self.openWindow)
        
        
    def openWindow(self):
        self.hide()
        self.second=SecondWindow()
        self.second.show()
        
def main():
    app=QtWidgets.QApplication(sys.argv)
    main=MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
