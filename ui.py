from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
import sys

class ui:
    def __init__(self):

        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.window.resize(480, 720)
        self.window.setWindowTitle('Product')

        self.text_name_2 = QLabel(self.window)
        self.text_manufacturer_2 = QLabel(self.window)
        self.text_barcode_2 = QLabel(self.window)
        self.text_country_2 = QLabel(self.window)
        self.text_price_2 = QLabel(self.window)
        self.text_calorie_2 = QLabel(self.window)
        self.text_fat_2 = QLabel(self.window)
        self.text_carbonhydrate_2 = QLabel(self.window)
        self.text_protein_2 = QLabel(self.window)

        self.init_ui(self)
        

    def init_ui(self):
        title = QLabel(self.window)
        title.setText('Product Information')
        title.move(10, 10)
        title.setFont(QFont('Times', 20))

        text_name = QLabel(self.window)
        text_name.setText('Name: ')
        text_name.setFont(QFont('Times', 16))
        text_name.move(10, 150)

        text_manufacturer = QLabel(self.window)
        text_manufacturer.setText('Manufacturer: ')
        text_manufacturer.setFont(QFont('Times', 16))
        text_manufacturer.move(10, 200)

        text_barcode = QLabel(self.window)
        text_barcode.setText('Barcode: ')
        text_barcode.setFont(QFont('Times', 16))
        text_barcode.move(10, 250)

        text_country = QLabel(self.window)
        text_country.setText('Country: ')
        text_country.setFont(QFont('Times', 16))
        text_country.move(10, 300)

        text_price = QLabel(self.window)
        text_price.setText('Price: ')
        text_price.setFont(QFont('Times', 16))
        text_price.move(10, 350)

        text_calorie = QLabel(self.window)
        text_calorie.setText('Calorie: ')
        text_calorie.setFont(QFont('Times', 16))
        text_calorie.move(10, 400)

        text_fat = QLabel(self.window)
        text_fat.setText('Fat: ')
        text_fat.setFont(QFont('Times', 16))
        text_fat.move(10, 450)

        text_carbonhydrate = QLabel(self.window)
        text_carbonhydrate.setText('Carbonhydrate: ')
        text_carbonhydrate.setFont(QFont('Times', 16))
        text_carbonhydrate.move(10, 500)

        text_protein = QLabel(self.window)
        text_protein.setText('Protein: ')
        text_protein.setFont(QFont('Times', 16))
        text_protein.move(10, 550)


        self.window.show()
        self.app.exec_()

    def update_ui(self, product):

        
        self.text_name_2.setText(product['name'])
        self.text_name_2.setFont(QFont('Times', 16))
        self.text_name_2.move(250, 150)

        self.text_manufacturer_2.setText(product['manufacturer'])
        self.text_manufacturer_2.setFont(QFont('Times', 16))
        self.text_manufacturer_2.move(250, 200)

        self.text_barcode_2.setText(product['barcode'])
        self.text_barcode_2.setFont(QFont('Times', 16))
        self.text_barcode_2.move(250, 250)

        self.text_country_2.setText(product['country'])
        self.text_country_2.setFont(QFont('Times', 16))
        self.text_country_2.move(250, 300)

        self.text_price_2.setText(product['price'])
        self.text_price_2.setFont(QFont('Times', 16))
        self.text_price_2.move(250, 350)

        self.text_calorie_2.setText(product['calorie'])
        self.text_calorie_2.setFont(QFont('Times', 16))
        self.text_calorie_2.move(250, 400)

        self.text_fat_2.setText(product['fat'])
        self.text_fat_2.setFont(QFont('Times', 16))
        self.text_fat_2.move(250, 450)

        self.text_carbonhydrate_2.setText(product['carbonhydrate'])
        self.text_carbonhydrate_2.setFont(QFont('Times', 16))
        self.text_carbonhydrate_2.move(250, 500)

        self.text_protein_2.setText(product['protein'])
        self.text_protein_2.setFont(QFont('Times', 16))
        self.text_protein_2.move(250, 550)

u = ui()