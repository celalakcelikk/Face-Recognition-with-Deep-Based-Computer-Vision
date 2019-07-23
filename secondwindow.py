# -*- coding: utf-8 -*-
"""
Created on Sat May  5 02:08:23 2019

@author: celal
"""
from PyQt5.QtGui import QImage
from PyQt5 import QtWidgets,QtGui,QtCore
import cv2
from PyQt5.QtCore import QTimer
from face_cam import cam_detect
from face_img import detect


class SecondWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.secondwindow()
        self.timer = QTimer()
        self.timer.timeout.connect(self.kamera_ac)

    def secondwindow(self):
        self.resim=''
        self.setStyleSheet("background: #efecf7;")
        self.setWindowTitle("Celal Akçelik Bitirme Tezi")
        self.setWindowIcon(QtGui.QIcon('images/igulogo.jpg'))
        self.setMinimumSize(1200,900)
        self.setMaximumSize(1200,900)
        
        
        #Tab oluşturma
        self.table=QtWidgets.QTabWidget(self)
        self.table.setStyleSheet("border: 0px solid black;border-radius: 0px;background: #efecf7;")
        self.table.move(0,0)
        self.table.resize(1200,810)
        self.table.setTabShape(QtWidgets.QTabWidget.TabShape(QtWidgets.QTabWidget.Triangular))
        
        #Anasayfaya Dön butonu
        self.anasyafaya_don_btn=QtWidgets.QPushButton(self)
        self.anasyafaya_don_btn.move(440,820)
        self.anasyafaya_don_btn.resize(281,51)
        self.anasyafaya_don_btn.setText("ANASAYFAYA DÖN")
        self.anasyafaya_don_btn.setStyleSheet("border: 10px solid #7bf864;border-radius: 20px;background: #7bf864;color:#ffffff;")
        self.anasyafaya_don_btn.setFont(QtGui.QFont("MS Shell Dlg 2", 15,QtGui.QFont.Bold))
        self.anasyafaya_don_btn.clicked.connect(self.anasayfa_clicked)
        
        #Resim tabı oluşturuldu.
        self.resimtab=QtWidgets.QWidget()
        self.resimtab.setStyleSheet("border: 0px solid black;border-radius: 10px;background: #efecf7;")
            
        #Orjinal Resim başlığı
        self.orjinal_resim_text=QtWidgets.QLabel(self.resimtab)
        self.orjinal_resim_text.setText("ORJİNAL RESİM")
        self.orjinal_resim_text.setStyleSheet("background-color:#461eb7;color:#ffffff;border-radius:20px;border-style: solid;")
        self.orjinal_resim_text.move(290,170)
        self.orjinal_resim_text.resize(171,51)
        self.orjinal_resim_text.setFont(QtGui.QFont("MS Shell Dlg 2", 13,QtGui.QFont.Bold))
        self.orjinal_resim_text.setAlignment(QtCore.Qt.AlignCenter)
        
        #Resmin gözükeceği yer
        self.orjinal_resim_img=QtWidgets.QLabel(self.resimtab)
        self.orjinal_resim_img.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.orjinal_resim_img.move(170,230)
        self.orjinal_resim_img.setScaledContents(True)
        self.orjinal_resim_img.resize(400,400)
        
        #Resim seçme butonu
        self.orjinal_resim_bulma_btn=QtWidgets.QPushButton(self.resimtab)
        self.orjinal_resim_bulma_btn.setText("RESİM SEÇ")
        self.orjinal_resim_bulma_btn.setStyleSheet("background-color:#4d9a5c;color:#ffffff;border-radius:20px;border-style: solid;")
        self.orjinal_resim_bulma_btn.move(290,650)
        self.orjinal_resim_bulma_btn.resize(171,51)
        self.orjinal_resim_bulma_btn.setFont(QtGui.QFont("MS Shell Dlg 2", 15,QtGui.QFont.Bold))
        self.orjinal_resim_bulma_btn.clicked.connect(self.resim_sec)
        
        #Resimde Bulunan Yüzler Başlığı
        self.bulunan_resimdeki_yuzler_text=QtWidgets.QLabel(self.resimtab)
        self.bulunan_resimdeki_yuzler_text.setText("RESİMDE BULUNAN YÜZLER")
        self.bulunan_resimdeki_yuzler_text.setStyleSheet("background-color:#461eb7;color:#ffffff;border-radius:20px;border-style: solid;")
        self.bulunan_resimdeki_yuzler_text.move(660,170)
        self.bulunan_resimdeki_yuzler_text.resize(261,51)
        self.bulunan_resimdeki_yuzler_text.setFont(QtGui.QFont("MS Shell Dlg 2", 13,QtGui.QFont.Bold))
        self.bulunan_resimdeki_yuzler_text.setAlignment(QtCore.Qt.AlignCenter)
        
        #Resminde Bulunan yuzler gözükeceği yer
        self.bulunan_resimdeki_yuzler_img=QtWidgets.QLabel(self.resimtab)
        self.bulunan_resimdeki_yuzler_img.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.bulunan_resimdeki_yuzler_img.move(590,230)
        self.bulunan_resimdeki_yuzler_img.setScaledContents(True)
        self.bulunan_resimdeki_yuzler_img.resize(400,400)
        
        #Resimdeki yuzleri bul butonu
        self.resimdeki_yuzleri_bul_btn=QtWidgets.QPushButton(self.resimtab)
        self.resimdeki_yuzleri_bul_btn.setText("RESİMDEKİ YÜZLERİ BUL")
        self.resimdeki_yuzleri_bul_btn.setStyleSheet("background-color:#4d9a5c;color:#ffffff;border-radius:20px;border-style: solid;")
        self.resimdeki_yuzleri_bul_btn.move(650,650)
        self.resimdeki_yuzleri_bul_btn.resize(291,51)
        self.resimdeki_yuzleri_bul_btn.setFont(QtGui.QFont("MS Shell Dlg 2", 15,QtGui.QFont.Bold))
        self.resimdeki_yuzleri_bul_btn.clicked.connect(self.yuz_bul)
        

        #Kamera tabı oluşturuldu.
        self.cameratab=QtWidgets.QWidget()
        self.cameratab.setStyleSheet("border: 0px solid black;border-radius: 10px;background: #efecf7; ")
        
        #Kamerada bulanan yüzler başlığı
        self.orjinal_goruntu_text=QtWidgets.QLabel(self.cameratab)
        self.orjinal_goruntu_text.setText("KAMERADA BULUNAN YÜZLER")
        self.orjinal_goruntu_text.setStyleSheet("background-color:#ee1010;color:#ffffff;border-radius:20px;border-style: solid;")
        self.orjinal_goruntu_text.move(430,70)
        self.orjinal_goruntu_text.resize(300,65)
        self.orjinal_goruntu_text.setFont(QtGui.QFont("MS Shell Dlg 2", 12,QtGui.QFont.Bold))
        self.orjinal_goruntu_text.setAlignment(QtCore.Qt.AlignCenter)
        
        #Kameranın Gözükeceği yer
        self.orjinal_goruntu_img=QtWidgets.QLabel(self.cameratab)
        self.orjinal_goruntu_img.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.orjinal_goruntu_img.move(230,150)
        self.orjinal_goruntu_img.setScaledContents(True)
        self.orjinal_goruntu_img.resize(700,500)

        #Kamera Açma butonu
        self.orjinal_goruntu_btn=QtWidgets.QPushButton(self.cameratab)
        self.orjinal_goruntu_btn.setText("KAMERAYI ÇALIŞTIR")
        self.orjinal_goruntu_btn.setStyleSheet("background-color:#360b71;color:#ffffff;border-radius:20px;border-style: solid;")
        self.orjinal_goruntu_btn.move(460,660)
        self.orjinal_goruntu_btn.resize(241,51)
        self.orjinal_goruntu_btn.setFont(QtGui.QFont("MS Shell Dlg 2", 15,QtGui.QFont.Bold))
        self.orjinal_goruntu_btn.clicked.connect(self.zaman_kontrol)

        self.table.addTab(self.resimtab,"Resimden Yüz Tanımlama")
        self.table.addTab(self.cameratab,"Kameradan Yüz Tanımlama")
        
        
    def resim_sec(self):
        self.resimUrl = QtWidgets.QFileDialog.getOpenFileName(self,"Lütfen bir resim seçiniz",'',"Image Files (*.png *.jpg *.jpeg)")
        self.resim=self.resimUrl[0]
        self.orjinal_resim_img.setPixmap(QtGui.QPixmap(self.resim))
        
    def yuz_bul(self):
        img=cv2.imread(str(self.resim))
        yuz=detect(img)
        cv2.imwrite('output/output.jpg',yuz)
        self.bulunan_resimdeki_yuzler_img.setPixmap(QtGui.QPixmap('output/output.jpg'))
    
    
    def kamera_ac(self):
        ret, image = self.cap.read()
        image=cam_detect(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.orjinal_goruntu_img.setPixmap(QtGui.QPixmap.fromImage(qImg))   
    
    def zaman_kontrol(self):
        print(self.timer.isActive())
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
        else:
            self.timer.stop()
            self.cap.release()
            
            
    
    def anasayfa_clicked(self):
        from mainwindow import MainWindow
        self.hide()
        self.mainwin=MainWindow()
        self.mainwin.show()
        
