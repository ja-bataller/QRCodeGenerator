from GUI.mainWindow import *

import os.path
from PIL import Image
from PyQt5.QtWidgets import *
import qrcode
import sys

class mainWindow(Ui_mainWindow, QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)

        self.pushButtonGenerate.clicked.connect(self.Generate)

    # if the user clicked the Generate Button this method will run
    def Generate(self):
        userinput = self.lineEditInput.text()
        if userinput != "":
            # QR Code Generator
            qr = qrcode.make(str(userinput))
            # QR code save path / file directory
            home = os.path.expanduser('~')
            location = os.path.join(home, 'Downloads')
            # QR code saved
            qr.save(os.path.join(location,userinput + ".png"))

            # QR code pop up Message if the QR code is successfully generated and saved
            QMessageBox.information(self, "SUCCESS", "<FONT COLOR='#eeeeee'>The QR code generated successfully. The QR code has been saved to Downloads.</FONT>")

            # QR code Image will automatically open  if the QR code is successfully generated and saved
            filename =(os.path.join(location,userinput + ".png"))
            img = Image.open(filename)
            img.show(filename)

            # Clear the lineEdit in the GUI
            self.lineEditInput.clear()
        else:
            # Validation if the User input is blank
            QMessageBox.warning(self, "FAILED", "<FONT COLOR='#eeeeee'>The input is empty.</FONT>")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main = mainWindow()
    main.show()

    sys.exit(app.exec())
