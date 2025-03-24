import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from UI.playfair import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_generate.clicked.connect(self.call_api_generate_matrix)
        
    def display_matrix(self, matrix):
        matrix_text = "\n".join([" ".join(row) for row in matrix])
        self.ui.txt_matrix.setPlainText(matrix_text)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data["encrypted_text"])
                self.display_matrix(data["matrix"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_text"])
                self.display_matrix(data["matrix"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error:", e)
        
    def call_api_generate_matrix(self):
        url = "http://127.0.0.1:5000/api/playfair/generate_matrix"
        key = self.ui.txt_key.toPlainText()

        if not key:
            QMessageBox.warning(self, "Warning", "Please enter a key!")
            return
        
        payload = {"key": key}

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.display_matrix(data["matrix"])
            else:
                QMessageBox.critical(self, "Error", "Failed to generate matrix!")
        except requests.exceptions.RequestException as e:
            print("Error:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
